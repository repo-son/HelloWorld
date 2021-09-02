weight = int(input('Enter the Weight: '))
weight_type = input('(L)bs or (K)g: ')

if weight_type.upper() == 'L':
    converted = weight * 0.45
    print(f'You are {converted} Kilos')
else:
    converted = weight / 0.45
    print(f'You are {converted} Pounds')
