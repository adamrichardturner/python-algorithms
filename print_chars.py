def stringPrint(str):
    builtString = ""
    for i in range(len(str)):
        builtString += ((i+1) * str[i])
        builtString += '\n'
    print(builtString[:-1])

print(len("\n")) # 1

stringPrint("abc")