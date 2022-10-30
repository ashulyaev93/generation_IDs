import random
from myAlgoritm import myLoops


print("Please, enter count customers:")
n_customers = int(input())
print("Please, enter seven numbers ID: ")
n_first_id = input()
i = 1

myLoops(n_first_id)

while i < n_customers:
    i += 1
    uniq = random.randint(1000000, 9999999)
    myLoops(uniq)
