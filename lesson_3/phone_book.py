def find_contact_by_name(contact_book, name):
    if contact_book.get(name):
        return contact_book.get(name)
    return None


def find_contact_by_phone(contact_book, phone):
    for key, value in contact_book.items():
        if value == phone:
            return key
    return None


def count_same_numbers(contact_book):
    sum = 0
    for value in contact_book.values():
        a = re.findall(r'.*(.)(\1)(\1)', value)
        if a:
            sum += 1
    return sum
