def is_even(num):
    return (num % 2 ==0)
print(is_even(9))
print(type(3))
print(isinstance(3, int))

#print(*[list(range(1,i+1)) for i in range(1, int(input())+1)], sep='\n')
#print(*[[i for i in range(1, n+1)] for i in range (1,n+1)], sep='\n')

ans = [[]]
def chunked_1(s):
    l = len(s)
    for n in range(1,len(s)+1):
        for j in range(0, l):
            ans.append(s[j:j+n])
        l -= 1
    return ans
print(chunked_1(input().split()))
