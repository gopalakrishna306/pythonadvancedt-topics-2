#
# y=10
# def test():
#     x=5
#     def test2():
#        return x
#     return  test2
#

# def f1(p):
#     def t (x,y,m):
#         return p(x,y,m)
#     return t
#
# @f1
# def f2(x,y,m):
#     return x+y+m
#
# print(f2(4,6,9))



#
# def test2(m):
#     def t(x):
#         p=m(x)
#         if p>20:
#             return "p is grate then twenty"
#         elif p==20:
#             return 'p==20'
#         else:
#             return 'p is less then 20'
#     return t
#
# @test2
# def test(x):
#     return x/2
#
# print(test(40))






# from  test import authencate,authencate2
#
# @authencate
# def login(u_n,p_w):
#     return [u_n,p_w]
#
# print(login('gopalakrishna',1234))

# def t3(func):
#     def wrapper():
#         kk=func()
#         return kk
#     return wrapper


# def outer(*uargs):
#     def t2(func):
#         def inner(a,b):
#             rs = func(a,b)
#             # print(rs)
#             # print(*uargs)
#             return [rs,*uargs]
#
#         return inner
#     return t2
#
# # @t3
# @outer(55,45,67)
# def t1(a,b):
#     return a,b
# print(t1(10,20))


#
#
# def t2(exp1,exp2):
#     def oueter(funk):
#         def inner(*args):
#             rs=funk(*args)
#             return '{} is {}-{} is {} and your are is {}'.format(exp1,rs[0],exp2,rs[1],rs[2])
#         return inner
#     return oueter
#
# @t2('hi your name', 'and your conctact numer is')
# def t1(n,p,a):
#     return [n,p,a]
#
# print(t1('gk',9652320676,28))
#








# def test(funk):
#     def inner(self,time):
#         res=funk(self,time)
#         r=res.upper()
#         return r
#     return inner
#


# class test:
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
#     @test
#     def wish(self,time):
#         return "hi {} {} your age is {} and your gender is{}".format(self.name,time,self.age,self.sex)
#
#
#
# p=test('gk',28,'male')
# print(p.wish('good-morning'))
#




#
#
# class test:
#     def __init__(self,funk):
#         self.funk=funk
#     def __call__(self,a,b,c):
#         try:
#             res=self.funk(a,b,c)
#         except Exception as error:
#             return error
#         return res
#
#
# @test
# def div(a,b,c):
#     return (a/b)/c
#
# print(div(10,4,3))
#
#
#



#
# class test2:
#     def __init__(self,func):
#         self.func=func
#     def __call__(self,name,x,y):
#         r=self.func(name,x,y)
#         return x+' '+r.upper()+" "+y
#
# @test2
# def test(name,x,y):
#     return name
#
# print(test('gopalakrishna','hi','goodmorning'))
#
# def test(funk):
#     def inner(self,v,j):
#         r=funk(self,v,j)
#         return "name is {} and age is {} and sex is {} -{}-{}".format(r[0].upper(),r[1].upper(),r[2],v,j)
#     return inner
#
#
# class person:
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
#     @test
#     def details(self,v,j):
#         return [self.name,self.sex,self.age,v,j]
#
#
# gk=person('gopala',28,'male')
# print(gk.details('kod','swe'))




#----------------------------------------------------------------------------

#
# def dec(funk):
#     def inner(n):
#         k=funk()
#         return k+'welcome to decorotor'
#     return inner
#
#
# @dec
# def test():
#     return 'hai'
# print(test('gopalakrishna'))









def f3(fn):
	def inner(x,y,z):
		print('excuting f3')    # f2 return sir thotapoola was comming here the gopalakrish nadddi g here
		r=fn(x,y,z)
		# print(r)
		return r+' '+z
	return inner




def f2(fn):
	def inner(x,y,z):
		print('excuting f2')				# first the list was comming to here .so r[0]+r[1]====sir thotapoola
		r=fn(x,y,z)
		return  r[0]+' '+r[1]
	return inner

@f3
@f2
def t1(x,y,z):
	return [x,y,z]


                                                                                                   excuting orreder is    f2,f3
print(t1('mrs','thotapoola','gopalakrishna'))










# def dec(funk):
#     def inner(n):
#         k=funk(n)
#         return k+'welcome to decorotor'
#     return inner
#
#
# @dec
# def test(n):
#     return 'hai'+n
# print(test('gopalakrishna'))










# def dec():
#     def outer(funk):
#         def inner(n):
#             k=funk(n)
#             return k+'welcome to decorotor'
#         return inner
#     return outer
#
# @dec()
# def test(n):
#     return 'hai'+n
# print(test('gopalakrishna'))




# def f2(funk):                   # first way
#     def inner():                # if there is no arguements to chaild fucntion this is way we have to declare
#         k=funk()
#         return k+'testing'
#     return inner
#
# @f2
# def f1():
#     return  'this is f1'
#
# print(f1())


# def dec(funk):              #  if we have  arguments   to chaild fuction
#     def inner(n):
#         k=funk(n)
#         return k+'welcome to decorotor'
#     return inner
#
#
# @dec
# def test(n):
#     return 'hai '+n
# print(test('gopalakrishna '))



# def dec():                                              # if we have arguments to chaild fuction t this way also correct
#     def outer(funk):
#         def inner(n):
#             k=funk(n)
#             return k+' welcome to decorotor'
#         return inner
#     return outer
#
# @dec()
# def test(n):
#     return 'hai  '+n
# print(test('gopalakrishna'))



# def dec(s):                              # if we have arguments for chaild class and decoration aslo this is the way we can use it
#     def outer(funk):
#         def inner(n):
#             k=funk(n)
#             return k+'welcome to decorotor' +s
#         return inner
#     return outer
#
# @dec('thanks for paractising')
# def test(n):
#     return 'hai'+n
# print(test('gopalakrishna'))



def dec(s1,s2):                              # if we have arguments for chaild class and decoration aslo this is the way we can use it
    def outer(funk):
        def inner(n):
            k=funk(n)
            return k+'welcome to decorotor' +s1+s2
        return inner
    return outer

@dec('thanks for paractising','dont stop leaning')
def test(n):
    return 'hai'+n
print(test('gopalakrishna'))










