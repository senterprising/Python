#Program for Addition of two numbers by user inputs

#Storing values by key value pair
x = input('Enter first number: ')
y = input('Enter second number: ')

#Adding two numbers after converting string variabels to float
sum = float(x) + float(y)

#Displaying the Sum
print('The sum of {0} and {1} is {2}'.format(x, y, sum))
