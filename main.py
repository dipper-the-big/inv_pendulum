import gymnasium as gym

env = gym.make('CartPole-v1', render_mode='human')

env.reset()

Kp = 50
Ti = 20
Td = 10

tot_rew = 0
force = 0
Ie = 0
for _ in range(2000):
  observation, reward, terminated, truncated, info = env.step(force)
  tot_rew += reward

  e = observation[2]
  Ie += e
  de = observation[3]

  F = Kp*(e) + Ti*(Ie) + Td*(de)

  force = 1 if F > 0 else 0
  if terminated or truncated:
    # print(tot_rew)
    observation = env.reset()
    Ie = 0
    tot_rew = 0

env.close()
