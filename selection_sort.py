def selection_sorts(arr):

   n = len(arr)
   for i in range(n-1):
      current_minimum = i
      for j in range(i+1, n):
         if arr[j] < arr[current_minimum]:
            current_minimum = j
      arr[i], arr[current_minimum] = arr[current_minimum], arr[i]

   return arr

x = selection_sorts([64, 25, 12, 22, 11])
print(x)