'''
__program__: Encrypts a message by adding key value
__author__: Abhinav Anil
__submittedTo__: dataSciTech
__email__: dataascii@gmail.com
__instagram__: @data.sci_

'''

#Hint: Hello, if key =3, then add 3 to every character, So the encrypt meassage of Hello -> K h o o r.

message = "DataSciTech"
index  = 0
while index < len(message):
    letter = message[index]
    print(chr(ord(letter) + 3), end=' ')
    index += 1

