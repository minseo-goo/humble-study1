# 환경 설정 (영상 순서대로)

모든 명령은 Ubuntu 22.04 터미널에서 실행합니다. 복사 후 터미널에 붙여넣기는 `Ctrl+Shift+V`입니다.

## 1-1. Ubuntu 22.04 설치
PC 설치 또는 VM. 강의 환경은 **22.04 LTS**입니다. 설치 후 우분투 버전을 올리지 마세요(업그레이드 안내가 떠도 무시).

## 1-2, 1-3. Terminator와 터미널 기본 명령
```bash
sudo apt update
sudo apt install -y terminator
```
기본 명령(`ls`, `mkdir`, `cd`)은 1-5 영상에서 `ls`(목록), `mkdir`(폴더 생성)로 다시 나옵니다.

## 1-4. Chrome / pip3

강사 순서: 저장소 업데이트 → 모듈 업그레이드 → wget 확인 → Chrome .deb 설치 → pip3 설치/업그레이드.

```bash
sudo apt update
sudo apt upgrade -y

# wget이 있는지 확인. 에러가 나면 설치
wget --version
sudo apt install -y wget

# Chrome 설치 (.deb를 홈 폴더에 받은 뒤 설치)
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install -y ./google-chrome-stable_current_amd64.deb
```
- 강사는 이후 Chromium(`sudo apt install chromium-browser`)도 언급하지만 선택 사항입니다.
- 기본 웹브라우저 변경: 설정 → 기본 애플리케이션 → 웹 → Chrome

```bash
# pip3 확인과 설치
pip3 --version
sudo apt install -y python3-pip
pip3 install --upgrade pip
python3 --version        # 22.04는 3.10.x
```
`pip3 --version`이 "command not found"면 `python3-pip`를 설치합니다. 버전 의존성 때문에 pip는 항상 최신으로 유지하라고 강조합니다.

## 1-5. Jupyter Notebook과 Markdown

```bash
jupyter --version               # 없으면 command not found
pip3 install jupyter            # 강의에서는 pip install jupyter
pip3 install numpy matplotlib   # P 챕터(삼각함수 그리기)에서 필요

mkdir python
cd python
jupyter notebook                # 웹 브라우저가 열림 → New → Python 3
```
- 셀 실행: `Shift+Enter`
- 셀 상태: 파란색은 선택 상태, 녹색은 편집 상태. `Esc`로 선택 상태가 되고 `M`을 누르면 마크다운 셀
- 마크다운 문법: `#`(큰 제목), `##`, `###`, `* 목록`, `*기울임*`, `**굵게**`, `***둘 다***`, `> 인용문`, 코드 블록은 백틱 3개 + 언어명

**중요**: ROS2 실습에서는 `humble`(2-4에서 만드는 alias)을 **실행한 터미널에서** `jupyter notebook`을 띄워야 합니다.

## 1-6. VSCode (선택)

```bash
# code.visualstudio.com 에서 Linux .deb (x64) 다운로드 후
cd ~/Downloads
sudo apt install ./code_*_amd64.deb
code                              # 실행
```
- 파이썬 파일 확장명은 `.py`. 처음 열면 Python 확장(익스텐션) 설치 안내가 뜨니 설치합니다.
- 경로에서 `.`은 현재 폴더, `..`은 상위 폴더입니다.
- ARM 노트북이면 ARM64용 .deb를 받습니다.

## 2-1. Sublime Text (선택)

강사는 ROS 수업에서 Sublime을 추천하지만 VSCode를 써도 됩니다.
공식 사이트(sublimetext.com → Download → Linux)의 apt 안내를 그대로 따릅니다. 안내문 중 **Stable 채널만** 선택하세요(Dev는 무시).
```bash
subl ~/.bashrc          # 설치 후 이렇게 파일을 엽니다
```

## 2-2. ROS2 Humble 설치

강사는 인터넷의 "한 줄 설치" 대신 **공식 문서(docs.ros.org Humble, Ubuntu Debian packages)를 직접 따라 하라**고 강조합니다.
공식 문서의 코드를 복사해 붙여넣는 순서이고, 이 저장소의 `scripts/install_ros2_humble.sh`가 같은 순서입니다.

