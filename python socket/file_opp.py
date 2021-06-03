#### type of model sin python file operatins
####  a,a+,ab+,r,r+,rb,rb+,w,w+,wb,wb+


#
# 'r' - reading mode. The default. It allows you only to read the file, not to modify it. When using this mode the file must exist.
#
# 'w' - writing mode. It will create a new file if it does not exist, otherwise will erase the file and allow you to write to it.
#
# 'a' - append mode. It will write data to the end of the file. It does not erase the file, and the file must exist for this mode.
#
# 'rb' - reading mode in binary. This is similar to r except that the reading is forced in binary mode. This is also a default choice.
#
# 'r+' - reading mode plus writing mode at the same time. This allows you to read and write into files at the same time without having to use r and w.
#
# 'rb+' - reading and writing mode in binary. The same as r+ except the data is in binary
#
# 'wb' - writing mode in binary. The same as w except the data is in binary.
#
# 'w+' - writing and reading mode. The exact same as r+ but if the file does not exist, a new one is made. Otherwise, the file is overwritten.
#
# 'wb+' - writing and reading mode in binary mode. The same as w+ but the data is in binary.
#
# 'ab' - appending in binary mode. Similar to a except that the data is in binary.
#
# 'a+' - appending and reading mode. Similar to w+ as it will create a new file if the file does not exist. Otherwise, the file pointer is at the end of the file if it exists.
#
# 'ab+' - appending and reading mode in binary. The same as a+ except that the data is in binary.
#


# --------------------------------------------------------------------------------------------

# if you using r model file should be exit
#     r
#     r for read
#    r+  read and write
#    rb   read binary
#    rb+   read and write of binary

# -----------------------------------------------------------------------------------------------

# if we using w mode same as r but if file is not there it will create

#     w

    # w   write
    # w+  read and write
    # wb  write binary
    # wb+ read and write of binary




# with open("abc.txt") as f:                # file open with mode only otherwise it will not work  it will work is file is avalibale for readingf only.
#     print(f.writable())
#     print(f.readable())

# with open("abc.txt" ,'r') as f:             # if using r mode file must exixt
#     print(f.writable())
#     print(f.readable())


# with open("abc.txt" ,'r+') as f:        #for read and wirte at same time but file must be exist
#     print(f.writable())
#     print(f.readable())

# with open("abc.txt" ,'rb') as f:      #for binary write file must be there
#     print(f.writable())
#     print(f.readable())

# ----------------------------------------------------------------------------------------------------------------------------

# with open("abc.txt", 'a') as f:       # if file not there file will be created
#     print(f.writable())
#     f.write(' \n thotapoola')
#     f.write(' file poineter is end of previous content')
#     print(f.readable())

# with open("abc.txt", 'a+') as f:      # if file not there file will be created .but file poined start with zero
#     print(f.writable())
#     f.write(' \n thotapoola')
#     f.write('\n file poineter is end of previous content')
#     print(f.readable())

# with open("abc.txt", 'ab') as f:      # if file not there file will be created .but file poined start with zero
#     print(f.writable())
#     print(f.readable())

# with open("abc.txt", 'a+') as f:      # if file not there file will be created .but file poined start with zero
#     print(f.writable())
#     print(f.readable())

# -------------------------------------------------------------------------------------------------------------------------


# with open("abc.txt", 'w') as f:      # if file not there file will be created .but file poined start with zero
#     print(f.writable())
#     # f.write(' \n thotapoola')
#     # f.write('\n file poineter is end of previous content')
#     print(f.readable())

# with open("abc.txt", 'w+') as f:      # if file not there file will be created .but file poined start with zero
#     print(f.writable())
#     f.write(' \n thotapoola')
#     f.write('\n file poineter is end of previous content')
#     print(f.readable())


# with open("abc.txt", 'wb') as f:      # if file not there file will be created .but file poined start with zero
#     print(f.writable())
#     f.write(' \n thotapoola')
#     f.write('\n file poineter is end of previous content')
#     print(f.readable())


# with open("abc.txt", 'wb+') as f:      # if file not there file will be created .but file poined start with zero
#     print(f.writable())
#     f.write(' \n thotapoola')
#     f.write('\n file poineter is end of previous content')
#     print(f.readable())

