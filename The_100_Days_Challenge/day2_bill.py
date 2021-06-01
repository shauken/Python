print('Welcome to the tip calculator.')

total = float(input('What was the total bill? $'))

percentage = int(input('What percentage tip would you like to give? 10, 12, or 15? '))

split = int(input('how many people to split the bill? '))

bill = ((total * (percentage/100) + total)/split)

print(f'Each person should pay: ${round(bill,2)}')