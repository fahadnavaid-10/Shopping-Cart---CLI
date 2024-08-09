from abc import ABC, abstractmethod
from time import strftime

class Details:
    details = {}
    items_bought = []
    product_lst = {
        '1': 'Leather Handbag', '2': 'Diamond Earrings', '3': 'Gold Bracelet',
        '4': 'Silver Necklace', '5': 'Bronze Necklace', '6': 'Fitness Tracker',
        '7': 'Basketball', '8': 'Yoga Mat', '9': 'Sunglasses', '10': 'Wristwatch'
    }
    menu = [
        '1.Leather Handbag', '2.Diamond Earrings', '3.Gold Bracelet', '4.Silver Necklace',
        '5.Bronze Necklace', '6.Fitness Tracker', '7.Basketball', '8.Yoga Mat',
        '9.Sunglasses', '10.Wristwatch'
    ]
    
    def __init__(self):
        try:
            with open('dictionary.txt') as f:
                for line in f:
                    key, value = line.strip().split(':')
                    Details.details[key] = value
        except FileNotFoundError:
            open('dictionary.txt', 'w').close()  # Create the file if it doessn't exist

    def get_details(self):
        return Details.details

    def get_menu(self):
        return Details.menu

    def get_product_list(self):
        return Details.product_lst


class User(ABC):
    def __init__(self, obj):
        self.detail = obj

    @abstractmethod
    def username(self):
        pass

    @abstractmethod
    def password(self):
        pass

    def adding_details(self, username, password):
        self.detail[username] = password

    def add_user_name(self):
        with open('username.txt', 'a') as f:
            for i in self.detail.keys():
                f.write((i + '\n'))

    def adding_details_txt(self):
        try:
            with open('dictionary.txt', 'r') as f:
                existing_details = {line.strip().split(':')[0]: line.strip().split(':')[1] for line in f}
        except FileNotFoundError:
            existing_details = {}

        existing_details.update(self.detail)

        with open('dictionary.txt', 'w') as f:
            for key, value in existing_details.items():
                f.write(f'{key}:{value}\n')


class Create_Account(User):
    def __init__(self, obj):
        super().__init__(obj)
        self.name = input('Enter your user name: ')
        self.username()

    def username(self):
        try:
            with open('username.txt', 'r') as f:
                word = f.read()
                while self.name in word.split('\n'):
                    print('Username already taken')
                    self.name = input('Enter unique username: ')
        except FileNotFoundError:
            open('username.txt', 'w').close()  # Create the file if it doesn't exist

    def password(self):
        pass_word = input('Enter an alphanumeric password: ')
        while True:
            if any(c.isalpha() for c in pass_word) and any(c.isdigit() for c in pass_word):
                print('Account created Successfully!')
                break
            else:
                print('Choose a strong password')
                pass_word = input('Re-enter alphanumeric Password: ')
        self.password = pass_word

        # saving details within this method
        super().adding_details(self.name, self.password)
        super().add_user_name()
        super().adding_details_txt()


class Login(User):
    def __init__(self, obj):
        super().__init__(obj)
        self.name = input('Enter Your user name: ')
        self.username()

    def username(self):
        while self.name not in self.detail:
            print('Username not found')
            self.name = input('Enter correct name: ')

    def password(self):
        while True:
            self.password = input('Enter your password: ')
            actual_pass = self.detail.get(self.name)
            if self.password == actual_pass:
                print('Login Successful')
                break
            else:
                print('Incorrect password!')


