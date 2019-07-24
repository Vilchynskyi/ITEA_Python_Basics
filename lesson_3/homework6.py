import re
from phone_book import (find_contact_by_name,
                        find_contact_by_phone,
                        count_same_numbers,
                        delete_contact
                        )


if __name__ == '__main__':
    contact_book = {}
    print('1 - Add to contact book'
          '\n2 - Find a contact by phone'
          '\n3 - Find a contact by name'
          '\n4 - Change a contact'
          '\n5 - Delete a contact'
          '\n6 - Count how many numbers have 3+ same numbers in a row '
          '\n7 - Exit')
    user_input = int(input('\nWhat to do? '))
    while 1 <= user_input <= 6:
        if user_input == 1:
            contact_book[input('Insert name ')] = input('Insert number ')
            print('Contact was successfully added \n')
        elif user_input == 2:
            phone = input('\nInsert contact phone ')
            print(find_contact_by_phone(contact_book, phone))
        elif user_input == 3:
            name = input('\nInsert contact name ')
            print(find_contact_by_name(contact_book, name))
        elif user_input == 4:
            name = input('\nInsert contact name ')
            contact_book.pop(name)
            contact_book[input('Insert new name ')] = input('Insert new number ')
            print('Contact was successfully changed \n')
        elif user_input == 5:
            user_input = input('Insert contact name which you want to delete ')
            print(delete_contact(contact_book, user_input))
        elif user_input == 6:
            print(count_same_numbers(contact_book))
        user_input = int(input('\nWhat to do? '))
