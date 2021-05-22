# import re
# p='ab{2}c'      # it was looking for a c  if b present or no present no problum it b present 10000  times also no problium
# st='adbcd efhgh i  abbcacb acd ja'
# k=re.findall(p,st)
# print(k)
# # #
# import re
# p='[a]+'      # it was looking for a c  and b shoild be atleast one time
# st='adbcd #$efhgh i aca caca aaabcdefgh abcacb ccccccc @$aaaaaaaaaaabdcefghigj acd999 24354j54@@@@##&$^$%^$&#3543a  ab'
# k=re.findall(p,st)
# print(k)

# import re
# p='b{0,3}s$'
# # it was looking for a c  and b shoild 0 time or 1 time .not more then 1 time
# st='bas abababa abbab abababa 123456bababa @#$#sbasbdb bdbadjewd jeie2edo s'
# # st='bbbs'
# k=re.search(p,st)
# print(k)
# #

# import re
# p=r'([aeiouAEIOU])\1+'      # it was looking for a c  and b shoild 0 time or 1 time .not more then 1 time
# st='rabcdeefgyYhFjkIoomnpOeorteeeeet'
# k=re.finditer(p,st)
# for m in k:
#     print(m)
#
#
#
# import re
# p=r'\d{2,4}[*.-]\d{2,4}[*.-]\d{2,4}'      # it was looking for a c  and b shoild 0 time or 1 time .not more then 1 time
# st='12-02-20123  12.04.2024  12*04*2018  12-23*2103   2014*21-13 23-12-2014'
# k=re.findall(p,st)
# k=re.finditer(p,st)
# # print(list(k))
# for m in k:
#     print(m.group())

#

#
# import re
# sd=re.compile(r'^[a-zA-Z][-\w\.]+@[a-z]+\.[a-z]{2,3}$')     # it was looking for a c  and b shoild 0 time or 1 time .not more then 1 time
# st='g123.12o_p1233@qsdl.com'
# # print(list(sd.finditer(st)))
# k=sd.finditer(st)
# # # print(k)
# for m in k:
#     print(m)


#
# import re
# x='91'
# sd=re.compile(r'^[0+91]?[6789][0-9]{9}$')     # it was looking for a c  and b shoild 0 time or 1 time .not more then 1 time
# st='9652320676'
# k=sd.finditer(st)
# print(k)
# for m in k:
#     print(m)
#


# #
# import re
#
# sd=r'[gop]'     # it was looking for a c  and b shoild 0 time or 1 time .not more then 1 time
# st='gooop'
# k=re.match(sd,st)
# print(k)

def test():
    return 1









