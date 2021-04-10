# CPE 202 Lab 1a
from typing import Optional
from typing import List

# Maybe_List (Optional[List]) is either
# Python List
# or
# None

# Maybe_integer (Optional[int]) is either
# integer
# or
# None

# Maybe_List -> Maybe_integer
def max_list_iter(int_list: Optional[List]) -> Optional[int]:
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   if isinstance(int_list, list):
      l = len(int_list)
      l = l - 1
      if l > - 1:
         num = int_list[l]
         while l > -1:
            if int_list[l] >= num:
               num = int_list[l]
               l = l - 1
            else:
               l = l - 1
         return num

      else:
         return None

   else:
      raise ValueError

# Maybe_List -> Maybe_List
def reverse_list(int_list: Optional[List]) -> Optional[List]:
   """reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if isinstance(int_list, list):
      z = []
      l = len(int_list)
      l = l - 1
      while l > -1:
         z.append(int_list[l])
         l -= 1
      return z

   else:
      raise ValueError

# Maybe_List -> None
def reverse_list_mutate(int_list: Optional[List]) -> None:
   """reverses a list of numbers, modifying the input list, returns None
   If list is None, raises ValueError"""
   if isinstance(int_list, list):
      z = int_list
      l = len(int_list)
      l = l - 1
      a = 0
      if l % 2 == 0:
         mid = int(l - ((l/2) - 1))
         #if a == mid:
            #a += 2
            #l -= 2
         while l > a:
            b = z[a]
            x = z[l]
            int_list.pop(a)
            int_list.insert(a, x)
            int_list.pop(l)
            int_list.insert(l, b)
            a += 1
            l -= 1

      else:
         while l > -1:
            b = z[a]
            x = z[l]
            int_list.pop(a)
            int_list.insert(a, x)
            int_list.pop(l)
            int_list.insert(l, b)
            a += 2
            l -= 2

      return None

   else:
      raise ValueError
