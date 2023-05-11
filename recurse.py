def irecurse(x):
    if (x > 0):
        ans = x + irecurse(x - 1)
        print(ans)
    else:
        ans = 0
        return ans
        
irecurse(5)

# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(6)
