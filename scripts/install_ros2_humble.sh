#!/usr/bin/env bash
# 2-2 ROS2 Humble 설치 (Ubuntu 22.04 전용)
# 강의는 공식 문서를 직접 따라 하라고 안내합니다. 이 스크립트는 같은 순서입니다.
# 공식 문서: https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debs.html
# 설치 방법이 바뀔 수 있으니 실패하면 공식 문서의 최신 명령을 확인하세요.
set -euo pipefail

if ! grep -q "22.04" /etc/os-release; then
  echo "이 스크립트는 Ubuntu 22.04 전용입니다." >&2
  exit 1
fi

# 로케일 UTF-8
sudo apt update
sudo apt install -y locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

# universe 저장소, 키, 저장소 등록
sudo apt install -y software-properties-common curl
sudo add-apt-repository -y universe
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key \
  -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo "$UBUNTU_CODENAME") main" \
  | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

# 키와 저장소 확인
ls /usr/share/keyrings | grep -i ros || true
ls /etc/apt/sources.list.d | grep -i ros || true

# 설치 (우분투 버전은 올리지 않음)
sudo apt update
sudo apt upgrade -y
sudo apt install -y ros-humble-desktop      # 다운로드 약 2.5GB
sudo apt install -y ros-dev-tools           # 공식 문서 권장(colcon 등), 입문편 실습에는 필수 아님

echo
echo "설치 확인: ls /opt/ros/humble   (setup.bash 가 보여야 함)"
echo "다음: scripts/bashrc_snippet.sh 를 ~/.bashrc 에 추가하세요."
