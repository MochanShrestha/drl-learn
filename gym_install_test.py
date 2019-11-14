
import gym

env = gym.make('BipedalWalker-v2')    # Create the mountain car environment
env.reset()
for _ in range(2000):   # Run for 2000 steps
    env.render()
    env.step(env.action_space.sample())