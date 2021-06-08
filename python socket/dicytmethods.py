d={chr(x):x for x in range(97,110)}

print(d['a'])   # to acces a value
print(d.get('a'))    # acces another way 

print(d.setdefalut('a'))    # it return a value it aslo one mthod to acceses .but in above methods you wil get error .but below method give messase age defalut  
print(d.setdefault("z",'thnaks for serching that key is not thre'))



print(d.keys())     #list aof all keys  
    #dict_keys(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'])
  
print(d.values()  #list of all values 
  #dict_values([97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109])
      
print(d.fromkeys())

d.clear()  # it will clear dict
print(d)  #  ---{}
  
d.update({"A":65})   # it will updatee dict         
      #{'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'A': 65}
      

d.pop()      #TypeError: pop expected at least 1 argument, got 0
      
d.pop('a')   #it removes  specified key from dict band return its value  a=10
      
d.popitem()  # it wont take any argument and it will remove last item from dict and return its (key,value) as tuple.
      
d.setdefalut()        
      
