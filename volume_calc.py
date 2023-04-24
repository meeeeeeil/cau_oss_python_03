width = float(input("width: "))
depth = float(input("depth: 0"))
height = float(input("height: "))

volume = width + depth + height

print("Volume:", volume)

total_length = depth + width + height

if total_length <= 80:
    charge = 5000
elif total_length <=100:
    charge = 8000
elif total_length <=120:
    charge = 10000
elif total_length <=160:
    charge = 13000
else:
    charge = "unvaliable"

print("Total length:", total_length)
print("Charge:", charge)
