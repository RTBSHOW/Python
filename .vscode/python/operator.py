a = int(input("Enter the value of a:")) 
# =is an assignment operator
# increment operator
a+=5

b = int(input("Enter the value of b:"))
# grab the value of b and multiply by 5 and assign the value on b
b*=5
c=a+b


print(c)
# Comparision operators
d=5>3
e=43==33
f=5!=3
g=54==43
print(d)
print(e)
print(f)
print(g)     

# lohgical operators
# turyth table of 'or' operator
i=True or False
print("True or True is",True or True)
print("True or False is",True or False)
print("False or True is",False or True)     
print("False or False is",False or False)
# turyth table of 'and' operator
print("True and True is",True and True)     
print("True and False is",True and False)
print("False and True is",False and True)
print("False and False is",False and False)
# turyth table of 'not' operator
print("not True is",not True)
print("not False is",not False)