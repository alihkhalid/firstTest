# Import any modules that we need.
import numpy as np
import datetime

print("Hello, world!")

now = datetime.datetime.now()

print("Current date and time using strftime:")
print(now.strftime("%Y-%m-%d %H:%M:%S"))
print("Wait, we live in the UK! Current date and time is given below.")
print(now.strftime("%d-%m-%Y %H:%M:%S"))

a = np.array([20,30,40])
b = np.array([2,2,2])
c = a.dot(b)

print('The dot product of', a, " and ", b, " is ", c)
