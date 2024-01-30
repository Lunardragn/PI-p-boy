## DEBUG, real script will have much much more
callout = "Current module: "
module = "None"
currentmodule = int(input("Select module type:"))
if currentmodule == 0:
	print(callout + "None")
	module = "None"
elif currentmodule == 1:
	print(callout + "Sound")
	module = "Sound"
elif currentmodule == 2:
	print(callout + "Ultrasonic Distance")
	module = "Ultrasonic Distance"
elif currentmodule == 3:
	print(callout + "GPS")
	module = "GPS"
else:
	print(callout + "None")
	module = "None"
print(module)
