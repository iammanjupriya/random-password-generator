import random
print("Hello, World!")
randomchars ="ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*?"
nop = int(input("please enter the number of password:"))
lop = int(input("please enter the length of password:"))

print ("Here are your randam passwords:")

for i in range(nop):
 pwd=""
 for x in range(lop):
  pwd=pwd+random.choice(randomchars)
 print(pwd)
