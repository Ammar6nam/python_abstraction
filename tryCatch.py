# name = input('Enter your name: ')

# print(f'name is: {name}')


amount=input('how much do you want to withdraw? ')

userVisit=100
noOfVisits=5
bonus=10

try:
    if userVisit>float(amount)+bonus:
        newAmount=float(amount)+bonus
    else:
        newAmount=float(amount)
    print(newAmount)
except :
    print('Try to put right value')
else:
    print('No Errors!')
finally:
    print('moving to other steps: ')

# if userVisit>noOfVisits:
#     newAmount=float(amount)+bonus
# else:
#     newAmount=float(amount)
