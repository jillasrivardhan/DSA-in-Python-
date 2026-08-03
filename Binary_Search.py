#Binary Search Algorithm

def bs(arr, key):
   n = len(arr)
   low = 0 #starting
   high = n - 1 #ending

   x = arr.sort() #sorting the array(optional)

   while low <= high:
      mid = (low + high) // 2 #midpoint=6

      if key > arr[mid]:
         low = mid + 1
      
      elif key < arr[mid]:
         high = mid - 1
         
      else:
         print("Element found at index:", mid)
         break


res = bs([11, 21, 32,6, 4, 54, 16, 7, 18, 90], 118)

#checking if the element is found or not

if res != None:
   print(res)
else:
   print("Element not found in the array")
