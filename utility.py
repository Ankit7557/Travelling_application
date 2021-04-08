
def cities():
    list1 = ["NEW YORK","SAN FRANCISCO","NEW DELHI","MUMBAI","LONDON","MADRID",
             "DUBAI","LOS ANGELES","CHENNAI","KOLKATA","BERLIN","ROME","VENICE"
             "MILAN","NAPLES","SINGAPORE"]
    return list1

def get_info():
    name = input('Enter name: ')
    surname = input('Enter surname: ')
    email = input('Enter your email: ')
    phone = input('Enter phone: ')
    location = input('Enter your current location: ')
    requires = input('Enter requirements:(Smoking: No, Pet: Yes, Luggage: Yes) ')
    passengers = input('How many passengers?: ')
    print('Name: ', name, 
            '\nSurname:', surname, 
            '\nE-mail:', email, 
            '\nfrom', location,
            '\nwith these requires:', requires, 
            '\nwith these passengers', passengers)

def services():
    print('1: Find ride\n'
      '2: Offer ride\n'
      '3: How it works\n'
      'Q: Quit')