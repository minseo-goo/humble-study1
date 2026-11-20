# 자주 막히는 지점

| 증상 | 원인과 해결 |
|---|---|
| `ros2: command not found` | `humble`을 실행하지 않음. 새 터미널을 열면 매번 `humble`부터 |
| `humble: command not found` | `~/.bashrc`에 alias가 없거나 `source ~/.bashrc`(`sb`)를 안 함 |
| `ros2 node list`에 `/turtlesim`이 여러 개 | 같은 공유기의 다른 사람과 `ROS_DOMAIN_ID`가 같음. 서로 다른 값으로 변경 |
| 내가 보낸 값이 아닌 것이 섞여 옴 | 위와 동일. 또는 터미널마다 ID가 다름 → `echo $ROS_DOMAIN_ID` |
| alias를 지웠는데 계속 남아 있음 | `source ~/.bashrc`로는 기존 alias가 지워지지 않음. 터미널을 껐다 켬 |
| alias 등록이 안 됨 | `alias 이름='...'`에서 `=` 양쪽 공백 금지. 따옴표 안의 따옴표는 `\"`로 |
| `jupyter: command not found` | `pip3 install jupyter` 후 새 터미널. 계속 안 되면 `export PATH=$PATH:~/.local/bin` |
| 노트북에서 `import rclpy` 실패 | `humble`을 실행한 터미널에서 `jupyter notebook`을 띄우지 않음 |
| `rp.init()` 에러 (이미 초기화됨) | 같은 커널에서 두 번 실행. Kernel → Restart 후 처음부터 |
| 구독/발행 셀이 끝나지 않음 | `rp.spin`은 블로킹. Kernel → Interrupt, 또는 카운터와 예외로 종료(4-2) |
| 서비스 요청이 안 감 | `ros2 service list`로 이름 확인. turtlesim_node 실행 여부. float 필드에 정수를 넣지 않았는지 |
| turtlesim 창이 안 뜸 | VM 그래픽 확인. 로그인 화면에서 Wayland 대신 "Ubuntu on Xorg" 선택 |
| Qt 버전 충돌 경고 | 거북이 창이 뜨면 무시 가능 |
| 우분투 "새 버전 업그레이드" 안내 | 무시. 22.04를 유지해야 Humble이 동작 |
| apt 키/저장소 오류 | 공식 문서의 최신 설치 명령 재확인. 설치 방법은 조금씩 바뀜 |
| 방향키로 거북이가 안 움직임 | `turtle_teleop_key`를 실행한 터미널을 클릭해서 활성화 |
