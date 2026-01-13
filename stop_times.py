# Uses matplotlib to visualize
# You may need to install it
import matplotlib.pyplot as plot

# 'N' is the scale of the X-axis
N = 100000

# A list of the stopping times for each starting number
stop_times = []

# 'n' is the starting number
n = 2

i = 1
while i < N:
    n = i

    # 'j' keeps track of the stopping time for the current 'n'
    j = 0

    # Repeat until the cycle reaches 1
    # The cycle would then repeat 1, 4, 2, 1, etc... infinitely
    # The conjecture generally just states that all starting numbers will eventually reach 1
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = (n * 3) + 1
        j = j + 1
    stop_times.append(j)
    i = i + 1

x_axis = [i for i in range(1, N)]

# Plot the results
plot.scatter(x_axis, stop_times, s=5)
plot.show()
