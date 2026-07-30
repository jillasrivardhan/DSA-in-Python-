#=======================
    #linear search
#=======================

import random

def linear_search(arr):
   key = random.choice(arr)
   n = len(arr)
   i = 0
   for i in range(n):
      if key == arr[i]:
         print('found',arr[i])
      else:
         print("not-found")
linear_search([1,2,34,5,6,78,9])