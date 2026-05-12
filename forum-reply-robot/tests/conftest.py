import importlib.abc
import importlib.machinery
import importlib.util
import os
import sys
import types


ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SCHEMA_DIR = os.path.join(ROOT_DIR, "src", "ForumBot", "SchemaValidation")

for path in (ROOT_DIR, SCHEMA_DIR):
    if path not in sys.path:
        sys.path.insert(0, path)


if "psycopg2" not in sys.modules:
    psycopg2_module = types.ModuleType("psycopg2")
    psycopg2_module.connect = lambda **kwargs: None
    extras_module = types.ModuleType("psycopg2.extras")
    extras_module.Json = lambda value: value
    extras_module.execute_values = lambda cursor, query, data: None
    psycopg2_module.extras = extras_module
    sys.modules["psycopg2"] = psycopg2_module
    sys.modules["psycopg2.extras"] = extras_module


if "langchain_openai" not in sys.modules:
    langchain_module = types.ModuleType("langchain_openai")

    class DummyChatOpenAI:
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs

        def invoke(self, prompt):
            raise RuntimeError("ChatOpenAI.invoke should be mocked in tests")

    langchain_module.ChatOpenAI = DummyChatOpenAI
    sys.modules["langchain_openai"] = langchain_module


if "langchain_core" not in sys.modules:
    langchain_core_module = types.ModuleType("langchain_core")
    prompts_module = types.ModuleType("langchain_core.prompts")
    output_parsers_module = types.ModuleType("langchain_core.output_parsers")

    class _DummyRunnable:
        def __init__(self, invoke_fn):
            self._invoke_fn = invoke_fn

        def invoke(self, input_value):
            return self._invoke_fn(input_value)

        def __or__(self, other):
            if hasattr(other, "invoke"):
                return _DummyRunnable(lambda x: other.invoke(self.invoke(x)))
            if callable(other):
                return _DummyRunnable(lambda x: other(self.invoke(x)))
            return _DummyRunnable(lambda x: self.invoke(x))

    class DummyChatPromptTemplate:
        def __init__(self, messages):
            self.messages = messages

        @classmethod
        def from_messages(cls, messages):
            return cls(messages)

        def invoke(self, input_value):
            return input_value

        def __or__(self, other):
            if hasattr(other, "invoke"):
                return _DummyRunnable(lambda x: other.invoke(self.invoke(x)))
            if callable(other):
                return _DummyRunnable(lambda x: other(self.invoke(x)))
            return _DummyRunnable(lambda x: self.invoke(x))

    class DummyStrOutputParser:
        def invoke(self, value):
            if hasattr(value, "content"):
                return value.content
            return value

    prompts_module.ChatPromptTemplate = DummyChatPromptTemplate
    output_parsers_module.StrOutputParser = DummyStrOutputParser

    langchain_core_module.prompts = prompts_module
    langchain_core_module.output_parsers = output_parsers_module

    sys.modules["langchain_core"] = langchain_core_module
    sys.modules["langchain_core.prompts"] = prompts_module
    sys.modules["langchain_core.output_parsers"] = output_parsers_module


if "flask" not in sys.modules:
    flask_module = types.ModuleType("flask")

    class DummyFlask:
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs

        def route(self, *args, **kwargs):
            def decorator(func):
                return func

            return decorator

        def run(self, *args, **kwargs):
            return None

    def jsonify(*args, **kwargs):
        return {"args": args, "kwargs": kwargs}

    flask_module.Flask = DummyFlask
    flask_module.jsonify = jsonify
    sys.modules["flask"] = flask_module


if "git" not in sys.modules:
    git_module = types.ModuleType("git")

    class DummyRepo:
        def __init__(self, *args, **kwargs):
            self.remotes = types.SimpleNamespace(origin=types.SimpleNamespace(pull=lambda *a, **k: None))

        @staticmethod
        def clone_from(*args, **kwargs):
            return None

    class DummyGitCommandError(Exception):
        pass

    git_module.Repo = DummyRepo
    git_module.exc = types.SimpleNamespace(GitCommandError=DummyGitCommandError)
    sys.modules["git"] = git_module


class _ExtractReviewsLoader(importlib.abc.Loader):
    def create_module(self, spec):
        return None

    def exec_module(self, module):
        def extract_review_points_from_html(content):
            return []

        def is_redfish_related(title, content):
            return False

        module.extract_review_points_from_html = extract_review_points_from_html
        module.is_redfish_related = is_redfish_related


_ORIGINAL_SPEC_FROM_FILE_LOCATION = importlib.util.spec_from_file_location


def _patched_spec_from_file_location(name, location, *args, **kwargs):
    if name == "extract_reviews" and location and not os.path.exists(location):
        return importlib.machinery.ModuleSpec(
            name=name,
            loader=_ExtractReviewsLoader(),
            origin="synthetic://extract_reviews",
        )
    return _ORIGINAL_SPEC_FROM_FILE_LOCATION(name, location, *args, **kwargs)


importlib.util.spec_from_file_location = _patched_spec_from_file_location
