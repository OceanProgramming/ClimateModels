import math
import numpy as np
import matplotlib.pyplot as plt

fac = math.pi * math.pow(6370000, 2)
sigma = 5.67E-8 #Stefan-Boltzmann-Konstante

solar_radiation = 1360 * fac #Eintreffende Sonnenstrahlung
surface_heat_cap = 2E8 * 4 * fac #Waermekapazitaet der Erdoberflaeche

albedo = 0.3
emissivity = 0.6

dt = 3600 * 24# * 365 # 1 Jahr
steps = 10000

def absorbed_radiation():
    return solar_radiation * (1-albedo)

def outgoing_radiation(temp):
    return emissivity * 4 * fac * sigma * temp**4

def step(temperature):
    return temperature + (absorbed_radiation() - outgoing_radiation(temperature)) * dt / surface_heat_cap


temp_data = np.zeros(steps+1)
time_data = np.zeros(steps+1)

temp_data[0] = 0

for n in range(steps):
    time_data[n+1] = n+1
    temp_data[n+1] = step(temp_data[n])

print(temp_data[steps])

plt.plot(time_data, temp_data)
plt.xlim(xmin=0.0)
plt.ylim(ymin=0.0)
plt.xlabel('Zeit in Tagen')
plt.ylabel('Durschnittstemperatur in K');

plt.savefig('result.png')