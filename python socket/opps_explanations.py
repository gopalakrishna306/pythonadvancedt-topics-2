# class Bank:
#     __bankname="HDFC"
#     def __init__(self,name,age,sex,account_opening_balance,address,password):
#         self.__name=name
#         self.__age=age
#         self.__add=address
#         self.__cur_bal=account_opening_balance
#         self.__password=password
#         print(f"accout is  created sucessfully for {self.__name}  with {account_opening_balance}")
#     def deposit(self,amount_to_deposit):
#         if amount_to_deposit>0:
#             self.__cur_bal= self.__cur_bal+amount_to_deposit
#         else:
#             return 'please check your amount is shoud be grate then zero'
#         return f"balance {amount_to_deposit} deposited sucessfully to {self.__name} now your balance is {self.__cur_bal}"
#
#     def withdraw(self,amout_to_be_with_draw):
#         if amout_to_be_with_draw > self.__cur_bal:
#             return "insuffciant funds "
#         else:
#             p_w=input('please enter password to with draw amount ')
#             if p_w==self.__password:
#                 self.__cur_bal=self.__cur_bal-amout_to_be_with_draw
#                 return  f"{amout_to_be_with_draw}  is debited from your accout your current balance is " +str(self.__cur_bal)
#             else:
#                 return 'wrong credentials'
#
#     @property
#     def balance_statemnt(self):
#         return f"{self.__name}_balane amonut  " +str(self.__cur_bal)
#
#     def set_name(self, name_to_chnage):
#         self.__name=name_to_chnage
#         return "name change sucessfully"
#     @property
#     def show_all_deatils(self):
#         return self.__name+" "+str(self.__age)+" "+self.__add
#
#     def transfer(self,others,amout):
#         if self.__cur_bal > amout:
#             # p_w=input(f"{self.__name}  please enter password to send aount to {others.__name} is {amout}:---")
#             # if self.__password==p_w:
#             #     others.deposit(amout)
#             self.__cur_bal=self.withdraw(amout)
#             return "transefer sucessfully after transfer "+ self.balance_statemnt
#             # else:
#             #     return 'wrong passsword'
#         else:
#             return 'your balance is less then trying to send'
#
#     def __add__(self, other):
#         return self.__cur_bal+other.__cur_bal
#
#     def __sub__(self, other):
#         return self.__cur_bal-other.__cur_bal
#
#     def setpassword(self):
#         old_pwd=input('enter old password :')
#         if old_pwd==self.__password:
#             new_password=input('please enter new password')
#             self.__password=new_password
#             return 'passwod is set seucessfully'
#         else:
#             return 'your old password valid please try again with valid password'
#
# print(Bank)
# def test(b):
#     obj=b("gopalakrishna",28,"male",500,'kduru','gk12345')
#     return obj
#
# Ac001=test(Bank)
# print(dir(Ac001))
# print(Ac001.balance_statemnt)
#
#
# print(dir(Bank))
# print(Bank._Bank__bankname)
# Bank._Bank__bankname="ICCIC"
# print(Bank._Bank__bankname)
# ACC100001=Bank("gopalakrishna",28,"male",500,'kduru','gk12345')
# print(ACC100001.balance_statemnt)
# ACC100001.deposit(900)
# print(ACC100001.balance_statemnt)
# print(ACC100001.withdraw(200))
# print(ACC100001.withdraw(2100))
# print(ACC100001.balance_statemnt)
# print(ACC100001.__cur_bal)
# print(ACC100001.__name)
# print(ACC100001.__age)
# print(ACC100001.__sex)
# print(ACC100001.__add)
# print(ACC100001.deposit(500))
# print(ACC100001.balance_statemnt)
# print(ACC100001.show_all_deatils)
# print(ACC100001.set_name('gknaidu'))
# print(ACC100001.show_all_deatils)
# ACC100002=Bank("venkey",23,'male',600,'koduru','vk123456')
# print(ACC100001.transfer(400))
# print(ACC100001+ACC100002)
# print(ACC100001-ACC100002)
# print(ACC100002.deposit(1000))
# print(ACC100001+ACC100002)
# print(ACC100002.balance_statemnt+ACC100001.balance_statemnt)
# print(ACC100002.transfer(ACC100001,200))
# print(ACC100001.balance_statemnt)
# print(ACC100002.balance_statemnt)
# print(ACC100001.deposit(1000))
# print(ACC100001.transfer(ACC100002,1600))
# print(ACC100002.balance_statemnt)
# print(ACC100002.transfer(ACC100001,12))
# print(ACC100001.balance_statemnt)
# print(ACC100002.balance_statemnt)
# ACC100003=Bank('somu',24,'male',0,'hyd','sm123456')
# print(ACC100001.transfer(ACC100003,110))
# print(ACC100002.transfer(ACC100003,1980))
# print(ACC100001.balance_statemnt)
# print(ACC100002.balance_statemnt)
# print(ACC100003.balance_statemnt)
# print(ACC100003.transfer(ACC100001,20))
# print(ACC100001.balance_statemnt)
# print(ACC100001.setpassword())
# print(ACC100001.transfer(ACC100003,200))
# print(ACC100003.balance_statemnt)
# ACC100003.setpassword()
# print(ACC100003.transfer(ACC100001,100))
#

reg_for_pass=r'^[A-Za-z][\w]{7}$'
import re
s=re.compile(reg_for_pass)
print(s)
srtingg='Gopalakr'
if re.match(reg_for_pass,srtingg):
    print('sucess')
else:
    print('fial')






