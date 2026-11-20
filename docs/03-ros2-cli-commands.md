# 챕터 3: Turtlesim으로 배우는 ROS2 CLI

모든 터미널에서 **가장 먼저 `humble`** 을 실행합니다. 터미널은 Terminator로 분할해서 씁니다.

## 3-1. Turtlesim 실행

turtlesim은 `ros-humble-desktop`에 포함되어 있어 따로 설치할 필요가 없습니다. 빠져 있을 때만:
```bash
sudo apt install ros-humble-turtlesim
```
```bash
humble
ros2 run turtlesim turtlesim_node            # 거북이 창이 뜸

# 패키지 안의 실행 파일 목록 보기: 아래에서 Tab Tab
ros2 run turtlesim <Tab><Tab>
```
- 노드(Node) = ROS에서 실행 가능한 최소 단위
- 실행 형식: `ros2 run <패키지> <노드>`
- 우분투와 Qt 버전 충돌로 경고가 떠도 거북이가 뜨면 무시해도 됩니다.
- 거북이 색과 모양은 실행할 때마다 랜덤입니다.
- `ros2 run`을 쳤는데 "인식하지 못하는 명령"이면 `humble`을 안 한 것입니다.
- 출력이 많을 때 걸러보기: `alias | grep humble`

## 3-2. setup.bash 강조

`sudo apt install`로 설치한 ROS 패키지는 `/opt/ros/humble` 아래에 있고, `source /opt/ros/humble/setup.bash`로 읽어야 `ros2` 명령을 쓸 수 있습니다. 이를 alias(`humble`)로 만든 것입니다.

## 3-3. Node
```bash
# 터미널 A
humble
ros2 run turtlesim turtlesim_node

# 터미널 B
humble
ros2 node list                    # 현재 실행 중인 노드 목록
ros2 node info /turtlesim         # 이 노드가 제공하는 subscriber, publisher, service, action
```
- `/turtlesim`이 여러 개 보이면 도메인 ID가 겹쳤거나 오타입니다. `echo $ROS_DOMAIN_ID`로 확인하세요.
- info에서 `/turtle1/cmd_vel`은 subscriber, `/turtle1/pose`와 `/turtle1/color_sensor`는 publisher로 나옵니다.

## 3-4. Service 기초
Service는 **클라이언트가 요청(request)하면 서버가 응답(response)** 하는 구조입니다. 응답 데이터는 없을 수도 있습니다.
```bash
ros2 service list                                       # turtlesim이 제공하는 서비스
ros2 service type /turtle1/teleport_absolute            # 서비스 타입(데이터형) 확인
ros2 interface show turtlesim/srv/TeleportAbsolute      # 데이터 정의 확인
```
`TeleportAbsolute` 정의는 아래처럼 `---`를 기준으로 위가 request, 아래가 response입니다.
```
float32 x
float32 y
float32 theta
---
```
response가 비어 있어서 돌려주는 값이 없습니다.

## 3-5. Service call 1
```bash
ros2 service call /turtle1/teleport_absolute turtlesim/srv/TeleportAbsolute "{x: 2.0, y: 2.0, theta: 1.57}"
```
- 요청 데이터는 **큰따옴표 + 중괄호**
- `x:` 처럼 키와 콜론은 붙이고 값 앞에 한 칸 띄움
- `theta`는 라디안. 1.57은 약 90도, 3.14는 약 180도
- Tab 자동완성을 적극 활용하세요.

## 3-6. Service call 2 (spawn)
```bash
ros2 interface show turtlesim/srv/Spawn
```
```
float32 x
float32 y
float32 theta
string name        # optional
---
string name
```
```bash
ros2 service call /spawn turtlesim/srv/Spawn "{x: 1.0, y: 1.0, theta: 0.0, name: ''}"
# → response: name='turtle2', 거북이가 한 마리 더 생김
ros2 service list                 # /turtle1/... 와 /turtle2/... 가 함께 보임
```
- `name`은 비워도(`''`) 되고, 비우면 자동으로 `turtle2`
- 거북이마다 **네임스페이스**(`/turtle1`, `/turtle2`)가 붙어 같은 이름의 서비스를 거북이별로 구분합니다. 코드를 한 번 짜 두고 네임스페이스만 바꿔 여러 로봇에 쓰는 구조입니다.
```bash
ros2 service call /turtle2/teleport_absolute turtlesim/srv/TeleportAbsolute "{x: 8.0, y: 8.0, theta: 0.0}"
```

