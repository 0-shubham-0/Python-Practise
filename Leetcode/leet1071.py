def gcdOfStrings(str1,str2):
    l1,l2=len(str1),len(str2)
    def valid(a):
        if l1%a or l2%a:
            return False
        if str1[:i]*(l1/a)==str1 and str1[:i]*(l2/a)==str2:
            return True
        
    for i in range(min(l1,l2),0,-1):
        if valid(i):
            return str1[:i]
import math
math.gcd
a="jff"
print(a*3=="jffjffjff")