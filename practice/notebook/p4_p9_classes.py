# %% [markdown]
# # P-4 ~ P-9. 클래스, 상속, 오버라이딩, super
# 강의 코드를 복원한 예시입니다. 클래스 이름은 강의와 다를 수 있습니다.

# %%
import numpy as np
import matplotlib.pyplot as plt

# %% [markdown]
# ## P-4, P-5. 클래스 만들기

# %%
class DrawSin:
    def __init__(self, amp, freq, bias, end_time):
        self.amp = amp
        self.freq = freq
        self.bias = bias
        self.end_time = end_time

    def calc_sin(self):
        self.t = np.arange(0, self.end_time, 0.01)
        return self.amp * np.sin(2 * np.pi * self.freq * self.t) + self.bias

    def draw_sin(self):
        self.sin = self.calc_sin()
        plt.figure(figsize=(12, 6))
        plt.plot(self.t, self.sin)
        plt.grid()
        plt.show()

# %%
ds = DrawSin(1, 1, 0, 3)
print(ds.__dict__)          # 인스턴스 변수 확인

# %%
ds.freq = 5.0               # 값 바꾸기
ds.draw_sin()

# %% [markdown]
# ## P-6, P-7. 상속: 부모 클래스를 괄호 안에 쓰면 __init__ 등을 그대로 물려받음

# %%
class DrawSinCos(DrawSin):
    def calc_cos(self):
        self.t = np.arange(0, self.end_time, 0.01)
        return self.amp * np.cos(2 * np.pi * self.freq * self.t) + self.bias

    def draw_cos(self):
        self.cos = self.calc_cos()
        plt.figure(figsize=(12, 6))
        plt.plot(self.t, self.cos)
        plt.grid()
        plt.show()

# %%
dsc = DrawSinCos(1, 1, 0, 3)     # __init__ 을 따로 만들지 않았지만 같은 인자를 받음
dsc.draw_sin()                   # 부모의 함수
dsc.draw_cos()                   # 자식이 추가한 함수

# %% [markdown]
# ## P-8. 메서드 오버라이딩: 같은 이름의 함수를 다시 정의하면 자식 것으로 덮어씀

# %%
class DrawSinCos2(DrawSinCos):
    def draw_sin(self):                       # 부모와 같은 이름 → 오버라이딩
        self.sin = self.calc_sin()
        plt.figure(figsize=(12, 6))
        plt.plot(self.t, self.sin)
        plt.title('sin (override)')           # 꾸미기 기능 추가
        plt.xlabel('time [s]')
        plt.grid()
        plt.show()

# %%
DrawSinCos2(1, 1, 0, 3).draw_sin()

# %% [markdown]
# ## P-9. super(): __init__ 을 다시 정의하면 부모의 __init__ 이 덮어써지므로 super() 로 불러온다

# %%
class DrawSinCosBroken(DrawSinCos2):
    def __init__(self, ts):                   # 부모의 __init__ 을 덮어써서 amp, freq 등이 사라짐
        self.ts = ts

print(DrawSinCosBroken(0.01).__dict__)        # {'ts': 0.01} 만 남음

# %%
class DrawSinCos3(DrawSinCos2):
    def __init__(self, amp, freq, bias, end_time, ts):
        super().__init__(amp, freq, bias, end_time)   # 부모의 초기화 유지
        self.ts = ts                                  # 샘플링 타임 추가

    def calc_sin(self):
        self.t = np.arange(0, self.end_time, self.ts)
        return self.amp * np.sin(2 * np.pi * self.freq * self.t) + self.bias

# %%
d3 = DrawSinCos3(1, 1, 0, 3, 0.1)
print(d3.__dict__)
d3.draw_sin()
