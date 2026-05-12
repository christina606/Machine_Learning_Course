from controller import Robot

robot = Robot()
devices = robot.getDeviceList()

for name, info in devices.items():
    print(name, info)


    # left_motor=robot.getDevice('motor_1')
    # right_motor=robot.getDevice('motor_2')
    # if not left_motor:
        # print("dont find")
    # left_motor.setPosition(float('inf'))
    # left_motor.setVelocity(0.0)
    # right_motor.setPosition(float('inf'))
    # right_motor.setVelocity(0.0)


    # while robot.step(timestep) != -1:
    
        # left_speed=0.5*max_speed
        # right_speed=0.5*max_speed
        # left_motor.setVelocity(left_speed)
        # right_motor.setVelocity(right_speed)

    
    
    