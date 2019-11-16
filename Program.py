import os
import BuildClasses.TripPickerClass as TP


decision = 'x'

while decision.upper() == 'X':
    os.system('clear')
    print('WELCOME TO THE TRIP PACKAGE MANAGER'.center(95, '.'))
    destination = input('Enter your desired destination: ')
    budget = int(input('Enter your budget type (1 - 1 STAR, 2 - 2 STAR, 3 - 3 STAR, 4 - 4 STAR, 5 - 5 STAR): '))

    user1 = TP.TripPicker(destination, budget)

    print('As per your choices, we recommend the below package...\n')

    print('DESTINATION - {0}\n'.format(destination))
    print('BUDGET TYPE - {0} STARS\n'.format(budget))
    print('RECOMMENDED HOTEL - {}\n'.format(user1.GetHotel()))
    print('PLACES YOU WILL VISIT...\n{0}'.format(user1.GetPlaces()))
    print('TOTAL PRICE OF THE TOUR (INCLUDING HOTEL STAY, FOOD, CAR): Rs. {0}\n\n'.format(user1.GetPrice()))

    decision = input("Press 'C' to CONFIRM this recommendation or press 'X' to change your preferences again: ")


print('\nThis recommendation has been successfully selected.')
print('Best Wishes for your upcoming journey.\n\n')

print('THANK YOU FOR USING OUR SYSTEM'.center(95, '.'))
print('\n')
