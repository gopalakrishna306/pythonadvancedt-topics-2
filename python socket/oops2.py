# def captalise(func):
#     def inner(self):
#         return func(self).upper()
#     return inner
#
#
# class student:
#     clz=''
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex= sex
#     @captalise
#     def wish(self):
#         return f"hai {self.name}"
#     @captalise
#     def details(self):
#         return f"name:{self.name} and age is {self.age} and sex is {self.sex}"
#
# ob1=student('gk',28,'male')
#
# print(ob1.wish())
# print(ob1.details())
# ob2=student('rk',29,'male')
# print(ob2.wish())
# print(ob2.details())
# print(student.__dict__)
#
# #### only oops hold this kind of information
#
# print(student.clz)
# student.clz='gate'
# student.add='koodada'
# print(student.clz)
# print(student.add)
# student.year=1988
# print(student.year)
# print(ob2.year)
# print(ob1.year)

#####################################################


#
# class test2:
#     def __init__(self):
#         self.x='gopalakrishna'
#     @property
#     def show(self):
#         return 'gopalakrishna'
#
#
# s=test2()
# # test2.exp='exmaple'
# s.love='i love gopalakrishna'
# # print(s.show(8))
# s3=test2()
# # print(s.love)
# print(s3.show)
# # test2.x='now it willl show'


#
#
#
# class test3:
#     cls_name='testing'
#     def __init__(self):
#         self.x='gopalakrishna'
#
#     def show(self,a,b):
#         return a+b
#
#     def clsm(cls):
#         return 'clsmethod'
#
#     @staticmethod
#     def stm():
#         return 6
#
#     def testing(self,a,b):
#         return test3.show(self,a,b)
#
#
# print(test3.cls_name)
# # print(test3.x)            by using class name we connt get static variables ,local variables and as well as instance variables
# # print(test3.a,test3.b)
#
# ob1=test3()
# print(ob1.cls_name)
# print(ob1.x)
# print(ob1.show(3,4))
# # print(ob1.a,ob1.b)
# # we cont get local variables by refrence object aslo
# print(test3.show('',6,6))
# print(test3.clsm(9))
# print(test3.stm())
# print(test3.testing(4,5,9))


######################setter ans  getter


#
# class test5:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def set_name(self,newname):
#         self.name=newname
#     def get_name(self):
#         return self.name
#
#     def show(self):
#         return self.name+" "+str(self.age)
#
#
# test5.name='ravi'
# test5.age=26
# test4=test5('gopala',24)
# print(test4.show())
# test4.show='edq'
# print(test4.__dict__)
# # print(test5.__dict__)
#
# test4.name='somu'
# test4.age=6
# print(test4.__dict__)
# test4.set_name('sraani')
# print(test4.__dict__)
# print(test4.get_name())
#


#
# class test5:
#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age
#
#     def set_name(self,newname,age):
#         self.__name=newname
#         self.__age=age
#     @property
#     def get_name(self):
#         return self.__name
#     @property
#     def get_age(self):
#         return self.__age
#
#     def show(self):
#         return self.name+" "+str(self.age)
#
# g=test5('gopalakrisha',28)
# g.set_name('gknaidu',34)
#
# print(g.get_name)
# print(g.get_age)


class test5:
    def __init__(self,name,age):
        # pass
        self.__name=name
        self.__age=age

    def set_name(self,newname,age):
        e=1245
        r=int(input('enter number'))
        if r==e:
            self.__name=newname
            self.__age=age
        else:
            print('we cant set')
    @property
    def get_name(self):
        return self.__name
    @property
    def get_age(self):
        return self.__age

    def show(self,x):
        return x+" "+self.__name+" "+str(self.__age)

    def __priatemethod(self):
        print('**************')

    @staticmethod
    def static(c,d):
        return c,d

    def testprovemethod(self,x,c,d):
        self.__priatemethod()
        # self.show(x)
        return [self.show(x),self.static(c,d)]



g=test5('gknaidu',34)
# g.set_name('gknaidu',34)
# print(g.__name)
# print(g.__age)
# print(g.get_name)
# print(g.get_age)
# print(g.show())
# print(g.__priatemethod)
# print(g.testprovemethod('hai',4,5))
# print(g.static(2,3))



class test6():
    def __init__(self,name):
        pass
        # self.__name=name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name=name




g=test6('gk')
g.name='gopalakrishna'
print(g.name)






