# %% [markdown]
# # 5-1, 5-2. Service Client (teleport_absolute)
# 실행 전: `humble` → `ros2 run turtlesim turtlesim_node`
# float 필드에는 float 값(1.0)을 넣으세요.

# %%
import rclpy as rp
from turtlesim.srv import TeleportAbsolute

# %%
rp.init()
test_node = rp.create_node('client_test')

# %%
cli = test_node.create_client(TeleportAbsolute, '/turtle1/teleport_absolute')

# %%
req = TeleportAbsolute.Request()
print(req)

# %%
req.x = 1.0
req.y = 1.0
req.theta = 0.0
print(req)

# %%
future = cli.call_async(req)                        # 요청 보내기
rp.spin_until_future_complete(test_node, future)    # 응답이 올 때까지 대기
print(future.result())

# %% [markdown]
# ## 5-2. 서비스가 준비될 때까지 기다리기
# turtlesim_node 를 끈 상태에서 실행하면 "Waiting" 이 반복되고, 다시 켜면 이어서 호출됩니다.

# %%
while not cli.wait_for_service(timeout_sec=1.0):
    print('Waiting for service...')

req.x = 9.0
req.y = 9.0
req.theta = 1.57
future = cli.call_async(req)
rp.spin_until_future_complete(test_node, future)
print(future.result())
