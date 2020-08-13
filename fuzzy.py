import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Generate universe variables
dist = np.arange(0, 50, 1)
speed = np.arange(0, 100, 1)
Brake_F = np.arange(0, 100, 1)

distance = ctrl.Antecedent(dist, 'distance')
speed = ctrl.Antecedent(speed, 'speed')
Brake_F = ctrl.Consequent(Brake_F,'Brake_F')

# Generate fuzzy membership functions
distance['V_cls'] = fuzz.trimf(distance.universe, [0, 0, 10])
distance['cls'] = fuzz.trimf(distance.universe, [5, 15, 25])
distance['far'] = fuzz.trimf(distance.universe, [20, 30, 40])
distance['V_far'] = fuzz.trimf(distance.universe, [35, 50, 50])

speed['V_slow'] = fuzz.trapmf(speed.universe, [0, 0, 20, 30])
speed['slow'] = fuzz.trapmf(speed.universe, [20, 30, 45, 55])
speed['fast'] = fuzz.trapmf(speed.universe, [45, 55, 70, 80])
speed['V_fast'] = fuzz.trapmf(speed.universe, [70, 80, 100,100])

Brake_F['V_L'] = fuzz.trimf(Brake_F.universe, [0, 20, 40])
Brake_F['L'] = fuzz.trimf(Brake_F.universe, [20, 40, 60])
Brake_F['H'] = fuzz.trimf(Brake_F.universe, [40, 60, 80])
Brake_F['V_H'] = fuzz.trimf(Brake_F.universe, [60, 100, 100])

# Generate rules
rule1 = ctrl.Rule(distance['V_cls'] & speed['V_slow'] , Brake_F['V_H'])
rule2 = ctrl.Rule(distance['cls'] & speed['V_slow'] , Brake_F['V_L'])
rule3 = ctrl.Rule(distance['V_cls'] & speed['slow'] , Brake_F['V_H'])
rule4 = ctrl.Rule(distance['cls'] & speed['slow'] , Brake_F['L'])
rule5 = ctrl.Rule(distance['far'] & speed['slow'] , Brake_F['V_L'])
rule6 = ctrl.Rule(distance['V_cls'] & speed['fast'] , Brake_F['V_H'])
rule7 = ctrl.Rule(distance['cls'] & speed['fast'] , Brake_F['L'])
rule8 = ctrl.Rule(distance['far'] & speed['fast'] , Brake_F['V_L'])
rule9 = ctrl.Rule(distance['V_cls'] & speed['V_fast'] , Brake_F['V_H'])
rule10 = ctrl.Rule(distance['cls'] & speed['V_fast'] , Brake_F['H'])
rule11 = ctrl.Rule(distance['far'] & speed['V_fast'] , Brake_F['L'])
rule12 = ctrl.Rule(distance['V_far'] & speed['V_fast'] , Brake_F['V_L'])

brake_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12])
braking = ctrl.ControlSystemSimulation(brake_ctrl)

while True:
        s = int(input("Enter speed (0-100 km/h) : "))
        d = int(input("Enter distance (m) : "))
        if (s/2 <= d):
                print ("No brake, driving safe!")
        else:
                braking.input['speed'] = s
                braking.input['distance'] = d
        
                braking.compute()
                print ("Brake Force(%): ", braking.output['Brake_F'])
                print ("New speed is: ", s-(s*braking.output['Brake_F']/100))
                
