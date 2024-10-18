# Robots that Suggest Safe Alternatives

## Installation:
Navigate to each submodule and install from source.
Make sure to install RARL first to avoid dependency issues!

## Navigation

# Run Training
'''
python safety_rl/sim_dubins_policy.py -w -wi 50000 -a -sf -n "anneal_9999"
'''

# Run OOA
''' Python
python safety_rl/sim_dubins_policy.py -ooa -p /home/joe/Documents/safealts/safety_rl/experiments/dubins_policy-DDQN/anneal_9999-toEnd/model/Q-400000.pth -cfg /home/joe/Documents/safealts/safety_rl/experiments/dubins_policy-DDQN/anneal_9999-toEnd/model/CONFIG.pkl
'''

## Manipulation

# Run Training
''' Python
python safety_rl/sim_lift_policy.py -w -wi 50000 -cp 50000 -mu 400000 -of "safety_rl/experiments/Lift_policy"
'''

# Run OOA
''' Python
python safety_rl/sim_lift_policy.py -ooa -cfg /home/joe/Documents/safealts/safety_rl/experiments/Lift_policy/LiftPolicy-DDQN/anneal_9999-toEnd/model/CONFIG.pkl -p /home/joe/Documents/safealts/safety_rl/experiments/Lift_policy/LiftPolicy-DDQN/anneal_9999-toEnd/model/Q-400000.pth
'''
