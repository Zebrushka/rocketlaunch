import rocketlaunch.rocket
#import rocketlaunch.bodies
from math import pi, sqrt

motor_isp = 350
wet_mass = 0.4
dry_mass = 0.1

mass_ship = 200
altitude = 500
MASS_BODY = 1.08*10**20
RADIUS_BODY = 252000
STANDARD_GRAVITY_BODY = 0.101

rocketlaunch.rocket.Vacuum_dV(motor_isp, wet_mass, dry_mass)
print(rocketlaunch.rocket.Force_Gravity(mass_ship, altitude, MASS_BODY, RADIUS_BODY, STANDARD_GRAVITY_BODY))

thrust = 10
mass_flow = thrust/motor_isp
reference_area = 0.04
#rocketlaunch.rocket.Main_simulation(thrust, motor_isp, mass_flow, dry_mass, wet_mass, reference_area, MASS_BODY, RADIUS_BODY, STANDARD_GRAVITY_BODY)
v_1 = rocketlaunch.rocket.First_space_velocity(MASS_BODY, RADIUS_BODY)

G = 6.674 * 10**-11
T = ((2 * pi * RADIUS_BODY)/v_1)/60 # sqrt((RADIUS_BODY*3/G * MASS_BODY)) 

h = ((STANDARD_GRAVITY_BODY * RADIUS_BODY**2)/v_1**2)/1000
print("Период обращения:", T,  "мин, Высота орбиты:", h, "км")