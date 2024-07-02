your_name = input("Enter Your name: ").lower()
partner_name = input("Enter Your Partner name: ").lower()

add_name = your_name+partner_name 
t = add_name.count('t')
r = add_name.count('r')
u = add_name.count('u')
e = add_name.count('e')
true = t+r+u+e
print(true)
l = add_name.count('l')
o = add_name.count('o')
v = add_name.count('v')
e = add_name.count('e')
love = l+o+v+e
print(love)
score = int(str(true)+str(love))
print(score)