class Shopping:
    cart = []
    items_bought = []

    def __init__(self, menu, product_lst):
        self.menu = menu
        self.product_lst = product_lst

    def welcome(self):
        print('\nWelcome to our Shopping Store')

    def display_product_details(self, choice):
        product_detail = {
            '1': 'Leather bag \n Price: $50.00 \n Colour: Brown',
            '2': 'Diamond Earrings \n Price: $1,000.00 \n Original Diamond Pearl',
            '3': 'Gold Bracelet \n Price: $500.00 \n Hook Stripes',
            '4': 'Silver Necklace \n Price: $80.00 \n Colour: Silver',
            '5': 'Bronze Necklace \n Price: $80.00 \n Original Bronze',
            '6': 'Fitness Tracker \n Price: $80.00 \n Colour: Black',
            '7': 'Basketball \n Price: $25.00 \n Pure Leather Ball',
            '8': 'Yoga Mat \n Price: $20.00 \n Colour: Grey',
            '9': 'Sunglasses \n Price: $120.00 \n Colour: Black',
            '10': 'Wristwatch \n Price: $200.00 \n Colour: Brown'
        }
        print('\nProduct Description\n', product_detail.get(choice))

    def __add__(self,other):
        Shopping.cart.append(other)

    def __sub__(self,other):
        Shopping.cart.remove(other)

    def add_to_cart(self, choice):
        result = self.product_lst.get(choice)
        self+result #operator overloading
        print('Added Successfully!')

    def continue_shopping(self):
        while True:
            cont = input('\nDo you want to explore more products? [y/n] ').lower()
            if cont == 'y':
                return True
            elif cont == 'n':
                return False
            else:
                print('Choose Correct option ')

    def start_shopping(self):    
        while True:
            print('\nMenu')
            for i in self.menu:
                print(i)
            choice = input('\nEnter the product number you want to explore:  ')
            while choice not in self.product_lst:
                print(f'Please enter a valid product number from the list!')
                choice = input('Enter the product number you want to explore: ')
            self.display_product_details(choice)

            choice2 = input('\nWant to add in the cart? [y/n] ').lower()
            while choice2 not in ['y', 'n']:
                print('Choose Correct option')
                choice2 = input('Want to add in the cart? [y/n]')

            if choice2 == 'y':
                self.add_to_cart(choice)

            if not self.continue_shopping():
                break

    def discard_product(self):
        choice3 = input('\nDo you want to discard any product from the cart? [Y/n] ').lower()
        while choice3 not in ['y', 'n']:
            choice3 = input('Enter Correct option [y/n]').lower()
        if choice3 == 'y':
            print(f'\nYour Cart:')
            while True:
                for i in range(len(Shopping.cart)):
                    print(f'{i+1}. {Shopping.cart[i]}')
                while True:
                    try:                   
                        discard = int(input('Enter the number of the product you want to discard: '))
                        if 0 <= discard <= len(Shopping.cart):
                            product = Shopping.cart[discard - 1]
                            self-product #operator overloading
                            print(f'\n{product} discarded from the cart.')
                            break
                    except:
                        print('Choose correct number')

                more_discard = input('\nDo you want to discard more products? [y/n] ').lower()
                while more_discard not in ['y', 'n']:
                    more_discard = input('Enter correct option\n[y/n]')
                if more_discard == 'n':
                    break
                print('Products Discarded Successfully!')

    def finalize_shopping(self):
        asking = input('\nDo you want to buy all products from your cart? [y,n]').lower()
        while asking not in ['y', 'n']:
            asking = input('Enter correct option [y/n]: ').lower()

        if asking == 'n':
            while True:
                print('\nYour Cart:')
                # Display the cart items with correct indexing
                for i in range(len(Shopping.cart)):
                    print(f'{i+1}. {Shopping.cart[i]}')

                try:
                    buy = input('\nEnter the numbers of the products you want to buy, separated by commas: ')
                    total_num = buy.split(',')

                    # Validate input and add items to items_bought
                    for num in total_num:
                        index = int(num) - 1  # Adjust for zero-based index
                        if 0 <= index < len(Shopping.cart):
                            Shopping.items_bought.append(Shopping.cart[index])
                        else:
                            raise ValueError('Invalid number')

                    break  # Exit the loop after successful input

                except ValueError:
                    print('Choose correct numbers that are available in the cart')

        else:
            Shopping.items_bought.extend(self.cart)
        print('\nPRODUCT BOUGHT SUCCESSFULLY!\n')

    def view_history(self):
        view = input("Do you want to view your history?[y/n]: \n").lower()
        while view not in ['y', 'n']:
            view = input('Enter correct option[y/n]: \n').lower()
        return view

    def view_exit(self):
        exit_command = input("\nPress 'e' to exit: ").lower()
        while exit_command != 'e':
            exit_command = input('Press correct command!')
        print('*' * 5, "Thank you For Coming", '*' * 5)


class History(Shopping):
    def __init__(self, username):
        self.filename = f'{username}_history.txt'

    def welcome(self):
        print('\nWelcome to your history box! Here you will see your shopping history')
        try:
            with open(self.filename) as f:
                content = f.read()
                print(content)
        except FileNotFoundError:
            print("No history found.")

    def newuser_info(self, username, password):
        with open(self.filename, 'a') as f:
            f.write(f'\nUsername={username}\nPassword={password}\n')

    def add_shopping_info(self):
        with open(self.filename, 'a') as f:
            time = strftime(f'%d-%m-%Y \nTime of exit: %H:%M:%S\n')
            f.write(f'\nShopping date: {time}\n')
            f.write(f'Your cart: \n{super().cart} \nItems Bought: \n{super().items_bought}\n')


# client code
obj = Details()

choice = input('Enter your choice: \n1.Create Account\n2.Login\n')
while choice not in ['1', '2']:
    choice = input('Enter correct choice: ')
if choice == '1':
    acc = Create_Account(obj.get_details()) #Association
else:
    acc = Login(obj.get_details())#Association

acc.username()
acc.password()

shopping = Shopping(obj.get_menu(), obj.get_product_list())  # Association
shopping.welcome() 
shopping.start_shopping()
shopping.discard_product()
shopping.finalize_shopping()

history = History(acc.name)

if isinstance(acc, Create_Account):
    history.newuser_info(acc.name, acc.password)

history.add_shopping_info()

view=shopping.view_history()
if view=='y':
    history.welcome() #method overriding
shopping.view_exit()

