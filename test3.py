

# def makeCoffee (coffeeType):
#     match coffeeType:
#         case 'off':
#             print('thank you! logging off!')
#             exit()
#         case 'report':
#             print('write to us your complaint please:  ')
#             print (f'Reporting: ({str(input())})....','thank you :) ',sep='\n')
#             exit()
#         case  'latte' :
#             x=str(input('Which size you need please? Big "b" or small "s" : '))
#             if x=='s':
#                 cost=3.5
#                 print (f'Small Latte costs {cost}€ ')
#             if x=='b':
#                 cost=5.2
#                 print (f'Big Latte costs {cost}€ ')
#         case 'espresso':
#             x=str(input('Which size you need please? Big "b" or small "s" : '))
#             if x=='s':
#                 cost=3
#                 print (f'Small Espresso costs: {cost}€ ')
#             if x=='b':
#                 cost=4.2
#                 print (f'Big Espresso costs: {cost}€ ')
#         case 'cappuccino':
#             x=str(input('Which size you need please? Big "b" or small "s" : '))
#             if x=='s':
#                 cost=4
#                 print (f'Small Cappuccino costs: {cost}€ ')
#             if x=='b':
#                 cost=6
#                 print (f'Big Cappuccino costs: {cost}€ ')
#         case _:
#             print('Error!! ', 'Try again please! :) ', sep='\n')
#             exit()


# input1=str(input('chose one of those please: espresso - latte - cappuccino, otherwise chose off or report :) '))
# makeCoffee(input1)
# cost=int(input('if you need big cup put 5, if small cup 3 please :) '))

# match coffeeType,cost:
    # case 'espresso',3:
    #     print('Making small Espresso :) ')
    # case 'espresso',5:
    #     print ('Making big Espresso :) ')
    # case 'latte',3:
    #     print ('Making small Latte :) ')
    # case 'latte',5:
    #     print ('Making big Latte :) ')
    # case 'cappuccino',3:
    #     print ('Making small Cappuccino :) ')
    # case 'cappuccino',5:
    #     print ('Making big Cappuccino :) ')
    # case _:



# more=str(input('you need more operation? :) "y for yes or n for no" '))
# match more:
#     case 'y':
#         coffeeType,cost
#     case 'n':
#         print('thank you!, Enjoy your drink :)')

# if self.checkResources(waterNeeded,milkNeeded,beansNeeded):
#     print(f'Making {coffeeType} ...')
#     self.water-=waterNeeded
#     self.milk-=milkNeeded
#     self.coffeeBeans-=beansNeeded
#     self.money+=cost
#     print(f'Here is your {coffeeType}! Enjoy! :)')
# else:
#     print('Sorry, not enough resources to make your Coffee!')

# def serveCoffee (water,milk,coffee,waterNeeded,milkNeeded,coffeeNeeded):
#         x=0
#         while x==0:
#             coffeeType=str(input('chose one of those please: espresso "e" - latte "l" - cappuccino "c", otherwise chose off or report :) '))
#             if water < 4*waterNeeded:
#                 print(water,4*waterNeeded)
#                 print(bool(water < 4*waterNeeded))
#                 print('Sorry, no water enough!, ask the for help to re-full the Water! ')
#                 print(f'the levels of the recipes:',f'Water: {water}ml',f'Milk: {milk}ml',f'Coffee Beans: {coffee}g',sep='\n')
#                 break
#             if milk < 4*milkNeeded:
#                 print('Sorry, no milk enough!, ask the for help to re-full the Milk! ')
#                 print(f'the levels of the recipes:',f'Water: {water}ml',f'Milk: {milk}ml',f'Coffee Beans: {coffee}g',sep='\n')
#                 break
#             if coffee<4*coffeeNeeded:
#                 print('Sorry, no coffee enough!, ask the for help to re-full the Coffee! ')
#                 print(f'the levels of the recipes:',f'Water: {water}ml',f'Milk: {milk}ml',f'Coffee Beans: {coffee}g',sep='\n')
#                 break
#             if water >= 4*waterNeeded and milk >= 4*milkNeeded and coffee>=4*coffeeNeeded:       
#              match coffeeType:
#                 case 'o':
#                     print('thank you! logging off!')
#                     exit()
#                 case 'r':
#                     print('write to us your complaint please:  ')
#                     print (f'Reporting: ({str(input())})....','thank you :) ',sep='\n')
#                     exit()
#                 case  'l' :
#                     factorWater=1
#                     factorMilk=2
#                     factorCoffee=0.5
#                     x=str(input('Which size you need please? Big "b" or small "s" : '))
#                     if x=='s':
#                         water-=factorWater*waterNeeded
#                         milk -=factorMilk*milkNeeded
#                         coffee-=factorCoffee*coffeeNeeded
#                         cost=3.5
#                         print (f'Small Latte costs {cost}€ ')
                        
#                     if x=='b':
#                         water-=2*factorWater*waterNeeded
#                         milk -=2*factorMilk*milkNeeded
#                         coffee-=2*factorCoffee*coffeeNeeded
#                         cost=5.2
#                         print (f'Big Latte costs {cost}€ ')
                        
#                 case 'e':
#                     factorWater=1
#                     factorMilk=0
#                     factorCoffee=2
#                     x=str(input('Which size you need please? Big "b" or small "s" : '))
#                     if x=='s':
#                         water-=factorWater*waterNeeded
#                         milk -=factorMilk*milkNeeded
#                         coffee-=factorCoffee*coffeeNeeded
#                         cost=3
#                         print (f'Small Espresso costs: {cost}€ ')
                        
#                     if x=='b':
#                         water-=2*factorWater*waterNeeded
#                         milk -=2*factorMilk*milkNeeded
#                         coffee-=2*factorCoffee*coffeeNeeded
#                         cost=4.2
#                         print (f'Big Espresso costs: {cost}€ ')
                        
#                 case 'c':
#                     factorWater=1
#                     factorMilk=2
#                     factorCoffee=2
#                     x=str(input('Which size you need please? Big "b" or small "s" : '))
#                     if x=='s':
#                         water-=factorWater*waterNeeded
#                         milk -=factorMilk*milkNeeded
#                         coffee-=factorCoffee*coffeeNeeded
#                         cost=4
#                         print (f'Small Cappuccino costs: {cost}€ ')
                        
#                     if x=='b':
#                         water-=2*factorWater*waterNeeded
#                         milk -=2*factorMilk*milkNeeded
#                         coffee-=2*factorCoffee*coffeeNe200eded
#                         cost=6
#                         print (f'Big Cappuccino costs: {cost}€ ')
                        
#                 case _:
#                     print('Error!! ', 'Try again please! :) ', sep='\n')
#                     exit()
#             print(f'the levels of the recipes:',f'Water: {water}ml',f'Milk: {milk}ml',f'Coffee Beans: {coffee}g',sep='\n')
#             print('If you need 1 more drink press "y" ')
#             y=input()
#             if y=='y':
#                 x=0
                
#             else:
#                 x=1            
            
# serveCoffee (3,3,3,1,200,3)           



# water1=int(input('Enter the amount of water in "ml" '))
# milk1=int(input('Enter the amount of milk in "ml" '))
# coffee1=int(input('Enter the amount of coffee beans in "ml" '))

# input1=str(input('what do you want to drink? '))


