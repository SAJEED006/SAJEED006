def abc_recursion(k):
    if k>0:
        result=k+abc_recursion(k-1)
        return result
    else:
        result=0
        return result
print("answer is =",abc_recursion(3))





