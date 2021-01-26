'''
__program__: Print Pattern
__author__: Abhinav Anil
__submittedTo__: dataSciTech
__email__: dataascii@gmail.com
__instagram__: @data.sci_

'''

# A
# AB
# ABC
# ABCD
# ABCDE
# ABCDEF

for i in range(1,7):
    ch = 'A'
    print()
    for j in range(1, i+1):
        print(ch, end=' ')
        ch = chr(ord(ch)+1)