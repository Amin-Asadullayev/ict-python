sentence, temp, say = input("Write a sentence: ")+" ", "", 0
for i in sentence:
    if i == " ":
        if temp:
            say+=1
            temp=""
    else: temp+=i
print(say)