## 3-7. Topic 1
Topic은 발행자(publisher)가 막 발행하고 구독자(subscriber)가 듣는 구조입니다. **토픽 이름과 메시지 타입**을 알면 누구나 들을 수 있습니다.
```bash
ros2 run turtlesim turtlesim_node        # 터미널 A
```
```bash
ros2 topic list                          # 터미널 B
ros2 topic list -t                       # 데이터 타입도 함께
ros2 topic list -v                       # publisher/subscriber를 나눠서 표시
ros2 topic info /turtle1/pose            # 타입, publisher 수, subscriber 수
ros2 interface show turtlesim/msg/Pose   # x, y, theta, linear_velocity, angular_velocity
ros2 topic echo /turtle1/pose            # 구독해서 값을 계속 출력. 중지는 Ctrl+C
```
- `/turtle1/pose`는 turtle1이 발행합니다.
- `/turtle1/cmd_vel`은 turtle1이 구독하는 토픽입니다(아직 발행자는 없음).
- 거북이가 안 움직이면 같은 값이 계속 올라옵니다.

## 3-8. Topic 2 (cmd_vel)
`cmd_vel`은 command velocity의 약자로, 주행 로봇에서 가장 흔한 토픽입니다.
```bash
ros2 interface show geometry_msgs/msg/Twist
```
```
Vector3 linear
    float64 x
    float64 y
    float64 z
Vector3 angular
    float64 x
    float64 y
    float64 z
```
- `linear`는 x, y, z 축 방향 속도, `angular`는 x(roll), y(pitch), z(yaw) 축을 중심으로 한 회전 속도입니다.

```bash
# 직진
ros2 topic pub /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.0}}"

# 원호 그리며 이동 (직진 + 회전)
ros2 topic pub /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}"
```
- `ros2 topic pub`은 기본으로 **반복 발행**하며, 멈추려면 `Ctrl+C`
- 한 번만: `--once`, 주기 지정: `-r 10`(10Hz)
- 터미널 두 개에서 동시에 같은 토픽에 발행하면 두 신호가 합쳐진 경로가 나옵니다.
- 이때 `rqt_graph`를 실행하면 두 발행자가 `/turtlesim` 노드의 `cmd_vel`로 연결된 모습이 보입니다.

## 3-9. Action
Action은 Service와 Topic이 섞인 구조입니다: **목표(goal) 전달 → 중간 과정은 피드백(topic) → 결과(result)**.
```bash
ros2 run turtlesim turtlesim_node           # 터미널 A
ros2 run turtlesim turtle_teleop_key        # 터미널 B (방향키로 이동)
```
- 방향키를 누르려면 **turtle_teleop_key를 실행한 터미널을 클릭해서 활성화**
- 알파벳 키(G, B, V, C, D, E, R, T 등)를 누르면 거북이가 절대 각도로 회전하는 액션이 실행됩니다. 터미널에 `Rotation goal completed successfully` 같은 결과가 뜹니다.
- 회전 중에 다른 키를 누르면 이전 goal이 취소·대체되고, `F`를 누르면 멈춥니다.
```bash
ros2 action list                                         # /turtle1/rotate_absolute
ros2 interface show turtlesim/action/RotateAbsolute      # goal / result / feedback 정의
ros2 action send_goal /turtle1/rotate_absolute turtlesim/action/RotateAbsolute "{theta: 1.57}"
# 피드백도 보려면 --feedback 옵션 추가
```

## 한눈에 보는 명령 표

| 대상 | 목록 | 상세 | 사용 |
|---|---|---|---|
| Node | `ros2 node list` | `ros2 node info /노드` | `ros2 run 패키지 노드` |
| Service | `ros2 service list` | `ros2 interface show 타입` | `ros2 service call 이름 타입 "{...}"` |
| Topic | `ros2 topic list -t` | `ros2 topic info 이름` | 구독 `ros2 topic echo 이름`, 발행 `ros2 topic pub 이름 타입 "{...}"` |
| Action | `ros2 action list` | `ros2 interface show 타입` | `ros2 action send_goal 이름 타입 "{...}"` |
| 시각화 | `rqt_graph` | | |
