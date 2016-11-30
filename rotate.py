from BrickPi import *
BrickPiSetup()
port = PORT_C
BrickPi.MotorEnable[port] = 1

def rotateMotor(power, deg, port):
    BrickPiUpdateValues()
    enc = BrickPi.Encoder[port]
    if deg > 0:
        target_pos = enc + deg
        while enc < target_pos:
            BrickPiUpdateValues()
            enc = BrickPi.Encoder[port]
            BrickPi.MotorSpeed[port] = power
        motorStop(port, '+')
    else:
        target_pos = enc - deg
        while enc > deg:
            BrickPiUpdateValues()
            enc = BrickPi.Encoder[port]
            BrickPi.MotorSpeed[port] = -power
        motorStop(port, '-')

def motorStop(port, direction):
    """breaks the specified motor. put + for forwards or -,
    direction must be specified so that the motor can break."""
    if direction == '+':
        power = -10
    else:
        power = 10
    print("breaking")
    for i in range(0, 2):
        BrickPiUpdateValues()
        BrickPi.MotorSpeed[port] = power
    BrickPi.MotorSpeed[port] = 0

#Rotate motor A 360 degrees
rotateMotor(255, 700, port)
