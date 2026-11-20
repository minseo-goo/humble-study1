# %% [markdown]
# # 4-2. Topic을 받는 횟수 제한하기
# 카운터를 쓰고, 정해진 횟수가 넘으면 예외를 발생시켜 spin 을 빠져나옵니다.
# 예외로 중단된 뒤에는 Kernel → Restart 하고 처음 셀부터 다시 실행하세요.

# %%
import rclpy as rp
from turtlesim.msg import Pose

# %%
rp.init()
test_node = rp.create_node('test')

# %%
cnt = 0

def callback(data):
    global cnt                  # 함수 밖의 변수를 쓰려면 global
    cnt += 1
    print(cnt, data.x, data.y)
    if cnt >= 3:
        raise Exception('subscription stop')

# %%
test_node.create_subscription(Pose, '/turtle1/pose', callback, 10)

# %%
rp.spin(test_node)