1. 로케일 UTF-8 설정
2. universe 저장소 활성화, ROS 키 등록, 저장소를 sources list에 추가
3. 키와 저장소 확인: `ls /usr/share/keyrings`, `ls /etc/apt/sources.list.d`
4. `sudo apt update` → `sudo apt upgrade` (우분투 버전은 올리지 않는다)
5. `sudo apt install ros-humble-desktop` (다운로드 약 2.5GB)
6. 공식 문서 안내에 따라 `ros-dev-tools`도 설치(colcon 등. 입문편 실습에는 필수 아님)

**설치 확인** (터미널 2개 + 1개)
```bash
ls /opt/ros/humble                       # 안에 setup.bash 가 있어야 함

# 터미널 A
source /opt/ros/humble/setup.bash
ros2 run demo_nodes_cpp talker

# 터미널 B
source /opt/ros/humble/setup.bash
ros2 run demo_nodes_py listener

# 터미널 C
source /opt/ros/humble/setup.bash
rqt_graph
```
listener에 숫자가 순서대로 올라오면 성공입니다. 같은 공유기를 쓰는 사람이 여럿이면 숫자가 뒤죽박죽일 수 있고(정상), 2-5에서 해결합니다.

## 2-3. bashrc 설정
- `echo $SHELL`로 확인하면 우분투 기본 쉘은 bash
- 터미널을 열 때 처음 실행되는 설정 파일이 **홈 폴더의 `~/.bashrc`**
- 파일 끝에 줄을 추가하고 저장해도 열려 있는 터미널에는 반영되지 않습니다. `source ~/.bashrc` 또는 터미널 재시작

```bash
subl ~/.bashrc        # 또는 code ~/.bashrc, gedit ~/.bashrc
```
강사는 처음에 파일 끝에 `source /opt/ros/humble/setup.bash`와 확인용 `echo "..."` 메시지를 직접 넣어서 보여주지만, 2-4에서 지우고 alias로 바꿉니다.

## 2-4. alias 설정 (최종 형태)

강사의 규칙
- `alias 이름='명령'` 형식에서 **`=` 양쪽에 공백 금지**
- `alias`만 입력하면 등록된 alias 목록이 나옴. `alias | grep humble`로 특정 alias 확인
- alias를 지우고 `source ~/.bashrc`로 다시 읽어도 **이미 등록된 alias는 사라지지 않음**. 터미널을 껐다 켜야 함
- 연습으로 만든 alias와 직접 `source` 한 줄은 지움

`~/.bashrc` 끝에 넣을 최종 내용 (`scripts/bashrc_snippet.sh`와 동일)
```bash
alias humble='source /opt/ros/humble/setup.bash; export ROS_DOMAIN_ID=13; echo "ROS_DOMAIN_ID : $ROS_DOMAIN_ID"; echo "ros2 humble activate"'
alias sb='source ~/.bashrc; echo "bashrc reloaded"'
```
사용
```bash
sb          # bashrc를 다시 읽기
humble      # ROS2 환경 활성화. hu + Tab 으로 자동 완성
```
- `ROS_DOMAIN_ID`는 강사의 예시값이 13입니다. 같은 공간(같은 공유기)에서 수업한다면 **서로 다른 숫자**를 쓰세요(0~101).
- 이렇게 alias로 분리하는 이유는 conda나 Python venv 등 다른 환경과 충돌하지 않게 하려는 것입니다.

**대안** (3-2): alias를 만들지 않고 `.bashrc`에 `source /opt/ros/humble/setup.bash`를 그냥 넣어도 터미널을 열 때마다 자동으로 적용됩니다. 다만 conda나 venv를 쓰면 버전 충돌이 날 수 있습니다.

## 2-5. ROS_DOMAIN_ID

- ROS2는 DDS를 쓰므로 같은 네트워크에서 도메인 ID가 같은 노드끼리 서로 연결됩니다.
- 한 강의실에서 모두 같은 ID를 쓰면 옆 사람 노드와 섞입니다.
- 위 alias에 `export ROS_DOMAIN_ID=숫자`를 넣어 두면 `humble`을 실행할 때마다 적용됩니다.
- 스펠링 주의: `ROS_DOMAIN_ID`
- 확인: `echo $ROS_DOMAIN_ID`

## 확인 체크리스트

```bash
humble
echo $ROS_DOMAIN_ID
ros2 -h
ros2 run turtlesim turtlesim_node
```
