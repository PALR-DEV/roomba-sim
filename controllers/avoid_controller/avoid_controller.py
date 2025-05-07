"""avoid_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)
left_motor = robot.getDevice("left wheel motor")
right_motor = robot.getDevice("right wheel motor")

left_motor.setPosition(float("inf"))
right_motor.setPosition(float("inf"))

ds_names = ['ps0', 'ps1', 'ps2', 'ps3', 'ps4', 'ps5', 'ps6', 'ps7']
sensors = [robot.getDevice(name) for name in ds_names]

for sensor in sensors:
    sensor.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    sensor_values=[sensor.getValue() for sensor in sensors]
    print("Sensor values:", sensor_values)
    
    left_speed = 2.0
    right_speed = 2.0
    
    if sensor_values[0] > 80.0 or sensor_values[7] > 88.0:
        left_speed = -2.0
        right_speed - 2.0
        
    left_motor.setVelocity(left_speed)
    right_motor.setVelocity(right_speed)
    
    # left_motor.setVelocity(0.2)
    # right_motor.setVelocity(0.2)
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.
