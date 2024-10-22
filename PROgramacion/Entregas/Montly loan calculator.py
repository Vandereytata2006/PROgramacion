P = float(input('Enter your principal loan amount: '))
annual_rate = float(input('Enter your annual interest rate (as a percentage): ')) / 100
years = int(input('Enter your loan term in years: '))

r = annual_rate / 12
n = years * 12

M=P*(r*(1+r)**n)/((1+r)**n-1)

print(f'Your monthly payment for this loan is: {M}€')