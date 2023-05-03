import matplotlib.pyplot as plt

# Data for the main sequence
ms_temp = [30000, 25000, 20000, 15000, 12000, 10000, 8000, 6000, 5000, 4000, 3500]
ms_lum = [10000000, 1000000, 100000, 10000, 1000, 100, 10, 1, 0.1, 0.001, 0.0001]

# Data for the red giants and supergiants
rg_temp = [5000, 4500, 4000, 3500]
rg_lum = [100, 500, 1000, 1000]
sg_temp = [10000, 7500, 6500, 5500, 3500]
sg_lum = [100000, 10000, 50000, 100000, 100000]

# data for white dwarfs
wd_temp = [20000, 15000, 10000, 8000]
wd_lum = [0.005, 0.001, 0.0005, 0.0001]

# Plot the data
plt.figure(figsize=(8,6))
plt.scatter(ms_temp, ms_lum, color='green', s=100, marker='o', edgecolor='black')
plt.scatter(rg_temp, rg_lum, color='red', s=150, marker='o', edgecolor='black')
plt.scatter(sg_temp, sg_lum, color='yellow', s=200, marker='o', edgecolor='black')
plt.scatter(wd_temp, wd_lum, color='blue', s=50, marker='o', edgecolor='black')

# Set the axes labels and limits
plt.xlabel('Temperature (K)')
plt.ylabel('Luminosity (Lsun)')
plt.xlim(40000, 1000)
plt.ylim(0.0001, 10000000)

# Add labels to the color-coded groups
plt.text(20000, 500, 'Main Sequence', ha='center', va='center', color='green', fontsize=16)
plt.text(4000, 5000, 'Red Giants', ha='center', va='center', color='red', fontsize=16)
plt.text(5500, 500000, 'Supergiants', ha='center', va='center', color='yellow', fontsize=16)
plt.text(15000, 0.0001, 'White Dwarfs', ha='center', va='center', color='blue', fontsize=16)

# Add a line for R=0.1 Rsun
x = [3500, 20000]
y = [0.001, 1]
plt.plot(x, y, linestyle=':', color='blue', label="0.1 Rsun")

# Add a line for R=1 Rsun
x = [3500, 20000]
y = [0.1, 85]
plt.plot(x, y, linestyle=':', color='black', label="1 Rsun")

# Add a line for R=10 Rsun
x = [3500, 20000]
y = [10, 5000]
plt.plot(x, y, linestyle=':', color='green', label="10 Rsun")



# Add gridlines
plt.grid(linestyle='--', linewidth=0.5)

plt.xscale('log')
plt.yscale('log')
plt.xlim(40000, 2000)
plt.ylim(0.000005, 2000000)
plt.legend()
plt.title("Herztsprung Russel Diagram")
# Show the plot
plt.show()