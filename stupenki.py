s = input("подстрока ")
t = input("строка ")

l = 0

for i in range(len(s)):
    j = 0
    j = t.find(s[i])
    if j != -1:
        l += 1
if l == len(s):
    print("True")
elif l != len(s):
    print("False")