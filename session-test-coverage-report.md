[2026/10/16 15:58:00.665 GMT+08:00] [INFO]  : [JobStatusPlugin] onStarted: j_Z947ObnE #1
[2026/10/16 15:58:00.667 GMT+08:00] Resume disabled by user, switching to high-performance, low-durability mode.
[2026/10/16 15:58:00.775 GMT+08:00] [INFO] [PRE_ENV:slave_create] : 该步骤开始执行
[2026/10/16 15:58:00.778 GMT+08:00] [INFO] [PRE_ENV:slave_create] : [slave] resources pool message: 2d46c49a941146c78a1b9cb5e80f936a
[2026/10/16 15:58:00.779 GMT+08:00] [WARNING] [PRE_ENV:slave_create] : [slave] find empty runtime, location: PRE_ENV.slave_create
[2026/10/16 15:58:00.779 GMT+08:00] [INFO] [PRE_ENV:slave_create] : [slave] Fixed content: No
[2026/10/16 15:58:00.881 GMT+08:00] [INFO] [PRE_ENV:slave_create] : [slave] Find available executor node:agent_1791951148880-ggFwBKGEbn
[2026/10/16 15:58:00.932 GMT+08:00] [INFO] [PRE_ENV:slave_create] : 该步骤执行完成
[2026/10/16 15:58:00.967 GMT+08:00] [INFO] [代码检出:external_pre_checkout] : 该步骤开始执行
[2026/10/16 15:58:00.968 GMT+08:00] [INFO] [代码检出:external_pre_checkout] : git plugin version: 1.12.5
[2026/10/16 15:58:00.997 GMT+08:00] [INFO] [代码检出:external_pre_checkout] : 成功配置文件。
[2026/10/16 15:58:01.295 GMT+08:00] [INFO] [代码检出:external_pre_checkout] : [WARN]DEV.CB.02101217,用户名或密码为空。
[2026/10/16 15:58:01.295 GMT+08:00] [INFO] [代码检出:external_pre_checkout] : 创建gitcode代码访问凭证成功。
[2026/10/16 15:58:01.295 GMT+08:00] [INFO] [代码检出:external_pre_checkout] : 该步骤执行完成
[2026/10/16 15:58:01.368 GMT+08:00] No credentials specified
[2026/10/16 15:58:01.368 GMT+08:00] set customize username password****           
[2026/10/16 15:58:01.383 GMT+08:00] addDefaultCredentials
[2026/10/16 15:58:01.396 GMT+08:00] git plugin version: 3.12.22-h1.cbu.codearts.build.r1
[2026/10/16 15:58:01.409 GMT+08:00] Cloning the remote Git repository
[2026/10/16 15:58:01.409 GMT+08:00] Using shallow clone
[2026/10/16 15:58:01.409 GMT+08:00] Avoid fetching tags
[2026/10/16 15:58:01.409 GMT+08:00] Honoring refspec on initial clone
[2026/10/16 15:58:01.428 GMT+08:00] Cloning repository https://gitcode.com/A1streomeria/ci_test.git
[2026/10/16 15:58:01.428 GMT+08:00]  > git init /opt/agent_1791951148880/workspace/j_Z947ObnE # timeout=10
[2026/10/16 15:58:01.433 GMT+08:00] Fetching upstream changes from https://gitcode.com/A1streomeria/ci_test.git
[2026/10/16 15:58:01.433 GMT+08:00]  > git --version # timeout=10
[2026/10/16 15:58:01.435 GMT+08:00]  > git --version # 'git version 2.34.1'
[2026/10/16 15:58:01.436 GMT+08:00] using GIT_ASKPASS to set credentials  username and password**** [2026/10/16 15:58:01.436 GMT+08:00] scmType is gitcode
[2026/10/16 15:58:01.437 GMT+08:00]  > git -c *** fetch --no-tags --force --progress --depth=1 -- https://gitcode.com/A1streomeria/ci_test.git +refs/heads/main:refs/remotes/origin/main # timeout=120
[2026/10/16 15:58:02.023 GMT+08:00]  > git config remote.origin.url https://gitcode.com/A1streomeria/ci_test.git # timeout=10
[2026/10/16 15:58:02.026 GMT+08:00]  > git config --add remote.origin.fetch +refs/heads/main:refs/remotes/origin/main # timeout=10
[2026/10/16 15:58:02.041 GMT+08:00]  > git config remote.origin.url https://gitcode.com/A1streomeria/ci_test.git # timeout=10
[2026/10/16 15:58:02.057 GMT+08:00] Fetching upstream changes from https://gitcode.com/A1streomeria/ci_test.git
[2026/10/16 15:58:02.057 GMT+08:00] using GIT_ASKPASS to set credentials  username and password**** [2026/10/16 15:58:02.058 GMT+08:00] scmType is gitcode
[2026/10/16 15:58:02.058 GMT+08:00]  > git -c *** fetch --no-tags --force --progress --depth=1 -- https://gitcode.com/A1streomeria/ci_test.git +refs/heads/main:refs/remotes/origin/main # timeout=120
[2026/10/16 15:58:02.490 GMT+08:00] Checking out Revision 782d2fc3d67ba916903476127e6043d3370ce0e1 (origin/main)
[2026/10/16 15:58:02.490 GMT+08:00] Disable Git LFS pull
[2026/10/16 15:58:02.549 GMT+08:00] Commit message: "update: 更新文件 smoke_A3.sh"
[2026/10/16 15:58:02.549 GMT+08:00] First time build. Skipping changelog.
[2026/10/16 15:58:02.579 GMT+08:00] [INFO] [代码检出:external_post_checkout] : 该步骤开始执行
[2026/10/16 15:58:02.652 GMT+08:00] [INFO] [代码检出:external_post_checkout] : 该步骤执行完成
[2026/10/16 15:58:03.115 GMT+08:00] + set -euo pipefail
[2026/10/16 15:58:03.115 GMT+08:00] + echo 'pid: 4211ddb76d924f938aaef60ef4c4c2a1'
[2026/10/16 15:58:03.115 GMT+08:00] pid: 4211ddb76d924f938aaef60ef4c4c2a1
[2026/10/16 15:58:03.115 GMT+08:00] + echo 'prid: f18b4f92325f49be83b9aba2e4d2a133'
[2026/10/16 15:58:03.115 GMT+08:00] prid: f18b4f92325f49be83b9aba2e4d2a133
[2026/10/16 15:58:03.115 GMT+08:00] + GIT_USER=*****
[2026/10/16 15:58:03.115 GMT+08:00] + GIT_PWD=*****
[2026/10/16 15:58:03.115 GMT+08:00] + PROJECT_ID=6b5df9811c84434296883cb706db6211
[2026/10/16 15:58:03.115 GMT+08:00] + JOB_RUN_ID=e739572ace2a4723a5d9d31263feee3c_20261016_5
[2026/10/16 15:58:03.115 GMT+08:00] + BASE_DIR=***//openlibing-pytest-executor-workspace
[2026/10/16 15:58:03.115 GMT+08:00] + EXECUTOR_LOG_DIR=***//openlibing-pytest-executor-workspace/executor-log
[2026/10/16 15:58:03.115 GMT+08:00] + EXECUTOR_LOG_FILE=***//openlibing-pytest-executor-workspace/executor-log/scheduler_framework.log
[2026/10/16 15:58:03.115 GMT+08:00] + PYTEST_TESTKIT_DIR=***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testkit
[2026/10/16 15:58:03.115 GMT+08:00] + TESTCASE_COLLETOR_DIR=***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testcase-collector
[2026/10/16 15:58:03.115 GMT+08:00] + EXECUTOR_BRANCH=master
[2026/10/16 15:58:03.115 GMT+08:00] + OBS_INFO='{"ak":"*****","sk":"*****","bucket_name":"ascend-package","server":"https://obs.cn-north-4.myhuaweicloud.com","base_url":"https://ascend-package.obs.cn-north-4.myhuaweicloud.com/msmodelslim/nightly/log"}'
[2026/10/16 15:58:03.115 GMT+08:00] ++ date +%Y%m%d
[2026/10/16 15:58:03.115 GMT+08:00] + TASK_ID=6b5df9811c84434296883cb706db6211202610162041
[2026/10/16 15:58:03.115 GMT+08:00] + MAX_WORKERS=2
[2026/10/16 15:58:03.115 GMT+08:00] + echo '[INFO] create work dir'
[2026/10/16 15:58:03.115 GMT+08:00] [INFO] create work dir
[2026/10/16 15:58:03.115 GMT+08:00] + mkdir -p ***//openlibing-pytest-executor-workspace
[2026/10/16 15:58:03.115 GMT+08:00] + wget https://obs-community.obs.cn-north-1.myhuaweicloud.com/obsutil/current/obsutil_linux_arm64.tar.gz --no-check-certificate
[2026/10/16 15:58:03.115 GMT+08:00] --2026-10-16 07:58:02--  https://obs-community.obs.cn-north-1.myhuaweicloud.com/obsutil/current/obsutil_linux_arm64.tar.gz
[2026/10/16 15:58:03.115 GMT+08:00] Resolving obs-community.obs.cn-north-1.myhuaweicloud.com (obs-community.obs.cn-north-1.myhuaweicloud.com)... ***.***.***.27, ***.***.***.163, ***.***.***.98
[2026/10/16 15:58:03.115 GMT+08:00] Connecting to obs-community.obs.cn-north-1.myhuaweicloud.com (obs-community.obs.cn-north-1.myhuaweicloud.com)|***.***.***.27|:443... connected.
[2026/10/16 15:58:03.115 GMT+08:00] HTTP request sent, awaiting response... 200 OK
[2026/10/16 15:58:03.115 GMT+08:00] Length: 4408763 (4.2M) [application/gzip]
[2026/10/16 15:58:03.116 GMT+08:00] Saving to: 'obsutil_linux_arm64.tar.gz'
[2026/10/16 15:58:03.116 GMT+08:00] 
[2026/10/16 15:58:03.116 GMT+08:00]      0K .......... .......... .......... .......... ..........  1% 2.09M 2s
[2026/10/16 15:58:03.116 GMT+08:00]     50K .......... .......... .......... .......... ..........  2% 6.37M 1s
[2026/10/16 15:58:03.116 GMT+08:00]    100K .......... .......... .......... .......... ..........  3% 7.86M 1s
[2026/10/16 15:58:03.116 GMT+08:00]    150K .......... .......... .......... .......... ..........  4% 14.1M 1s
[2026/10/16 15:58:03.116 GMT+08:00]    200K .......... .......... .......... .......... ..........  5% 12.1M 1s
[2026/10/16 15:58:03.116 GMT+08:00]    250K .......... .......... .......... .......... ..........  6% 18.9M 1s
[2026/10/16 15:58:03.116 GMT+08:00]    300K .......... .......... .......... .......... ..........  8% 23.0M 1s
[2026/10/16 15:58:03.153 GMT+08:00]    350K ..starting check in ***/@tmp/durable-a4cf0ddb
[2026/10/16 15:58:02.481 GMT+08:00]  > git rev-parse origin/main^{commit} # timeout=10
[2026/10/16 15:58:02.497 GMT+08:00]  > git config core.sparsecheckout # timeout=10
[2026/10/16 15:58:02.500 GMT+08:00]  > git checkout -f 782d2fc3d67ba916903476127e6043d3370ce0e1 # timeout=120
[2026/10/16 15:58:02.513 GMT+08:00]  > git branch -a -v --no-abbrev # timeout=10
[2026/10/16 15:58:02.516 GMT+08:00]  > git checkout -b main 782d2fc3d67ba916903476127e6043d3370ce0e1 # timeout=120
[2026/10/16 15:58:03.441 GMT+08:00] ........ .......... .......... .......... ..........  9% 22.5M 1s
[2026/10/16 15:58:03.441 GMT+08:00]    400K .......... .......... .......... .......... .......... 10% 25.5M 0s
[2026/10/16 15:58:03.441 GMT+08:00]    450K .......... .......... .......... .......... .......... 11% 20.0M 0s
[2026/10/16 15:58:03.442 GMT+08:00]    500K .......... .......... .......... .......... .......... 12% 49.5M 0s
[2026/10/16 15:58:03.442 GMT+08:00]    550K .......... .......... .......... .......... .......... 13% 29.9M 0s
[2026/10/16 15:58:03.442 GMT+08:00]    600K .......... .......... .......... .......... .......... 15% 33.3M 0s
[2026/10/16 15:58:03.442 GMT+08:00]    650K .......... .......... .......... .......... .......... 16% 69.8M 0s
[2026/10/16 15:58:03.442 GMT+08:00]    700K .......... .......... .......... .......... .......... 17% 34.3M 0s
[2026/10/16 15:58:03.442 GMT+08:00]    750K .......... .......... .......... .......... .......... 18%  109M 0s
[2026/10/16 15:58:03.442 GMT+08:00]    800K .......... .......... .......... .......... .......... 19% 40.7M 0s
[2026/10/16 15:58:03.442 GMT+08:00]    850K .......... .......... .......... .......... .......... 20% 43.7M 0s
[2026/10/16 15:58:03.442 GMT+08:00]    900K .......... .......... .......... .......... .......... 22% 84.2M 0s
[2026/10/16 15:58:03.442 GMT+08:00]    950K .......... .......... .......... .......... .......... 23% 29.1M 0s
[2026/10/16 15:58:03.442 GMT+08:00]   1000K .......... .......... .......... .......... .......... 24%  169M 0s
[2026/10/16 15:58:03.442 GMT+08:00]   1050K .......... .......... .......... .......... .......... 25% 56.7M 0s
[2026/10/16 15:58:03.442 GMT+08:00]   1100K .......... .......... .......... .......... .......... 26% 79.3M 0s
[2026/10/16 15:58:03.442 GMT+08:00]   1150K .......... .......... .......... .......... .......... 27% 54.7M 0s
[2026/10/16 15:58:03.442 GMT+08:00]   1200K .......... .......... .......... .......... .......... 29% 48.3M 0s
[2026/10/16 15:58:03.442 GMT+08:00]   1250K .......... .......... .......... .......... .......... 30% 91.4M 0s
[2026/10/16 15:58:03.442 GMT+08:00]   1300K .......... .......... .......... .......... .......... 31%  119M 0s
[2026/10/16 15:58:03.442 GMT+08:00]   1350K .......... .......... .......... .......... .......... 32% 73.4M 0s
[2026/10/16 15:58:03.442 GMT+08:00]   1400K .......... .......... .......... .......... .......... 33%  134M 0s
[2026/10/16 15:58:03.442 GMT+08:00]   1450K .......... .......... .......... .......... .......... 34% 71.6M 0s
[2026/10/16 15:58:03.442 GMT+08:00]   1500K .......... .......... .......... .......... .......... 36%  140M 0s
[2026/10/16 15:58:03.442 GMT+08:00]   1550K .......... .......... .......... .......... .......... 37% 83.8M 0s
[2026/10/16 15:58:03.442 GMT+08:00]   1600K .......... .......... .......... .......... .......... 38% 86.1M 0s
[2026/10/16 15:58:03.442 GMT+08:00]   1650K .......... .......... .......... .......... .......... 39% 95.1M 0s
[2026/10/16 15:58:03.442 GMT+08:00]   1700K .......... .......... .......... .......... .......... 40%  122M 0s
[2026/10/16 15:58:03.442 GMT+08:00]   1750K .......... .......... .......... .......... .......... 41% 92.6M 0s
[2026/10/16 15:58:03.442 GMT+08:00]   1800K .......... .......... .......... .......... .......... 42%  145M 0s
[2026/10/16 15:58:03.442 GMT+08:00]   1850K .......... .......... .......... .......... .......... 44% 94.7M 0s
[2026/10/16 15:58:03.442 GMT+08:00]   1900K .......... .......... .......... .......... .......... 45%  166M 0s
[2026/10/16 15:58:03.442 GMT+08:00]   1950K .......... .......... .......... .......... .......... 46% 53.6M 0s
[2026/10/16 15:58:03.442 GMT+08:00]   2000K .......... .......... .......... .......... .......... 47%  226M 0s
[2026/10/16 15:58:03.442 GMT+08:00]   2050K .......... .......... .......... .......... .......... 48%  335M 0s
[2026/10/16 15:58:03.442 GMT+08:00]   2100K .......... .......... .......... .......... .......... 49% 82.1M 0s
[2026/10/16 15:58:03.442 GMT+08:00]   2150K .......... .......... .......... .......... .......... 51%  220M 0s
[2026/10/16 15:58:03.442 GMT+08:00]   2200K .......... .......... .......... .......... .......... 52% 98.9M 0s
[2026/10/16 15:58:03.442 GMT+08:00]   2250K .......... .......... .......... .......... .......... 53%  379M 0s
[2026/10/16 15:58:03.442 GMT+08:00]   2300K .......... .......... .......... .......... .......... 54%  131M 0s
[2026/10/16 15:58:03.442 GMT+08:00]   2350K .......... .......... .......... .......... .......... 55%  106M 0s
[2026/10/16 15:58:03.442 GMT+08:00]   2400K .......... .......... .......... .......... .......... 56%  155M 0s
[2026/10/16 15:58:03.442 GMT+08:00]   2450K .......... .......... .......... .......... .......... 58% 57.5M 0s
[2026/10/16 15:58:03.442 GMT+08:00]   2500K .......... .......... .......... .......... .......... 59%  327M 0s
[2026/10/16 15:58:03.442 GMT+08:00]   2550K .......... .......... .......... .......... .......... 60%  316M 0s
[2026/10/16 15:58:03.442 GMT+08:00]   2600K .......... .......... .......... .......... .......... 61%  143M 0s
[2026/10/16 15:58:03.442 GMT+08:00]   2650K .......... .......... .......... .......... .......... 62%  115M 0s
[2026/10/16 15:58:03.442 GMT+08:00]   2700K .......... .......... .......... .......... .......... 63%  373M 0s
[2026/10/16 15:58:03.442 GMT+08:00]   2750K .......... .......... .......... .......... .......... 65%  117M 0s
[2026/10/16 15:58:03.442 GMT+08:00]   2800K .......... .......... .......... .......... .......... 66%  159M 0s
[2026/10/16 15:58:03.442 GMT+08:00]   2850K .......... .......... .......... .......... .......... 67%  165M 0s
[2026/10/16 15:58:03.442 GMT+08:00]   2900K .......... .......... .......... .......... .......... 68%  195M 0s
[2026/10/16 15:58:03.442 GMT+08:00]   2950K .......... .......... .......... .......... .......... 69%  237M 0s
[2026/10/16 15:58:03.442 GMT+08:00]   3000K .......... .......... .......... .......... .......... 70%  187M 0s
[2026/10/16 15:58:03.442 GMT+08:00]   3050K .......... .......... .......... .......... .......... 72%  157M 0s
[2026/10/16 15:58:03.442 GMT+08:00]   3100K .......... .......... .......... .......... .......... 73%  170M 0s
[2026/10/16 15:58:03.442 GMT+08:00]   3150K .......... .......... .......... .......... .......... 74%  268M 0s
[2026/10/16 15:58:03.443 GMT+08:00]   3200K .......... .......... .......... .......... .......... 75%  165M 0s
[2026/10/16 15:58:03.443 GMT+08:00]   3250K .......... .......... .......... .......... .......... 76%  229M 0s
[2026/10/16 15:58:03.443 GMT+08:00]   3300K .......... .......... .......... .......... .......... 77%  137M 0s
[2026/10/16 15:58:03.443 GMT+08:00]   3350K .......... .......... .......... .......... .......... 78%  248M 0s
[2026/10/16 15:58:03.443 GMT+08:00]   3400K .......... .......... .......... .......... .......... 80%  139M 0s
[2026/10/16 15:58:03.443 GMT+08:00]   3450K .......... .......... .......... .......... .......... 81%  340M 0s
[2026/10/16 15:58:03.443 GMT+08:00]   3500K .......... .......... .......... .......... .......... 82%  310M 0s
[2026/10/16 15:58:03.443 GMT+08:00]   3550K .......... .......... .......... .......... .......... 83% 15.1M 0s
[2026/10/16 15:58:03.443 GMT+08:00]   3600K .......... .......... .......... .......... .......... 84%  221M 0s
[2026/10/16 15:58:03.443 GMT+08:00]   3650K .......... .......... .......... .......... .......... 85%  301M 0s
[2026/10/16 15:58:03.443 GMT+08:00]   3700K .......... .......... .......... .......... .......... 87%  362M 0s
[2026/10/16 15:58:03.443 GMT+08:00]   3750K .......... .......... .......... .......... .......... 88%  316M 0s
[2026/10/16 15:58:03.443 GMT+08:00]   3800K .......... .......... .......... .......... .......... 89%  232M 0s
[2026/10/16 15:58:03.443 GMT+08:00]   3850K .......... .......... .......... .......... .......... 90%  300M 0s
[2026/10/16 15:58:03.443 GMT+08:00]   3900K .......... .......... .......... .......... .......... 91%  234M 0s
[2026/10/16 15:58:03.443 GMT+08:00]   3950K .......... .......... .......... .......... .......... 92%  363M 0s
[2026/10/16 15:58:03.443 GMT+08:00]   4000K .......... .......... .......... .......... .......... 94%  227M 0s
[2026/10/16 15:58:03.443 GMT+08:00]   4050K .......... .......... .......... .......... .......... 95%  308M 0s
[2026/10/16 15:58:03.443 GMT+08:00]   4100K .......... .......... .......... .......... .......... 96%  325M 0s
[2026/10/16 15:58:03.443 GMT+08:00]   4150K .......... .......... .......... .......... .......... 97%  339M 0s
[2026/10/16 15:58:03.443 GMT+08:00]   4200K .......... .......... .......... .......... .......... 98%  315M 0s
[2026/10/16 15:58:03.443 GMT+08:00]   4250K .......... .......... .......... .......... .......... 99%  357M 0s
[2026/10/16 15:58:03.443 GMT+08:00]   4300K .....                                                 100%  199M=0.09s
[2026/10/16 15:58:03.443 GMT+08:00] 
[2026/10/16 15:58:03.443 GMT+08:00] 2026-10-16 07:58:03 (45.0 MB/s) - 'obsutil_linux_arm64.tar.gz' saved [4408763/4408763]
[2026/10/16 15:58:03.443 GMT+08:00] 
[2026/10/16 15:58:03.443 GMT+08:00] + tar -zxvf obsutil_linux_arm64.tar.gz
[2026/10/16 15:58:03.443 GMT+08:00] obsutil_linux_arm64_5.8.9/
[2026/10/16 15:58:03.443 GMT+08:00] obsutil_linux_arm64_5.8.9/obsutil
[2026/10/16 15:58:03.443 GMT+08:00] obsutil_linux_arm64_5.8.9/setup.sh
[2026/10/16 15:58:03.443 GMT+08:00] ++ ls -d obsutil_linux_arm64_5.8.9/
[2026/10/16 15:58:03.443 GMT+08:00] ++ head -n1
[2026/10/16 15:58:03.443 GMT+08:00] ++ sed 's|/$||'
[2026/10/16 15:58:03.443 GMT+08:00] + OBSUTIL_DIR=obsutil_linux_arm64_5.8.9
[2026/10/16 15:58:03.443 GMT+08:00] + chmod +x obsutil_linux_arm64_5.8.9/obsutil
[2026/10/16 15:58:03.443 GMT+08:00] + ./obsutil_linux_arm64_5.8.9/obsutil config -i=***** -k=***** -e=obs.cn-north-4.myhuaweicloud.com
[2026/10/16 15:58:03.443 GMT+08:00] Config file url:
[2026/10/16 15:58:03.443 GMT+08:00]   /root/.obsutilconfig
[2026/10/16 15:58:03.443 GMT+08:00] 
[2026/10/16 15:58:03.443 GMT+08:00] Update config file successfully!
[2026/10/16 15:58:03.443 GMT+08:00] + echo '[INFO] git clone openlibing-pytest-excutor...'
[2026/10/16 15:58:03.443 GMT+08:00] [INFO] git clone openlibing-pytest-excutor...
[2026/10/16 15:58:03.443 GMT+08:00] + GIT_TERMINAL_PROMPT=0
[2026/10/16 15:58:03.443 GMT+08:00] + git clone --depth 1 -b master https://*****:*****@gitcode.com/openlibing/openlibing-pytest-executor.git ***//openlibing-pytest-executor-workspace/openlibing-pytest-executor
[2026/10/16 15:58:03.443 GMT+08:00] Cloning into '***//openlibing-pytest-executor-workspace/openlibing-pytest-executor'...
[2026/10/16 15:58:04.140 GMT+08:00] + mkdir -p ***//openlibing-pytest-executor-workspace/executor-log
[2026/10/16 15:58:04.140 GMT+08:00] + mkdir -p ***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testkit
[2026/10/16 15:58:04.140 GMT+08:00] + mkdir -p ***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testcase-collector
[2026/10/16 15:58:04.140 GMT+08:00] + PYTEST_TESTKIT_FILE=***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testkit/pytest_testkit-1.0.0-py3-none-any.whl
[2026/10/16 15:58:04.140 GMT+08:00] + wget -P ***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testkit https://gitcode.com/openlibing/openlibing-pytest-executor/releases/download/v1.0.0-alpha/pytest_testkit-1.0.0-py3-none-any.whl
[2026/10/16 15:58:04.140 GMT+08:00] --2026-10-16 07:58:03--  https://gitcode.com/openlibing/openlibing-pytest-executor/releases/download/v1.0.0-alpha/pytest_testkit-1.0.0-py3-none-any.whl
[2026/10/16 15:58:04.140 GMT+08:00] Resolving gitcode.com (gitcode.com)... ***.***.***.180
[2026/10/16 15:58:04.140 GMT+08:00] Connecting to gitcode.com (gitcode.com)|***.***.***.180|:443... connected.
[2026/10/16 15:58:04.140 GMT+08:00] HTTP request sent, awaiting response... 302 Found
[2026/10/16 15:58:04.140 GMT+08:00] Location: https://file-cdn.gitcode.com/9099034/releases/untagger_9ce1facf929d40eb8e6df8f014be9136/pytest_testkit-1.0.0-py3-none-any.whl?auth_key=1792137483-43988a3f1320489abbd42a32c30be283-0-ffaf94e05e6a50906a18cf6b7a23962b4d37f6ccd6cba56faa37465b6eb678e8 [following]
[2026/10/16 15:58:04.140 GMT+08:00] --2026-10-16 07:58:03--  https://file-cdn.gitcode.com/9099034/releases/untagger_9ce1facf929d40eb8e6df8f014be9136/pytest_testkit-1.0.0-py3-none-any.whl?auth_key=1792137483-43988a3f1320489abbd42a32c30be283-0-ffaf94e05e6a50906a18cf6b7a23962b4d37f6ccd6cba56faa37465b6eb678e8
[2026/10/16 15:58:04.140 GMT+08:00] Resolving file-cdn.gitcode.com (file-cdn.gitcode.com)... ***.***.***.155, ***.***.***.152, ***.***.***.153, ...
[2026/10/16 15:58:04.140 GMT+08:00] Connecting to file-cdn.gitcode.com (file-cdn.gitcode.com)|***.***.***.155|:443... connected.
[2026/10/16 15:58:04.465 GMT+08:00] HTTP request sent, awaiting response... 200 OK
[2026/10/16 15:58:04.465 GMT+08:00] Length: 73249 (72K) [application/octet-stream]
[2026/10/16 15:58:04.465 GMT+08:00] Saving to: '***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testkit/pytest_testkit-1.0.0-py3-none-any.whl'
[2026/10/16 15:58:04.465 GMT+08:00] 
[2026/10/16 15:58:04.465 GMT+08:00]      0K .......... .......... .......... .......... .......... 69% 1.54M 0s
[2026/10/16 15:58:04.465 GMT+08:00]     50K .......... .......... .                               100% 8.59M=0.03s
[2026/10/16 15:58:04.465 GMT+08:00] 
[2026/10/16 15:58:04.465 GMT+08:00] 2026-10-16 07:58:04 (2.05 MB/s) - '***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testkit/pytest_testkit-1.0.0-py3-none-any.whl' saved [73249/73249]
[2026/10/16 15:58:04.465 GMT+08:00] 
[2026/10/16 15:58:04.465 GMT+08:00] + ls ***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testkit/pytest_testkit-1.0.0-py3-none-any.whl
[2026/10/16 15:58:04.465 GMT+08:00] ***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testkit/pytest_testkit-1.0.0-py3-none-any.whl
[2026/10/16 15:58:04.465 GMT+08:00] + TESTCASE_COLLETOR_FILE=***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testcase-collector/pytest_testcase_collector-1.0.0-py3-none-any.whl
[2026/10/16 15:58:04.465 GMT+08:00] + wget -P ***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testcase-collector https://gitcode.com/openlibing/openlibing-pytest-executor/releases/download/pytest-testcase-collector-1.0.0/pytest_testcase_collector-1.0.0-py3-none-any.whl
[2026/10/16 15:58:04.465 GMT+08:00] --2026-10-16 07:58:04--  https://gitcode.com/openlibing/openlibing-pytest-executor/releases/download/pytest-testcase-collector-1.0.0/pytest_testcase_collector-1.0.0-py3-none-any.whl
[2026/10/16 15:58:04.465 GMT+08:00] Resolving gitcode.com (gitcode.com)... ***.***.***.180
[2026/10/16 15:58:04.465 GMT+08:00] Connecting to gitcode.com (gitcode.com)|***.***.***.180|:443... connected.
[2026/10/16 15:58:04.465 GMT+08:00] HTTP request sent, awaiting response... 302 Found
[2026/10/16 15:58:04.465 GMT+08:00] Location: https://file-cdn.gitcode.com/9099034/releases/untagger_8a06d959d9f74ac09748fb720f5d85e8/pytest_testcase_collector-1.0.0-py3-none-any.whl?auth_key=1792137484-6c34a900fe544ac3906f25e1b6a05e81-0-0320e1a069348581ff91b2ff2dcd126ec65986645963aa4392c86c3c9bfa10b0 [following]
[2026/10/16 15:58:04.465 GMT+08:00] --2026-10-16 07:58:04--  https://file-cdn.gitcode.com/9099034/releases/untagger_8a06d959d9f74ac09748fb720f5d85e8/pytest_testcase_collector-1.0.0-py3-none-any.whl?auth_key=1792137484-6c34a900fe544ac3906f25e1b6a05e81-0-0320e1a069348581ff91b2ff2dcd126ec65986645963aa4392c86c3c9bfa10b0
[2026/10/16 15:58:04.465 GMT+08:00] Resolving file-cdn.gitcode.com (file-cdn.gitcode.com)... ***.***.***.155, ***.***.***.152, ***.***.***.153, ...
[2026/10/16 15:58:04.465 GMT+08:00] Connecting to file-cdn.gitcode.com (file-cdn.gitcode.com)|***.***.***.155|:443... connected.
[2026/10/16 15:58:04.465 GMT+08:00] HTTP request sent, awaiting response... 200 OK
[2026/10/16 15:58:04.465 GMT+08:00] Length: 15058 (15K) [application/octet-stream]
[2026/10/16 15:58:04.465 GMT+08:00] Saving to: '***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testcase-collector/pytest_testcase_collector-1.0.0-py3-none-any.whl'
[2026/10/16 15:58:04.465 GMT+08:00] 
[2026/10/16 15:58:04.465 GMT+08:00]      0K .......... ....                                       100%  325M=0s
[2026/10/16 15:58:04.465 GMT+08:00] 
[2026/10/16 15:58:04.465 GMT+08:00] 2026-10-16 07:58:04 (325 MB/s) - '***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testcase-collector/pytest_testcase_collector-1.0.0-py3-none-any.whl' saved [15058/15058]
[2026/10/16 15:58:04.465 GMT+08:00] 
[2026/10/16 15:58:04.465 GMT+08:00] + ls ***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testcase-collector/pytest_testcase_collector-1.0.0-py3-none-any.whl
[2026/10/16 15:58:04.465 GMT+08:00] ***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testcase-collector/pytest_testcase_collector-1.0.0-py3-none-any.whl
[2026/10/16 15:58:04.465 GMT+08:00] + echo '[INFO] git clone testcase code...'
[2026/10/16 15:58:04.465 GMT+08:00] [INFO] git clone testcase code...
[2026/10/16 15:58:04.465 GMT+08:00] + TEST_CASE_DIR=***//openlibing-pytest-executor-workspace/pytest-infra
[2026/10/16 15:58:04.465 GMT+08:00] + mkdir -p ***//openlibing-pytest-executor-workspace/pytest-infra
[2026/10/16 15:58:04.465 GMT+08:00] + CASE_BRANCH=main
[2026/10/16 15:58:04.465 GMT+08:00] + GIT_TERMINAL_PROMPT=0
[2026/10/16 15:58:04.465 GMT+08:00] + git clone --depth 1 -b main https://*****:*****@gitcode.com/AscendTest/pytest-infra.git ***//openlibing-pytest-executor-workspace/pytest-infra
[2026/10/16 15:58:04.465 GMT+08:00] Cloning into '***//openlibing-pytest-executor-workspace/pytest-infra'...
[2026/10/16 15:58:05.595 GMT+08:00] + pip config set global.index-url https://mirrors.huaweicloud.com/repository/pypi/simple
[2026/10/16 15:58:05.918 GMT+08:00] Writing to /root/.config/pip/pip.conf
[2026/10/16 15:58:05.918 GMT+08:00] + echo '[INFO] execute test cases...'
[2026/10/16 15:58:05.918 GMT+08:00] [INFO] execute test cases...
[2026/10/16 15:58:05.919 GMT+08:00] + pip install -r ***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor/requirements.txt -q
[2026/10/16 15:58:06.242 GMT+08:00] WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager, possibly rendering your system unusable. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv. Use the --root-user-action option if you know what you are doing and want to suppress this warning.
[2026/10/16 15:58:06.242 GMT+08:00] + python3 -u ***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor/main.py --testcase_dir ***//openlibing-pytest-executor-workspace/pytest-infra --log_dir ***//openlibing-pytest-executor-workspace/executor-log --pytest_testkit_path ***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testkit/pytest_testkit-1.0.0-py3-none-any.whl --testcase_collector_path ***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/openlibing-pytest-executor/pytest-testcase-collector/pytest_testcase_collector-1.0.0-py3-none-any.whl --obs '{"ak":"*****","sk":"*****","bucket_name":"ascend-package","server":"https://obs.cn-north-4.myhuaweicloud.com","base_url":"https://ascend-package.obs.cn-north-4.myhuaweicloud.com/msmodelslim/nightly/log"}' --task_id 6b5df9811c84434296883cb706db6211202610162041 --testcase_config_file resources/env_config/mindstudio_ini/pytest_mindstudio_modelslim_a3.ini --image_label swr.cn-north-4.myhuaweicloud.com/atlas-ci/mindstudio-msmodelslim-nightly:a3-aarch64 --pipeline_id 4211ddb76d924f938aaef60ef4c4c2a1 --pipeline_run_id f18b4f92325f49be83b9aba2e4d2a133 --job_run_id e739572ace2a4723a5d9d31263feee3c_20261016_5 --scheduler_secret '*****' --max_workers 2
[2026/10/16 15:58:06.243 GMT+08:00] + tee -a ***//openlibing-pytest-executor-workspace/executor-log/scheduler_framework.log
[2026/10/16 15:58:06.565 GMT+08:00] [281472948195360] [INFO] Not using HidevLab, skipping key generation
[2026/10/16 15:58:06.565 GMT+08:00] [281472948195360] [INFO] Successfully obtained local IP via UDP method: ***.***.***.215
[2026/10/16 15:58:06.565 GMT+08:00] [281472948195360] [INFO] Read pytest config from ***//openlibing-pytest-executor-workspace/pytest-infra/resources/env_config/mindstudio_ini/pytest_mindstudio_modelslim_a3.ini: {'infra_log_level': 'INFO'}
[2026/10/16 15:58:06.566 GMT+08:00] [281472948195360] [INFO] pytest_config: {'infra_log_level': 'INFO'}
[2026/10/16 15:58:06.566 GMT+08:00] [281472948195360] [INFO] Step 1: Collecting and filtering test cases with @pytest.mark.env...
[2026/10/16 15:58:06.566 GMT+08:00] [281472948195360] [INFO] Collecting pytest cases from directory: ***//openlibing-pytest-executor-workspace/pytest-infra
[2026/10/16 15:58:06.566 GMT+08:00] [281472948195360] [INFO] Installing dependencies from ***//openlibing-pytest-executor-workspace/pytest-infra/requirements.txt
[2026/10/16 15:58:07.262 GMT+08:00] [281472948195360] [INFO] Successfully installed requirements from ***//openlibing-pytest-executor-workspace/pytest-infra/requirements.txt
[2026/10/16 15:58:07.262 GMT+08:00] [281472948195360] [INFO] Case filtering in directory: ***//openlibing-pytest-executor-workspace/pytest-infra
[2026/10/16 15:58:07.262 GMT+08:00] [281472948195360] [INFO] Case filter config file: resources/env_config/mindstudio_ini/pytest_mindstudio_modelslim_a3.ini
[2026/10/16 15:58:07.586 GMT+08:00] [281472948195360] [INFO] pytest collect stdout:
[2026/10/16 15:58:07.587 GMT+08:00] testcase/mindstudio/modelslim/test_analyze_check_param_error.py: 5
[2026/10/16 15:58:07.587 GMT+08:00] testcase/mindstudio/modelslim/test_analyze_sensitive_layers.py: 2
[2026/10/16 15:58:07.587 GMT+08:00] testcase/mindstudio/modelslim/test_quant_no_transformers_warning.py: 1
[2026/10/16 15:58:07.587 GMT+08:00] testcase/mindstudio/modelslim/test_quant_qwen3_32b_w8a16_awq.py: 1
[2026/10/16 15:58:07.587 GMT+08:00] testcase/mindstudio/modelslim/test_quant_qwen3_32b_w8a8.py: 2
[2026/10/16 15:58:07.587 GMT+08:00] testcase/mindstudio/modelslim/test_quant_qwen3_8b_w8a8s.py: 1
[2026/10/16 15:58:07.587 GMT+08:00] testcase/mindstudio/modelslim/test_quant_qwen3_vl_30b_a3b_w8a8_mxfp8.py: 1
[2026/10/16 15:58:07.587 GMT+08:00] testcase/mindstudio/modelslim/test_quant_qwen3_vl_4b_w8a8.py: 1
[2026/10/16 15:58:07.587 GMT+08:00] 
[2026/10/16 15:58:07.587 GMT+08:00] 
[2026/10/16 15:58:07.587 GMT+08:00] [281472948195360] [WARNING] pytest collect stderr:
[2026/10/16 15:58:07.587 GMT+08:00] [2026-10-16 07:58:07][INFO][plugin.py:285] Infra logging initialized: dir=logs, level=INFO, size=10MB, count=-1
[2026/10/16 15:58:07.587 GMT+08:00] [2026-10-16 07:58:07][INFO][plugin.py:342] No testbed source (no --testbed and no TESTBED_DEVICES), environment management disabled
[2026/10/16 15:58:07.587 GMT+08:00] [2026-10-16 07:58:07][INFO][plugin.py:241] Pre-action registry initialized
[2026/10/16 15:58:07.587 GMT+08:00] [2026-10-16 07:58:07][INFO][plugin.py:880] Collected environment info exported to COLLECTED_INFO environment variable
[2026/10/16 15:58:07.587 GMT+08:00] [2026-10-16 07:58:07][INFO][plugin.py:953] output collected info file to: /tmp/tmpcc076tp1.json
[2026/10/16 15:58:07.587 GMT+08:00] [2026-10-16 07:58:07][INFO][plugin.py:1090] Test session completed
[2026/10/16 15:58:07.587 GMT+08:00] 
[2026/10/16 15:58:07.587 GMT+08:00] [281472948195360] [INFO] Collected 14 test cases
[2026/10/16 15:58:07.587 GMT+08:00] [281472948195360] [INFO] Step 2: Grouping test cases by environments...
[2026/10/16 15:58:07.587 GMT+08:00] [281472948195360] [INFO] Environment block: {'mindstudio_single_device_1_a2a3_env_type-nodes_A3-A3': {'case_list_len': 14}}
[2026/10/16 15:58:07.587 GMT+08:00] [281472948195360] [INFO] Step 3: Allocating environments and executing tests...
[2026/10/16 15:58:07.587 GMT+08:00] [281472948195360] [INFO] Submitting task for env_id: mindstudio_single_device_1_a2a3_env_type-nodes_A3-A3
[2026/10/16 15:58:07.587 GMT+08:00] [281472894431520] [INFO] Allocating environment for env_id: mindstudio_single_device_1_a2a3_env_type-nodes_A3-A3
[2026/10/16 15:58:07.587 GMT+08:00] [281472894431520] [INFO] Using image label: swr.cn-north-4.myhuaweicloud.com/atlas-ci/mindstudio-msmodelslim-nightly:a3-aarch64
[2026/10/16 15:58:07.587 GMT+08:00] [281472894431520] [INFO] env_device_resource is empty, skipping mock allocation
[2026/10/16 15:58:07.587 GMT+08:00] [281472894431520] [INFO] Creating k8s environment with name: codearts-4211ddb76d924f938aaef60ef4c4c2a1-f18b4f92325f49be83b9aba2e4d2a133-e739572ace2a4723a5d9d31263feee3c_20261016_5, ttl: None, health_ttl: 600
[2026/10/16 15:58:07.587 GMT+08:00] [281472894431520] [INFO] apply_env_k8s, payload={'env_definition': {'nodes_1': [{'name': 'device', 'res_type': 'container', 'cpu_arch': 'ARM', 'cpu_core_num': 64, 'npu_gen': 'A3', 'npu_model': 'Ascend 910C', 'npu_num': 1, 'shm_size': '180Gi', 'mount_source_data': ['mindstudio_data'], 'mount_dest_dir': ['/home/autotest'], 'resources': {'cpu': {'request': '48', 'limit': '128'}, 'memory': {'request': '256Gi', 'limit': '1024Gi'}}, 'use_nfs': True, 'memory_size': 256, 'pool': 'onprem-ai', 'env': {'LD_LIBRARY_PATH': '/usr/lib64/:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/driver/lib64/common:/usr/lib/aarch64-linux-gnu/:'}, 'image_label': 'swr.cn-north-4.myhuaweicloud.com/atlas-ci/mindstudio-msmodelslim-nightly:a3-aarch64'}]}, 'extend_env_comments': {'job_info': 'codearts-4211ddb76d924f938aaef60ef4c4c2a1-f18b4f92325f49be83b9aba2e4d2a133-e739572ace2a4723a5d9d31263feee3c_20261016_5'}, 'ssh_mesh': 'group', 'extend_labels': {'cluster': 'false', 'modelslim': 'true'}, 'health_ttl': 600}
[2026/10/16 15:58:07.587 GMT+08:00] [281472894431520] [INFO] Environment allocation successful, env ID: lease-env1792137487-5237
[2026/10/16 15:58:07.587 GMT+08:00] [281472894431520] [INFO] Starting to query task status for task_id[lease-env1792137487-5237]
[2026/10/16 15:58:07.587 GMT+08:00] [281472894431520] [INFO] ***start 0 times query***
[2026/10/16 15:58:23.368 GMT+08:00] [281472894431520] [INFO] apply_env_res: {'env_id': 'lease-env1792137487-5237', 'groups': {}, 'status': 'provisioning', 'name': 'env', 'created_at': '2026-10-16T07:58:07Z', 'expires_at': '2026-10-16T11:58:07Z', 'ttl': '14400', 'topology': '', 'extend_env_comments': {'job_info': 'codearts-4211ddb76d924f938aaef60ef4c4c2a1-f18b4f92325f49be83b9aba2e4d2a133-e739572ace2a4723a5d9d31263feee3c_20261016_5'}, 'progress': {'total': 1, 'ready': 0, 'failed': 0, 'pending': 1}, 'ssh_mesh': {'enabled': False, 'scope': '', 'enrolled': [], 'failed': []}, 'errors': None}
[2026/10/16 15:58:23.368 GMT+08:00] [281472894431520] [INFO] allocation_result is empty, wait 30s to query again
[2026/10/16 15:58:56.609 GMT+08:00] [281472894431520] [INFO] ***start 1 times query***
[2026/10/16 15:59:09.653 GMT+08:00] [281472894431520] [INFO] apply_env_res: {'env_id': 'lease-env1792137487-5237', 'groups': {'nodes_1': [{'name': 'device', 'res_type': 'container', 'status': 'rejected', 'node_ip': '', 'npu_ids': [], 'privileged': False}]}, 'status': 'rejected', 'name': 'env', 'created_at': '2026-10-16T07:58:07Z', 'expires_at': '2026-10-16T11:58:07Z', 'ttl': '14400', 'topology': '', 'extend_env_comments': {'job_info': 'codearts-4211ddb76d924f938aaef60ef4c4c2a1-f18b4f92325f49be83b9aba2e4d2a133-e739572ace2a4723a5d9d31263feee3c_20261016_5'}, 'progress': {'total': 1, 'ready': 0, 'failed': 1, 'pending': 0}, 'ssh_mesh': {'enabled': False, 'scope': '', 'enrolled': [], 'failed': []}, 'errors': ["nodes_1/device: no matching nodes for labels={'kubernetes.io/arch': 'arm64', 'pool': 'onprem-ai', 'accelerator-type': 'module-a3-16', 'accelerator-model': 'Ascend-910C', 'cluster': 'false', 'modelslim': 'true', 'nfs': 'true'}"]}
[2026/10/16 15:59:09.653 GMT+08:00] [281472894431520] [ERROR] Environment allocation rejected, status: rejected
[2026/10/16 15:59:09.653 GMT+08:00] [281472894431520] [ERROR] Failed to allocate environment: Environment allocation rejected: Unknown
[2026/10/16 15:59:09.653 GMT+08:00] Traceback (most recent call last):
[2026/10/16 15:59:09.653 GMT+08:00]   File "***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor/src/scheduler/env_manager.py", line 301, in allocate_environments
[2026/10/16 15:59:09.653 GMT+08:00]     self._query_k8s_env_status(
[2026/10/16 15:59:09.653 GMT+08:00]   File "***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor/src/scheduler/env_manager.py", line 386, in _query_k8s_env_status
[2026/10/16 15:59:09.653 GMT+08:00]     raise RuntimeError(
[2026/10/16 15:59:09.653 GMT+08:00] RuntimeError: Environment allocation rejected: Unknown
[2026/10/16 15:59:09.653 GMT+08:00] [281472894431520] [ERROR] Failed to allocate environment for env_id: mindstudio_single_device_1_a2a3_env_type-nodes_A3-A3, error: Environment allocation rejected: Unknown
[2026/10/16 15:59:09.653 GMT+08:00] Traceback (most recent call last):
[2026/10/16 15:59:09.653 GMT+08:00]   File "***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor/src/run_scheduler.py", line 260, in _allocate_environments_and_execute
[2026/10/16 15:59:09.653 GMT+08:00]     self.env_manager.allocate_environments(env_case_info)
[2026/10/16 15:59:09.653 GMT+08:00]   File "***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor/src/scheduler/env_manager.py", line 301, in allocate_environments
[2026/10/16 15:59:09.653 GMT+08:00]     self._query_k8s_env_status(
[2026/10/16 15:59:09.653 GMT+08:00]   File "***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor/src/scheduler/env_manager.py", line 386, in _query_k8s_env_status
[2026/10/16 15:59:09.653 GMT+08:00]     raise RuntimeError(
[2026/10/16 15:59:09.653 GMT+08:00] RuntimeError: Environment allocation rejected: Unknown
[2026/10/16 15:59:09.653 GMT+08:00] [281472948195360] [INFO] Task completed for env_id: mindstudio_single_device_1_a2a3_env_type-nodes_A3-A3, result: False
[2026/10/16 15:59:09.653 GMT+08:00] [281472948195360] [ERROR] Failed to execute cases for env_id: mindstudio_single_device_1_a2a3_env_type-nodes_A3-A3
[2026/10/16 15:59:09.653 GMT+08:00] [281472948195360] [INFO] All environments allocated and tests executed.
[2026/10/16 15:59:09.653 GMT+08:00] [281472948195360] [INFO] Step 4: Collecting and archiving logs to OBS...
[2026/10/16 15:59:09.653 GMT+08:00] [281472948195360] [INFO] don't upload to obs,  no xml found in ***//openlibing-pytest-executor-workspace/openlibing-pytest-executor/pytest-executor/case-logs
[2026/10/16 15:59:09.653 GMT+08:00] [281472948195360] [INFO] Step 5: Releasing environments...
[2026/10/16 15:59:09.653 GMT+08:00] [281472948195360] [INFO] Releasing 1 environments
[2026/10/16 15:59:22.699 GMT+08:00] [281472948195360] [INFO] Successfully released environment: lease-env1792137487-5237
[2026/10/16 15:59:22.699 GMT+08:00] [281472948195360] [INFO] All tasks completed.
[2026/10/16 15:59:22.699 GMT+08:00] [281472948195360] [ERROR] No test case result found. Exiting.
[2026/10/16 15:59:22.699 GMT+08:00] [281472948195360] [INFO] Cleaned archive_log_dir: removed 0 files
[2026/10/16 15:59:22.699 GMT+08:00] + echo '[ERROR]execute openlibing-pytest-executor. main.py fail, log file is ***//openlibing-pytest-executor-workspace/executor-log/scheduler_framework.log'
[2026/10/16 15:59:22.699 GMT+08:00] [ERROR]execute openlibing-pytest-executor. main.py fail, log file is ***//openlibing-pytest-executor-workspace/executor-log/scheduler_framework.log
[2026/10/16 15:59:22.699 GMT+08:00] + ./obsutil_linux_arm64_5.8.9/obsutil chattri obs://ascend-package/msmodelslim/nightly/log/6b5df9811c84434296883cb706db6211202610162041 -r -f -acl=public-read -i=***** -k=***** -e=obs.cn-north-4.myhuaweicloud.com
[2026/10/16 15:59:22.699 GMT+08:00] Start at 2026-10-16 07:59:22.558278297 +0000 UTC
[2026/10/16 15:59:22.700 GMT+08:00] 
[2026/10/16 15:59:23.023 GMT+08:00] [_____________________________________________________________________________] ?% tps:0.00 0/0 28ms
Warn: No task to run
[2026/10/16 15:59:23.023 GMT+08:00] + exit 1
[2026/10/16 15:59:23.086 GMT+08:00] [ERROR]  : script returned exit code 1, exitMessage is: command run failed
[2026/10/16 15:59:23.151 GMT+08:00] [INFO]  : [JobStatusPlugin] onCompleted: j_Z947ObnE #1
[2026/10/16 15:59:28.224 GMT+08:00] Finished: FAILURE
