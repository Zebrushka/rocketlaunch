import rocketlaunch.rocket
# rocketsim.rocket.initialize_variables()

motor_isp = 350
wet_mass = 0.4
dry_mass = 0.1

mass_ship = 200
altitude = 500
MASS_BODY = 1*10^21
RADIUS_BODY = 251000
STANDARD_GRAVITY_BODY = 1.101

rocketlaunch.rocket.Vacuum_dV(motor_isp, wet_mass, dry_mass)
print(rocketlaunch.rocket.Force_Gravity(mass_ship, altitude, MASS_BODY, RADIUS_BODY, STANDARD_GRAVITY_BODY))

thrust = 10
mass_flow = thrust/motor_isp
reference_area = 0.04
rocketlaunch.rocket.Main_simulation(thrust, motor_isp, mass_flow, dry_mass, wet_mass, reference_area, MASS_BODY, RADIUS_BODY, STANDARD_GRAVITY_BODY)