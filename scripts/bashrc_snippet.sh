# ===== ROS2 Humble 설정 (2-3 ~ 2-5): ~/.bashrc 끝에 추가 =====
# 강의 방식: ROS 환경을 alias 하나(humble)로 묶고, 필요할 때만 불러옵니다.
# 주의: alias 에서 = 양쪽에 공백을 넣지 마세요.

# ROS_DOMAIN_ID 는 같은 공유기에서 다른 사람과 겹치지 않는 숫자(0~101)로 바꾸세요. (강사 예시는 13)
alias humble='source /opt/ros/humble/setup.bash; export ROS_DOMAIN_ID=13; echo "ROS_DOMAIN_ID : $ROS_DOMAIN_ID"; echo "ros2 humble activate"'

# bashrc 다시 읽기
alias sb='source ~/.bashrc; echo "bashrc reloaded"'
