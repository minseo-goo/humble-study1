# %% [markdown]
# # P-2, P-3. 삼각함수 그려보기
# y = A * sin(2π f t) + B
# A 진폭, f 주파수(Hz), B 바이어스. `pip3 install numpy matplotlib` 필요

# %%
import numpy as np
import matplotlib.pyplot as plt

# %%
t = np.arange(0, 6, 0.01)     # 6은 포함하지 않아 600개
print(t.shape)

# %%
y = np.sin(np.pi * t)
print(y.shape)

# %%
plt.figure(figsize=(12, 6))
plt.plot(t, y)
plt.grid()
plt.show()

# %% [markdown]
# ## 함수로 재사용성 높이기

# %%
def sin_wave(a, f, b, end_time, ts=0.01):
    t = np.arange(0, end_time, ts)
    y = a * np.sin(2 * np.pi * f * t) + b
    return t, y

def draw_sin(a, f, b, end_time):
    t, y = sin_wave(a, f, b, end_time)
    plt.figure(figsize=(12, 6))
    plt.plot(t, y)
    plt.grid()
    plt.show()

# %%
draw_sin(1, 1, 0, 3)     # A=1, f=1Hz, B=0, 3초

# %%
draw_sin(2, 2, 1, 3)     # 진폭 2, 2Hz, 위로 1만큼 이동
