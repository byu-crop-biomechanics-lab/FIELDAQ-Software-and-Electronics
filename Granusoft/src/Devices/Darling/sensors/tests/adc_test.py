from connections import *

def adc_test():
    print("\n **********Beginning ADC Test********** \n")
    for i in range(24):
        print("CHAN0 Sample ", i, " value: ", CHAN0.value, " voltage:", CHAN0.voltage)
        print("CHAN1 Sample ", i, " value: ", CHAN1.value, " voltage:", CHAN1.voltage)
        print("CHAN2 Sample ", i, " value: ", CHAN2.value, " voltage:", CHAN2.voltage)
        print("CHAN3 Sample ", i, " value: ", CHAN3.value, " voltage:", CHAN3.voltage)
        print("CHAN4 Sample ", i, " value: ", CHAN4.value, " voltage:", CHAN4.voltage)
        #print("CHAN5 Sample ", i, " value: ", CHAN5.value, " voltage:", CHAN5.voltage)
        print("CHAN6 Sample ", i, " value: ", CHAN6.value, " voltage:", CHAN6.voltage)
        print("CHAN7 Sample ", i, " value: ", CHAN7.value, " voltage:", CHAN7.voltage)
        print()
        sleep(.5)
    print("\n **********Ending ADC Test********** \n")


if __name__ == "__main__":
    adc_test()
