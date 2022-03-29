# Temperature Converter CLI
# Python 3
#
# Justin M. Rains
# jmrains@protonmail.com
# 2022-03-26

inp_temp = input("Enter the temperature in ° C or F (ex. 10c or 50 F): ")
inp_temp = inp_temp.strip().lower()

# Conversion from Celsisus to Fahrenheit
if (inp_temp.endswith("c")):
    inp_temp = inp_temp.strip().split(" ")[0]
    if inp_temp.endswith("c"):
        inp_temp = float(inp_temp[:-1])
    else:
        inp_temp = float(inp_temp)
    print(f"Converting from {inp_temp}° C.")
    out_temp = ((inp_temp * 9 / 5) + 32)
    if out_temp % 1 == 0:
        print(f"The temperature is {round(out_temp)}° F.")
    else:
        print(f"The temperature is approximately {round(out_temp)}° F.")

# Conversion from Fahrenheit to Celsius
elif (inp_temp.endswith("f")):
    inp_temp = inp_temp.strip().split(" ")[0]
    if inp_temp.endswith("f"):
        inp_temp = float(inp_temp[:-1])
    else:
        inp_temp = float(inp_temp)
    print(f"Converting from {inp_temp}° F.")
    out_temp = ((inp_temp - 32) * 5 / 9)
    if out_temp % 1 == 0:
        print(f"The temperature is {round(out_temp)}° C.")
    else:
        print(f"The temperature is approximately {round(out_temp)}° C.")

# Something has gone awry; don't crash on bad input
else:
    print("Error. Please try again.")
