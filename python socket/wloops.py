# i=-1
# while True:
#     i=i+1
#     if i==5:
#         i=i-1
#     if i==10:
#         continue
#     if i==15:
#         break
#     print(i)


# for x in range(0,15)
#     if x==5:
#         continue
#     if x==10:
#         continue
#     if x==15:
#         break
#     print(x)

# i=0
# while i<=5:
#     print('gk')
#     i=i+1

# i=10
# while i>=0:
#     print('gk')
#     i=i-1

#
# i=0
# while 1:
#     i=i+1
#     if i==5:
#         continue
#     if i==7:
#         continue
#     if i>=10:
#         break
#     print(i)



# i=1
# while i<10:
#     i=i+1
#     print(i)
#     if i==5:
#         pass
#     if i==7:
#         continue
#     i=i+1

from  functools import  reduce



# mylist=[[1,3],[6,3],[4,5],[6,7]]
# def test(x,y):
#     if x[0]>y[0] or x[1]>y[1]:
#         pass
#     else:
#         return x

# m=list(reduce(test,mylist))
# print(m)
# for i in range(len(mylist)):
#     for j in range(i,len(mylist)):
#         print(i,j)
# for i in range(len(mylist)):
#     for j in range(i,len(mylist)):
#         print(mylist[i],mylist[j])
#         if mylist[i][0]>mylist[j][0] or mylist[i][1]>mylist[j][1]:
#             continue
#         else:
#             f_l.append(mylist[i])

# print(f_l)
# f_2=[]
# for x in f_l:
#     if x in f_l and x not in f_2:
#         f_2.append(x)
# print(f_2)



# for s in x:
#     for k in x:
#         print(s,k,end='')
#     print('\n')
#

# for i in range(len(mylist)):
#     for x in range(1,len(mylist)):
#         print(mylist[i],mylist[x])



# print(f_l)




from collections import Counter

# s = ['aabaab', 'aaaaabb']
# t = ['bbabbc', 'abb']
# def is_close(s,t):
#     lst = []
#     for a,b in zip(s,t):
#         c1 = Counter(a.lower())
#         c2 = Counter(b.lower())
#         if max((c1-c2).values()) > 3 or max((c2-c1).values()) > 3:
#             lst.append('NO')
#         else:
#             lst.append('YES')
#     return lst
#
#
# print(is_close(s,t))



# l=[x for x in range(100)]
# k=filter(lambda x: x<70,l)
# print(list(k)


x= {'one':1,'two':2,'three':3}
print(type(x))



















































