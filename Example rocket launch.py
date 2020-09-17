import rocketlaunch.rocket
#import rocketlaunch.bodies
from math import pi, sqrt

motor_isp = 350
wet_mass = 2000
dry_mass = 1000

mass_ship = 200
altitude = 500
"Марс"
MASS_BODY = 5.9726*10**24
RADIUS_BODY = 6371 * 10**3
STANDARD_GRAVITY_BODY = 9.780327
thrust = 100
mass_flow = thrust/motor_isp
reference_area = 0.04

# rocketlaunch.rocket.Vacuum_dV(motor_isp, wet_mass, dry_mass)
# print("Force Gravity =", rocketlaunch.rocket.Force_Gravity(mass_ship, altitude, MASS_BODY, RADIUS_BODY, STANDARD_GRAVITY_BODY))

# rocketlaunch.rocket.Main_simulation(thrust, motor_isp, mass_flow, dry_mass, wet_mass, reference_area, MASS_BODY, RADIUS_BODY, STANDARD_GRAVITY_BODY)
# v_1 = rocketlaunch.rocket.First_space_velocity(MASS_BODY, RADIUS_BODY)

# G = 6.674 * 10**-11
# T = ((2 * pi * RADIUS_BODY)/v_1)/60 # sqrt((RADIUS_BODY*3/G * MASS_BODY)) 

# h = (((STANDARD_GRAVITY_BODY * RADIUS_BODY**2)/v_1**2) - RADIUS_BODY)/1000
# print("Первая косическая равна",v_1,"м/с, Период обращения:", T,  "мин, минимальная высота орбиты для первой косической:", h, "км")

rocketlaunch.rocket.run()