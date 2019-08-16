import gym
import numpy as np
from gym import wrappers

env = gym.make('CartPole-v1')

bestLength = 0
episode_lengths = []

best_weights = np.zeros(4)

for i in range(100): 
#for updating parameter sets
    new_weights = np.random.uniform(-1.0, 1.0, 4)

    length = []
    for j in range(100):
    #for actual episodes (games played)
        
        observation = env.reset()
        #contains a 4-vector representing cart pos and vel, and pole angle and tip vel --> the state of the system
        
        done = False
        cnt = 0

        while not done:
            #env.render()
            #commented out because when training, it'll take astronomical time to render each 'play'

            cnt += 1

            action = 1 if np.dot(observation, new_weights) > 0 else 0
            #step right if dot product of observation and new weights is greater than 0, step left elsewise

            observation, reward, done, _ = env.step(action)
            #reward is given when agent takes a step that doesn't knock over pole

            if done:
            #game ends if pole goes past 15 degrees from center or cart goes past 2.4 units from center
                #env.close()
                break
        length.append(cnt)
    avg_length = float(sum(length) / len(length))
    #of 100 episodes
    
    if avg_length > bestLength:
        bestLength = avg_length
        best_weights = new_weights
    episode_lengths.append(avg_length)
    if i % 10 == 0:
        print('best length is ', bestLength)
            
done = False
cnt = 0
env = wrappers.Monitor(env, 'vids', force=True)
observation = env.reset()

while not done:
    #env.render()
    #commented out because when training, it'll take astronomical time to render each 'play'

    cnt += 1

    action = 1 if np.dot(observation, best_weights) > 0 else 0
    #step right if dot product of observation and new weights is greater than 0, step left elsewise

    observation, reward, done, _ = env.step(action)
    #reward is given when agent takes a step that doesn't knock over pole

    if done:
    #game ends if pole goes past 15 degrees from center or cart goes past 2.4 units from center
        #env.close()
        break

