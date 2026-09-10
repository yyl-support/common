[2026/09/10 17:26:22.661 GMT+08:00] [INFO]  : [JobStatusPlugin] onStarted: j_YDkS2cnP #1
[2026/09/10 17:26:22.663 GMT+08:00] Resume disabled by user, switching to high-performance, low-durability mode.
[2026/09/10 17:26:22.772 GMT+08:00] [INFO] [PRE_ENV:slave_create] : 该步骤开始执行
[2026/09/10 17:26:22.773 GMT+08:00] [INFO] [PRE_ENV:slave_create] : [slave] resources pool message: 5559c4d79a5e41ccb0cf0b2b9143106b
[2026/09/10 17:26:22.775 GMT+08:00] [WARNING] [PRE_ENV:slave_create] : [slave] find empty runtime, location: PRE_ENV.slave_create
[2026/09/10 17:26:22.775 GMT+08:00] [INFO] [PRE_ENV:slave_create] : [slave] Fixed content: No
[2026/09/10 17:26:22.880 GMT+08:00] [INFO] [PRE_ENV:slave_create] : [slave] Find available executor node:agent_1789024043350-W79IIG7Tr8
[2026/09/10 17:26:22.933 GMT+08:00] [INFO] [PRE_ENV:slave_create] : 该步骤执行完成
[2026/09/10 17:26:22.968 GMT+08:00] [INFO] [代码检出:external_pre_checkout] : 该步骤开始执行
[2026/09/10 17:26:22.969 GMT+08:00] [INFO] [代码检出:external_pre_checkout] : git plugin version: 1.12.5
[2026/09/10 17:26:22.984 GMT+08:00] [INFO] [代码检出:external_pre_checkout] : 成功配置文件。
[2026/09/10 17:26:23.320 GMT+08:00] [INFO] [代码检出:external_pre_checkout] : [WARN]DEV.CB.02101217,用户名或密码为空。
[2026/09/10 17:26:23.320 GMT+08:00] [INFO] [代码检出:external_pre_checkout] : 创建gitcode代码访问凭证成功。
[2026/09/10 17:26:23.321 GMT+08:00] [INFO] [代码检出:external_pre_checkout] : 该步骤执行完成
[2026/09/10 17:26:23.372 GMT+08:00] No credentials specified
[2026/09/10 17:26:23.373 GMT+08:00] set customize username password****           
[2026/09/10 17:26:23.384 GMT+08:00] addDefaultCredentials
[2026/09/10 17:26:23.395 GMT+08:00] git plugin version: 3.12.22-h1.cbu.codearts.build.r1
[2026/09/10 17:26:23.406 GMT+08:00] Cloning the remote Git repository
[2026/09/10 17:26:23.406 GMT+08:00] Using shallow clone
[2026/09/10 17:26:23.406 GMT+08:00] Avoid fetching tags
[2026/09/10 17:26:23.406 GMT+08:00] Honoring refspec on initial clone
[2026/09/10 17:26:23.415 GMT+08:00] Cloning repository https://gitcode.com/cann-dev/CANN-CI.git
[2026/09/10 17:26:23.415 GMT+08:00]  > git init /opt/agent_1789024043350/workspace/j_YDkS2cnP # timeout=10
[2026/09/10 17:26:23.421 GMT+08:00] Fetching upstream changes from https://gitcode.com/cann-dev/CANN-CI.git
[2026/09/10 17:26:23.422 GMT+08:00]  > git --version # timeout=10
[2026/09/10 17:26:23.425 GMT+08:00]  > git --version # 'git version 2.34.1'
[2026/09/10 17:26:23.425 GMT+08:00] using GIT_ASKPASS to set credentials  username and password**** [2026/09/10 17:26:23.426 GMT+08:00] scmType is gitcode
[2026/09/10 17:26:23.426 GMT+08:00]  > git -c *** fetch --no-tags --force --progress --depth=1 -- https://gitcode.com/cann-dev/CANN-CI.git +refs/heads/test_smoke:refs/remotes/origin/test_smoke # timeout=120
[2026/09/10 17:26:24.092 GMT+08:00]  > git config remote.origin.url https://gitcode.com/cann-dev/CANN-CI.git # timeout=10
[2026/09/10 17:26:24.096 GMT+08:00]  > git config --add remote.origin.fetch +refs/heads/test_smoke:refs/remotes/origin/test_smoke # timeout=10
[2026/09/10 17:26:24.111 GMT+08:00]  > git config remote.origin.url https://gitcode.com/cann-dev/CANN-CI.git # timeout=10
[2026/09/10 17:26:24.126 GMT+08:00] Fetching upstream changes from https://gitcode.com/cann-dev/CANN-CI.git
[2026/09/10 17:26:24.126 GMT+08:00] using GIT_ASKPASS to set credentials  username and password**** [2026/09/10 17:26:24.128 GMT+08:00] scmType is gitcode
[2026/09/10 17:26:24.128 GMT+08:00]  > git -c *** fetch --no-tags --force --progress --depth=1 -- https://gitcode.com/cann-dev/CANN-CI.git +refs/heads/test_smoke:refs/remotes/origin/test_smoke # timeout=120
[2026/09/10 17:26:24.672 GMT+08:00] Checking out Revision 8db165473ae4621a98eb52f4d7d5601dd5246f58 (origin/test_smoke)
[2026/09/10 17:26:24.672 GMT+08:00] Disable Git LFS pull
[2026/09/10 17:26:24.735 GMT+08:00] Commit message: "smoke image"
[2026/09/10 17:26:24.735 GMT+08:00] First time build. Skipping changelog.
[2026/09/10 17:26:24.764 GMT+08:00] [INFO] [代码检出:external_post_checkout] : 该步骤开始执行
[2026/09/10 17:26:24.818 GMT+08:00] [INFO] [代码检出:external_post_checkout] : 该步骤执行完成
[2026/09/10 17:26:25.239 GMT+08:00] + set -euo pipefail
[2026/09/10 17:26:25.239 GMT+08:00] + apt install python3.10-venv -y
[2026/09/10 17:26:25.239 GMT+08:00] 
[2026/09/10 17:26:25.239 GMT+08:00] WARNING: apt does not have a stable CLI interface. Use with caution in scripts.
[2026/09/10 17:26:25.239 GMT+08:00] 
[2026/09/10 17:26:25.271 GMT+08:00] Reading package lists...starting check in ***/@tmp/durable-0400243c
[2026/09/10 17:26:24.666 GMT+08:00]  > git rev-parse origin/test_smoke^{commit} # timeout=10
[2026/09/10 17:26:24.681 GMT+08:00]  > git config core.sparsecheckout # timeout=10
[2026/09/10 17:26:24.684 GMT+08:00]  > git checkout -f 8db165473ae4621a98eb52f4d7d5601dd5246f58 # timeout=120
[2026/09/10 17:26:24.702 GMT+08:00]  > git branch -a -v --no-abbrev # timeout=10
[2026/09/10 17:26:24.706 GMT+08:00]  > git checkout -b test_smoke 8db165473ae4621a98eb52f4d7d5601dd5246f58 # timeout=120
[2026/09/10 17:26:26.840 GMT+08:00] 
[2026/09/10 17:26:27.154 GMT+08:00] Building dependency tree...
[2026/09/10 17:26:27.155 GMT+08:00] Reading state information...
[2026/09/10 17:26:27.830 GMT+08:00] The following additional packages will be installed:
[2026/09/10 17:26:27.831 GMT+08:00]   libpython3.10 libpython3.10-dev libpython3.10-minimal libpython3.10-stdlib
[2026/09/10 17:26:27.831 GMT+08:00]   python3-pip-whl python3-setuptools-whl python3.10 python3.10-dev
[2026/09/10 17:26:27.831 GMT+08:00]   python3.10-minimal
[2026/09/10 17:26:27.831 GMT+08:00] Suggested packages:
[2026/09/10 17:26:27.831 GMT+08:00]   python3.10-doc binfmt-support
[2026/09/10 17:26:27.831 GMT+08:00] The following NEW packages will be installed:
[2026/09/10 17:26:27.831 GMT+08:00]   python3-pip-whl python3-setuptools-whl python3.10-venv
[2026/09/10 17:26:27.831 GMT+08:00] The following packages will be upgraded:
[2026/09/10 17:26:27.831 GMT+08:00]   libpython3.10 libpython3.10-dev libpython3.10-minimal libpython3.10-stdlib
[2026/09/10 17:26:27.831 GMT+08:00]   python3.10 python3.10-dev python3.10-minimal
[2026/09/10 17:26:28.143 GMT+08:00] 7 upgraded, 3 newly installed, 0 to remove and 89 not upgraded.
[2026/09/10 17:26:28.143 GMT+08:00] Need to get 15.0 MB of archives.
[2026/09/10 17:26:28.143 GMT+08:00] After this operation, 2899 kB of additional disk space will be used.
[2026/09/10 17:26:28.143 GMT+08:00] Get:1 http://ports.ubuntu.com/ubuntu-ports jammy-updates/main arm64 python3.10-dev arm64 3.10.12-1~22.04.18 [508 kB]
[2026/09/10 17:26:31.003 GMT+08:00] Get:2 http://ports.ubuntu.com/ubuntu-ports jammy-updates/main arm64 libpython3.10-dev arm64 3.10.12-1~22.04.18 [4671 kB]
[2026/09/10 17:26:33.181 GMT+08:00] Get:3 http://ports.ubuntu.com/ubuntu-ports jammy-updates/main arm64 libpython3.10 arm64 3.10.12-1~22.04.18 [1888 kB]
[2026/09/10 17:26:33.494 GMT+08:00] Get:4 http://ports.ubuntu.com/ubuntu-ports jammy-updates/main arm64 python3.10 arm64 3.10.12-1~22.04.18 [508 kB]
[2026/09/10 17:26:33.494 GMT+08:00] Get:5 http://ports.ubuntu.com/ubuntu-ports jammy-updates/main arm64 libpython3.10-stdlib arm64 3.10.12-1~22.04.18 [1848 kB]
[2026/09/10 17:26:34.594 GMT+08:00] Get:6 http://ports.ubuntu.com/ubuntu-ports jammy-updates/main arm64 python3.10-minimal arm64 3.10.12-1~22.04.18 [2245 kB]
[2026/09/10 17:26:35.270 GMT+08:00] Get:7 http://ports.ubuntu.com/ubuntu-ports jammy-updates/main arm64 libpython3.10-minimal arm64 3.10.12-1~22.04.18 [814 kB]
[2026/09/10 17:26:35.270 GMT+08:00] Get:8 http://ports.ubuntu.com/ubuntu-ports jammy-updates/universe arm64 python3-pip-whl all 22.0.2+dfsg-1ubuntu0.7 [1683 kB]
[2026/09/10 17:26:35.947 GMT+08:00] Get:9 http://ports.ubuntu.com/ubuntu-ports jammy-updates/universe arm64 python3-setuptools-whl all 59.6.0-1.2ubuntu0.22.04.3 [789 kB]
[2026/09/10 17:26:35.947 GMT+08:00] Get:10 http://ports.ubuntu.com/ubuntu-ports jammy-updates/universe arm64 python3.10-venv arm64 3.10.12-1~22.04.18 [5726 B]
[2026/09/10 17:26:36.262 GMT+08:00] debconf: delaying package configuration, since apt-utils is not installed
[2026/09/10 17:26:36.262 GMT+08:00] Fetched 15.0 MB in 8s (1802 kB/s)
[2026/09/10 17:26:36.262 GMT+08:00] (Reading database ... 
(Reading database ... 5%
(Reading database ... 10%
(Reading database ... 15%
(Reading database ... 20%
(Reading database ... 25%
(Reading database ... 30%
(Reading database ... 35%
(Reading database ... 40%
(Reading database ... 45%
(Reading database ... 50%
(Reading database ... 55%
(Reading database ... 60%
(Reading database ... 65%
(Reading database ... 70%
(Reading database ... 75%
(Reading database ... 80%
(Reading database ... 85%
(Reading database ... 90%
(Reading database ... 95%
(Reading database ... 100%
(Reading database ... 28393 files and directories currently installed.)
[2026/09/10 17:26:36.262 GMT+08:00] Preparing to unpack .../0-python3.10-dev_3.10.12-1~22.04.18_arm64.deb ...
[2026/09/10 17:26:36.262 GMT+08:00] Unpacking python3.10-dev (3.10.12-1~22.04.18) over (3.10.12-1~22.04.14) ...
[2026/09/10 17:26:36.262 GMT+08:00] Preparing to unpack .../1-libpython3.10-dev_3.10.12-1~22.04.18_arm64.deb ...
[2026/09/10 17:26:36.262 GMT+08:00] Unpacking libpython3.10-dev:arm64 (3.10.12-1~22.04.18) over (3.10.12-1~22.04.14) ...
[2026/09/10 17:26:36.576 GMT+08:00] Preparing to unpack .../2-libpython3.10_3.10.12-1~22.04.18_arm64.deb ...
[2026/09/10 17:26:36.576 GMT+08:00] Unpacking libpython3.10:arm64 (3.10.12-1~22.04.18) over (3.10.12-1~22.04.14) ...
[2026/09/10 17:26:36.576 GMT+08:00] Preparing to unpack .../3-python3.10_3.10.12-1~22.04.18_arm64.deb ...
[2026/09/10 17:26:36.576 GMT+08:00] Unpacking python3.10 (3.10.12-1~22.04.18) over (3.10.12-1~22.04.14) ...
[2026/09/10 17:26:36.576 GMT+08:00] Preparing to unpack .../4-libpython3.10-stdlib_3.10.12-1~22.04.18_arm64.deb ...
[2026/09/10 17:26:36.891 GMT+08:00] Unpacking libpython3.10-stdlib:arm64 (3.10.12-1~22.04.18) over (3.10.12-1~22.04.14) ...
[2026/09/10 17:26:36.891 GMT+08:00] Preparing to unpack .../5-python3.10-minimal_3.10.12-1~22.04.18_arm64.deb ...
[2026/09/10 17:26:36.891 GMT+08:00] Unpacking python3.10-minimal (3.10.12-1~22.04.18) over (3.10.12-1~22.04.14) ...
[2026/09/10 17:26:37.205 GMT+08:00] Preparing to unpack .../6-libpython3.10-minimal_3.10.12-1~22.04.18_arm64.deb ...
[2026/09/10 17:26:37.205 GMT+08:00] Unpacking libpython3.10-minimal:arm64 (3.10.12-1~22.04.18) over (3.10.12-1~22.04.14) ...
[2026/09/10 17:26:37.205 GMT+08:00] Selecting previously unselected package python3-pip-whl.
[2026/09/10 17:26:37.205 GMT+08:00] Preparing to unpack .../7-python3-pip-whl_22.0.2+dfsg-1ubuntu0.7_all.deb ...
[2026/09/10 17:26:37.205 GMT+08:00] Unpacking python3-pip-whl (22.0.2+dfsg-1ubuntu0.7) ...
[2026/09/10 17:26:37.205 GMT+08:00] Selecting previously unselected package python3-setuptools-whl.
[2026/09/10 17:26:37.205 GMT+08:00] Preparing to unpack .../8-python3-setuptools-whl_59.6.0-1.2ubuntu0.22.04.3_all.deb ...
[2026/09/10 17:26:37.205 GMT+08:00] Unpacking python3-setuptools-whl (59.6.0-1.2ubuntu0.22.04.3) ...
[2026/09/10 17:26:37.205 GMT+08:00] Selecting previously unselected package python3.10-venv.
[2026/09/10 17:26:37.205 GMT+08:00] Preparing to unpack .../9-python3.10-venv_3.10.12-1~22.04.18_arm64.deb ...
[2026/09/10 17:26:37.205 GMT+08:00] Unpacking python3.10-venv (3.10.12-1~22.04.18) ...
[2026/09/10 17:26:37.519 GMT+08:00] Setting up python3-setuptools-whl (59.6.0-1.2ubuntu0.22.04.3) ...
[2026/09/10 17:26:37.519 GMT+08:00] Setting up python3-pip-whl (22.0.2+dfsg-1ubuntu0.7) ...
[2026/09/10 17:26:37.519 GMT+08:00] Setting up libpython3.10-minimal:arm64 (3.10.12-1~22.04.18) ...
[2026/09/10 17:26:37.519 GMT+08:00] Setting up python3.10-minimal (3.10.12-1~22.04.18) ...
[2026/09/10 17:26:38.197 GMT+08:00] Setting up libpython3.10-stdlib:arm64 (3.10.12-1~22.04.18) ...
[2026/09/10 17:26:38.197 GMT+08:00] Setting up libpython3.10:arm64 (3.10.12-1~22.04.18) ...
[2026/09/10 17:26:38.197 GMT+08:00] Setting up python3.10 (3.10.12-1~22.04.18) ...
[2026/09/10 17:26:39.299 GMT+08:00] Setting up libpython3.10-dev:arm64 (3.10.12-1~22.04.18) ...
[2026/09/10 17:26:39.299 GMT+08:00] Setting up python3.10-dev (3.10.12-1~22.04.18) ...
[2026/09/10 17:26:39.299 GMT+08:00] Setting up python3.10-venv (3.10.12-1~22.04.18) ...
[2026/09/10 17:26:39.299 GMT+08:00] Processing triggers for libc-bin (2.35-0ubuntu3.13) ...
[2026/09/10 17:26:39.299 GMT+08:00] + PROJECT_ID=1e20b309fcb34b00a0043a87e461c95a
[2026/09/10 17:26:39.299 GMT+08:00] + JOB_RUN_ID=671e50b108d64e71939420950f1be3d0_20260910_7
[2026/09/10 17:26:39.299 GMT+08:00] + BASE_DIR=***//openlibing-pytest-executor-workspace
[2026/09/10 17:26:39.299 GMT+08:00] + EXECUTOR_LOG_DIR=***//openlibing-pytest-executor-workspace/executor-log
[2026/09/10 17:26:39.299 GMT+08:00] + EXECUTOR_LOG_FILE=***//openlibing-pytest-executor-workspace/executor-log/scheduler_framework.log
[2026/09/10 17:26:39.299 GMT+08:00] + PYTEST_TESTKIT_DIR=***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testkit
[2026/09/10 17:26:39.300 GMT+08:00] + TESTCASE_COLLETOR_DIR=***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testcase-collector
[2026/09/10 17:26:39.300 GMT+08:00] + EXECUTOR_BRANCH=lishaocun_develop
[2026/09/10 17:26:39.300 GMT+08:00] + OBS_INFO='{"ak":"*****","sk":"*****","bucket_name":"ascend-cann-open","server":"https://obs.cn-north-4.myhuaweicloud.com","base_url":"https://ascend-cann-open.obs.cn-north-4.myhuaweicloud.com/version_smoke"}'
[2026/09/10 17:26:39.300 GMT+08:00] ++ date +%Y%m%d
[2026/09/10 17:26:39.300 GMT+08:00] + TASK_ID=1e20b309fcb34b00a0043a87e461c95a202609102218
[2026/09/10 17:26:39.300 GMT+08:00] + MAX_WORKERS=2
[2026/09/10 17:26:39.300 GMT+08:00] + echo '[INFO] clear workspace dir'
[2026/09/10 17:26:39.300 GMT+08:00] [INFO] clear workspace dir
[2026/09/10 17:26:39.300 GMT+08:00] + '[' -d ***//openlibing-pytest-executor-workspace ']'
[2026/09/10 17:26:39.300 GMT+08:00] + echo '[INFO] workspace dir not exits'
[2026/09/10 17:26:39.300 GMT+08:00] [INFO] workspace dir not exits
[2026/09/10 17:26:39.300 GMT+08:00] + echo '[INFO] create work dir'
[2026/09/10 17:26:39.300 GMT+08:00] [INFO] create work dir
[2026/09/10 17:26:39.300 GMT+08:00] + mkdir -p ***//openlibing-pytest-executor-workspace
[2026/09/10 17:26:39.300 GMT+08:00] + echo '[INFO] git clone openlibing-pytest-excutor...'
[2026/09/10 17:26:39.300 GMT+08:00] [INFO] git clone openlibing-pytest-excutor...
[2026/09/10 17:26:39.300 GMT+08:00] + GIT_TERMINAL_PROMPT=0
[2026/09/10 17:26:39.300 GMT+08:00] + git clone --depth 1 -b lishaocun_develop https://gitcode.com/openlibing/openlibing-pytest-executor.git ***//openlibing-pytest-executor-workspace/openlibing-pytest-executor
[2026/09/10 17:26:39.300 GMT+08:00] Cloning into '***//openlibing-pytest-executor-workspace/openlibing-pytest-executor'...
[2026/09/10 17:26:39.977 GMT+08:00] + mkdir -p ***//openlibing-pytest-executor-workspace/executor-log
[2026/09/10 17:26:39.977 GMT+08:00] + mkdir -p ***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testkit
[2026/09/10 17:26:39.977 GMT+08:00] + mkdir -p ***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testcase-collector
[2026/09/10 17:26:39.977 GMT+08:00] + PYTEST_TESTKIT_FILE=***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testkit/pytest_testkit-1.0.0-py3-none-any.whl
[2026/09/10 17:26:39.977 GMT+08:00] + cd ***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testkit
[2026/09/10 17:26:39.977 GMT+08:00] + wget https://gitcode.com/openlibing/openlibing-pytest-executor/releases/download/v1.0.0-alpha/pytest_testkit-1.0.0-py3-none-any.whl
[2026/09/10 17:26:39.977 GMT+08:00] --2026-09-10 09:26:39--  https://gitcode.com/openlibing/openlibing-pytest-executor/releases/download/v1.0.0-alpha/pytest_testkit-1.0.0-py3-none-any.whl
[2026/09/10 17:26:39.978 GMT+08:00] Resolving gitcode.com (gitcode.com)... ***.***.***.91
[2026/09/10 17:26:39.978 GMT+08:00] Connecting to gitcode.com (gitcode.com)|***.***.***.91|:443... connected.
[2026/09/10 17:26:39.978 GMT+08:00] HTTP request sent, awaiting response... 302 Found
[2026/09/10 17:26:39.978 GMT+08:00] Location: https://file-cdn.gitcode.com/9099034/releases/untagger_49126fd431864af2bd607d9192ff2c33/pytest_testkit-1.0.0-py3-none-any.whl?auth_key=1789032399-e617a3417b3346e3a880c8c382dc9abd-0-cba762fc15c030d104244afc47a1185a179851e16644a60966974369602b79ba [following]
[2026/09/10 17:26:39.978 GMT+08:00] --2026-09-10 09:26:39--  https://file-cdn.gitcode.com/9099034/releases/untagger_49126fd431864af2bd607d9192ff2c33/pytest_testkit-1.0.0-py3-none-any.whl?auth_key=1789032399-e617a3417b3346e3a880c8c382dc9abd-0-cba762fc15c030d104244afc47a1185a179851e16644a60966974369602b79ba
[2026/09/10 17:26:39.978 GMT+08:00] Resolving file-cdn.gitcode.com (file-cdn.gitcode.com)... ***.***.***.155, ***.***.***.157, ***.***.***.153, ...
[2026/09/10 17:26:39.978 GMT+08:00] Connecting to file-cdn.gitcode.com (file-cdn.gitcode.com)|***.***.***.155|:443... connected.
[2026/09/10 17:26:39.978 GMT+08:00] HTTP request sent, awaiting response... 200 OK
[2026/09/10 17:26:39.978 GMT+08:00] Length: 102245 (100K) [application/octet-stream]
[2026/09/10 17:26:39.978 GMT+08:00] Saving to: 'pytest_testkit-1.0.0-py3-none-any.whl'
[2026/09/10 17:26:39.978 GMT+08:00] 
[2026/09/10 17:26:39.978 GMT+08:00]      0K .......... .......... .......... .......... .......... 50% 1.76M 0s
[2026/09/10 17:26:39.978 GMT+08:00]     50K .......... .......... .......... .......... ......... 100% 5.41M=0.04s
[2026/09/10 17:26:39.978 GMT+08:00] 
[2026/09/10 17:26:39.978 GMT+08:00] 2026-09-10 09:26:39 (2.66 MB/s) - 'pytest_testkit-1.0.0-py3-none-any.whl' saved [102245/102245]
[2026/09/10 17:26:39.978 GMT+08:00] 
[2026/09/10 17:26:39.978 GMT+08:00] + ls ***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testkit/pytest_testkit-1.0.0-py3-none-any.whl
[2026/09/10 17:26:39.978 GMT+08:00] ***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testkit/pytest_testkit-1.0.0-py3-none-any.whl
[2026/09/10 17:26:39.978 GMT+08:00] + TESTCASE_COLLETOR_FILE=***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testcase-collector/pytest_testcase_collector-1.0.0-py3-none-any.whl
[2026/09/10 17:26:39.978 GMT+08:00] + cd ***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testcase-collector
[2026/09/10 17:26:39.978 GMT+08:00] + wget https://gitcode.com/openlibing/openlibing-pytest-executor/releases/download/pytest-testcase-collector-1.0.0/pytest_testcase_collector-1.0.0-py3-none-any.whl
[2026/09/10 17:26:39.978 GMT+08:00] --2026-09-10 09:26:39--  https://gitcode.com/openlibing/openlibing-pytest-executor/releases/download/pytest-testcase-collector-1.0.0/pytest_testcase_collector-1.0.0-py3-none-any.whl
[2026/09/10 17:26:39.978 GMT+08:00] Resolving gitcode.com (gitcode.com)... ***.***.***.91
[2026/09/10 17:26:39.978 GMT+08:00] Connecting to gitcode.com (gitcode.com)|***.***.***.91|:443... connected.
[2026/09/10 17:26:39.978 GMT+08:00] HTTP request sent, awaiting response... 302 Found
[2026/09/10 17:26:39.978 GMT+08:00] Location: https://file-cdn.gitcode.com/9099034/releases/untagger_8a06d959d9f74ac09748fb720f5d85e8/pytest_testcase_collector-1.0.0-py3-none-any.whl?auth_key=1789032399-193b6c95ea0d4491b408eac8b6b56224-0-30088f87a6a40d47da2c514b5a16353252486ddfaee98b70f3408bfe8fc882ec [following]
[2026/09/10 17:26:39.978 GMT+08:00] --2026-09-10 09:26:39--  https://file-cdn.gitcode.com/9099034/releases/untagger_8a06d959d9f74ac09748fb720f5d85e8/pytest_testcase_collector-1.0.0-py3-none-any.whl?auth_key=1789032399-193b6c95ea0d4491b408eac8b6b56224-0-30088f87a6a40d47da2c514b5a16353252486ddfaee98b70f3408bfe8fc882ec
[2026/09/10 17:26:39.978 GMT+08:00] Resolving file-cdn.gitcode.com (file-cdn.gitcode.com)... ***.***.***.155, ***.***.***.157, ***.***.***.153, ...
[2026/09/10 17:26:39.978 GMT+08:00] Connecting to file-cdn.gitcode.com (file-cdn.gitcode.com)|***.***.***.155|:443... connected.
[2026/09/10 17:26:40.296 GMT+08:00] HTTP request sent, awaiting response... 200 OK
[2026/09/10 17:26:40.296 GMT+08:00] Length: 15058 (15K) [application/octet-stream]
[2026/09/10 17:26:40.296 GMT+08:00] Saving to: 'pytest_testcase_collector-1.0.0-py3-none-any.whl'
[2026/09/10 17:26:40.296 GMT+08:00] 
[2026/09/10 17:26:40.296 GMT+08:00]      0K .......... ....                                       100%  224M=0s
[2026/09/10 17:26:40.296 GMT+08:00] 
[2026/09/10 17:26:40.296 GMT+08:00] 2026-09-10 09:26:39 (224 MB/s) - 'pytest_testcase_collector-1.0.0-py3-none-any.whl' saved [15058/15058]
[2026/09/10 17:26:40.296 GMT+08:00] 
[2026/09/10 17:26:40.296 GMT+08:00] + ls ***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testcase-collector/pytest_testcase_collector-1.0.0-py3-none-any.whl
[2026/09/10 17:26:40.296 GMT+08:00] ***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testcase-collector/pytest_testcase_collector-1.0.0-py3-none-any.whl
[2026/09/10 17:26:40.296 GMT+08:00] + echo '[INFO] git clone testcase code...'
[2026/09/10 17:26:40.296 GMT+08:00] [INFO] git clone testcase code...
[2026/09/10 17:26:40.296 GMT+08:00] + TEST_CASE_DIR=***//openlibing-pytest-executor-workspace/pytest-infra
[2026/09/10 17:26:40.296 GMT+08:00] + mkdir -p ***//openlibing-pytest-executor-workspace/pytest-infra
[2026/09/10 17:26:40.296 GMT+08:00] + CASE_BRANCH=main
[2026/09/10 17:26:40.296 GMT+08:00] + GIT_TERMINAL_PROMPT=0
[2026/09/10 17:26:40.296 GMT+08:00] + git clone --depth 1 -b main https://gitcode.com/Xu-yejie/pytest-infra.git ***//openlibing-pytest-executor-workspace/pytest-infra
[2026/09/10 17:26:40.296 GMT+08:00] Cloning into '***//openlibing-pytest-executor-workspace/pytest-infra'...
[2026/09/10 17:26:42.649 GMT+08:00] + echo '[INFO] execute test cases...'
[2026/09/10 17:26:42.649 GMT+08:00] [INFO] execute test cases...
[2026/09/10 17:26:42.649 GMT+08:00] + '[' '!' -f ***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor/main.py ']'
[2026/09/10 17:26:42.649 GMT+08:00] + python3 -m venv venv
[2026/09/10 17:26:46.390 GMT+08:00] + source venv/bin/activate
[2026/09/10 17:26:46.391 GMT+08:00] ++ deactivate nondestructive
[2026/09/10 17:26:46.391 GMT+08:00] ++ '[' -n '' ']'
[2026/09/10 17:26:46.391 GMT+08:00] ++ '[' -n '' ']'
[2026/09/10 17:26:46.391 GMT+08:00] ++ '[' -n /usr/bin/sh -o -n '' ']'
[2026/09/10 17:26:46.391 GMT+08:00] ++ hash -r
[2026/09/10 17:26:46.391 GMT+08:00] ++ '[' -n '' ']'
[2026/09/10 17:26:46.391 GMT+08:00] ++ unset VIRTUAL_ENV
[2026/09/10 17:26:46.391 GMT+08:00] ++ unset VIRTUAL_ENV_PROMPT
[2026/09/10 17:26:46.391 GMT+08:00] ++ '[' '!' nondestructive = nondestructive ']'
[2026/09/10 17:26:46.391 GMT+08:00] ++ VIRTUAL_ENV=***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testcase-collector/venv
[2026/09/10 17:26:46.391 GMT+08:00] ++ export VIRTUAL_ENV
[2026/09/10 17:26:46.391 GMT+08:00] ++ _OLD_VIRTUAL_PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
[2026/09/10 17:26:46.391 GMT+08:00] ++ PATH=***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testcase-collector/venv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
[2026/09/10 17:26:46.391 GMT+08:00] ++ export PATH
[2026/09/10 17:26:46.391 GMT+08:00] ++ '[' -n '' ']'
[2026/09/10 17:26:46.391 GMT+08:00] ++ '[' -z '' ']'
[2026/09/10 17:26:46.391 GMT+08:00] ++ _OLD_VIRTUAL_PS1=
[2026/09/10 17:26:46.391 GMT+08:00] ++ PS1='(venv) '
[2026/09/10 17:26:46.391 GMT+08:00] ++ export PS1
[2026/09/10 17:26:46.391 GMT+08:00] ++ VIRTUAL_ENV_PROMPT='(venv) '
[2026/09/10 17:26:46.391 GMT+08:00] ++ export VIRTUAL_ENV_PROMPT
[2026/09/10 17:26:46.391 GMT+08:00] ++ '[' -n /usr/bin/sh -o -n '' ']'
[2026/09/10 17:26:46.391 GMT+08:00] ++ hash -r
[2026/09/10 17:26:46.391 GMT+08:00] + python -m pip install --upgrade pip -i https://mirrors.huaweicloud.com/repository/pypi/simple -q
[2026/09/10 17:26:49.255 GMT+08:00] + cd ***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor
[2026/09/10 17:26:49.255 GMT+08:00] + pip install -r requirements.txt -i https://mirrors.huaweicloud.com/repository/pypi/simple -q
[2026/09/10 17:27:08.163 GMT+08:00] + tee -a ***//openlibing-pytest-executor-workspace/executor-log/scheduler_framework.log
[2026/09/10 17:27:08.163 GMT+08:00] + python -u ***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor/main.py --testcase_dir ***//openlibing-pytest-executor-workspace/pytest-infra --log_dir ***//openlibing-pytest-executor-workspace/executor-log --pytest_testkit_path ***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testkit/pytest_testkit-1.0.0-py3-none-any.whl --testcase_collector_path ***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testcase-collector/pytest_testcase_collector-1.0.0-py3-none-any.whl --obs '{"ak":"*****","sk":"*****","bucket_name":"ascend-cann-open","server":"https://obs.cn-north-4.myhuaweicloud.com","base_url":"https://ascend-cann-open.obs.cn-north-4.myhuaweicloud.com/version_smoke"}' --task_id 1e20b309fcb34b00a0043a87e461c95a202609102218 --testcase_config_file resources/pytest_cann_ops-cv.ini --image_label swr.cn-north-4.myhuaweicloud.com/hw-ascend/smoke:ops-cv-910b --pipeline_id 528772518c054c5f8f4625cc5dd1cda0 --pipeline_run_id e700906deacc49609e3b95eab5c1678a --job_run_id 671e50b108d64e71939420950f1be3d0_20260910_7 --scheduler_secret '{apig_code:57e3545e43154e8e8c6a74b4c74193868758f6d0979446008f3cd37e88362d91,k8s_auth:arc-fxqZJDtt8oipppQt}' --max_workers 2
[2026/09/10 17:27:08.163 GMT+08:00] 2026-09-10 09:27:05 [sched] [281473752154144] [INFO] Not using HidevLab, skipping key generation
[2026/09/10 17:27:08.163 GMT+08:00] 2026-09-10 09:27:05 [sched] [281473752154144] [INFO] Successfully obtained local IP via UDP method: ***.***.***.5
[2026/09/10 17:27:08.163 GMT+08:00] 2026-09-10 09:27:05 [sched] [281473752154144] [INFO] Read pytest config from ***//openlibing-pytest-executor-workspace/pytest-infra/resources/pytest_cann_ops-cv.ini: {'infra_log_level': 'INFO', 'error_log_fail': 'true'}
[2026/09/10 17:27:08.163 GMT+08:00] 2026-09-10 09:27:05 [sched] [281473752154144] [INFO] pytest_config: {'infra_log_level': 'INFO', 'error_log_fail': 'true'}
[2026/09/10 17:27:08.163 GMT+08:00] 2026-09-10 09:27:05 [sched] [281473752154144] [INFO] Step 1: Collecting and filtering test cases with @pytest.mark.env...
[2026/09/10 17:27:08.163 GMT+08:00] 2026-09-10 09:27:05 [sched] [281473752154144] [INFO] Collecting pytest cases from directory: ***//openlibing-pytest-executor-workspace/pytest-infra
[2026/09/10 17:27:12.792 GMT+08:00] 2026-09-10 09:27:11 [sched] [281473752154144] [INFO] Successfully installed pytest_testkit-1.0.0-py3-none-any.whl
[2026/09/10 17:27:12.792 GMT+08:00] 2026-09-10 09:27:11 [sched] [281473752154144] [INFO] Installing dependencies from ***//openlibing-pytest-executor-workspace/pytest-infra/requirements.txt
[2026/09/10 17:27:31.710 GMT+08:00] 2026-09-10 09:27:29 [sched] [281473752154144] [INFO] Successfully installed requirements from ***//openlibing-pytest-executor-workspace/pytest-infra/requirements.txt
[2026/09/10 17:27:31.710 GMT+08:00] 2026-09-10 09:27:29 [sched] [281473752154144] [INFO] Case filtering in directory: ***//openlibing-pytest-executor-workspace/pytest-infra
[2026/09/10 17:27:31.710 GMT+08:00] 2026-09-10 09:27:29 [sched] [281473752154144] [INFO] Case filter config file: resources/pytest_cann_ops-cv.ini
[2026/09/10 17:27:31.710 GMT+08:00] 2026-09-10 09:27:30 [sched] [281473752154144] [INFO] pytest collect stdout:
[2026/09/10 17:27:31.710 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnGridSampler2DBackward_network.py::TestAclnnGridSampler2DBackwardExecutor::test_gdd_smk_aclnngridsampler2dbackward
[2026/09/10 17:27:31.710 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnGridSampler2D_deter.py::TestAclnnGridSampler2DExecutor::test_gdd_detesmk_aclnngridsampler2d
[2026/09/10 17:27:31.710 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnGridSampler2D_network.py::TestAclnnGridSampler2DExecutor::test_gdd_smk_aclnngridsampler2d
[2026/09/10 17:27:31.710 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnGridSampler3DBackward_network.py::TestAclnnGridSampler3DBackwardExecutor::test_gdd_smk_aclnngridsampler3dbackward
[2026/09/10 17:27:31.710 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnGridSampler3D_deter.py::TestAclnnGridSampler3DExecutor::test_gdd_detesmk_aclnngridsampler3d
[2026/09/10 17:27:31.710 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnGridSampler3D_network.py::TestAclnnGridSampler3DExecutor::test_gdd_smk_aclnngridsampler3d
[2026/09/10 17:27:31.710 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnResize_deter.py::TestAclnnResizeExecutor::test_gdd_detesmk_aclnnresize
[2026/09/10 17:27:31.710 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnResize_network.py::TestAclnnResizeExecutor::test_gdd_smk_aclnnresize
[2026/09/10 17:27:31.710 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleBicubic2dAA.py::TestAclnnUpsampleBicubic2dAAExecutor::test_gdd_detesmk_aclnnupsamplebicubic2daa
[2026/09/10 17:27:31.710 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleBicubic2dAAGrad.py::TestAclnnUpsampleBicubic2dAAGradExecutor::test_gdd_detesmk_aclnnupsamplebicubic2daagrad
[2026/09/10 17:27:31.710 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleBicubic2dAA_network.py::TestAclnnUpsampleBicubic2dAAExecutor::test_gdd_smk_aclnnupsamplebicubic2daa
[2026/09/10 17:27:31.710 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleBicubic2dBackward_network.py::TestAclnnUpsampleBicubic2dBackwardExecutor::test_gdd_smk_aclnnupsamplebicubic2dbackward
[2026/09/10 17:27:31.710 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleBicubic2d_deter.py::TestAclnnUpsampleBicubic2dExecutor::test_gdd_detesmk_aclnnupsamplebicubic2d
[2026/09/10 17:27:31.710 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleBicubic2d_network.py::TestAclnnUpsampleBicubic2dExecutor::test_gdd_smk_aclnnupsamplebicubic2d
[2026/09/10 17:27:31.710 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleBilinear2dAA.py::TestAclnnUpsampleBilinear2dAAExecutor::test_gdd_smk_aclnnupsamplebilinear2daa
[2026/09/10 17:27:31.711 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleBilinear2dAABackward.py::TestAclnnUpsampleBilinear2dAABackwardExecutor::test_gdd_detesmk_aclnnupsamplebilinear2daabackward
[2026/09/10 17:27:31.711 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleBilinear2dAABackward_network.py::TestAclnnUpsampleBilinear2dAABackwardExecutor::test_gdd_smk_aclnnupsamplebilinear2daabackward
[2026/09/10 17:27:31.711 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleBilinear2dAA_deter.py::TestAclnnUpsampleBilinear2dAAExecutor::test_gdd_detesmk_aclnnupsamplebilinear2daa
[2026/09/10 17:27:31.711 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleBilinear2dBackwardV2.py::TestAclnnUpsampleBilinear2dBackwardV2Executor::test_gdd_smk_aclnnupsamplebilinear2dbackwardv2
[2026/09/10 17:27:31.711 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleBilinear2dBackward_deter.py::TestAclnnUpsampleBilinear2dBackwardExecutor::test_gdd_detesmk_aclnnupsamplebilinear2dbackward
[2026/09/10 17:27:31.711 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleBilinear2dBackward_network.py::TestAclnnUpsampleBilinear2dBackwardExecutor::test_gdd_smk_aclnnupsamplebilinear2dbackward
[2026/09/10 17:27:31.711 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleBilinear2d_deter.py::TestAclnnUpsampleBilinear2dExecutor::test_gdd_detesmk_aclnnupsamplebilinear2d
[2026/09/10 17:27:31.711 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleBilinear2d_network.py::TestAclnnUpsampleBilinear2dExecutor::test_gdd_smk_aclnnupsamplebilinear2d
[2026/09/10 17:27:31.711 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleLinear1d.py::TestAclnnUpsampleLinear1dExecutor::test_gdd_detesmk_aclnnupsamplelinear1d
[2026/09/10 17:27:31.711 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleLinear1dBackward.py::TestAclnnUpsampleLinear1dBackwardExecutor::test_gdd_smk_aclnnupsamplelinear1dbackward
[2026/09/10 17:27:31.711 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleLinear1dBackward_deter.py::TestAclnnUpsampleLinear1dBackwardExecutor::test_gdd_detesmk_aclnnupsamplelinear1dbackward
[2026/09/10 17:27:31.711 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleLinear1d_network.py::TestAclnnUpsampleLinear1dExecutor::test_gdd_smk_aclnnupsamplelinear1d
[2026/09/10 17:27:31.711 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearest1d.py::TestAclnnUpsampleNearest1dExecutor::test_gdd_smk_aclnnupsamplenearest1d
[2026/09/10 17:27:31.711 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearest1dBackward.py::TestAclnnUpsampleNearest1dBackwardExecutor::test_gdd_detesmk_aclnnupsamplenearest1dbackward
[2026/09/10 17:27:31.711 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearest1dBackward_network.py::TestAclnnUpsampleNearest1dBackwardExecutor::test_gdd_smk_aclnnupsamplenearest1dbackward
[2026/09/10 17:27:31.711 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearest1dV2.py::TestAclnnUpsampleNearest1dV2Executor::test_gdd_smk_aclnnupsamplenearest1dv2
[2026/09/10 17:27:31.711 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearest1d_deter.py::TestAclnnUpsampleNearest1dExecutor::test_gdd_detesmk_aclnnupsamplenearest1d
[2026/09/10 17:27:31.711 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearest2d.py::TestAclnnUpsampleNearest2dExecutor::test_gdd_detesmk_aclnnupsamplenearest2d
[2026/09/10 17:27:31.711 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearest2dBackward.py::TestAclnnUpsampleNearest2dBackwardExecutor::test_gdd_detesmk_aclnnupsamplenearest2dbackward
[2026/09/10 17:27:31.711 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearest2dBackward_network.py::TestAclnnUpsampleNearest2dBackwardExecutor::test_gdd_smk_aclnnupsamplenearest2dbackward
[2026/09/10 17:27:31.711 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearest2dV2.py::TestAclnnUpsampleNearest2dV2Executor::test_gdd_smk_aclnnupsamplenearest2dv2
[2026/09/10 17:27:31.711 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearest3d.py::TestAclnnUpsampleNearest3dExecutor::test_gdd_detesmk_aclnnupsamplenearest3d
[2026/09/10 17:27:31.711 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearest3dBackward.py::TestAclnnUpsampleNearest3dBackwardExecutor::test_gdd_detesmk_aclnnupsamplenearest3dbackward
[2026/09/10 17:27:31.711 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearest3dBackward_network.py::TestAclnnUpsampleNearest3dBackwardExecutor::test_gdd_smk_aclnnupsamplenearest3dbackward
[2026/09/10 17:27:31.711 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearest3d_network.py::TestAclnnUpsampleNearest3dExecutor::test_gdd_smk_aclnnupsamplenearest3d
[2026/09/10 17:27:31.711 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearestExact1d.py::TestAclnnUpsampleNearestExact1dExecutor::test_gdd_detesmk_aclnnupsamplenearestexact1d
[2026/09/10 17:27:31.711 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearestExact1dBackward.py::TestAclnnUpsampleNearestExact1dBackwardExecutor::test_gdd_smk_aclnnupsamplenearestexact1dbackward
[2026/09/10 17:27:31.711 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearestExact1dBackward_deter.py::TestAclnnUpsampleNearestExact1dBackwardExecutor::test_gdd_detesmk_aclnnupsamplenearestexact1dbackward
[2026/09/10 17:27:31.711 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearestExact1d_network.py::TestAclnnUpsampleNearestExact1dExecutor::test_gdd_smk_aclnnupsamplenearestexact1d
[2026/09/10 17:27:31.711 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearestExact2d.py::TestAclnnUpsampleNearestExact2dExecutor::test_gdd_detesmk_aclnnupsamplenearestexact2d
[2026/09/10 17:27:31.711 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearestExact2dBackward.py::TestAclnnUpsampleNearestExact2dBackwardExecutor::test_gdd_detesmk_aclnnupsamplenearestexact2dbackward
[2026/09/10 17:27:31.711 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearestExact2dBackward_network.py::TestAclnnUpsampleNearestExact2dBackwardExecutor::test_gdd_smk_aclnnupsamplenearestexact2dbackward
[2026/09/10 17:27:31.711 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearestExact2d_network.py::TestAclnnUpsampleNearestExact2dExecutor::test_gdd_smk_aclnnupsamplenearestexact2d
[2026/09/10 17:27:31.711 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearestExact3d.py::TestAclnnUpsampleNearestExact3dExecutor::test_gdd_smk_aclnnupsamplenearestexact3d
[2026/09/10 17:27:31.711 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearestExact3dBackward.py::TestAclnnUpsampleNearestExact3dBackwardExecutor::test_gdd_detesmk_aclnnupsamplenearestexact3dbackward
[2026/09/10 17:27:31.711 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearestExact3dBackward_network.py::TestAclnnUpsampleNearestExact3dBackwardExecutor::test_gdd_smk_aclnnupsamplenearestexact3dbackward
[2026/09/10 17:27:31.711 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearestExact3d_deter.py::TestAclnnUpsampleNearestExact3dExecutor::test_gdd_detesmk_aclnnupsamplenearestexact3d
[2026/09/10 17:27:31.711 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleTrilinear3dBackward.py::TestAclnnUpsampleTrilinear3dBackwardExecutor::test_gdd_detesmk_aclnnupsampletrilinear3dbackward
[2026/09/10 17:27:31.711 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleTrilinear3dBackward_network.py::TestAclnnUpsampleTrilinear3dBackwardExecutor::test_gdd_smk_aclnnupsampletrilinear3dbackward
[2026/09/10 17:27:31.711 GMT+08:00] testcase/cann/ops-cv/test_ops_cv.py::TestAclnnRoiAlignV2::test_cann_opscv_objdetect_aclnn_roi_align_v2_accuracy
[2026/09/10 17:27:31.711 GMT+08:00] testcase/cann/ops-cv/test_ops_cv.py::TestAclnnRoiAlignV2Backward::test_cann_opscv_objdetect_aclnn_roi_align_v2_backward_accuracy
[2026/09/10 17:27:31.711 GMT+08:00] 
[2026/09/10 17:27:31.711 GMT+08:00] =============================== warnings summary ===============================
[2026/09/10 17:27:31.711 GMT+08:00] testcase/cann/ops-cv/conftest.py:19
[2026/09/10 17:27:31.711 GMT+08:00]   ***//openlibing-pytest-executor-workspace/pytest-infra/testcase/cann/ops-cv/conftest.py:19: PytestUnknownMarkWarning: Unknown pytest.mark.archive_src - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
[2026/09/10 17:27:31.712 GMT+08:00]     item.add_marker(pytest.mark.archive_src(_ARCHIVE_SRC, dst=_ARCHIVE_DST))
[2026/09/10 17:27:31.712 GMT+08:00] 
[2026/09/10 17:27:31.712 GMT+08:00] -- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
[2026/09/10 17:27:31.712 GMT+08:00] 56 tests collected in 0.63s
[2026/09/10 17:27:31.712 GMT+08:00] 
[2026/09/10 17:27:31.712 GMT+08:00] 2026-09-10 09:27:30 [sched] [281473752154144] [WARNING] pytest collect stderr:
[2026/09/10 17:27:31.712 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:285] Infra logging initialized: dir=logs, level=INFO, size=10MB, count=-1
[2026/09/10 17:27:31.712 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:342] No testbed source (no --testbed and no TESTBED_DEVICES), environment management disabled
[2026/09/10 17:27:31.712 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:241] Pre-action registry initialized
[2026/09/10 17:27:31.712 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnngridsampler2dbackward>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.712 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnngridsampler2d>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.712 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnngridsampler2d>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.712 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnngridsampler3dbackward>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.712 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnngridsampler3d>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.712 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnngridsampler3d>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.712 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnnresize>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.712 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnresize>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.712 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnnupsamplebicubic2daa>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.712 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnnupsamplebicubic2daagrad>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.712 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnupsamplebicubic2daa>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.712 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnupsamplebicubic2dbackward>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.712 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnnupsamplebicubic2d>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.712 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnupsamplebicubic2d>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.712 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnupsamplebilinear2daa>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.712 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnnupsamplebilinear2daabackward>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.712 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnupsamplebilinear2daabackward>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.712 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnnupsamplebilinear2daa>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.712 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnupsamplebilinear2dbackwardv2>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.712 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnnupsamplebilinear2dbackward>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.712 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnupsamplebilinear2dbackward>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.712 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnnupsamplebilinear2d>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.712 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnupsamplebilinear2d>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.712 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnnupsamplelinear1d>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.712 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnupsamplelinear1dbackward>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.712 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnnupsamplelinear1dbackward>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.712 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnupsamplelinear1d>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.712 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnupsamplenearest1d>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.712 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnnupsamplenearest1dbackward>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.712 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnupsamplenearest1dbackward>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.712 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnupsamplenearest1dv2>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.712 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnnupsamplenearest1d>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.712 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnnupsamplenearest2d>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.712 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnnupsamplenearest2dbackward>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.712 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnupsamplenearest2dbackward>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.712 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnupsamplenearest2dv2>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.712 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnnupsamplenearest3d>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.713 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnnupsamplenearest3dbackward>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.713 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnupsamplenearest3dbackward>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.713 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnupsamplenearest3d>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.713 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnnupsamplenearestexact1d>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.713 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnupsamplenearestexact1dbackward>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.713 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnnupsamplenearestexact1dbackward>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.713 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnupsamplenearestexact1d>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.713 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnnupsamplenearestexact2d>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.713 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnnupsamplenearestexact2dbackward>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.713 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnupsamplenearestexact2dbackward>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.713 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnupsamplenearestexact2d>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.713 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnupsamplenearestexact3d>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.713 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnnupsamplenearestexact3dbackward>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.713 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnupsamplenearestexact3dbackward>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.713 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnnupsamplenearestexact3d>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.713 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnnupsampletrilinear3dbackward>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.713 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnupsampletrilinear3dbackward>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 17:27:31.713 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_cann_opscv_objdetect_aclnn_roi_align_v2_accuracy>[{'level': 'P0', 'type': 'Functional', 'scene': 'functional'}]
[2026/09/10 17:27:31.713 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:698] item: match[True]<Function test_cann_opscv_objdetect_aclnn_roi_align_v2_backward_accuracy>[{'level': 'P0', 'type': 'Functional', 'scene': 'functional'}]
[2026/09/10 17:27:31.713 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:707] filter case with inifile: attributes[{'level': ['P0'], 'type': ['Functional']}]
[2026/09/10 17:27:31.713 GMT+08:00] filtered cases: [<Function test_gdd_smk_aclnngridsampler2dbackward>, <Function test_gdd_detesmk_aclnngridsampler2d>, <Function test_gdd_smk_aclnngridsampler2d>, <Function test_gdd_smk_aclnngridsampler3dbackward>, <Function test_gdd_detesmk_aclnngridsampler3d>, <Function test_gdd_smk_aclnngridsampler3d>, <Function test_gdd_detesmk_aclnnresize>, <Function test_gdd_smk_aclnnresize>, <Function test_gdd_detesmk_aclnnupsamplebicubic2daa>, <Function test_gdd_detesmk_aclnnupsamplebicubic2daagrad>, <Function test_gdd_smk_aclnnupsamplebicubic2daa>, <Function test_gdd_smk_aclnnupsamplebicubic2dbackward>, <Function test_gdd_detesmk_aclnnupsamplebicubic2d>, <Function test_gdd_smk_aclnnupsamplebicubic2d>, <Function test_gdd_smk_aclnnupsamplebilinear2daa>, <Function test_gdd_detesmk_aclnnupsamplebilinear2daabackward>, <Function test_gdd_smk_aclnnupsamplebilinear2daabackward>, <Function test_gdd_detesmk_aclnnupsamplebilinear2daa>, <Function test_gdd_smk_aclnnupsamplebilinear2dbackwardv2>, <Function test_gdd_detesmk_aclnnupsamplebilinear2dbackward>, <Function test_gdd_smk_aclnnupsamplebilinear2dbackward>, <Function test_gdd_detesmk_aclnnupsamplebilinear2d>, <Function test_gdd_smk_aclnnupsamplebilinear2d>, <Function test_gdd_detesmk_aclnnupsamplelinear1d>, <Function test_gdd_smk_aclnnupsamplelinear1dbackward>, <Function test_gdd_detesmk_aclnnupsamplelinear1dbackward>, <Function test_gdd_smk_aclnnupsamplelinear1d>, <Function test_gdd_smk_aclnnupsamplenearest1d>, <Function test_gdd_detesmk_aclnnupsamplenearest1dbackward>, <Function test_gdd_smk_aclnnupsamplenearest1dbackward>, <Function test_gdd_smk_aclnnupsamplenearest1dv2>, <Function test_gdd_detesmk_aclnnupsamplenearest1d>, <Function test_gdd_detesmk_aclnnupsamplenearest2d>, <Function test_gdd_detesmk_aclnnupsamplenearest2dbackward>, <Function test_gdd_smk_aclnnupsamplenearest2dbackward>, <Function test_gdd_smk_aclnnupsamplenearest2dv2>, <Function test_gdd_detesmk_aclnnupsamplenearest3d>, <Function test_gdd_detesmk_aclnnupsamplenearest3dbackward>, <Function test_gdd_smk_aclnnupsamplenearest3dbackward>, <Function test_gdd_smk_aclnnupsamplenearest3d>, <Function test_gdd_detesmk_aclnnupsamplenearestexact1d>, <Function test_gdd_smk_aclnnupsamplenearestexact1dbackward>, <Function test_gdd_detesmk_aclnnupsamplenearestexact1dbackward>, <Function test_gdd_smk_aclnnupsamplenearestexact1d>, <Function test_gdd_detesmk_aclnnupsamplenearestexact2d>, <Function test_gdd_detesmk_aclnnupsamplenearestexact2dbackward>, <Function test_gdd_smk_aclnnupsamplenearestexact2dbackward>, <Function test_gdd_smk_aclnnupsamplenearestexact2d>, <Function test_gdd_smk_aclnnupsamplenearestexact3d>, <Function test_gdd_detesmk_aclnnupsamplenearestexact3dbackward>, <Function test_gdd_smk_aclnnupsamplenearestexact3dbackward>, <Function test_gdd_detesmk_aclnnupsamplenearestexact3d>, <Function test_gdd_detesmk_aclnnupsampletrilinear3dbackward>, <Function test_gdd_smk_aclnnupsampletrilinear3dbackward>, <Function test_cann_opscv_objdetect_aclnn_roi_align_v2_accuracy>, <Function test_cann_opscv_objdetect_aclnn_roi_align_v2_backward_accuracy>]
[2026/09/10 17:27:31.713 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:757] Collected environment info exported to COLLECTED_INFO environment variable
[2026/09/10 17:27:31.713 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:830] output collected info file to: /tmp/tmpq0q4gcxa.json
[2026/09/10 17:27:31.713 GMT+08:00] [2026-09-10 09:27:30][INFO][plugin.py:967] Test session completed
[2026/09/10 17:27:31.713 GMT+08:00] 
[2026/09/10 17:27:31.713 GMT+08:00] 2026-09-10 09:27:30 [sched] [281473752154144] [INFO] Collected 56 test cases
[2026/09/10 17:27:31.713 GMT+08:00] 2026-09-10 09:27:30 [sched] [281473752154144] [INFO] Step 2: Grouping test cases by environments...
[2026/09/10 17:27:31.713 GMT+08:00] 2026-09-10 09:27:30 [sched] [281473752154144] [INFO] Environment block: {'cann_single_A2_device_3_cover_single_type-nodes_1-A2': {'case_list_len': 14}, 'cann_single_A2_device_2_cover_single_type-nodes_1-A2': {'case_list_len': 15}, 'cann_single_A2_device_1_cover_single_type-nodes_1-A2': {'case_list_len': 14}, 'cann_single_A2_device_4_cover_single_type-nodes_1-A2': {'case_list_len': 13}}
[2026/09/10 17:27:31.713 GMT+08:00] 2026-09-10 09:27:30 [sched] [281473752154144] [INFO] Step 3: Allocating environments and executing tests...
[2026/09/10 17:27:31.713 GMT+08:00] 2026-09-10 09:27:30 [sched] [281473752154144] [INFO] Submitting task for env_id: cann_single_A2_device_3_cover_single_type-nodes_1-A2
[2026/09/10 17:27:31.713 GMT+08:00] 2026-09-10 09:27:30 [sched] [281473700065568] [INFO] Allocating environment for env_id: cann_single_A2_device_3_cover_single_type-nodes_1-A2
[2026/09/10 17:27:31.713 GMT+08:00] 2026-09-10 09:27:30 [sched] [281473752154144] [INFO] Submitting task for env_id: cann_single_A2_device_2_cover_single_type-nodes_1-A2
[2026/09/10 17:27:31.713 GMT+08:00] 2026-09-10 09:27:30 [sched] [281473700065568] [INFO] Using image label: swr.cn-north-4.myhuaweicloud.com/hw-ascend/smoke:ops-cv-910b
[2026/09/10 17:27:31.713 GMT+08:00] 2026-09-10 09:27:30 [sched] [281473700065568] [INFO] env_device_resource is empty, skipping mock allocation
[2026/09/10 17:27:31.713 GMT+08:00] 2026-09-10 09:27:30 [sched] [281473691611424] [INFO] Allocating environment for env_id: cann_single_A2_device_2_cover_single_type-nodes_1-A2
[2026/09/10 17:27:31.714 GMT+08:00] 2026-09-10 09:27:30 [sched] [281473700065568] [INFO] Creating k8s environment with name: codearts-528772518c054c5f8f4625cc5dd1cda0-e700906deacc49609e3b95eab5c1678a-671e50b108d64e71939420950f1be3d0_20260910_7, ttl: None
[2026/09/10 17:27:31.714 GMT+08:00] 2026-09-10 09:27:30 [sched] [281473691611424] [INFO] Using image label: swr.cn-north-4.myhuaweicloud.com/hw-ascend/smoke:ops-cv-910b
[2026/09/10 17:27:31.714 GMT+08:00] 2026-09-10 09:27:30 [sched] [281473700065568] [INFO] apply_env_k8s, payload={'env_definition': {'nodes_1': [{'name': 'device', 'res_type': 'container', 'cpu_arch': 'ARM', 'cpu_core_num': 48, 'npu_gen': 'A2', 'npu_num': 2, 'shm_size': '256Gi', 'memory_size': 256, 'resources': {'cpu': {'request': '48', 'limit': '128'}, 'memory': {'request': '256Gi', 'limit': '1024Gi'}}, 'use_nfs': True, 'mount_source_data': ['cann_ops_data1', 'cann_ops_data2', 'cann_ops_data3', 'cann_ops_data4', 'cann_ops_data5', 'cann_duo_os_autos_test', 'cann_duo_os_imagenet', 'cann_duo_os_acl', 'cann_duo_os_pyacl'], 'mount_dest_dir': ['/autotest/ATK_BIN', '/autotest/atk_output', '/autotest/config', '/autotest/golden_path', '/autotest/result', '/autos_test', '/data/imagenet2012', '/home/infer/bin_bak/acl', '/home/pyacl'], 'pool': 'ascend-general-a2', 'image_label': 'swr.cn-north-4.myhuaweicloud.com/hw-ascend/smoke:ops-cv-910b'}]}, 'extend_env_comments': {'job_info': 'codearts-528772518c054c5f8f4625cc5dd1cda0-e700906deacc49609e3b95eab5c1678a-671e50b108d64e71939420950f1be3d0_20260910_7'}, 'ssh_mesh': 'group', 'extend_labels': {'cluster': 'false'}}
[2026/09/10 17:27:31.714 GMT+08:00] 2026-09-10 09:27:30 [sched] [281473691611424] [INFO] env_device_resource is empty, skipping mock allocation
[2026/09/10 17:27:31.714 GMT+08:00] 2026-09-10 09:27:30 [sched] [281473691611424] [INFO] Creating k8s environment with name: codearts-528772518c054c5f8f4625cc5dd1cda0-e700906deacc49609e3b95eab5c1678a-671e50b108d64e71939420950f1be3d0_20260910_7, ttl: None
[2026/09/10 17:27:31.714 GMT+08:00] 2026-09-10 09:27:30 [sched] [281473691611424] [INFO] apply_env_k8s, payload={'env_definition': {'nodes_1': [{'name': 'device', 'res_type': 'container', 'cpu_arch': 'ARM', 'cpu_core_num': 48, 'npu_gen': 'A2', 'npu_num': 2, 'shm_size': '256Gi', 'memory_size': 256, 'resources': {'cpu': {'request': '48', 'limit': '128'}, 'memory': {'request': '256Gi', 'limit': '1024Gi'}}, 'use_nfs': True, 'mount_source_data': ['cann_ops_data1', 'cann_ops_data2', 'cann_ops_data3', 'cann_ops_data4', 'cann_ops_data5', 'cann_duo_os_autos_test', 'cann_duo_os_imagenet', 'cann_duo_os_acl', 'cann_duo_os_pyacl'], 'mount_dest_dir': ['/autotest/ATK_BIN', '/autotest/atk_output', '/autotest/config', '/autotest/golden_path', '/autotest/result', '/autos_test', '/data/imagenet2012', '/home/infer/bin_bak/acl', '/home/pyacl'], 'pool': 'ascend-general-a2', 'image_label': 'swr.cn-north-4.myhuaweicloud.com/hw-ascend/smoke:ops-cv-910b'}]}, 'extend_env_comments': {'job_info': 'codearts-528772518c054c5f8f4625cc5dd1cda0-e700906deacc49609e3b95eab5c1678a-671e50b108d64e71939420950f1be3d0_20260910_7'}, 'ssh_mesh': 'group', 'extend_labels': {'cluster': 'false'}}
[2026/09/10 17:27:31.714 GMT+08:00] 2026-09-10 09:27:31 [sched] [281473691611424] [INFO] Environment allocation successful, env ID: lease-env1789032450-6590
[2026/09/10 17:27:31.714 GMT+08:00] 2026-09-10 09:27:31 [sched] [281473691611424] [INFO] Starting to query task status for task_id[lease-env1789032450-6590]
[2026/09/10 17:27:31.714 GMT+08:00] 2026-09-10 09:27:31 [sched] [281473691611424] [INFO] ***start 0 times query***
[2026/09/10 17:27:31.714 GMT+08:00] 2026-09-10 09:27:31 [sched] [281473700065568] [INFO] Environment allocation successful, env ID: lease-env1789032450-3750
[2026/09/10 17:27:31.714 GMT+08:00] 2026-09-10 09:27:31 [sched] [281473700065568] [INFO] Starting to query task status for task_id[lease-env1789032450-3750]
[2026/09/10 17:27:31.714 GMT+08:00] 2026-09-10 09:27:31 [sched] [281473700065568] [INFO] ***start 0 times query***
[2026/09/10 17:27:31.714 GMT+08:00] 2026-09-10 09:27:31 [sched] [281473691611424] [INFO] allocation_result is empty, wait 30s to query again
[2026/09/10 17:27:31.714 GMT+08:00] 2026-09-10 09:27:31 [sched] [281473700065568] [INFO] allocation_result is empty, wait 30s to query again
[2026/09/10 17:28:04.771 GMT+08:00] 2026-09-10 09:28:01 [sched] [281473691611424] [INFO] ***start 1 times query***
[2026/09/10 17:28:04.771 GMT+08:00] 2026-09-10 09:28:01 [sched] [281473700065568] [INFO] ***start 1 times query***
[2026/09/10 17:28:04.771 GMT+08:00] 2026-09-10 09:28:01 [sched] [281473700065568] [INFO] apply_env_res: {'env_id': 'lease-env1789032450-3750', 'groups': {'nodes_1': [{'name': 'device', 'res_type': 'container', 'status': 'rejected', 'node_ip': '', 'npu_ids': [], 'privileged': False}]}, 'status': 'rejected', 'name': 'env', 'created_at': '2026-09-10T09:27:31Z', 'expires_at': '2026-09-10T13:27:31Z', 'ttl': '14400', 'topology': '', 'extend_env_comments': {'job_info': 'codearts-528772518c054c5f8f4625cc5dd1cda0-e700906deacc49609e3b95eab5c1678a-671e50b108d64e71939420950f1be3d0_20260910_7'}, 'progress': {'total': 1, 'ready': 0, 'failed': 1, 'pending': 0}, 'ssh_mesh': {'enabled': False, 'scope': '', 'enrolled': [], 'failed': []}, 'errors': None}
[2026/09/10 17:28:04.771 GMT+08:00] 2026-09-10 09:28:01 [sched] [281473700065568] [ERROR] Environment allocation rejected, status: rejected
[2026/09/10 17:28:04.771 GMT+08:00] 2026-09-10 09:28:01 [sched] [281473700065568] [ERROR] Failed to allocate environment: Environment allocation rejected: Unknown
[2026/09/10 17:28:04.771 GMT+08:00] Traceback (most recent call last):
[2026/09/10 17:28:04.771 GMT+08:00]   File "***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor/src/scheduler/env_manager.py", line 297, in allocate_environments
[2026/09/10 17:28:04.771 GMT+08:00]     self._query_k8s_env_status(
[2026/09/10 17:28:04.771 GMT+08:00]   File "***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor/src/scheduler/env_manager.py", line 382, in _query_k8s_env_status
[2026/09/10 17:28:04.771 GMT+08:00]     raise RuntimeError(
[2026/09/10 17:28:04.772 GMT+08:00] RuntimeError: Environment allocation rejected: Unknown
[2026/09/10 17:28:04.772 GMT+08:00] 2026-09-10 09:28:01 [sched] [281473700065568] [ERROR] Failed to allocate environment for env_id: cann_single_A2_device_3_cover_single_type-nodes_1-A2, error: Environment allocation rejected: Unknown
[2026/09/10 17:28:04.772 GMT+08:00] Traceback (most recent call last):
[2026/09/10 17:28:04.772 GMT+08:00]   File "***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor/src/run_scheduler.py", line 237, in _allocate_environments_and_execute
[2026/09/10 17:28:04.772 GMT+08:00]     self.env_manager.allocate_environments(env_case_info)
[2026/09/10 17:28:04.772 GMT+08:00]   File "***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor/src/scheduler/env_manager.py", line 297, in allocate_environments
[2026/09/10 17:28:04.772 GMT+08:00]     self._query_k8s_env_status(
[2026/09/10 17:28:04.772 GMT+08:00]   File "***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor/src/scheduler/env_manager.py", line 382, in _query_k8s_env_status
[2026/09/10 17:28:04.772 GMT+08:00]     raise RuntimeError(
[2026/09/10 17:28:04.772 GMT+08:00] RuntimeError: Environment allocation rejected: Unknown
[2026/09/10 17:28:04.772 GMT+08:00] 2026-09-10 09:28:01 [sched] [281473752154144] [INFO] Task completed for env_id: cann_single_A2_device_3_cover_single_type-nodes_1-A2, result: False
[2026/09/10 17:28:04.772 GMT+08:00] 2026-09-10 09:28:01 [sched] [281473752154144] [ERROR] Failed to execute cases for env_id: cann_single_A2_device_3_cover_single_type-nodes_1-A2
[2026/09/10 17:28:04.772 GMT+08:00] 2026-09-10 09:28:01 [sched] [281473691611424] [INFO] apply_env_res: {'env_id': 'lease-env1789032450-6590', 'groups': {'nodes_1': [{'name': 'device', 'res_type': 'container', 'status': 'rejected', 'node_ip': '', 'npu_ids': [], 'privileged': False}]}, 'status': 'rejected', 'name': 'env', 'created_at': '2026-09-10T09:27:31Z', 'expires_at': '2026-09-10T13:27:31Z', 'ttl': '14400', 'topology': '', 'extend_env_comments': {'job_info': 'codearts-528772518c054c5f8f4625cc5dd1cda0-e700906deacc49609e3b95eab5c1678a-671e50b108d64e71939420950f1be3d0_20260910_7'}, 'progress': {'total': 1, 'ready': 0, 'failed': 1, 'pending': 0}, 'ssh_mesh': {'enabled': False, 'scope': '', 'enrolled': [], 'failed': []}, 'errors': None}
[2026/09/10 17:28:04.772 GMT+08:00] 2026-09-10 09:28:01 [sched] [281473691611424] [ERROR] Environment allocation rejected, status: rejected
[2026/09/10 17:28:04.772 GMT+08:00] 2026-09-10 09:28:01 [sched] [281473691611424] [ERROR] Failed to allocate environment: Environment allocation rejected: Unknown
[2026/09/10 17:28:04.772 GMT+08:00] Traceback (most recent call last):
[2026/09/10 17:28:04.772 GMT+08:00]   File "***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor/src/scheduler/env_manager.py", line 297, in allocate_environments
[2026/09/10 17:28:04.772 GMT+08:00]     self._query_k8s_env_status(
[2026/09/10 17:28:04.772 GMT+08:00]   File "***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor/src/scheduler/env_manager.py", line 382, in _query_k8s_env_status
[2026/09/10 17:28:04.772 GMT+08:00]     raise RuntimeError(
[2026/09/10 17:28:04.772 GMT+08:00] RuntimeError: Environment allocation rejected: Unknown
[2026/09/10 17:28:04.772 GMT+08:00] 2026-09-10 09:28:01 [sched] [281473691611424] [ERROR] Failed to allocate environment for env_id: cann_single_A2_device_2_cover_single_type-nodes_1-A2, error: Environment allocation rejected: Unknown
[2026/09/10 17:28:04.772 GMT+08:00] Traceback (most recent call last):
[2026/09/10 17:28:04.772 GMT+08:00]   File "***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor/src/run_scheduler.py", line 237, in _allocate_environments_and_execute
[2026/09/10 17:28:04.772 GMT+08:00]     self.env_manager.allocate_environments(env_case_info)
[2026/09/10 17:28:04.772 GMT+08:00]   File "***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor/src/scheduler/env_manager.py", line 297, in allocate_environments
[2026/09/10 17:28:04.772 GMT+08:00]     self._query_k8s_env_status(
[2026/09/10 17:28:04.772 GMT+08:00]   File "***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor/src/scheduler/env_manager.py", line 382, in _query_k8s_env_status
[2026/09/10 17:28:04.772 GMT+08:00]     raise RuntimeError(
[2026/09/10 17:28:04.772 GMT+08:00] RuntimeError: Environment allocation rejected: Unknown
[2026/09/10 17:28:04.772 GMT+08:00] 2026-09-10 09:28:01 [sched] [281473752154144] [INFO] Task completed for env_id: cann_single_A2_device_2_cover_single_type-nodes_1-A2, result: False
[2026/09/10 17:28:04.772 GMT+08:00] 2026-09-10 09:28:01 [sched] [281473752154144] [ERROR] Failed to execute cases for env_id: cann_single_A2_device_2_cover_single_type-nodes_1-A2
[2026/09/10 17:28:04.772 GMT+08:00] 2026-09-10 09:28:01 [sched] [281473752154144] [INFO] Submitting task for env_id: cann_single_A2_device_1_cover_single_type-nodes_1-A2
[2026/09/10 17:28:04.772 GMT+08:00] 2026-09-10 09:28:01 [sched] [281473691611424] [INFO] Allocating environment for env_id: cann_single_A2_device_1_cover_single_type-nodes_1-A2
[2026/09/10 17:28:04.772 GMT+08:00] 2026-09-10 09:28:01 [sched] [281473752154144] [INFO] Submitting task for env_id: cann_single_A2_device_4_cover_single_type-nodes_1-A2
[2026/09/10 17:28:04.772 GMT+08:00] 2026-09-10 09:28:01 [sched] [281473691611424] [INFO] Using image label: swr.cn-north-4.myhuaweicloud.com/hw-ascend/smoke:ops-cv-910b
[2026/09/10 17:28:04.772 GMT+08:00] 2026-09-10 09:28:01 [sched] [281473700065568] [INFO] Allocating environment for env_id: cann_single_A2_device_4_cover_single_type-nodes_1-A2
[2026/09/10 17:28:04.772 GMT+08:00] 2026-09-10 09:28:01 [sched] [281473691611424] [INFO] env_device_resource is empty, skipping mock allocation
[2026/09/10 17:28:04.772 GMT+08:00] 2026-09-10 09:28:01 [sched] [281473700065568] [INFO] Using image label: swr.cn-north-4.myhuaweicloud.com/hw-ascend/smoke:ops-cv-910b
[2026/09/10 17:28:04.772 GMT+08:00] 2026-09-10 09:28:01 [sched] [281473691611424] [INFO] Creating k8s environment with name: codearts-528772518c054c5f8f4625cc5dd1cda0-e700906deacc49609e3b95eab5c1678a-671e50b108d64e71939420950f1be3d0_20260910_7, ttl: None
[2026/09/10 17:28:04.772 GMT+08:00] 2026-09-10 09:28:01 [sched] [281473700065568] [INFO] env_device_resource is empty, skipping mock allocation
[2026/09/10 17:28:04.772 GMT+08:00] 2026-09-10 09:28:01 [sched] [281473691611424] [INFO] apply_env_k8s, payload={'env_definition': {'nodes_1': [{'name': 'device', 'res_type': 'container', 'cpu_arch': 'ARM', 'cpu_core_num': 48, 'npu_gen': 'A2', 'npu_num': 2, 'shm_size': '256Gi', 'memory_size': 256, 'resources': {'cpu': {'request': '48', 'limit': '128'}, 'memory': {'request': '256Gi', 'limit': '1024Gi'}}, 'use_nfs': True, 'mount_source_data': ['cann_ops_data1', 'cann_ops_data2', 'cann_ops_data3', 'cann_ops_data4', 'cann_ops_data5', 'cann_duo_os_autos_test', 'cann_duo_os_imagenet', 'cann_duo_os_acl', 'cann_duo_os_pyacl'], 'mount_dest_dir': ['/autotest/ATK_BIN', '/autotest/atk_output', '/autotest/config', '/autotest/golden_path', '/autotest/result', '/autos_test', '/data/imagenet2012', '/home/infer/bin_bak/acl', '/home/pyacl'], 'pool': 'ascend-general-a2', 'image_label': 'swr.cn-north-4.myhuaweicloud.com/hw-ascend/smoke:ops-cv-910b'}]}, 'extend_env_comments': {'job_info': 'codearts-528772518c054c5f8f4625cc5dd1cda0-e700906deacc49609e3b95eab5c1678a-671e50b108d64e71939420950f1be3d0_20260910_7'}, 'ssh_mesh': 'group', 'extend_labels': {'cluster': 'false'}}
[2026/09/10 17:28:04.772 GMT+08:00] 2026-09-10 09:28:01 [sched] [281473700065568] [INFO] Creating k8s environment with name: codearts-528772518c054c5f8f4625cc5dd1cda0-e700906deacc49609e3b95eab5c1678a-671e50b108d64e71939420950f1be3d0_20260910_7, ttl: None
[2026/09/10 17:28:04.772 GMT+08:00] 2026-09-10 09:28:01 [sched] [281473700065568] [INFO] apply_env_k8s, payload={'env_definition': {'nodes_1': [{'name': 'device', 'res_type': 'container', 'cpu_arch': 'ARM', 'cpu_core_num': 48, 'npu_gen': 'A2', 'npu_num': 2, 'shm_size': '256Gi', 'memory_size': 256, 'resources': {'cpu': {'request': '48', 'limit': '128'}, 'memory': {'request': '256Gi', 'limit': '1024Gi'}}, 'use_nfs': True, 'mount_source_data': ['cann_ops_data1', 'cann_ops_data2', 'cann_ops_data3', 'cann_ops_data4', 'cann_ops_data5', 'cann_duo_os_autos_test', 'cann_duo_os_imagenet', 'cann_duo_os_acl', 'cann_duo_os_pyacl'], 'mount_dest_dir': ['/autotest/ATK_BIN', '/autotest/atk_output', '/autotest/config', '/autotest/golden_path', '/autotest/result', '/autos_test', '/data/imagenet2012', '/home/infer/bin_bak/acl', '/home/pyacl'], 'pool': 'ascend-general-a2', 'image_label': 'swr.cn-north-4.myhuaweicloud.com/hw-ascend/smoke:ops-cv-910b'}]}, 'extend_env_comments': {'job_info': 'codearts-528772518c054c5f8f4625cc5dd1cda0-e700906deacc49609e3b95eab5c1678a-671e50b108d64e71939420950f1be3d0_20260910_7'}, 'ssh_mesh': 'group', 'extend_labels': {'cluster': 'false'}}
[2026/09/10 17:28:04.773 GMT+08:00] 2026-09-10 09:28:01 [sched] [281473691611424] [INFO] Environment allocation successful, env ID: lease-env1789032481-2464
[2026/09/10 17:28:04.773 GMT+08:00] 2026-09-10 09:28:01 [sched] [281473691611424] [INFO] Starting to query task status for task_id[lease-env1789032481-2464]
[2026/09/10 17:28:04.773 GMT+08:00] 2026-09-10 09:28:01 [sched] [281473691611424] [INFO] ***start 0 times query***
[2026/09/10 17:28:04.773 GMT+08:00] 2026-09-10 09:28:01 [sched] [281473700065568] [INFO] Environment allocation successful, env ID: lease-env1789032481-1782
[2026/09/10 17:28:04.773 GMT+08:00] 2026-09-10 09:28:01 [sched] [281473700065568] [INFO] Starting to query task status for task_id[lease-env1789032481-1782]
[2026/09/10 17:28:04.773 GMT+08:00] 2026-09-10 09:28:01 [sched] [281473700065568] [INFO] ***start 0 times query***
[2026/09/10 17:28:04.773 GMT+08:00] 2026-09-10 09:28:01 [sched] [281473700065568] [INFO] allocation_result is empty, wait 30s to query again
[2026/09/10 17:28:04.773 GMT+08:00] 2026-09-10 09:28:01 [sched] [281473691611424] [INFO] allocation_result is empty, wait 30s to query again
[2026/09/10 17:28:32.251 GMT+08:00] 2026-09-10 09:28:31 [sched] [281473700065568] [INFO] ***start 1 times query***
[2026/09/10 17:28:32.251 GMT+08:00] 2026-09-10 09:28:31 [sched] [281473691611424] [INFO] ***start 1 times query***
[2026/09/10 17:28:32.251 GMT+08:00] 2026-09-10 09:28:31 [sched] [281473700065568] [INFO] apply_env_res: {'env_id': 'lease-env1789032481-1782', 'groups': {'nodes_1': [{'name': 'device', 'res_type': 'container', 'status': 'rejected', 'node_ip': '', 'npu_ids': [], 'privileged': False}]}, 'status': 'rejected', 'name': 'env', 'created_at': '2026-09-10T09:28:01Z', 'expires_at': '2026-09-10T13:28:01Z', 'ttl': '14400', 'topology': '', 'extend_env_comments': {'job_info': 'codearts-528772518c054c5f8f4625cc5dd1cda0-e700906deacc49609e3b95eab5c1678a-671e50b108d64e71939420950f1be3d0_20260910_7'}, 'progress': {'total': 1, 'ready': 0, 'failed': 1, 'pending': 0}, 'ssh_mesh': {'enabled': False, 'scope': '', 'enrolled': [], 'failed': []}, 'errors': None}
[2026/09/10 17:28:32.251 GMT+08:00] 2026-09-10 09:28:31 [sched] [281473700065568] [ERROR] Environment allocation rejected, status: rejected
[2026/09/10 17:28:32.251 GMT+08:00] 2026-09-10 09:28:31 [sched] [281473700065568] [ERROR] Failed to allocate environment: Environment allocation rejected: Unknown
[2026/09/10 17:28:32.251 GMT+08:00] Traceback (most recent call last):
[2026/09/10 17:28:32.251 GMT+08:00]   File "***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor/src/scheduler/env_manager.py", line 297, in allocate_environments
[2026/09/10 17:28:32.251 GMT+08:00]     self._query_k8s_env_status(
[2026/09/10 17:28:32.251 GMT+08:00]   File "***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor/src/scheduler/env_manager.py", line 382, in _query_k8s_env_status
[2026/09/10 17:28:32.251 GMT+08:00]     raise RuntimeError(
[2026/09/10 17:28:32.251 GMT+08:00] RuntimeError: Environment allocation rejected: Unknown
[2026/09/10 17:28:32.251 GMT+08:00] 2026-09-10 09:28:31 [sched] [281473700065568] [ERROR] Failed to allocate environment for env_id: cann_single_A2_device_4_cover_single_type-nodes_1-A2, error: Environment allocation rejected: Unknown
[2026/09/10 17:28:32.251 GMT+08:00] Traceback (most recent call last):
[2026/09/10 17:28:32.251 GMT+08:00]   File "***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor/src/run_scheduler.py", line 237, in _allocate_environments_and_execute
[2026/09/10 17:28:32.251 GMT+08:00]     self.env_manager.allocate_environments(env_case_info)
[2026/09/10 17:28:32.251 GMT+08:00]   File "***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor/src/scheduler/env_manager.py", line 297, in allocate_environments
[2026/09/10 17:28:32.251 GMT+08:00]     self._query_k8s_env_status(
[2026/09/10 17:28:32.251 GMT+08:00]   File "***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor/src/scheduler/env_manager.py", line 382, in _query_k8s_env_status
[2026/09/10 17:28:32.251 GMT+08:00]     raise RuntimeError(
[2026/09/10 17:28:32.251 GMT+08:00] RuntimeError: Environment allocation rejected: Unknown
[2026/09/10 17:28:32.252 GMT+08:00] 2026-09-10 09:28:31 [sched] [281473752154144] [INFO] Task completed for env_id: cann_single_A2_device_4_cover_single_type-nodes_1-A2, result: False
[2026/09/10 17:28:32.252 GMT+08:00] 2026-09-10 09:28:31 [sched] [281473752154144] [ERROR] Failed to execute cases for env_id: cann_single_A2_device_4_cover_single_type-nodes_1-A2
[2026/09/10 17:28:32.252 GMT+08:00] 2026-09-10 09:28:31 [sched] [281473691611424] [INFO] apply_env_res: {'env_id': 'lease-env1789032481-2464', 'groups': {'nodes_1': [{'name': 'device', 'res_type': 'container', 'status': 'rejected', 'node_ip': '', 'npu_ids': [], 'privileged': False}]}, 'status': 'rejected', 'name': 'env', 'created_at': '2026-09-10T09:28:01Z', 'expires_at': '2026-09-10T13:28:01Z', 'ttl': '14400', 'topology': '', 'extend_env_comments': {'job_info': 'codearts-528772518c054c5f8f4625cc5dd1cda0-e700906deacc49609e3b95eab5c1678a-671e50b108d64e71939420950f1be3d0_20260910_7'}, 'progress': {'total': 1, 'ready': 0, 'failed': 1, 'pending': 0}, 'ssh_mesh': {'enabled': False, 'scope': '', 'enrolled': [], 'failed': []}, 'errors': None}
[2026/09/10 17:28:32.252 GMT+08:00] 2026-09-10 09:28:31 [sched] [281473691611424] [ERROR] Environment allocation rejected, status: rejected
[2026/09/10 17:28:32.252 GMT+08:00] 2026-09-10 09:28:31 [sched] [281473691611424] [ERROR] Failed to allocate environment: Environment allocation rejected: Unknown
[2026/09/10 17:28:32.252 GMT+08:00] Traceback (most recent call last):
[2026/09/10 17:28:32.252 GMT+08:00]   File "***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor/src/scheduler/env_manager.py", line 297, in allocate_environments
[2026/09/10 17:28:32.252 GMT+08:00]     self._query_k8s_env_status(
[2026/09/10 17:28:32.252 GMT+08:00]   File "***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor/src/scheduler/env_manager.py", line 382, in _query_k8s_env_status
[2026/09/10 17:28:32.252 GMT+08:00]     raise RuntimeError(
[2026/09/10 17:28:32.252 GMT+08:00] RuntimeError: Environment allocation rejected: Unknown
[2026/09/10 17:28:32.252 GMT+08:00] 2026-09-10 09:28:31 [sched] [281473691611424] [ERROR] Failed to allocate environment for env_id: cann_single_A2_device_1_cover_single_type-nodes_1-A2, error: Environment allocation rejected: Unknown
[2026/09/10 17:28:32.252 GMT+08:00] Traceback (most recent call last):
[2026/09/10 17:28:32.252 GMT+08:00]   File "***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor/src/run_scheduler.py", line 237, in _allocate_environments_and_execute
[2026/09/10 17:28:32.252 GMT+08:00]     self.env_manager.allocate_environments(env_case_info)
[2026/09/10 17:28:32.252 GMT+08:00]   File "***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor/src/scheduler/env_manager.py", line 297, in allocate_environments
[2026/09/10 17:28:32.252 GMT+08:00]     self._query_k8s_env_status(
[2026/09/10 17:28:32.252 GMT+08:00]   File "***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor/src/scheduler/env_manager.py", line 382, in _query_k8s_env_status
[2026/09/10 17:28:32.252 GMT+08:00]     raise RuntimeError(
[2026/09/10 17:28:32.252 GMT+08:00] RuntimeError: Environment allocation rejected: Unknown
[2026/09/10 17:28:32.252 GMT+08:00] 2026-09-10 09:28:31 [sched] [281473752154144] [INFO] Task completed for env_id: cann_single_A2_device_1_cover_single_type-nodes_1-A2, result: False
[2026/09/10 17:28:32.252 GMT+08:00] 2026-09-10 09:28:31 [sched] [281473752154144] [ERROR] Failed to execute cases for env_id: cann_single_A2_device_1_cover_single_type-nodes_1-A2
[2026/09/10 17:28:32.252 GMT+08:00] 2026-09-10 09:28:31 [sched] [281473752154144] [INFO] All environments allocated and tests executed.
[2026/09/10 17:28:32.252 GMT+08:00] 2026-09-10 09:28:31 [sched] [281473752154144] [INFO] Step 4: Collecting and archiving logs to OBS...
[2026/09/10 17:28:32.252 GMT+08:00] 2026-09-10 09:28:31 [sched] [281473752154144] [INFO] don't upload to obs,  no xml found in ***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor/case-logs
[2026/09/10 17:28:32.252 GMT+08:00] 2026-09-10 09:28:31 [sched] [281473752154144] [INFO] Step 5: Releasing environments...
[2026/09/10 17:28:32.252 GMT+08:00] 2026-09-10 09:28:31 [sched] [281473752154144] [INFO] Releasing 4 environments
[2026/09/10 17:28:32.252 GMT+08:00] 2026-09-10 09:28:31 [sched] [281473752154144] [INFO] Successfully released environment: lease-env1789032450-6590
[2026/09/10 17:28:32.252 GMT+08:00] 2026-09-10 09:28:32 [sched] [281473752154144] [INFO] Successfully released environment: lease-env1789032450-3750
[2026/09/10 17:28:32.252 GMT+08:00] 2026-09-10 09:28:32 [sched] [281473752154144] [INFO] Successfully released environment: lease-env1789032481-2464
[2026/09/10 17:28:32.252 GMT+08:00] 2026-09-10 09:28:32 [sched] [281473752154144] [INFO] Successfully released environment: lease-env1789032481-1782
[2026/09/10 17:28:32.252 GMT+08:00] 2026-09-10 09:28:32 [sched] [281473752154144] [INFO] All tasks completed.
[2026/09/10 17:28:32.252 GMT+08:00] 2026-09-10 09:28:32 [sched] [281473752154144] [ERROR] No test case result found. Exiting.
[2026/09/10 17:28:32.566 GMT+08:00] + echo '[ERROR]execute openlibing-pytest-executor. main.py fail, log file is ***//openlibing-pytest-executor-workspace/executor-log/scheduler_framework.log'
[2026/09/10 17:28:32.566 GMT+08:00] [ERROR]execute openlibing-pytest-executor. main.py fail, log file is ***//openlibing-pytest-executor-workspace/executor-log/scheduler_framework.log
[2026/09/10 17:28:32.566 GMT+08:00] + exit 1
[2026/09/10 17:28:32.622 GMT+08:00] [ERROR]  : script returned exit code 1, exitMessage is: command run failed
[2026/09/10 17:28:32.689 GMT+08:00] [INFO]  : [JobStatusPlugin] onCompleted: j_YDkS2cnP #1
[2026/09/10 17:28:35.524 GMT+08:00] Finished: FAILURE
