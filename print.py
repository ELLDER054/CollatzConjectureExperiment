# Simply prints out the data for every number
# An even step is denoted as 'e'
# An odd step is denoted as 'o'
# n is on the left side of the screen
# The stopping time of the starting n is shown to the right of the stream of 'e's and 'o's
# i.e.
# 10 -  EOEEEE - 6
# meaning that, starting from 10, it took 6 cycles to bring it back to 1

# When I first ran this program, I saw lots of stopping times that were 13 away from nearby stopping times and I wondered what was significant about the number 13
# I'm sure somebody has researched this and this is likely what is seen as the "stairstep" pattern in the graph from stopping_times.py

# prints information for all numbers 2 to N
N = 4000

n = 2
i = 1
while i < N:
    n = i
    print(n, " - ", end="")
    j = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            print("e", end="")
        else:
            n = (n * 3) + 1
            print("o", end="")
        j = j + 1
    print(" - ", j)
    i = i + 1
