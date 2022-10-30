def myLoops(self):
    dig = []
    dig = list(int(d) for d in str(self))
    number = 0
    j = 0
    for k in dig:
        k = dig[j]
        number = number + k
        j += 1
    print("Customer with number: " + str(self) +
          " goes to group: " + str(number))
