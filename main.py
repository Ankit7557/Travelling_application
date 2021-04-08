import utility

utility.services()

passport_id = None
nationality = input('Please, Enter your nationality (native or foreigner): ').lower()

while True:

    if(nationality == 'native'):
        pass
    elif(nationality == 'foreigner'):
        passport_id = input('Please, Enter your Passport Id: ')
    else:
        print('Invalid Operation')
        break

    option = input('Enter your option: ')
    if (option == "1"):
        where = input('Where do you want to go?: ').upper()
        if utility.cities().__contains__(where):
            print('There are available trips for',where)    
        else:
            print('There are no available trips for',where)
            break
        utility.get_info()
        print('Your Passport id: ',passport_id)
        
    elif (option=='2'):
        car_type=input('Enter your car type: ')
        passengers=input('How many passangers do you want to carry?')
        where=input('Where do you want to go?')
        utility.get_info()
        print('Passport id: ',passport_id)
        print('to', where, )
        break

    elif (option=='3'):   
        string='BlaBlaCar is an Indian online marketplace for carpooling.\n' \
                    'Its website and mobile apps connect drivers and passengers willing to travel together\n' \
                    'Between cities and share the cost of the journey The platform had 70 million users in 2019 and\n' \
                    ' is available in 22 countries.'
        print(string)
        

    elif (option=='Q'):
        break








































