# ROS2 입문 실습 정리 (R2R - 무작정 따라하는 ROS2)

PinkLAB R2R 입문과정(민형기 강사) 영상을 따라 하면서 **복사해서 바로 실습**할 수 있게 정리한 저장소입니다.

- 재생목록: https://www.youtube.com/playlist?list=PL0xYz_4oqpvhj4JaPSTeGI2k5GQEE36oi
- 영상 36개 (마지막 영상은 전체 몰아보기)
- 강의 환경: **Ubuntu 22.04 + ROS2 Humble**, 코드 실습은 **Jupyter Notebook**에서 진행

> **주의**: 영상의 자동 생성 자막(음성 인식)을 읽고 정리했습니다. 명령어와 코드는 강사가 말한 내용을
> ROS2 Humble 공식 문서에 맞춰 복원한 것입니다. 영상 화면과 다르면 영상을 우선하세요.
> 어느 영상을 어느 정도 확인했는지는 [docs/00-verification-status.md](docs/00-verification-status.md)에 있습니다.

## 폴더 구조

```
README.md
docs/
  00-verification-status.md  영상별 확인 범위
  01-curriculum.md           36개 영상 목록
  02-environment-setup.md    설치·설정을 영상 순서대로 (복붙용)
  03-ros2-cli-commands.md    챕터 3 Turtlesim CLI 명령 (복붙용)
  04-python-rclpy.md         챕터 4~5 Python 코드 설명
  05-python-basics.md        P 챕터 Python 보충 설명
  06-troubleshooting.md      자주 막히는 지점
scripts/
  install_tools.sh           1챕터 도구 설치 (Chrome, pip3, Jupyter, numpy, matplotlib)
  install_ros2_humble.sh     2-2 ROS2 Humble 설치
  bashrc_snippet.sh          2-3 ~ 2-5 alias 설정
practice/
  notebooks/                 강의 따라 하기용 Jupyter 노트북 (.ipynb)와 같은 내용의 .py
  standalone_scripts/        노트북 없이 터미널에서 실행하는 참고용 스크립트
```

## 학습 순서

1. [환경 설정](docs/02-environment-setup.md): Ubuntu 도구 → ROS2 Humble → `humble` alias
2. [CLI 실습](docs/03-ros2-cli-commands.md): Turtlesim으로 Node / Service / Topic / Action
3. [Python 실습](docs/04-python-rclpy.md): 노트북에서 구독, 발행, Service Client
4. Python이 약하면 [P 챕터](docs/05-python-basics.md)를 먼저

## 빠른 시작 (Ubuntu 22.04)

```bash
bash scripts/install_tools.sh
bash scripts/install_ros2_humble.sh
cat scripts/bashrc_snippet.sh >> ~/.bashrc    # ROS_DOMAIN_ID 숫자는 본인 값으로 수정
source ~/.bashrc

humble                                         # 매번 새 터미널에서 먼저 실행
ros2 run turtlesim turtlesim_node
```

## 진행 체크리스트

- [ ] 1. Ubuntu, Terminator, 터미널 명령, Chrome, pip3, Jupyter, VSCode
- [ ] 2. Sublime(선택), ROS2 Humble 설치, bashrc, alias, ROS_DOMAIN_ID
- [ ] 3. Turtlesim: Node / Service / Topic / Action
- [ ] 4. Python으로 Topic 구독, 횟수 제한, 발행
- [ ] 5. Python으로 Service Client
- [ ] P. Python 보충 (삼각함수, 클래스, 상속, 오버라이딩, super)
