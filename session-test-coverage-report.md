[2026/09/10 19:09:19.620 GMT+08:00] [INFO]  : [JobStatusPlugin] onStarted: j_7aDD9a9E #1
[2026/09/10 19:09:19.621 GMT+08:00] Resume disabled by user, switching to high-performance, low-durability mode.
[2026/09/10 19:09:19.733 GMT+08:00] [INFO] [PRE_ENV:slave_create] : 该步骤开始执行
[2026/09/10 19:09:19.735 GMT+08:00] [INFO] [PRE_ENV:slave_create] : [slave] resources pool message: 5559c4d79a5e41ccb0cf0b2b9143106b
[2026/09/10 19:09:19.736 GMT+08:00] [WARNING] [PRE_ENV:slave_create] : [slave] find empty runtime, location: PRE_ENV.slave_create
[2026/09/10 19:09:19.736 GMT+08:00] [INFO] [PRE_ENV:slave_create] : [slave] Fixed content: No
[2026/09/10 19:09:19.841 GMT+08:00] [INFO] [PRE_ENV:slave_create] : [slave] Find available executor node:agent_1789024043350-W79IIG7Tr8
[2026/09/10 19:09:19.885 GMT+08:00] [INFO] [PRE_ENV:slave_create] : 该步骤执行完成
[2026/09/10 19:09:19.922 GMT+08:00] [INFO] [代码检出:external_pre_checkout] : 该步骤开始执行
[2026/09/10 19:09:19.924 GMT+08:00] [INFO] [代码检出:external_pre_checkout] : git plugin version: 1.12.5
[2026/09/10 19:09:19.948 GMT+08:00] [INFO] [代码检出:external_pre_checkout] : 成功配置文件。
[2026/09/10 19:09:20.131 GMT+08:00] [INFO] [代码检出:external_pre_checkout] : [WARN]DEV.CB.02101217,用户名或密码为空。
[2026/09/10 19:09:20.131 GMT+08:00] [INFO] [代码检出:external_pre_checkout] : 创建gitcode代码访问凭证成功。
[2026/09/10 19:09:20.132 GMT+08:00] [INFO] [代码检出:external_pre_checkout] : 该步骤执行完成
[2026/09/10 19:09:20.193 GMT+08:00] No credentials specified
[2026/09/10 19:09:20.193 GMT+08:00] set customize username password****           
[2026/09/10 19:09:20.204 GMT+08:00] addDefaultCredentials
[2026/09/10 19:09:20.215 GMT+08:00] git plugin version: 3.12.22-h1.cbu.codearts.build.r1
[2026/09/10 19:09:20.226 GMT+08:00] Cloning the remote Git repository
[2026/09/10 19:09:20.226 GMT+08:00] Using shallow clone
[2026/09/10 19:09:20.226 GMT+08:00] Avoid fetching tags
[2026/09/10 19:09:20.226 GMT+08:00] Honoring refspec on initial clone
[2026/09/10 19:09:20.236 GMT+08:00] Cloning repository https://gitcode.com/cann-dev/CANN-CI.git
[2026/09/10 19:09:20.236 GMT+08:00]  > git init /opt/agent_1789024043350/workspace/j_7aDD9a9E # timeout=10
[2026/09/10 19:09:20.242 GMT+08:00] Fetching upstream changes from https://gitcode.com/cann-dev/CANN-CI.git
[2026/09/10 19:09:20.242 GMT+08:00]  > git --version # timeout=10
[2026/09/10 19:09:20.245 GMT+08:00]  > git --version # 'git version 2.34.1'
[2026/09/10 19:09:20.246 GMT+08:00] using GIT_ASKPASS to set credentials  username and password**** [2026/09/10 19:09:20.247 GMT+08:00] scmType is gitcode
[2026/09/10 19:09:20.247 GMT+08:00]  > git -c *** fetch --no-tags --force --progress --depth=1 -- https://gitcode.com/cann-dev/CANN-CI.git +refs/heads/test_smoke:refs/remotes/origin/test_smoke # timeout=120
[2026/09/10 19:09:20.950 GMT+08:00]  > git config remote.origin.url https://gitcode.com/cann-dev/CANN-CI.git # timeout=10
[2026/09/10 19:09:20.954 GMT+08:00]  > git config --add remote.origin.fetch +refs/heads/test_smoke:refs/remotes/origin/test_smoke # timeout=10
[2026/09/10 19:09:20.980 GMT+08:00]  > git config remote.origin.url https://gitcode.com/cann-dev/CANN-CI.git # timeout=10
[2026/09/10 19:09:20.995 GMT+08:00] Fetching upstream changes from https://gitcode.com/cann-dev/CANN-CI.git
[2026/09/10 19:09:20.996 GMT+08:00] using GIT_ASKPASS to set credentials  username and password**** [2026/09/10 19:09:20.997 GMT+08:00] scmType is gitcode
[2026/09/10 19:09:20.997 GMT+08:00]  > git -c *** fetch --no-tags --force --progress --depth=1 -- https://gitcode.com/cann-dev/CANN-CI.git +refs/heads/test_smoke:refs/remotes/origin/test_smoke # timeout=120
[2026/09/10 19:09:21.562 GMT+08:00] Checking out Revision 8db165473ae4621a98eb52f4d7d5601dd5246f58 (origin/test_smoke)
[2026/09/10 19:09:21.562 GMT+08:00] Disable Git LFS pull
[2026/09/10 19:09:21.624 GMT+08:00] Commit message: "smoke image"
[2026/09/10 19:09:21.625 GMT+08:00] First time build. Skipping changelog.
[2026/09/10 19:09:21.653 GMT+08:00] [INFO] [代码检出:external_post_checkout] : 该步骤开始执行
[2026/09/10 19:09:21.716 GMT+08:00] [INFO] [代码检出:external_post_checkout] : 该步骤执行完成
[2026/09/10 19:09:22.167 GMT+08:00] + set -euo pipefail
[2026/09/10 19:09:22.167 GMT+08:00] + apt install python3.10-venv -y
[2026/09/10 19:09:22.167 GMT+08:00] 
[2026/09/10 19:09:22.167 GMT+08:00] WARNING: apt does not have a stable CLI interface. Use with caution in scripts.
[2026/09/10 19:09:22.167 GMT+08:00] 
[2026/09/10 19:09:22.199 GMT+08:00] Reading package lists...starting check in ***/@tmp/durable-5cf1a535
[2026/09/10 19:09:21.555 GMT+08:00]  > git rev-parse origin/test_smoke^{commit} # timeout=10
[2026/09/10 19:09:21.571 GMT+08:00]  > git config core.sparsecheckout # timeout=10
[2026/09/10 19:09:21.574 GMT+08:00]  > git checkout -f 8db165473ae4621a98eb52f4d7d5601dd5246f58 # timeout=120
[2026/09/10 19:09:21.592 GMT+08:00]  > git branch -a -v --no-abbrev # timeout=10
[2026/09/10 19:09:21.596 GMT+08:00]  > git checkout -b test_smoke 8db165473ae4621a98eb52f4d7d5601dd5246f58 # timeout=120
[2026/09/10 19:09:23.761 GMT+08:00] 
[2026/09/10 19:09:24.075 GMT+08:00] Building dependency tree...
[2026/09/10 19:09:24.075 GMT+08:00] Reading state information...
[2026/09/10 19:09:24.752 GMT+08:00] python3.10-venv is already the newest version (3.10.12-1~22.04.18).
[2026/09/10 19:09:24.752 GMT+08:00] 0 upgraded, 0 newly installed, 0 to remove and 89 not upgraded.
[2026/09/10 19:09:24.752 GMT+08:00] + PROJECT_ID=1e20b309fcb34b00a0043a87e461c95a
[2026/09/10 19:09:24.752 GMT+08:00] + JOB_RUN_ID=671e50b108d64e71939420950f1be3d0_20260910_10
[2026/09/10 19:09:24.752 GMT+08:00] + BASE_DIR=***//openlibing-pytest-executor-workspace
[2026/09/10 19:09:24.752 GMT+08:00] + EXECUTOR_LOG_DIR=***//openlibing-pytest-executor-workspace/executor-log
[2026/09/10 19:09:24.752 GMT+08:00] + EXECUTOR_LOG_FILE=***//openlibing-pytest-executor-workspace/executor-log/scheduler_framework.log
[2026/09/10 19:09:24.752 GMT+08:00] + PYTEST_TESTKIT_DIR=***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testkit
[2026/09/10 19:09:24.752 GMT+08:00] + TESTCASE_COLLETOR_DIR=***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testcase-collector
[2026/09/10 19:09:24.752 GMT+08:00] + EXECUTOR_BRANCH=lishaocun_develop
[2026/09/10 19:09:24.752 GMT+08:00] + OBS_INFO='{"ak":"*****","sk":"*****","bucket_name":"ascend-cann-open","server":"https://obs.cn-north-4.myhuaweicloud.com","base_url":"https://ascend-cann-open.obs.cn-north-4.myhuaweicloud.com/version_smoke"}'
[2026/09/10 19:09:24.752 GMT+08:00] ++ date +%Y%m%d
[2026/09/10 19:09:24.752 GMT+08:00] + TASK_ID=1e20b309fcb34b00a0043a87e461c95a2026091027911
[2026/09/10 19:09:24.752 GMT+08:00] + MAX_WORKERS=2
[2026/09/10 19:09:24.752 GMT+08:00] + echo '[INFO] clear workspace dir'
[2026/09/10 19:09:24.752 GMT+08:00] [INFO] clear workspace dir
[2026/09/10 19:09:24.752 GMT+08:00] + '[' -d ***//openlibing-pytest-executor-workspace ']'
[2026/09/10 19:09:24.752 GMT+08:00] + echo '[INFO] workspace dir not exits'
[2026/09/10 19:09:24.752 GMT+08:00] [INFO] workspace dir not exits
[2026/09/10 19:09:24.752 GMT+08:00] + echo '[INFO] create work dir'
[2026/09/10 19:09:24.752 GMT+08:00] [INFO] create work dir
[2026/09/10 19:09:24.752 GMT+08:00] + mkdir -p ***//openlibing-pytest-executor-workspace
[2026/09/10 19:09:24.752 GMT+08:00] + echo '[INFO] git clone openlibing-pytest-excutor...'
[2026/09/10 19:09:24.752 GMT+08:00] [INFO] git clone openlibing-pytest-excutor...
[2026/09/10 19:09:24.752 GMT+08:00] + GIT_TERMINAL_PROMPT=0
[2026/09/10 19:09:24.752 GMT+08:00] + git clone --depth 1 -b lishaocun_develop https://gitcode.com/openlibing/openlibing-pytest-executor.git ***//openlibing-pytest-executor-workspace/openlibing-pytest-executor
[2026/09/10 19:09:24.752 GMT+08:00] Cloning into '***//openlibing-pytest-executor-workspace/openlibing-pytest-executor'...
[2026/09/10 19:09:25.429 GMT+08:00] + mkdir -p ***//openlibing-pytest-executor-workspace/executor-log
[2026/09/10 19:09:25.429 GMT+08:00] + mkdir -p ***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testkit
[2026/09/10 19:09:25.429 GMT+08:00] + mkdir -p ***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testcase-collector
[2026/09/10 19:09:25.429 GMT+08:00] + PYTEST_TESTKIT_FILE=***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testkit/pytest_testkit-1.0.0-py3-none-any.whl
[2026/09/10 19:09:25.429 GMT+08:00] + cd ***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testkit
[2026/09/10 19:09:25.429 GMT+08:00] + wget https://gitcode.com/openlibing/openlibing-pytest-executor/releases/download/v1.0.0-alpha/pytest_testkit-1.0.0-py3-none-any.whl
[2026/09/10 19:09:25.429 GMT+08:00] --2026-09-10 11:09:25--  https://gitcode.com/openlibing/openlibing-pytest-executor/releases/download/v1.0.0-alpha/pytest_testkit-1.0.0-py3-none-any.whl
[2026/09/10 19:09:25.429 GMT+08:00] Resolving gitcode.com (gitcode.com)... ***.***.***.91
[2026/09/10 19:09:25.429 GMT+08:00] Connecting to gitcode.com (gitcode.com)|***.***.***.91|:443... connected.
[2026/09/10 19:09:25.429 GMT+08:00] HTTP request sent, awaiting response... 302 Found
[2026/09/10 19:09:25.429 GMT+08:00] Location: https://file-cdn.gitcode.com/9099034/releases/untagger_49126fd431864af2bd607d9192ff2c33/pytest_testkit-1.0.0-py3-none-any.whl?auth_key=1789038565-2f1c24873b0b446e956cb45277495139-0-c8111f4b293304932e08e64e95e11ee73025c0214d7193bebc8d1282d56a1ce6 [following]
[2026/09/10 19:09:25.429 GMT+08:00] --2026-09-10 11:09:25--  https://file-cdn.gitcode.com/9099034/releases/untagger_49126fd431864af2bd607d9192ff2c33/pytest_testkit-1.0.0-py3-none-any.whl?auth_key=1789038565-2f1c24873b0b446e956cb45277495139-0-c8111f4b293304932e08e64e95e11ee73025c0214d7193bebc8d1282d56a1ce6
[2026/09/10 19:09:25.429 GMT+08:00] Resolving file-cdn.gitcode.com (file-cdn.gitcode.com)... ***.***.***.156, ***.***.***.23, ***.***.***.157, ...
[2026/09/10 19:09:25.429 GMT+08:00] Connecting to file-cdn.gitcode.com (file-cdn.gitcode.com)|***.***.***.156|:443... connected.
[2026/09/10 19:09:25.429 GMT+08:00] HTTP request sent, awaiting response... 200 OK
[2026/09/10 19:09:25.429 GMT+08:00] Length: 102245 (100K) [application/octet-stream]
[2026/09/10 19:09:25.429 GMT+08:00] Saving to: 'pytest_testkit-1.0.0-py3-none-any.whl'
[2026/09/10 19:09:25.429 GMT+08:00] 
[2026/09/10 19:09:25.429 GMT+08:00]      0K .......... .......... .......... .......... .......... 50% 2.11M 0s
[2026/09/10 19:09:25.429 GMT+08:00]     50K .......... .......... .......... .......... ......... 100% 7.16M=0.03s
[2026/09/10 19:09:25.429 GMT+08:00] 
[2026/09/10 19:09:25.429 GMT+08:00] 2026-09-10 11:09:25 (3.26 MB/s) - 'pytest_testkit-1.0.0-py3-none-any.whl' saved [102245/102245]
[2026/09/10 19:09:25.429 GMT+08:00] 
[2026/09/10 19:09:25.429 GMT+08:00] + ls ***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testkit/pytest_testkit-1.0.0-py3-none-any.whl
[2026/09/10 19:09:25.429 GMT+08:00] ***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testkit/pytest_testkit-1.0.0-py3-none-any.whl
[2026/09/10 19:09:25.429 GMT+08:00] + TESTCASE_COLLETOR_FILE=***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testcase-collector/pytest_testcase_collector-1.0.0-py3-none-any.whl
[2026/09/10 19:09:25.429 GMT+08:00] + cd ***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testcase-collector
[2026/09/10 19:09:25.429 GMT+08:00] + wget https://gitcode.com/openlibing/openlibing-pytest-executor/releases/download/pytest-testcase-collector-1.0.0/pytest_testcase_collector-1.0.0-py3-none-any.whl
[2026/09/10 19:09:25.429 GMT+08:00] --2026-09-10 11:09:25--  https://gitcode.com/openlibing/openlibing-pytest-executor/releases/download/pytest-testcase-collector-1.0.0/pytest_testcase_collector-1.0.0-py3-none-any.whl
[2026/09/10 19:09:25.429 GMT+08:00] Resolving gitcode.com (gitcode.com)... ***.***.***.91
[2026/09/10 19:09:25.429 GMT+08:00] Connecting to gitcode.com (gitcode.com)|***.***.***.91|:443... connected.
[2026/09/10 19:09:25.429 GMT+08:00] HTTP request sent, awaiting response... 302 Found
[2026/09/10 19:09:25.429 GMT+08:00] Location: https://file-cdn.gitcode.com/9099034/releases/untagger_8a06d959d9f74ac09748fb720f5d85e8/pytest_testcase_collector-1.0.0-py3-none-any.whl?auth_key=1789038565-f49dc13694a24faca2a811d13bc6686b-0-48309cbb35f2f278b815e9dffdc9889f87ca4d1912ab2b6ce2adf7a0b55f1f5b [following]
[2026/09/10 19:09:25.430 GMT+08:00] --2026-09-10 11:09:25--  https://file-cdn.gitcode.com/9099034/releases/untagger_8a06d959d9f74ac09748fb720f5d85e8/pytest_testcase_collector-1.0.0-py3-none-any.whl?auth_key=1789038565-f49dc13694a24faca2a811d13bc6686b-0-48309cbb35f2f278b815e9dffdc9889f87ca4d1912ab2b6ce2adf7a0b55f1f5b
[2026/09/10 19:09:25.430 GMT+08:00] Resolving file-cdn.gitcode.com (file-cdn.gitcode.com)... ***.***.***.156, ***.***.***.23, ***.***.***.157, ...
[2026/09/10 19:09:25.430 GMT+08:00] Connecting to file-cdn.gitcode.com (file-cdn.gitcode.com)|***.***.***.156|:443... connected.
[2026/09/10 19:09:25.742 GMT+08:00] HTTP request sent, awaiting response... 200 OK
[2026/09/10 19:09:25.742 GMT+08:00] Length: 15058 (15K) [application/octet-stream]
[2026/09/10 19:09:25.742 GMT+08:00] Saving to: 'pytest_testcase_collector-1.0.0-py3-none-any.whl'
[2026/09/10 19:09:25.742 GMT+08:00] 
[2026/09/10 19:09:25.742 GMT+08:00]      0K .......... ....                                       100%  222M=0s
[2026/09/10 19:09:25.742 GMT+08:00] 
[2026/09/10 19:09:25.742 GMT+08:00] 2026-09-10 11:09:25 (222 MB/s) - 'pytest_testcase_collector-1.0.0-py3-none-any.whl' saved [15058/15058]
[2026/09/10 19:09:25.742 GMT+08:00] 
[2026/09/10 19:09:25.742 GMT+08:00] + ls ***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testcase-collector/pytest_testcase_collector-1.0.0-py3-none-any.whl
[2026/09/10 19:09:25.742 GMT+08:00] ***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testcase-collector/pytest_testcase_collector-1.0.0-py3-none-any.whl
[2026/09/10 19:09:25.742 GMT+08:00] + echo '[INFO] git clone testcase code...'
[2026/09/10 19:09:25.742 GMT+08:00] [INFO] git clone testcase code...
[2026/09/10 19:09:25.742 GMT+08:00] + TEST_CASE_DIR=***//openlibing-pytest-executor-workspace/pytest-infra
[2026/09/10 19:09:25.742 GMT+08:00] + mkdir -p ***//openlibing-pytest-executor-workspace/pytest-infra
[2026/09/10 19:09:25.742 GMT+08:00] + CASE_BRANCH=main
[2026/09/10 19:09:25.742 GMT+08:00] + GIT_TERMINAL_PROMPT=0
[2026/09/10 19:09:25.743 GMT+08:00] + git clone --depth 1 -b main https://gitcode.com/Xu-yejie/pytest-infra.git ***//openlibing-pytest-executor-workspace/pytest-infra
[2026/09/10 19:09:25.743 GMT+08:00] Cloning into '***//openlibing-pytest-executor-workspace/pytest-infra'...
[2026/09/10 19:09:27.919 GMT+08:00] + echo '[INFO] execute test cases...'
[2026/09/10 19:09:27.919 GMT+08:00] [INFO] execute test cases...
[2026/09/10 19:09:27.919 GMT+08:00] + '[' '!' -f ***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor/main.py ']'
[2026/09/10 19:09:27.919 GMT+08:00] + python3 -m venv venv
[2026/09/10 19:09:32.544 GMT+08:00] + source venv/bin/activate
[2026/09/10 19:09:32.544 GMT+08:00] ++ deactivate nondestructive
[2026/09/10 19:09:32.544 GMT+08:00] ++ '[' -n '' ']'
[2026/09/10 19:09:32.544 GMT+08:00] ++ '[' -n '' ']'
[2026/09/10 19:09:32.544 GMT+08:00] ++ '[' -n /usr/bin/sh -o -n '' ']'
[2026/09/10 19:09:32.544 GMT+08:00] ++ hash -r
[2026/09/10 19:09:32.544 GMT+08:00] ++ '[' -n '' ']'
[2026/09/10 19:09:32.544 GMT+08:00] ++ unset VIRTUAL_ENV
[2026/09/10 19:09:32.544 GMT+08:00] ++ unset VIRTUAL_ENV_PROMPT
[2026/09/10 19:09:32.544 GMT+08:00] ++ '[' '!' nondestructive = nondestructive ']'
[2026/09/10 19:09:32.545 GMT+08:00] ++ VIRTUAL_ENV=***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testcase-collector/venv
[2026/09/10 19:09:32.545 GMT+08:00] ++ export VIRTUAL_ENV
[2026/09/10 19:09:32.545 GMT+08:00] ++ _OLD_VIRTUAL_PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
[2026/09/10 19:09:32.545 GMT+08:00] ++ PATH=***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testcase-collector/venv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
[2026/09/10 19:09:32.545 GMT+08:00] ++ export PATH
[2026/09/10 19:09:32.545 GMT+08:00] ++ '[' -n '' ']'
[2026/09/10 19:09:32.545 GMT+08:00] ++ '[' -z '' ']'
[2026/09/10 19:09:32.545 GMT+08:00] ++ _OLD_VIRTUAL_PS1=
[2026/09/10 19:09:32.545 GMT+08:00] ++ PS1='(venv) '
[2026/09/10 19:09:32.545 GMT+08:00] ++ export PS1
[2026/09/10 19:09:32.545 GMT+08:00] ++ VIRTUAL_ENV_PROMPT='(venv) '
[2026/09/10 19:09:32.545 GMT+08:00] ++ export VIRTUAL_ENV_PROMPT
[2026/09/10 19:09:32.545 GMT+08:00] ++ '[' -n /usr/bin/sh -o -n '' ']'
[2026/09/10 19:09:32.545 GMT+08:00] ++ hash -r
[2026/09/10 19:09:32.545 GMT+08:00] + python -m pip install --upgrade pip -i https://mirrors.huaweicloud.com/repository/pypi/simple -q
[2026/09/10 19:09:35.404 GMT+08:00] + cd ***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor
[2026/09/10 19:09:35.404 GMT+08:00] + pip install -r requirements.txt -i https://mirrors.huaweicloud.com/repository/pypi/simple -q
[2026/09/10 19:09:48.318 GMT+08:00] + tee -a ***//openlibing-pytest-executor-workspace/executor-log/scheduler_framework.log
[2026/09/10 19:09:48.318 GMT+08:00] + python -u ***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor/main.py --testcase_dir ***//openlibing-pytest-executor-workspace/pytest-infra --log_dir ***//openlibing-pytest-executor-workspace/executor-log --pytest_testkit_path ***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testkit/pytest_testkit-1.0.0-py3-none-any.whl --testcase_collector_path ***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testcase-collector/pytest_testcase_collector-1.0.0-py3-none-any.whl --obs '{"ak":"*****","sk":"*****","bucket_name":"ascend-cann-open","server":"https://obs.cn-north-4.myhuaweicloud.com","base_url":"https://ascend-cann-open.obs.cn-north-4.myhuaweicloud.com/version_smoke"}' --task_id 1e20b309fcb34b00a0043a87e461c95a2026091027911 --testcase_config_file resources/pytest_cann_ops-cv.ini --image_label swr.cn-north-4.myhuaweicloud.com/hw-ascend/smoke:ops-cv-910b --pipeline_id 528772518c054c5f8f4625cc5dd1cda0 --pipeline_run_id e700906deacc49609e3b95eab5c1678a --job_run_id 671e50b108d64e71939420950f1be3d0_20260910_10 --scheduler_secret '{apig_code:57e3545e43154e8e8c6a74b4c74193868758f6d0979446008f3cd37e88362d91,k8s_auth:arc-fxqZJDtt8oipppQt}' --max_workers 2
[2026/09/10 19:09:48.318 GMT+08:00] 2026-09-10 11:09:46 [sched] [281473142173728] [INFO] Not using HidevLab, skipping key generation
[2026/09/10 19:09:48.318 GMT+08:00] 2026-09-10 11:09:46 [sched] [281473142173728] [INFO] Successfully obtained local IP via UDP method: ***.***.***.5
[2026/09/10 19:09:48.318 GMT+08:00] 2026-09-10 11:09:46 [sched] [281473142173728] [INFO] Read pytest config from ***//openlibing-pytest-executor-workspace/pytest-infra/resources/pytest_cann_ops-cv.ini: {'infra_log_level': 'INFO', 'error_log_fail': 'true'}
[2026/09/10 19:09:48.318 GMT+08:00] 2026-09-10 11:09:46 [sched] [281473142173728] [INFO] pytest_config: {'infra_log_level': 'INFO', 'error_log_fail': 'true'}
[2026/09/10 19:09:48.318 GMT+08:00] 2026-09-10 11:09:46 [sched] [281473142173728] [INFO] Step 1: Collecting and filtering test cases with @pytest.mark.env...
[2026/09/10 19:09:48.318 GMT+08:00] 2026-09-10 11:09:46 [sched] [281473142173728] [INFO] Collecting pytest cases from directory: ***//openlibing-pytest-executor-workspace/pytest-infra
[2026/09/10 19:09:54.081 GMT+08:00] 2026-09-10 11:09:53 [sched] [281473142173728] [INFO] Successfully installed pytest_testkit-1.0.0-py3-none-any.whl
[2026/09/10 19:09:54.081 GMT+08:00] 2026-09-10 11:09:53 [sched] [281473142173728] [INFO] Installing dependencies from ***//openlibing-pytest-executor-workspace/pytest-infra/requirements.txt
[2026/09/10 19:10:13.001 GMT+08:00] 2026-09-10 11:10:11 [sched] [281473142173728] [INFO] Successfully installed requirements from ***//openlibing-pytest-executor-workspace/pytest-infra/requirements.txt
[2026/09/10 19:10:13.001 GMT+08:00] 2026-09-10 11:10:11 [sched] [281473142173728] [INFO] Case filtering in directory: ***//openlibing-pytest-executor-workspace/pytest-infra
[2026/09/10 19:10:13.001 GMT+08:00] 2026-09-10 11:10:11 [sched] [281473142173728] [INFO] Case filter config file: resources/pytest_cann_ops-cv.ini
[2026/09/10 19:10:13.001 GMT+08:00] 2026-09-10 11:10:12 [sched] [281473142173728] [INFO] pytest collect stdout:
[2026/09/10 19:10:13.001 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnGridSampler2DBackward_network.py::TestAclnnGridSampler2DBackwardExecutor::test_gdd_smk_aclnngridsampler2dbackward
[2026/09/10 19:10:13.001 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnGridSampler2D_deter.py::TestAclnnGridSampler2DExecutor::test_gdd_detesmk_aclnngridsampler2d
[2026/09/10 19:10:13.001 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnGridSampler2D_network.py::TestAclnnGridSampler2DExecutor::test_gdd_smk_aclnngridsampler2d
[2026/09/10 19:10:13.001 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnGridSampler3DBackward_network.py::TestAclnnGridSampler3DBackwardExecutor::test_gdd_smk_aclnngridsampler3dbackward
[2026/09/10 19:10:13.001 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnGridSampler3D_deter.py::TestAclnnGridSampler3DExecutor::test_gdd_detesmk_aclnngridsampler3d
[2026/09/10 19:10:13.001 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnGridSampler3D_network.py::TestAclnnGridSampler3DExecutor::test_gdd_smk_aclnngridsampler3d
[2026/09/10 19:10:13.001 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnResize_deter.py::TestAclnnResizeExecutor::test_gdd_detesmk_aclnnresize
[2026/09/10 19:10:13.001 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnResize_network.py::TestAclnnResizeExecutor::test_gdd_smk_aclnnresize
[2026/09/10 19:10:13.001 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleBicubic2dAA.py::TestAclnnUpsampleBicubic2dAAExecutor::test_gdd_detesmk_aclnnupsamplebicubic2daa
[2026/09/10 19:10:13.001 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleBicubic2dAAGrad.py::TestAclnnUpsampleBicubic2dAAGradExecutor::test_gdd_detesmk_aclnnupsamplebicubic2daagrad
[2026/09/10 19:10:13.001 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleBicubic2dAA_network.py::TestAclnnUpsampleBicubic2dAAExecutor::test_gdd_smk_aclnnupsamplebicubic2daa
[2026/09/10 19:10:13.001 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleBicubic2dBackward_network.py::TestAclnnUpsampleBicubic2dBackwardExecutor::test_gdd_smk_aclnnupsamplebicubic2dbackward
[2026/09/10 19:10:13.001 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleBicubic2d_deter.py::TestAclnnUpsampleBicubic2dExecutor::test_gdd_detesmk_aclnnupsamplebicubic2d
[2026/09/10 19:10:13.001 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleBicubic2d_network.py::TestAclnnUpsampleBicubic2dExecutor::test_gdd_smk_aclnnupsamplebicubic2d
[2026/09/10 19:10:13.001 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleBilinear2dAA.py::TestAclnnUpsampleBilinear2dAAExecutor::test_gdd_smk_aclnnupsamplebilinear2daa
[2026/09/10 19:10:13.001 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleBilinear2dAABackward.py::TestAclnnUpsampleBilinear2dAABackwardExecutor::test_gdd_detesmk_aclnnupsamplebilinear2daabackward
[2026/09/10 19:10:13.001 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleBilinear2dAABackward_network.py::TestAclnnUpsampleBilinear2dAABackwardExecutor::test_gdd_smk_aclnnupsamplebilinear2daabackward
[2026/09/10 19:10:13.001 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleBilinear2dAA_deter.py::TestAclnnUpsampleBilinear2dAAExecutor::test_gdd_detesmk_aclnnupsamplebilinear2daa
[2026/09/10 19:10:13.001 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleBilinear2dBackwardV2.py::TestAclnnUpsampleBilinear2dBackwardV2Executor::test_gdd_smk_aclnnupsamplebilinear2dbackwardv2
[2026/09/10 19:10:13.001 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleBilinear2dBackward_deter.py::TestAclnnUpsampleBilinear2dBackwardExecutor::test_gdd_detesmk_aclnnupsamplebilinear2dbackward
[2026/09/10 19:10:13.001 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleBilinear2dBackward_network.py::TestAclnnUpsampleBilinear2dBackwardExecutor::test_gdd_smk_aclnnupsamplebilinear2dbackward
[2026/09/10 19:10:13.001 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleBilinear2d_deter.py::TestAclnnUpsampleBilinear2dExecutor::test_gdd_detesmk_aclnnupsamplebilinear2d
[2026/09/10 19:10:13.001 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleBilinear2d_network.py::TestAclnnUpsampleBilinear2dExecutor::test_gdd_smk_aclnnupsamplebilinear2d
[2026/09/10 19:10:13.001 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleLinear1d.py::TestAclnnUpsampleLinear1dExecutor::test_gdd_detesmk_aclnnupsamplelinear1d
[2026/09/10 19:10:13.001 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleLinear1dBackward.py::TestAclnnUpsampleLinear1dBackwardExecutor::test_gdd_smk_aclnnupsamplelinear1dbackward
[2026/09/10 19:10:13.001 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleLinear1dBackward_deter.py::TestAclnnUpsampleLinear1dBackwardExecutor::test_gdd_detesmk_aclnnupsamplelinear1dbackward
[2026/09/10 19:10:13.001 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleLinear1d_network.py::TestAclnnUpsampleLinear1dExecutor::test_gdd_smk_aclnnupsamplelinear1d
[2026/09/10 19:10:13.001 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearest1d.py::TestAclnnUpsampleNearest1dExecutor::test_gdd_smk_aclnnupsamplenearest1d
[2026/09/10 19:10:13.001 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearest1dBackward.py::TestAclnnUpsampleNearest1dBackwardExecutor::test_gdd_detesmk_aclnnupsamplenearest1dbackward
[2026/09/10 19:10:13.001 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearest1dBackward_network.py::TestAclnnUpsampleNearest1dBackwardExecutor::test_gdd_smk_aclnnupsamplenearest1dbackward
[2026/09/10 19:10:13.001 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearest1dV2.py::TestAclnnUpsampleNearest1dV2Executor::test_gdd_smk_aclnnupsamplenearest1dv2
[2026/09/10 19:10:13.001 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearest1d_deter.py::TestAclnnUpsampleNearest1dExecutor::test_gdd_detesmk_aclnnupsamplenearest1d
[2026/09/10 19:10:13.001 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearest2d.py::TestAclnnUpsampleNearest2dExecutor::test_gdd_detesmk_aclnnupsamplenearest2d
[2026/09/10 19:10:13.001 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearest2dBackward.py::TestAclnnUpsampleNearest2dBackwardExecutor::test_gdd_detesmk_aclnnupsamplenearest2dbackward
[2026/09/10 19:10:13.002 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearest2dBackward_network.py::TestAclnnUpsampleNearest2dBackwardExecutor::test_gdd_smk_aclnnupsamplenearest2dbackward
[2026/09/10 19:10:13.002 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearest2dV2.py::TestAclnnUpsampleNearest2dV2Executor::test_gdd_smk_aclnnupsamplenearest2dv2
[2026/09/10 19:10:13.002 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearest3d.py::TestAclnnUpsampleNearest3dExecutor::test_gdd_detesmk_aclnnupsamplenearest3d
[2026/09/10 19:10:13.002 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearest3dBackward.py::TestAclnnUpsampleNearest3dBackwardExecutor::test_gdd_detesmk_aclnnupsamplenearest3dbackward
[2026/09/10 19:10:13.002 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearest3dBackward_network.py::TestAclnnUpsampleNearest3dBackwardExecutor::test_gdd_smk_aclnnupsamplenearest3dbackward
[2026/09/10 19:10:13.002 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearest3d_network.py::TestAclnnUpsampleNearest3dExecutor::test_gdd_smk_aclnnupsamplenearest3d
[2026/09/10 19:10:13.002 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearestExact1d.py::TestAclnnUpsampleNearestExact1dExecutor::test_gdd_detesmk_aclnnupsamplenearestexact1d
[2026/09/10 19:10:13.002 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearestExact1dBackward.py::TestAclnnUpsampleNearestExact1dBackwardExecutor::test_gdd_smk_aclnnupsamplenearestexact1dbackward
[2026/09/10 19:10:13.002 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearestExact1dBackward_deter.py::TestAclnnUpsampleNearestExact1dBackwardExecutor::test_gdd_detesmk_aclnnupsamplenearestexact1dbackward
[2026/09/10 19:10:13.002 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearestExact1d_network.py::TestAclnnUpsampleNearestExact1dExecutor::test_gdd_smk_aclnnupsamplenearestexact1d
[2026/09/10 19:10:13.002 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearestExact2d.py::TestAclnnUpsampleNearestExact2dExecutor::test_gdd_detesmk_aclnnupsamplenearestexact2d
[2026/09/10 19:10:13.002 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearestExact2dBackward.py::TestAclnnUpsampleNearestExact2dBackwardExecutor::test_gdd_detesmk_aclnnupsamplenearestexact2dbackward
[2026/09/10 19:10:13.002 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearestExact2dBackward_network.py::TestAclnnUpsampleNearestExact2dBackwardExecutor::test_gdd_smk_aclnnupsamplenearestexact2dbackward
[2026/09/10 19:10:13.002 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearestExact2d_network.py::TestAclnnUpsampleNearestExact2dExecutor::test_gdd_smk_aclnnupsamplenearestexact2d
[2026/09/10 19:10:13.002 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearestExact3d.py::TestAclnnUpsampleNearestExact3dExecutor::test_gdd_smk_aclnnupsamplenearestexact3d
[2026/09/10 19:10:13.002 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearestExact3dBackward.py::TestAclnnUpsampleNearestExact3dBackwardExecutor::test_gdd_detesmk_aclnnupsamplenearestexact3dbackward
[2026/09/10 19:10:13.002 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearestExact3dBackward_network.py::TestAclnnUpsampleNearestExact3dBackwardExecutor::test_gdd_smk_aclnnupsamplenearestexact3dbackward
[2026/09/10 19:10:13.002 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleNearestExact3d_deter.py::TestAclnnUpsampleNearestExact3dExecutor::test_gdd_detesmk_aclnnupsamplenearestexact3d
[2026/09/10 19:10:13.002 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleTrilinear3dBackward.py::TestAclnnUpsampleTrilinear3dBackwardExecutor::test_gdd_detesmk_aclnnupsampletrilinear3dbackward
[2026/09/10 19:10:13.002 GMT+08:00] testcase/cann/ops-cv/resize/test_aclnnUpsampleTrilinear3dBackward_network.py::TestAclnnUpsampleTrilinear3dBackwardExecutor::test_gdd_smk_aclnnupsampletrilinear3dbackward
[2026/09/10 19:10:13.002 GMT+08:00] testcase/cann/ops-cv/test_ops_cv.py::TestAclnnRoiAlignV2::test_cann_opscv_objdetect_aclnn_roi_align_v2_accuracy
[2026/09/10 19:10:13.002 GMT+08:00] testcase/cann/ops-cv/test_ops_cv.py::TestAclnnRoiAlignV2Backward::test_cann_opscv_objdetect_aclnn_roi_align_v2_backward_accuracy
[2026/09/10 19:10:13.002 GMT+08:00] 
[2026/09/10 19:10:13.002 GMT+08:00] =============================== warnings summary ===============================
[2026/09/10 19:10:13.002 GMT+08:00] testcase/cann/ops-cv/conftest.py:19
[2026/09/10 19:10:13.002 GMT+08:00]   ***//openlibing-pytest-executor-workspace/pytest-infra/testcase/cann/ops-cv/conftest.py:19: PytestUnknownMarkWarning: Unknown pytest.mark.archive_src - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
[2026/09/10 19:10:13.002 GMT+08:00]     item.add_marker(pytest.mark.archive_src(_ARCHIVE_SRC, dst=_ARCHIVE_DST))
[2026/09/10 19:10:13.002 GMT+08:00] 
[2026/09/10 19:10:13.002 GMT+08:00] -- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
[2026/09/10 19:10:13.002 GMT+08:00] 56 tests collected in 0.62s
[2026/09/10 19:10:13.002 GMT+08:00] 
[2026/09/10 19:10:13.002 GMT+08:00] 2026-09-10 11:10:12 [sched] [281473142173728] [WARNING] pytest collect stderr:
[2026/09/10 19:10:13.002 GMT+08:00] [2026-09-10 11:10:11][INFO][plugin.py:285] Infra logging initialized: dir=logs, level=INFO, size=10MB, count=-1
[2026/09/10 19:10:13.002 GMT+08:00] [2026-09-10 11:10:11][INFO][plugin.py:342] No testbed source (no --testbed and no TESTBED_DEVICES), environment management disabled
[2026/09/10 19:10:13.002 GMT+08:00] [2026-09-10 11:10:11][INFO][plugin.py:241] Pre-action registry initialized
[2026/09/10 19:10:13.002 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnngridsampler2dbackward>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.002 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnngridsampler2d>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.002 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnngridsampler2d>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.002 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnngridsampler3dbackward>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.002 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnngridsampler3d>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.002 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnngridsampler3d>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.002 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnnresize>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.002 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnresize>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.002 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnnupsamplebicubic2daa>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.002 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnnupsamplebicubic2daagrad>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.002 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnupsamplebicubic2daa>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.002 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnupsamplebicubic2dbackward>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.002 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnnupsamplebicubic2d>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.003 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnupsamplebicubic2d>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.003 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnupsamplebilinear2daa>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.003 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnnupsamplebilinear2daabackward>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.003 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnupsamplebilinear2daabackward>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.003 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnnupsamplebilinear2daa>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.003 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnupsamplebilinear2dbackwardv2>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.003 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnnupsamplebilinear2dbackward>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.003 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnupsamplebilinear2dbackward>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.003 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnnupsamplebilinear2d>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.003 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnupsamplebilinear2d>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.003 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnnupsamplelinear1d>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.003 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnupsamplelinear1dbackward>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.003 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnnupsamplelinear1dbackward>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.003 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnupsamplelinear1d>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.003 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnupsamplenearest1d>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.003 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnnupsamplenearest1dbackward>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.003 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnupsamplenearest1dbackward>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.003 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnupsamplenearest1dv2>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.003 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnnupsamplenearest1d>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.003 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnnupsamplenearest2d>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.003 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnnupsamplenearest2dbackward>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.003 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnupsamplenearest2dbackward>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.003 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnupsamplenearest2dv2>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.003 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnnupsamplenearest3d>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.003 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnnupsamplenearest3dbackward>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.003 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnupsamplenearest3dbackward>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.003 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnupsamplenearest3d>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.003 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnnupsamplenearestexact1d>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.003 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnupsamplenearestexact1dbackward>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.003 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnnupsamplenearestexact1dbackward>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.003 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnupsamplenearestexact1d>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.003 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnnupsamplenearestexact2d>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.003 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnnupsamplenearestexact2dbackward>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.003 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnupsamplenearestexact2dbackward>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.003 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnupsamplenearestexact2d>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.003 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnupsamplenearestexact3d>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.003 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnnupsamplenearestexact3dbackward>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.003 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnupsamplenearestexact3dbackward>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.003 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnnupsamplenearestexact3d>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.003 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_detesmk_aclnnupsampletrilinear3dbackward>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.003 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_gdd_smk_aclnnupsampletrilinear3dbackward>[{'level': 'P0', 'type': 'Functional', 'scene': 'smoke'}]
[2026/09/10 19:10:13.003 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_cann_opscv_objdetect_aclnn_roi_align_v2_accuracy>[{'level': 'P0', 'type': 'Functional', 'scene': 'functional'}]
[2026/09/10 19:10:13.003 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:698] item: match[True]<Function test_cann_opscv_objdetect_aclnn_roi_align_v2_backward_accuracy>[{'level': 'P0', 'type': 'Functional', 'scene': 'functional'}]
[2026/09/10 19:10:13.003 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:707] filter case with inifile: attributes[{'level': ['P0'], 'type': ['Functional']}]
[2026/09/10 19:10:13.004 GMT+08:00] filtered cases: [<Function test_gdd_smk_aclnngridsampler2dbackward>, <Function test_gdd_detesmk_aclnngridsampler2d>, <Function test_gdd_smk_aclnngridsampler2d>, <Function test_gdd_smk_aclnngridsampler3dbackward>, <Function test_gdd_detesmk_aclnngridsampler3d>, <Function test_gdd_smk_aclnngridsampler3d>, <Function test_gdd_detesmk_aclnnresize>, <Function test_gdd_smk_aclnnresize>, <Function test_gdd_detesmk_aclnnupsamplebicubic2daa>, <Function test_gdd_detesmk_aclnnupsamplebicubic2daagrad>, <Function test_gdd_smk_aclnnupsamplebicubic2daa>, <Function test_gdd_smk_aclnnupsamplebicubic2dbackward>, <Function test_gdd_detesmk_aclnnupsamplebicubic2d>, <Function test_gdd_smk_aclnnupsamplebicubic2d>, <Function test_gdd_smk_aclnnupsamplebilinear2daa>, <Function test_gdd_detesmk_aclnnupsamplebilinear2daabackward>, <Function test_gdd_smk_aclnnupsamplebilinear2daabackward>, <Function test_gdd_detesmk_aclnnupsamplebilinear2daa>, <Function test_gdd_smk_aclnnupsamplebilinear2dbackwardv2>, <Function test_gdd_detesmk_aclnnupsamplebilinear2dbackward>, <Function test_gdd_smk_aclnnupsamplebilinear2dbackward>, <Function test_gdd_detesmk_aclnnupsamplebilinear2d>, <Function test_gdd_smk_aclnnupsamplebilinear2d>, <Function test_gdd_detesmk_aclnnupsamplelinear1d>, <Function test_gdd_smk_aclnnupsamplelinear1dbackward>, <Function test_gdd_detesmk_aclnnupsamplelinear1dbackward>, <Function test_gdd_smk_aclnnupsamplelinear1d>, <Function test_gdd_smk_aclnnupsamplenearest1d>, <Function test_gdd_detesmk_aclnnupsamplenearest1dbackward>, <Function test_gdd_smk_aclnnupsamplenearest1dbackward>, <Function test_gdd_smk_aclnnupsamplenearest1dv2>, <Function test_gdd_detesmk_aclnnupsamplenearest1d>, <Function test_gdd_detesmk_aclnnupsamplenearest2d>, <Function test_gdd_detesmk_aclnnupsamplenearest2dbackward>, <Function test_gdd_smk_aclnnupsamplenearest2dbackward>, <Function test_gdd_smk_aclnnupsamplenearest2dv2>, <Function test_gdd_detesmk_aclnnupsamplenearest3d>, <Function test_gdd_detesmk_aclnnupsamplenearest3dbackward>, <Function test_gdd_smk_aclnnupsamplenearest3dbackward>, <Function test_gdd_smk_aclnnupsamplenearest3d>, <Function test_gdd_detesmk_aclnnupsamplenearestexact1d>, <Function test_gdd_smk_aclnnupsamplenearestexact1dbackward>, <Function test_gdd_detesmk_aclnnupsamplenearestexact1dbackward>, <Function test_gdd_smk_aclnnupsamplenearestexact1d>, <Function test_gdd_detesmk_aclnnupsamplenearestexact2d>, <Function test_gdd_detesmk_aclnnupsamplenearestexact2dbackward>, <Function test_gdd_smk_aclnnupsamplenearestexact2dbackward>, <Function test_gdd_smk_aclnnupsamplenearestexact2d>, <Function test_gdd_smk_aclnnupsamplenearestexact3d>, <Function test_gdd_detesmk_aclnnupsamplenearestexact3dbackward>, <Function test_gdd_smk_aclnnupsamplenearestexact3dbackward>, <Function test_gdd_detesmk_aclnnupsamplenearestexact3d>, <Function test_gdd_detesmk_aclnnupsampletrilinear3dbackward>, <Function test_gdd_smk_aclnnupsampletrilinear3dbackward>, <Function test_cann_opscv_objdetect_aclnn_roi_align_v2_accuracy>, <Function test_cann_opscv_objdetect_aclnn_roi_align_v2_backward_accuracy>]
[2026/09/10 19:10:13.004 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:757] Collected environment info exported to COLLECTED_INFO environment variable
[2026/09/10 19:10:13.004 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:830] output collected info file to: /tmp/tmpyeewqciu.json
[2026/09/10 19:10:13.004 GMT+08:00] [2026-09-10 11:10:12][INFO][plugin.py:967] Test session completed
[2026/09/10 19:10:13.004 GMT+08:00] 
[2026/09/10 19:10:13.004 GMT+08:00] 2026-09-10 11:10:12 [sched] [281473142173728] [INFO] Collected 56 test cases
[2026/09/10 19:10:13.004 GMT+08:00] 2026-09-10 11:10:12 [sched] [281473142173728] [INFO] Step 2: Grouping test cases by environments...
[2026/09/10 19:10:13.004 GMT+08:00] 2026-09-10 11:10:12 [sched] [281473142173728] [INFO] Environment block: {'cann_single_A2_device_3_cover_single_type-nodes_1-A2': {'case_list_len': 14}, 'cann_single_A2_device_2_cover_single_type-nodes_1-A2': {'case_list_len': 15}, 'cann_single_A2_device_1_cover_single_type-nodes_1-A2': {'case_list_len': 14}, 'cann_single_A2_device_4_cover_single_type-nodes_1-A2': {'case_list_len': 13}}
[2026/09/10 19:10:13.004 GMT+08:00] 2026-09-10 11:10:12 [sched] [281473142173728] [INFO] Step 3: Allocating environments and executing tests...
[2026/09/10 19:10:13.004 GMT+08:00] 2026-09-10 11:10:12 [sched] [281473142173728] [INFO] Submitting task for env_id: cann_single_A2_device_3_cover_single_type-nodes_1-A2
[2026/09/10 19:10:13.004 GMT+08:00] 2026-09-10 11:10:12 [sched] [281473090056480] [INFO] Allocating environment for env_id: cann_single_A2_device_3_cover_single_type-nodes_1-A2
[2026/09/10 19:10:13.004 GMT+08:00] 2026-09-10 11:10:12 [sched] [281473142173728] [INFO] Submitting task for env_id: cann_single_A2_device_2_cover_single_type-nodes_1-A2
[2026/09/10 19:10:13.004 GMT+08:00] 2026-09-10 11:10:12 [sched] [281473090056480] [INFO] Using image label: swr.cn-north-4.myhuaweicloud.com/hw-ascend/smoke:ops-cv-910b
[2026/09/10 19:10:13.004 GMT+08:00] 2026-09-10 11:10:12 [sched] [281473081602336] [INFO] Allocating environment for env_id: cann_single_A2_device_2_cover_single_type-nodes_1-A2
[2026/09/10 19:10:13.004 GMT+08:00] 2026-09-10 11:10:12 [sched] [281473090056480] [INFO] env_device_resource is empty, skipping mock allocation
[2026/09/10 19:10:13.004 GMT+08:00] 2026-09-10 11:10:12 [sched] [281473081602336] [INFO] Using image label: swr.cn-north-4.myhuaweicloud.com/hw-ascend/smoke:ops-cv-910b
[2026/09/10 19:10:13.004 GMT+08:00] 2026-09-10 11:10:12 [sched] [281473090056480] [INFO] Creating k8s environment with name: codearts-528772518c054c5f8f4625cc5dd1cda0-e700906deacc49609e3b95eab5c1678a-671e50b108d64e71939420950f1be3d0_20260910_10, ttl: None
[2026/09/10 19:10:13.004 GMT+08:00] 2026-09-10 11:10:12 [sched] [281473081602336] [INFO] env_device_resource is empty, skipping mock allocation
[2026/09/10 19:10:13.004 GMT+08:00] 2026-09-10 11:10:12 [sched] [281473090056480] [INFO] apply_env_k8s, payload={'env_definition': {'nodes_1': [{'name': 'device', 'res_type': 'container', 'cpu_arch': 'ARM', 'cpu_core_num': 48, 'npu_gen': 'A2', 'npu_num': 2, 'shm_size': '256Gi', 'memory_size': 256, 'resources': {'cpu': {'request': '48', 'limit': '128'}, 'memory': {'request': '256Gi', 'limit': '1024Gi'}}, 'use_nfs': True, 'mount_source_data': ['cann_ops_data1', 'cann_ops_data2', 'cann_ops_data3', 'cann_ops_data4', 'cann_ops_data5', 'cann_duo_os_autos_test', 'cann_duo_os_imagenet', 'cann_duo_os_acl', 'cann_duo_os_pyacl'], 'mount_dest_dir': ['/autotest/ATK_BIN', '/autotest/atk_output', '/autotest/config', '/autotest/golden_path', '/autotest/result', '/autos_test', '/data/imagenet2012', '/home/infer/bin_bak/acl', '/home/pyacl'], 'pool': 'ascend-general-a2', 'image_label': 'swr.cn-north-4.myhuaweicloud.com/hw-ascend/smoke:ops-cv-910b'}]}, 'extend_env_comments': {'job_info': 'codearts-528772518c054c5f8f4625cc5dd1cda0-e700906deacc49609e3b95eab5c1678a-671e50b108d64e71939420950f1be3d0_20260910_10'}, 'ssh_mesh': 'group', 'extend_labels': {'cluster': 'false'}}
[2026/09/10 19:10:13.004 GMT+08:00] 2026-09-10 11:10:12 [sched] [281473081602336] [INFO] Creating k8s environment with name: codearts-528772518c054c5f8f4625cc5dd1cda0-e700906deacc49609e3b95eab5c1678a-671e50b108d64e71939420950f1be3d0_20260910_10, ttl: None
[2026/09/10 19:10:13.004 GMT+08:00] 2026-09-10 11:10:12 [sched] [281473081602336] [INFO] apply_env_k8s, payload={'env_definition': {'nodes_1': [{'name': 'device', 'res_type': 'container', 'cpu_arch': 'ARM', 'cpu_core_num': 48, 'npu_gen': 'A2', 'npu_num': 2, 'shm_size': '256Gi', 'memory_size': 256, 'resources': {'cpu': {'request': '48', 'limit': '128'}, 'memory': {'request': '256Gi', 'limit': '1024Gi'}}, 'use_nfs': True, 'mount_source_data': ['cann_ops_data1', 'cann_ops_data2', 'cann_ops_data3', 'cann_ops_data4', 'cann_ops_data5', 'cann_duo_os_autos_test', 'cann_duo_os_imagenet', 'cann_duo_os_acl', 'cann_duo_os_pyacl'], 'mount_dest_dir': ['/autotest/ATK_BIN', '/autotest/atk_output', '/autotest/config', '/autotest/golden_path', '/autotest/result', '/autos_test', '/data/imagenet2012', '/home/infer/bin_bak/acl', '/home/pyacl'], 'pool': 'ascend-general-a2', 'image_label': 'swr.cn-north-4.myhuaweicloud.com/hw-ascend/smoke:ops-cv-910b'}]}, 'extend_env_comments': {'job_info': 'codearts-528772518c054c5f8f4625cc5dd1cda0-e700906deacc49609e3b95eab5c1678a-671e50b108d64e71939420950f1be3d0_20260910_10'}, 'ssh_mesh': 'group', 'extend_labels': {'cluster': 'false'}}
[2026/09/10 19:10:13.004 GMT+08:00] 2026-09-10 11:10:12 [sched] [281473081602336] [INFO] Environment allocation successful, env ID: lease-env1789038612-2639
[2026/09/10 19:10:13.004 GMT+08:00] 2026-09-10 11:10:12 [sched] [281473081602336] [INFO] Starting to query task status for task_id[lease-env1789038612-2639]
[2026/09/10 19:10:13.004 GMT+08:00] 2026-09-10 11:10:12 [sched] [281473081602336] [INFO] ***start 0 times query***
[2026/09/10 19:10:13.004 GMT+08:00] 2026-09-10 11:10:12 [sched] [281473090056480] [INFO] Environment allocation successful, env ID: lease-env1789038612-4805
[2026/09/10 19:10:13.004 GMT+08:00] 2026-09-10 11:10:12 [sched] [281473090056480] [INFO] Starting to query task status for task_id[lease-env1789038612-4805]
[2026/09/10 19:10:13.004 GMT+08:00] 2026-09-10 11:10:12 [sched] [281473090056480] [INFO] ***start 0 times query***
[2026/09/10 19:10:13.004 GMT+08:00] 2026-09-10 11:10:12 [sched] [281473090056480] [INFO] allocation_result is empty, wait 30s to query again
[2026/09/10 19:10:13.004 GMT+08:00] 2026-09-10 11:10:12 [sched] [281473081602336] [INFO] allocation_result is empty, wait 30s to query again
[2026/09/10 19:10:46.073 GMT+08:00] 2026-09-10 11:10:42 [sched] [281473090056480] [INFO] ***start 1 times query***
[2026/09/10 19:10:46.073 GMT+08:00] 2026-09-10 11:10:42 [sched] [281473081602336] [INFO] ***start 1 times query***
[2026/09/10 19:10:46.073 GMT+08:00] 2026-09-10 11:10:42 [sched] [281473090056480] [INFO] apply_env_res: {'env_id': 'lease-env1789038612-4805', 'groups': {'nodes_1': [{'name': 'device', 'res_type': 'container', 'status': 'rejected', 'node_ip': '', 'npu_ids': [], 'privileged': False}]}, 'status': 'rejected', 'name': 'env', 'created_at': '2026-09-10T11:10:12Z', 'expires_at': '2026-09-10T15:10:12Z', 'ttl': '14400', 'topology': '', 'extend_env_comments': {'job_info': 'codearts-528772518c054c5f8f4625cc5dd1cda0-e700906deacc49609e3b95eab5c1678a-671e50b108d64e71939420950f1be3d0_20260910_10'}, 'progress': {'total': 1, 'ready': 0, 'failed': 1, 'pending': 0}, 'ssh_mesh': {'enabled': False, 'scope': '', 'enrolled': [], 'failed': []}, 'errors': None}
[2026/09/10 19:10:46.073 GMT+08:00] 2026-09-10 11:10:42 [sched] [281473090056480] [ERROR] Environment allocation rejected, status: rejected
[2026/09/10 19:10:46.073 GMT+08:00] 2026-09-10 11:10:42 [sched] [281473090056480] [ERROR] Failed to allocate environment: Environment allocation rejected: Unknown
[2026/09/10 19:10:46.073 GMT+08:00] Traceback (most recent call last):
[2026/09/10 19:10:46.073 GMT+08:00]   File "***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor/src/scheduler/env_manager.py", line 297, in allocate_environments
[2026/09/10 19:10:46.073 GMT+08:00]     self._query_k8s_env_status(
[2026/09/10 19:10:46.073 GMT+08:00]   File "***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor/src/scheduler/env_manager.py", line 382, in _query_k8s_env_status
[2026/09/10 19:10:46.073 GMT+08:00]     raise RuntimeError(
[2026/09/10 19:10:46.073 GMT+08:00] RuntimeError: Environment allocation rejected: Unknown
[2026/09/10 19:10:46.073 GMT+08:00] 2026-09-10 11:10:42 [sched] [281473090056480] [ERROR] Failed to allocate environment for env_id: cann_single_A2_device_3_cover_single_type-nodes_1-A2, error: Environment allocation rejected: Unknown
[2026/09/10 19:10:46.073 GMT+08:00] Traceback (most recent call last):
[2026/09/10 19:10:46.073 GMT+08:00]   File "***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor/src/run_scheduler.py", line 237, in _allocate_environments_and_execute
[2026/09/10 19:10:46.073 GMT+08:00]     self.env_manager.allocate_environments(env_case_info)
[2026/09/10 19:10:46.073 GMT+08:00]   File "***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor/src/scheduler/env_manager.py", line 297, in allocate_environments
[2026/09/10 19:10:46.073 GMT+08:00]     self._query_k8s_env_status(
[2026/09/10 19:10:46.073 GMT+08:00]   File "***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor/src/scheduler/env_manager.py", line 382, in _query_k8s_env_status
[2026/09/10 19:10:46.073 GMT+08:00]     raise RuntimeError(
[2026/09/10 19:10:46.073 GMT+08:00] RuntimeError: Environment allocation rejected: Unknown
[2026/09/10 19:10:46.073 GMT+08:00] 2026-09-10 11:10:42 [sched] [281473142173728] [INFO] Task completed for env_id: cann_single_A2_device_3_cover_single_type-nodes_1-A2, result: False
[2026/09/10 19:10:46.073 GMT+08:00] 2026-09-10 11:10:42 [sched] [281473142173728] [ERROR] Failed to execute cases for env_id: cann_single_A2_device_3_cover_single_type-nodes_1-A2
[2026/09/10 19:10:46.073 GMT+08:00] 2026-09-10 11:10:42 [sched] [281473081602336] [INFO] apply_env_res: {'env_id': 'lease-env1789038612-2639', 'groups': {'nodes_1': [{'name': 'device', 'res_type': 'container', 'status': 'rejected', 'node_ip': '', 'npu_ids': [], 'privileged': False}]}, 'status': 'rejected', 'name': 'env', 'created_at': '2026-09-10T11:10:12Z', 'expires_at': '2026-09-10T15:10:12Z', 'ttl': '14400', 'topology': '', 'extend_env_comments': {'job_info': 'codearts-528772518c054c5f8f4625cc5dd1cda0-e700906deacc49609e3b95eab5c1678a-671e50b108d64e71939420950f1be3d0_20260910_10'}, 'progress': {'total': 1, 'ready': 0, 'failed': 1, 'pending': 0}, 'ssh_mesh': {'enabled': False, 'scope': '', 'enrolled': [], 'failed': []}, 'errors': None}
[2026/09/10 19:10:46.073 GMT+08:00] 2026-09-10 11:10:42 [sched] [281473081602336] [ERROR] Environment allocation rejected, status: rejected
[2026/09/10 19:10:46.073 GMT+08:00] 2026-09-10 11:10:42 [sched] [281473081602336] [ERROR] Failed to allocate environment: Environment allocation rejected: Unknown
[2026/09/10 19:10:46.073 GMT+08:00] Traceback (most recent call last):
[2026/09/10 19:10:46.073 GMT+08:00]   File "***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor/src/scheduler/env_manager.py", line 297, in allocate_environments
[2026/09/10 19:10:46.073 GMT+08:00]     self._query_k8s_env_status(
[2026/09/10 19:10:46.073 GMT+08:00]   File "***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor/src/scheduler/env_manager.py", line 382, in _query_k8s_env_status
[2026/09/10 19:10:46.073 GMT+08:00]     raise RuntimeError(
[2026/09/10 19:10:46.073 GMT+08:00] RuntimeError: Environment allocation rejected: Unknown
[2026/09/10 19:10:46.073 GMT+08:00] 2026-09-10 11:10:42 [sched] [281473081602336] [ERROR] Failed to allocate environment for env_id: cann_single_A2_device_2_cover_single_type-nodes_1-A2, error: Environment allocation rejected: Unknown
[2026/09/10 19:10:46.073 GMT+08:00] Traceback (most recent call last):
[2026/09/10 19:10:46.073 GMT+08:00]   File "***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor/src/run_scheduler.py", line 237, in _allocate_environments_and_execute
[2026/09/10 19:10:46.073 GMT+08:00]     self.env_manager.allocate_environments(env_case_info)
[2026/09/10 19:10:46.073 GMT+08:00]   File "***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor/src/scheduler/env_manager.py", line 297, in allocate_environments
[2026/09/10 19:10:46.073 GMT+08:00]     self._query_k8s_env_status(
[2026/09/10 19:10:46.073 GMT+08:00]   File "***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor/src/scheduler/env_manager.py", line 382, in _query_k8s_env_status
[2026/09/10 19:10:46.073 GMT+08:00]     raise RuntimeError(
[2026/09/10 19:10:46.073 GMT+08:00] RuntimeError: Environment allocation rejected: Unknown
[2026/09/10 19:10:46.073 GMT+08:00] 2026-09-10 11:10:42 [sched] [281473142173728] [INFO] Task completed for env_id: cann_single_A2_device_2_cover_single_type-nodes_1-A2, result: False
[2026/09/10 19:10:46.074 GMT+08:00] 2026-09-10 11:10:42 [sched] [281473142173728] [ERROR] Failed to execute cases for env_id: cann_single_A2_device_2_cover_single_type-nodes_1-A2
[2026/09/10 19:10:46.074 GMT+08:00] 2026-09-10 11:10:42 [sched] [281473142173728] [INFO] Submitting task for env_id: cann_single_A2_device_1_cover_single_type-nodes_1-A2
[2026/09/10 19:10:46.074 GMT+08:00] 2026-09-10 11:10:42 [sched] [281473081602336] [INFO] Allocating environment for env_id: cann_single_A2_device_1_cover_single_type-nodes_1-A2
[2026/09/10 19:10:46.074 GMT+08:00] 2026-09-10 11:10:42 [sched] [281473142173728] [INFO] Submitting task for env_id: cann_single_A2_device_4_cover_single_type-nodes_1-A2
[2026/09/10 19:10:46.074 GMT+08:00] 2026-09-10 11:10:42 [sched] [281473081602336] [INFO] Using image label: swr.cn-north-4.myhuaweicloud.com/hw-ascend/smoke:ops-cv-910b
[2026/09/10 19:10:46.074 GMT+08:00] 2026-09-10 11:10:42 [sched] [281473090056480] [INFO] Allocating environment for env_id: cann_single_A2_device_4_cover_single_type-nodes_1-A2
[2026/09/10 19:10:46.074 GMT+08:00] 2026-09-10 11:10:42 [sched] [281473081602336] [INFO] env_device_resource is empty, skipping mock allocation
[2026/09/10 19:10:46.074 GMT+08:00] 2026-09-10 11:10:42 [sched] [281473090056480] [INFO] Using image label: swr.cn-north-4.myhuaweicloud.com/hw-ascend/smoke:ops-cv-910b
[2026/09/10 19:10:46.074 GMT+08:00] 2026-09-10 11:10:42 [sched] [281473081602336] [INFO] Creating k8s environment with name: codearts-528772518c054c5f8f4625cc5dd1cda0-e700906deacc49609e3b95eab5c1678a-671e50b108d64e71939420950f1be3d0_20260910_10, ttl: None
[2026/09/10 19:10:46.074 GMT+08:00] 2026-09-10 11:10:42 [sched] [281473090056480] [INFO] env_device_resource is empty, skipping mock allocation
[2026/09/10 19:10:46.074 GMT+08:00] 2026-09-10 11:10:42 [sched] [281473081602336] [INFO] apply_env_k8s, payload={'env_definition': {'nodes_1': [{'name': 'device', 'res_type': 'container', 'cpu_arch': 'ARM', 'cpu_core_num': 48, 'npu_gen': 'A2', 'npu_num': 2, 'shm_size': '256Gi', 'memory_size': 256, 'resources': {'cpu': {'request': '48', 'limit': '128'}, 'memory': {'request': '256Gi', 'limit': '1024Gi'}}, 'use_nfs': True, 'mount_source_data': ['cann_ops_data1', 'cann_ops_data2', 'cann_ops_data3', 'cann_ops_data4', 'cann_ops_data5', 'cann_duo_os_autos_test', 'cann_duo_os_imagenet', 'cann_duo_os_acl', 'cann_duo_os_pyacl'], 'mount_dest_dir': ['/autotest/ATK_BIN', '/autotest/atk_output', '/autotest/config', '/autotest/golden_path', '/autotest/result', '/autos_test', '/data/imagenet2012', '/home/infer/bin_bak/acl', '/home/pyacl'], 'pool': 'ascend-general-a2', 'image_label': 'swr.cn-north-4.myhuaweicloud.com/hw-ascend/smoke:ops-cv-910b'}]}, 'extend_env_comments': {'job_info': 'codearts-528772518c054c5f8f4625cc5dd1cda0-e700906deacc49609e3b95eab5c1678a-671e50b108d64e71939420950f1be3d0_20260910_10'}, 'ssh_mesh': 'group', 'extend_labels': {'cluster': 'false'}}
[2026/09/10 19:10:46.074 GMT+08:00] 2026-09-10 11:10:42 [sched] [281473090056480] [INFO] Creating k8s environment with name: codearts-528772518c054c5f8f4625cc5dd1cda0-e700906deacc49609e3b95eab5c1678a-671e50b108d64e71939420950f1be3d0_20260910_10, ttl: None
[2026/09/10 19:10:46.074 GMT+08:00] 2026-09-10 11:10:42 [sched] [281473090056480] [INFO] apply_env_k8s, payload={'env_definition': {'nodes_1': [{'name': 'device', 'res_type': 'container', 'cpu_arch': 'ARM', 'cpu_core_num': 48, 'npu_gen': 'A2', 'npu_num': 2, 'shm_size': '256Gi', 'memory_size': 256, 'resources': {'cpu': {'request': '48', 'limit': '128'}, 'memory': {'request': '256Gi', 'limit': '1024Gi'}}, 'use_nfs': True, 'mount_source_data': ['cann_ops_data1', 'cann_ops_data2', 'cann_ops_data3', 'cann_ops_data4', 'cann_ops_data5', 'cann_duo_os_autos_test', 'cann_duo_os_imagenet', 'cann_duo_os_acl', 'cann_duo_os_pyacl'], 'mount_dest_dir': ['/autotest/ATK_BIN', '/autotest/atk_output', '/autotest/config', '/autotest/golden_path', '/autotest/result', '/autos_test', '/data/imagenet2012', '/home/infer/bin_bak/acl', '/home/pyacl'], 'pool': 'ascend-general-a2', 'image_label': 'swr.cn-north-4.myhuaweicloud.com/hw-ascend/smoke:ops-cv-910b'}]}, 'extend_env_comments': {'job_info': 'codearts-528772518c054c5f8f4625cc5dd1cda0-e700906deacc49609e3b95eab5c1678a-671e50b108d64e71939420950f1be3d0_20260910_10'}, 'ssh_mesh': 'group', 'extend_labels': {'cluster': 'false'}}
[2026/09/10 19:10:46.074 GMT+08:00] 2026-09-10 11:10:42 [sched] [281473081602336] [INFO] Environment allocation successful, env ID: lease-env1789038642-9413
[2026/09/10 19:10:46.074 GMT+08:00] 2026-09-10 11:10:42 [sched] [281473081602336] [INFO] Starting to query task status for task_id[lease-env1789038642-9413]
[2026/09/10 19:10:46.074 GMT+08:00] 2026-09-10 11:10:42 [sched] [281473081602336] [INFO] ***start 0 times query***
[2026/09/10 19:10:46.074 GMT+08:00] 2026-09-10 11:10:42 [sched] [281473090056480] [INFO] Environment allocation successful, env ID: lease-env1789038642-8755
[2026/09/10 19:10:46.074 GMT+08:00] 2026-09-10 11:10:42 [sched] [281473090056480] [INFO] Starting to query task status for task_id[lease-env1789038642-8755]
[2026/09/10 19:10:46.074 GMT+08:00] 2026-09-10 11:10:42 [sched] [281473090056480] [INFO] ***start 0 times query***
[2026/09/10 19:10:46.074 GMT+08:00] 2026-09-10 11:10:43 [sched] [281473081602336] [INFO] allocation_result is empty, wait 30s to query again
[2026/09/10 19:10:46.074 GMT+08:00] 2026-09-10 11:10:43 [sched] [281473090056480] [INFO] allocation_result is empty, wait 30s to query again
[2026/09/10 19:11:13.550 GMT+08:00] 2026-09-10 11:11:13 [sched] [281473081602336] [INFO] apply_env_res: {'env_id': 'lease-env1789038642-9413', 'groups': {'nodes_1': [{'name': 'device', 'res_type': 'container', 'status': 'rejected', 'node_ip': '', 'npu_ids': [], 'privileged': False}]}, 'status': 'rejected', 'name': 'env', 'created_at': '2026-09-10T11:10:42Z', 'expires_at': '2026-09-10T15:10:42Z', 'ttl': '14400', 'topology': '', 'extend_env_comments': {'job_info': 'codearts-528772518c054c5f8f4625cc5dd1cda0-e700906deacc49609e3b95eab5c1678a-671e50b108d64e71939420950f1be3d0_20260910_10'}, 'progress': {'total': 1, 'ready': 0, 'failed': 1, 'pending': 0}, 'ssh_mesh': {'enabled': False, 'scope': '', 'enrolled': [], 'failed': []}, 'errors': None}
[2026/09/10 19:11:13.550 GMT+08:00]     raise RuntimeError(
[2026/09/10 19:11:13.550 GMT+08:00] RuntimeError: Environment allocation rejected: Unknown
[2026/09/10 19:11:13.550 GMT+08:00]   File "***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor/src/scheduler/env_manager.py", line 297, in allocate_environments
[2026/09/10 19:11:13.550 GMT+08:00] 2026-09-10 11:11:13 [sched] [281473142173728] [ERROR] Failed to execute cases for env_id: cann_single_A2_device_1_cover_single_type-nodes_1-A2
[2026/09/10 19:11:13.551 GMT+08:00]   File "***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor/src/scheduler/env_manager.py", line 297, in allocate_environments
[2026/09/10 19:11:13.551 GMT+08:00]     self._query_k8s_env_status(
[2026/09/10 19:11:13.551 GMT+08:00]   File "***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor/src/scheduler/env_manager.py", line 382, in _query_k8s_env_status
[2026/09/10 19:11:13.551 GMT+08:00]     raise RuntimeError(
[2026/09/10 19:11:13.551 GMT+08:00] Traceback (most recent call last):
[2026/09/10 19:11:13.551 GMT+08:00]     self.env_manager.allocate_environments(env_case_info)
[2026/09/10 19:11:13.551 GMT+08:00]   File "***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor/src/scheduler/env_manager.py", line 297, in allocate_environments
[2026/09/10 19:11:13.551 GMT+08:00]   File "***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor/src/scheduler/env_manager.py", line 382, in _query_k8s_env_status
[2026/09/10 19:11:13.551 GMT+08:00] 2026-09-10 11:11:13 [sched] [281473142173728] [ERROR] Failed to execute cases for env_id: cann_single_A2_device_4_cover_single_type-nodes_1-A2
[2026/09/10 19:11:13.551 GMT+08:00] 2026-09-10 11:11:13 [sched] [281473142173728] [INFO] Releasing 4 environments
[2026/09/10 19:11:14.489 GMT+08:00] + echo '[ERROR]execute openlibing-pytest-executor. main.py fail, log file is ***//openlibing-pytest-executor-workspace/executor-log/scheduler_framework.log'
[2026/09/10 19:11:16.028 GMT+08:00] Finished: FAILURE
