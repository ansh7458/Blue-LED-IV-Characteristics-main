import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Load data from CSV file, skipping the first row
data = np.loadtxt('LEDcurve.csv', delimiter=',', skiprows=1)  # adjust the filename

voltage = data[:, 0]
current = data[:, 1]

# Plot the original data and the fitting curve
plt.scatter(voltage,current, label='Data Points',color='red')
plt.plot(voltage, current, color='blue', linestyle='-', label='Obtained Curve')
plt.xlabel('Voltage across the LED in Volts')
plt.ylabel('Current through the LED in uA')
plt.legend()
plt.title('5mm Blue LED I-V Characteristic Curve')
plt.grid(True)
plt.show()