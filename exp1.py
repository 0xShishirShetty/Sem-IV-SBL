num1=input('enter the first number: ')
num2=input('enter the second number: ')

sum=float(num1)+float(num2)
dif=float(num1)-float(num2)
mul=float(num1)*float(num2)
div=float(num1)/float(num2)

print('sum of {0} and {1} is {2}'.format(num1,num2,sum))
print('difference of {0} and {1} is {2}'.format(num1,num2,dif))
print('multiplication of {0} and {1} is {2}'.format(num1,num2,mul))
print('division of {0} and {1} is {2}'.format(num1,num2,div))

if (num1>num2):
    print('{0} is greater than {1}'.format(num1,num2))
else:
    print('{0} is less than {1}'.format(num1,num2))



count=0
while(count<5):
    count=count+1
    print('BYE BYE')
print('end of while loop \n')    

for i in range(0,3):
    print('Hello')
print('end of for loop \n')
