##############################
def  add(x,y):
    return x+y
print(add(10,5))
######################### lambda is aslo another form for function more the nothing is there

l_m_d=lambda x,y:x+y
print(l_m_d(10,5))

l_m_d2=lambda x:x**2
print(l_m_d2(5))

l_m_d3_1=lambda x:[ n**2 for n in x]
print(l_m_d3_1([3,4,5]))

l_m_d3=lambda x:[n if n**2<2 else n/2 for n in x]
print(l_m_d3([3,4,5]))

l_m_d4=lambda x,y: x+y if x+y>2 else x-y
print(l_m_d4(1,2))

#######lambda == def functionname
####### x: (x) paranthsis and arguments
#########:--- logic and return that logic

l=[1,2,3,4,5]
# print(list(map(str,l)))

### here list(map(function,sequence)) means  list.append(function(x))  for x in seqence
### iam reversing string to int

t_l=list(map(str,l))
print(t_l)

t_l=t_l+['w','t']
print(t_l)
#### same thing i achived by lambda function
# print(list(map(lambda x:int(x),t_l)))

def intifying(x):
    try:
        rs=int(x)
        return rs
    except:
        return None
print(list(map(intifying,t_l)))

print(list(filter(intifying,t_l)))
# print(list(filter(int,t_l)))
print(list(filter(lambda x: intifying(x) ,t_l)))

def intcovverting(x):
    try:
        rs=int(x)
        return rs
    except:
        return None

print(list(filter(lambda x: intcovverting(x) ,t_l)))


from  functools import  reduce


def reducetesting(*args):
    print(args)         ### each time it will bring two elements of  target list list
    print(f'sumof two element s of target list {args[0]},{args[1]}  ',args[0]+args[1])   # after sum two elements replaced by sum  and this sum will first elemt of sum
    return args[0]+args[1]
print(reduce(reducetesting,l))

















