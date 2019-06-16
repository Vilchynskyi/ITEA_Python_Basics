# phone book
import re


def get_user_input(contacts_book):
    print('1 - Add to contact book\n2 - Find a contact\n3 - Change a contact'
          '\n4 - Delete a contact \n5 - Count how many numbers have 3+ same '
          'numbers in a row \n6 - Exit')
    user_input = int(input('\nWhat to do? '))
    while user_input > 6 or user_input < 1:
        user_input = int(input('\nTry again '))
    if user_input == 1:
        contacts_book[input('Insert name ')] = input('Insert number ')
        print('Contact was successfully added \n')
        get_user_input(contacts_book)
    elif user_input == 2:
        find_contact(contacts_book)
        get_user_input(contacts_book)
    elif user_input == 3:
        change_contact(contacts_book)
        get_user_input(contacts_book)
    elif user_input == 4:
        delete_contact(contacts_book)
        get_user_input(contacts_book)
    elif user_input == 5:
        print(count_same_numbers(contacts_book), 'contact(s) have a three '
                                                'or more same numbers\n')
        get_user_input(contacts_book)
    else:
        exit()


def find_contact(phone_book):
    user_input = int(input('\nFind by contact number - insert 1'
                           '\nFind by contact name - insert 2: '))
    if user_input == 1:
        contact_number = input('Insert contact number\n')
        for key, value in phone_book.items():
            if value == contact_number:
                print(key, '-', value)
                break
    elif user_input == 2:
        contact_name = input('Insert contact name\n')
        print('Number is ', phone_book.get(contact_name))
    return phone_book


def delete_contact(phone_book):
    user_input = input('Insert contact name which you want to delete ')
    for key, value in phone_book.items():
        if key == user_input:
            print('Do you want to delete ?', key, value)
            break
    user_choice = int(input('\nFind by contact number - insert 1'
                            '\nFind by contact name - insert 2: '))
    if user_choice == 1:
        phone_book.pop(key)
        print('Contact was deleted\n')
    elif user_input == 2:
        print('Maybe next time)\n')
    return phone_book


def change_contact(phone_book):
    user_input = input('Insert contact name which you want to change ')
    for key, value in phone_book.items():
        if key == user_input:
            phone_book.pop(key)
            phone_book[input('Insert new name ')] = input('Insert new number ')
            print('Contact successfully changed \n')
    return phone_book


def count_same_numbers(phone_book):
    sum = 0
    for value in phone_book.values():
        a = re.findall(r'.*(.)(\1)(\1)', value)
        if a:
            sum += 1
    return sum


if __name__ == '__main__':
    get_user_input({})
