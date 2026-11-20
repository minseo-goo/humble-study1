# %% [markdown]
# # 4-1. Python으로 topic 구독
# 실행 전: 터미널에서 `humble` → `ros2 run turtlesim turtlesim_node`
# 이 노트북도 `humble`을 실행한 터미널에서 `jupyter notebook`으로 띄워야 합니다.

# %%
import rclpy as rp
from turtlesim.msg import Pose

# %%
rp.init()                              # 커널당 한 번만 실행
test_node = rp.create_node('test')     # 터미널에서 ros2 node list 로 확인

# %%
def callback(data):
    print("callback")
    print(data)

# %%
test_node.create_subscription(Pose, '/turtle1/pose', callback, 10)

# %%
# rp.spin 은 끝나지 않고 계속 받습니다. 확인이 끝나면 Kernel → Interrupt 로 중지하고 주석 처리하세요.
# rp.spin(test_node)
