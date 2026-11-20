# %% [markdown]
# # 4-3. Topic 발행 (cmd_vel)
# 실행 전: `humble` → `ros2 run turtlesim turtlesim_node`

# %%
import rclpy as rp
from geometry_msgs.msg import Twist

# %%
rp.init()
test_node = rp.create_node('pub_test')

# %%
msg = Twist()          # 인스턴스 생성. 기본값이 들어 있음
print(msg)

# %%
msg.linear.x = 2.0
msg.angular.z = 2.0
print(msg)

# %%
pub = test_node.create_publisher(Twist, '/turtle1/cmd_vel', 10)

# %%
pub.publish(msg)       # 한 번 발행 → 거북이가 한 번 움직임

# %% [markdown]
# ## 타이머로 일정 간격 반복 발행
# 주기 0.1초 → 1.0 으로 바꾸면 1초에 한 번

# %%
cnt = 0

def timer_callback():
    global cnt
    cnt += 1
    print(cnt)
    pub.publish(msg)
    if cnt > 3:
        raise Exception('publish stop')

# %%
timer = test_node.create_timer(0.1, timer_callback)

# %%
rp.spin(test_node)
