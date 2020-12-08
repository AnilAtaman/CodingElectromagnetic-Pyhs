import matplotlib.pyplot as plt
import math
import numpy as np
#MAGNETIC FIELD BY INFITINELY LONG WIRE
Mo = 4 * math.pi * 10e-7
np.linspace(0, 0.5, 0.0001, endpoint=True)
I  = 10
magneticField_10 = []
counter = 0
incresement = 0.01
for R in np.arange(incresement, 0.5, incresement):
    magneticField_10.append(Mo * I / (2*math.pi*R))


I  = 30
magneticField_30 = []
counter = 0
incresement = 0.01
for R in np.arange(incresement, 0.5, incresement):
    magneticField_30.append(Mo * I / (2*math.pi*R))

I  = 50
magneticField_50 = []
counter = 0
incresement = 0.01
for R in np.arange(incresement, 0.5, incresement):
    magneticField_50.append(Mo * I / (2*math.pi*R))

fig, (ampere1,ampere1_1) = plt.subplots(2)

ampere1.plot(np.arange(incresement, 0.5, incresement),magneticField_10,label = 'I = 10')
ampere1.plot(np.arange(incresement, 0.5, incresement),magneticField_30,label = 'I = 30')
ampere1.plot(np.arange(incresement, 0.5, incresement),magneticField_50,label = 'I = 50')
ampere1.set_ylabel('Magnetic Field, Tesla')
ampere1.set_xlabel('Distance [m]')


ampere1_1.plot(np.arange(incresement, 0.5, incresement),magneticField_10,label = 'I = 10')
ampere1_1.plot(np.arange(incresement, 0.5, incresement),magneticField_30,label = 'I = 30')
ampere1_1.plot(np.arange(incresement, 0.5, incresement),magneticField_50,label = 'I = 50')
ampere1_1.set_ylabel('Magnetic Field, Tesla')
ampere1_1.set_xlabel('Distance [m]')
ampere1_1.set_ylim(0,magneticField_10[0])
fig.suptitle('Magnetic Field by Infınıtely Long Wire')
plt.legend()
plt.show()

##############








