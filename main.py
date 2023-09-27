import random

s = input()

if len(s) < 10:
    print("string not long enough")
elif len(s) > 10:
    print("string too long")
else:
    print("perfect string")
    
    
print(s[0], s[9])

word = ''

for char in s:
    word += char
    print(char)


shuffled_list = random.sample(s, len(s))

word = ""
for char in shuffled_list:
    word += char

print(word)