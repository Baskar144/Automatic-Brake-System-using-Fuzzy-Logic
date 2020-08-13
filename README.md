# Automatic Brake System using Fuzzy Logic
This system aims to maintain the following distance between two vehicles. The system automatically protects the distance by acting on the brake force without the driver having to press the brake.

Tracking distances are used as follows:

Speed (km/h)-Following Distance (m):

90-45

80-40

70-35

60-30

50-25

I have two inputs and one output, the inter-distance (meter) is based on ultra-sonic sensor and speed (km/h) is based on Hall effect principle. The output of our fuzzy proposed controller is brake force (%) pressure. Fuzzy logic design is consisting of inputs, output, and Mamdani-Fuzzy inference engine. The output is the brake force and is defuzzied using the centroid method.
