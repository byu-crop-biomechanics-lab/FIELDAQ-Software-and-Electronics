from connections import *

def temp_test():
    print("\n **********Beginning TEMP Test********** \n")

    for i in range(3):
        print("Temperature: ") #, am.temperature)
        print("Humidity: ") #, am.relative_humidity)
        time.sleep(2)

    print("\n **********Ending TEMP Test********** \n")

if __name__ == "__main__":
    temp_test()
