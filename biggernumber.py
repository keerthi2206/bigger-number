n1 = int(input('enter your number: '))
n2 = int(input('enter another number: '))
n3 = int(input('enter another number: '))

if n1>n2 and n1>n3:
    print(n1)
elif n2>n1 and n2>n3:
    print(n2)
else:
    print(n3)
