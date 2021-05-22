# class test:
#     p='class variable'
#     def __init__(self):
#         self.a=10
#         self.b=20
#
#
#     def show(self,a,b):
#         print('*******',self.a)
#         print(a,b)
#         return 'hai'
#     def add(self):
#         return self.a+self.b
#
# o=test()
# o.a=35
# print(o.a)
# print(o.b)
# print(o.show(22,34))
# print(o.add())
# print(o.p)
#
# test.p='tesssssssssssing'
#
# b=test()
# print('b reference',b.p)
#
# m=test()
# print(m.p)



#
# class test:
#     cv='class variable'
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def t2(self,a,b):
#         self.a=a
#         self.b=b
#
#         return self.a, self.b
#     @staticmethod
#     def t3(a,b):
#         print(a,b)
#     def t4(self):
#         print(self.a,self.b)
#
# o=test(10,20)
# print(o.cv)
# o.cv='gggg'
# print(o.cv)
# m=test(10,20)
# print(m.cv)
#
# test.cv='changing now by claas '
# d=test(10,20)
# print(d.cv)
# print(d.t2('gop','ala'))
# print(d.t3('kri','shna'))
# print(d.t4())
#


# ##################inhertence########################
#
# class parrents:
#     sir_name=''
#     def __init__(self,f_n,m_n,sir_name):
#         self.f_n=f_n
#         self.m_n=m_n
#         parrents.sir_name=sir_name
#     @staticmethod
#     def address(add):
#         return add
#     def property(self,m_p,f_p):
#         d={}
#         d[self.f_n]=f_p
#         d[self.m_n]=m_p
#         return d
#     def show(self):
#         # a=parrents.address()
#         return [self.m_n,self.f_n]
#
# class chi(parrents):
#     def __inint__(self,c_n,c_w):
#         self.c_n=c_n
#         self.c_w=c_w
#         self.add=super().address()
#
#     def ch_add(self):
#         return self.add
#






# t=parrents('ravi','lakshmi','thotapoola')
# t.address('koduru')
# # print(t.sir_name)
# # print(t.show())
# k=t.property(50000,600000)
# # print(k)
# # print(t.__dict__)
#

#
# gk=chi('gk','venkey','thotapoola')
# print(gk.f_n)
# print(gk.m_n)
# print(gk.sir_name)
# print(gk.address('hyd'))
# print(gk.ch_add())























