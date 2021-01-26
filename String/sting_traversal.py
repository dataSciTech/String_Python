'''
__program__: String traversal using indexing
__author__: Abhinav Anil
__submittedTo__: dataSciTech
__email__: dataascii@gmail.com
__instagram__: @data.sci_

'''

#A string can be traversed by accessing character(s) from one index to another.

def messages(message):
    index = 0
    for i in message:
        print("message[", index, "] = ", i)
        index += 1

messages(message = "Welcome to dataSciTech!")
