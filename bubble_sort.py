#==========================
       #bubble sort
#==========================

def bubble_sort(user_input):

   n = len(user_input)
   print(f"before sorting {user_input}")

   for i in range(n):
      for j in range(n-i-1):
         if user_input[j] > user_input[j+1]:
            user_input[j],user_input[j+1] = user_input[j+1],user_input[j]

   print(f"after sorting{user_input}")

bubble_sort([1,34,56,78,90,2,3,0,-1,5])