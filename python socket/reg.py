# with open('test.txt','r+')as f:
#     l=f.readlines()
#     c_l=[]
#     w_l=[]
#     import re
#     for x in l:
#         try:
#            p=r"^['a-z][\w\.\-]+@[a-z]+\.+[a-z]{2,3}$"
#            v=re.match(p, x)
#            if v:
#                c_l.append(v.group())
#            else:
#                w_l.append(x)
#         except Exception as sms:
#            print(sms)
#
# print(c_l)
# print(w_l)
#


# s='gopalak.2334-3_rishna2352@gmail.com'
# import re
# try:
#     p = r'^[a-z][\w]+[@][a-z]+[\.][a-z]+'
#     m_n = re.match(p, s)
#     print(m_n.group())
# except Exception as sms:
#     print(sms)





# s='gopalakrishhna306@gmail.com'
# import re
# p=r'^([a-z][\w\.\-]+)@([a-z]+)\.+([a-z]{2,3}$)'
# m=re.match(p,s)
# print(m.group(1))
# print(m.group(2))
# print(m.group(3))



# s='gopalakrishna'
# print(s[-1:-5:-1])
#

# l=[1,2,3,4,5,6]










