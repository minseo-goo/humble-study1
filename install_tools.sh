#!/usr/bin/env bash
# 1챕터 도구 설치: Terminator, wget, Chrome, pip3, Jupyter, numpy, matplotlib
# 강의 순서(1-2, 1-4, 1-5)를 따릅니다. Ubuntu 22.04 기준.
set -euo pipefail

sudo apt update
sudo apt upgrade -y

# 1-2 Terminator
sudo apt install -y terminator

# 1-4 wget, Chrome
sudo apt install -y wget
cd "$HOME"
wget -O google-chrome-stable_current_amd64.deb \
  https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install -y "./google-chrome-stable_current_amd64.deb"

# 1-4 pip3
sudo apt install -y python3-pip
pip3 install --upgrade pip

# 1-5 Jupyter, P챕터용 numpy/matplotlib
pip3 install jupyter numpy matplotlib

# 실습 폴더
mkdir -p "$HOME/python"

echo
echo "완료. 새 터미널에서 아래를 확인하세요."
echo "  python3 --version   # 3.10.x"
echo "  pip3 --version"
echo "  jupyter --version   # 안 되면: export PATH=\$PATH:~/.local/bin"
