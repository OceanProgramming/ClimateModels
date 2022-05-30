import math
import numpy as np
import matplotlib.pyplot as plt

fac = math.pi * math.pow(6370000, 2)
sigma = 5.67E-8 #Stefan-Boltzmann-Konstante

solar_radiation = 1360 * fac #Eintreffende Sonnenstrahlung
surface_heat_cap = 2E8 * 4 * fac #Waermekapazitaet der Erdoberflaeche
atmosphere_heat_cap = 5.95E21

albedo = 0.3

dt = 3600 * 24 #* 365 # 1 Jahr
steps = 10000

def absorbed_sun_radiation():
    return (1 - albedo) * solar_radiation

def outgoing_radiation(temp):
    return 4 * fac * sigma * temp**4

def out_atmosphere(t):
    return 0.8 * 4 * fac * sigma * t**4

temp_atm = 0
temp = 0

def step():
    global temp_atm
    global temp
    temp += (absorbed_sun_radiation() + out_atmosphere(temp_atm) - outgoing_radiation(temp)) * dt / surface_heat_cap
    temp_atm += (outgoing_radiation(temp) - 2 * out_atmosphere(temp_atm)) * dt / atmosphere_heat_cap

temp_data = np.zeros(steps + 1)
temp_atm_data = np.zeros(steps + 1)
time_data = np.zeros(steps + 1)

temp_data[0] = 0

for n in range(steps):
    time_data[n+1] = n + 1
    step()
    temp_data[n+1] = temp 
    temp_atm_data[n+1] = temp_atm 

#print(temp_data)
#print(f"T_a = {temp_atm}")

print(temp)

plt.plot(time_data, temp_data, temp_atm_data)
plt.xlim(xmin=0.0)
plt.ylim(ymin=0.0)
plt.xlabel('Zeit in Tagen')
plt.ylabel('Temperatur in K');

plt.savefig('result.png')