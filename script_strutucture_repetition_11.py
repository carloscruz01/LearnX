for w in range(0, 10):
    name = (str(input('Enter your name:')))
    if name:
        print('Candidates:', '[', name, ']')
    else:
        print('Try everyone')
print('___________________________________')
for z in range(0, 10):
    age = (float(input('Enter your age:')))
    #"""Usei o 00.99 para especificar que
    # por uma diferença de 0.01 uma pessoa x
    # faz parte do grupo y """
    if age <= 12.99:
        print('Your age is: [', age, ']  You are a child!')
    elif age <= 17.99:
        print('Your age is: [', age, ']  You are a teen!')
    elif age <= 59.99:
        print('Your age is: [', age, ']  You are a Adult!')
    else:
        print('Are you a old man')
print('___________________________________')
