def len(setir: str) -> int:
    say = 0
    for i in setir: say+=1
    return say

text, before, after = input("Text: "), input("What to change: "), input("To what to change: ")
i, bfrlen = 0, len(before)
while i<len(text):
    if text[i:i+bfrlen]==before:
        text = text[:i] + after + text[i+bfrlen:]
        i-=bfrlen
    i+=1
print(text)