# 챕터 4~5: Python(rclpy)으로 Topic·Service 다루기

강의는 **Jupyter Notebook 셀에서 한 줄씩 실행**하는 방식입니다. 코드는 `practice/notebooks/`에 있습니다.

## 실행 준비 (매번)

```bash
# 터미널 A: 거북이
humble
ros2 run turtlesim turtlesim_node

# 터미널 B: 노트북 (반드시 humble 실행 후)
humble
cd ~/python
jupyter notebook          # New → Python 3
```
- `humble`을 하지 않고 노트북을 띄우면 `import rclpy`나 `from turtlesim.msg import Pose`가 실패합니다.
- 노트북은 `.ipynb`를 열어도 되고, `.py`(`# %%` 셀 구분)는 VSCode에서 셀 단위로 실행할 수 있습니다.

## 4-1. Topic 구독

구독하려면 **토픽 이름**(`/turtle1/pose`)과 **데이터 타입**(`turtlesim.msg.Pose`) 두 가지를 알아야 합니다.

```python
import rclpy as rp
from turtlesim.msg import Pose

rp.init()                              # rclpy 초기화. 커널당 한 번만
test_node = rp.create_node('test')     # 노드 생성. 터미널에서 ros2 node list로 확인 가능

def callback(data):
    print("callback")
    print(data)

test_node.create_subscription(Pose, '/turtle1/pose', callback, 10)   # 큐 크기 10
# rp.spin(test_node)                   # 실행하면 끝나지 않고 계속 받음
```
- `rp.spin(test_node)`는 블로킹이라 노트북에서는 메뉴의 **Kernel → Interrupt**로 중지합니다. 확인한 뒤에는 주석 처리하고 Clear Output으로 화면을 정리합니다.
- 확인: `ros2 node list`, `ros2 topic info /turtle1/pose`, `rqt_graph`
- 노트북은 연속 데이터를 실시간으로 계속 보는 데는 적합하지 않습니다.

## 4-2. 받는 횟수 제한 (카운터)

한 번만 받으면 첫 토픽은 비어 있을 수 있고, 무한히 받으면 다른 셀을 실행할 수 없어서 **카운터로 제한**합니다.

```python
cnt = 0

def callback(data):
    global cnt                          # 함수 밖 변수를 쓰려면 global
    cnt += 1
    print(cnt, data.x, data.y)
    if cnt >= 3:
        raise Exception('subscription stop')   # 예외로 spin을 빠져나옴

test_node.create_subscription(Pose, '/turtle1/pose', callback, 10)
rp.spin(test_node)
```
- 예외가 발생해 중단되면 **Kernel → Restart**를 한 뒤 `rp.init()`부터 다시 실행합니다.
- 이렇게 하면 데이터 구조를 파악할 때 편합니다.

## 4-3. Topic 발행

```python
import rclpy as rp
from geometry_msgs.msg import Twist

rp.init()
test_node = rp.create_node('pub_test')

msg = Twist()           # 클래스를 인스턴스로 만듦. 기본값이 들어 있음
print(msg)              # linear, angular 각각 x, y, z = 0.0
msg.linear.x = 2.0
msg.angular.z = 2.0
print(msg)

pub = test_node.create_publisher(Twist, '/turtle1/cmd_vel', 10)
pub.publish(msg)        # 한 번 발행 → 거북이가 한 번 움직임
```
- `Shift+Tab`으로 함수의 사용 옵션(인자) 설명을 볼 수 있습니다.
- 반복 발행은 **타이머**를 사용합니다.

```python
cnt = 0

def timer_callback():
    global cnt
    cnt += 1
    print(cnt)
    pub.publish(msg)
    if cnt > 3:
        raise Exception('publish stop')

timer = test_node.create_timer(0.1, timer_callback)   # 0.1초 주기. 1.0으로 바꾸면 1초에 한 번
rp.spin(test_node)
```
- 주기와 횟수를 곱한 시간만큼 움직입니다(1초 주기에 4번이면 약 4초).

## 5-1, 5-2. Service Client

Service **Server**는 이 강의에서 만들지 않고(패키지 만들 때 다룸), 이미 있는 서버를 쓰는 **Client**만 다룹니다.

```python
import rclpy as rp
from turtlesim.srv import TeleportAbsolute

rp.init()
test_node = rp.create_node('client_test')

cli = test_node.create_client(TeleportAbsolute, '/turtle1/teleport_absolute')
req = TeleportAbsolute.Request()       # 요청 데이터 타입 인스턴스
print(req)                             # x, y, theta = 0.0

req.x = 1.0
req.y = 1.0
req.theta = 0.0

future = cli.call_async(req)           # 요청 보내기 (비동기)
rp.spin_until_future_complete(test_node, future)   # 응답이 올 때까지 spin
print(future.result())
```
- **float 필드에는 float 값**(`9.0`)을 넣습니다. 정수 `9`를 넣으면 타입 에러가 날 수 있습니다. 강사는 `float(9)` 또는 `9.`도 가능하다고 설명합니다.
- 서버가 아직 준비되지 않았을 때를 대비해 대기 코드를 넣습니다.

```python
while not cli.wait_for_service(timeout_sec=1.0):
    print('Waiting for service...')
```
- 테스트: 거북이(turtlesim_node)를 끈 상태에서 실행하면 "Waiting" 메시지가 반복되고, 다시 켜면 이어서 서비스가 호출됩니다.
- `create_client` 등 `Node`의 메서드가 궁금하면 ROS2 Humble 공식 문서(rclpy API)를 보라는 것이 강사의 조언입니다. 블로그나 영상은 시간이 지나면 낡습니다.
- 노트북에서 `test_node.`을 치고 Tab으로 메서드 목록을 볼 수 있습니다. 안 뜨면 직접 타이핑하세요.

## 같은 코드를 터미널에서 실행하려면

`practice/standalone_scripts/`에 노트북 없이 `python3 파일.py`로 실행하는 참고용 스크립트가 있습니다(강의 코드가 아니라 같은 내용을 스크립트로 옮긴 것).
