from connections import *

def accl_test():
    print("\n **********Beginning ACCL Test********** \n")
    sleep_time = .1
    for i in range(int(3.0/sleep_time)):
        x, y, z = [value / adafruit_lis3dh.STANDARD_GRAVITY for value in \
                    lis3dh.acceleration]
        print("x = %0.3f G, y = %0.3f G, z = %0.3f G" % (x, y, z))

        sleep(sleep_time)

    print("\n **********Ending ACCL Test********** \n")

if __name__ == "__main__":
    accl_test()
