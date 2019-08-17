import gym
import numpy as np
import matplotlib.pyplot as plt
from gym import spaces

env = gym.make('CartPole-v1')

maxstates = 10**4
#represents the state space as discrete -- a limited amount of possibilities
gamma = 0.5
#set the discount factor -- how much importance we give to future rewards
alpha = 0.1
#set the learning rate -- extent to which our Q-values are being updated every iteration



env.reset()

print(env.action_space)
print(env.observation_space)
print(env.observation_space.high)
print(env.observation_space.low)

space = spaces.Discrete(8)
x = space.sample()
assert space.contains(x)
assert space.n == 8

q_table = np.zeros([env.observation_space.n, env.action_space.n])
#initialize q table that will be filled after episodes


