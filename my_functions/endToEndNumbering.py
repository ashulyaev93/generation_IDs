from myAlgoritm import myLoops


print("Please, enter count customers:")
n_customers = int(input())
i = 1

while i <= n_customers:
    uniq = '{:0=7}'.format(i)
    i += 1
    myLoops(uniq)
