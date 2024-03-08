from connections import *

def motor_test():
    print("\n **********Beginning Motor Test********** \n")
    duration = 1
    freq = 50

    for motor, in1, in2, pwm in zip(MOTORS, IN1, IN2, PWM):
        p = GPIO.PWM(pwm, freq)
        p.start(0)

        # Drive the motor clockwise
        print("Driving Motor {} clockwise for {} seconds".format(motor, duration))
        GPIO.output(in1, GPIO.HIGH)
        GPIO.output(in2, GPIO.LOW)
        p.ChangeDutyCycle(50)
        sleep(duration)

        # Drive the motor counterclockwise
        print("Driving Motor {} counterclockwise for {} seconds".format(motor, duration))
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.HIGH)
        p.ChangeDutyCycle(100)
        sleep(duration)

        # Reset all the GPIO pins by setting them to LOW
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)
        p.stop()

    print("\n **********Ending Motor Test********** \n")

if __name__ == "__main__":
    motor_test()
