import numpy as np
import matplotlib.pyplot as plt

SIGMA = 5.67E-8 # stefan-boltzmann-konstante
TEMP_AVG = 0 # K, avg. temp
Q = 341.3  # the insolation

F_reflected = 101.9  #  reflected shortwave flux in W/m2

ALPHA = F_reflected / Q # Planetary Albedo
HEAT_CAPACITY = 1E8 # J/m2/K or C
HEAT_CAPACITY_ATM = 5E8 # J/m2/K or C
RAD_FORCING = 3
TAU = 0.6 # the greenhouse factor

EPSILON = 0.586

def absorbed_short_radiation(Q=Q, alpha=ALPHA):
    return (1-alpha)*Q 

def out_from_surf(temp):
    return SIGMA * temp ** 4

def radiation(temp):
    return SIGMA * temp ** 4

def atm_radiation(atm_temp):
    return EPSILON * SIGMA * atm_temp ** 4


dt = 3600 * 24 * 35 # 1 Jahr

# dE / dt = in - out = ASR - OLR (E: heat content)
# T_2 = T_1 + dt/C*(ASR-OLR(T_1))

temp_atm = 289.09536670009
temp_atm_n_rf = 289.09536670009

temp = 300.79667714
temp_n_rf = 300.79667714

def step(n):
    rf = 0.07*n
    if(n > 100):
        rf = 0
    global temp_atm, temp, temp_n_rf, temp_atm_n_rf
    temp_atm += dt / HEAT_CAPACITY_ATM * (radiation(temp) - 2*atm_radiation(temp_atm))
    temp += dt / HEAT_CAPACITY * (absorbed_short_radiation(alpha=0.32) + atm_radiation(temp_atm) - radiation(temp)  + rf )

    temp_atm_n_rf += dt / HEAT_CAPACITY_ATM * (radiation(temp_n_rf) - 2*atm_radiation(temp_atm_n_rf))
    temp_n_rf += dt / HEAT_CAPACITY * (absorbed_short_radiation(alpha=0.32) + atm_radiation(temp_atm_n_rf) - radiation(temp_n_rf))



numsteps = 300
Tsteps = np.zeros(numsteps)
T_atm = np.zeros(numsteps)

Years = np.zeros(numsteps)
Tsteps[0] = 0
for n in range(numsteps):
    Years[n] = n
    step(n)
    Tsteps[n] = temp 
    T_atm[n] = temp_n_rf 

print(f"Mit RF = {temp}")
print(f"Ohn RF = {temp_n_rf}")

plt.plot(Years, Tsteps, T_atm)

plt.xticks(ticks=[0,30, 50, 100, 150, 200, 250, 300], labels=[0, 3, 5, 10, 15, 20, 25, 30])

plt.xlabel('Zeit in Jahren')

plt.ylabel('Temperatur in K');
plt.savefig('result.png')