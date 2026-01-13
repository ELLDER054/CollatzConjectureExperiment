# Uses matplotlib for visualization
# You may need to install it
import matplotlib.pyplot as plot

# 'N' is the scale of the x-axis
N = 4000

# Stores the max_heights
max_heights = []
max_height = 0

i = 1
while i < N:
    n = i
    max_height = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = (n * 3) + 1

        # Collects the maximum height
        if n > max_height:
            max_height = n
    max_heights.append(max_height)
    i = i + 1

x_axis = [i for i in range(1, N)]

# Plot for visualization
plot.scatter(x_axis, max_heights, s=5)
plot.show()
