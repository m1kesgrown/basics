def input_error(func):

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return 'Enter user name'
        except ValueError:
            return 'Give me name and phone please'
        except IndexError:
            return 'Enter user name'

    return wrapper


phone_book = {}
end_words = ['close', 'good bye', 'exit']


@input_error
def add_contact(name, phone_number):
    phone_book[name] = phone_number
    return f'Contact {name} with phone number {phone_number} has been saved.'


@input_error
def change_phone_number(name, new_phone_number):
    if name in phone_book:
        phone_book[name] = new_phone_number
        return f'Phone number for {name} has been updated to {new_phone_number}.'
    else:
        raise KeyError


@input_error
def get_phone_number(name):
    if name in phone_book:
        return f'The phone number for {name} is {phone_book[name]}.'
    else:
        raise KeyError


def show_all_contacts():
    if phone_book:
        result = 'All contacts:\n'
        for name, phone_number in phone_book.items():
            result += f'{name}: {phone_number}\n'
        return result.strip()
    else:
        return 'The phone book is empty.'


def main():

    commands = {
        'add': add_contact,
        'change': change_phone_number,
        'phone': get_phone_number,
        'show_all': show_all_contacts
    }

    while True:
        user_input = input('').lower()

        if user_input in end_words:
            print('Good bye!')
            break

        if user_input == 'hello':
            print('How can I help you?')
            continue

        command_parts = user_input.split()

        if command_parts[0] in commands:
            try:
                command = command_parts[0]
                if command == 'add':
                    if len(command_parts) < 3:
                        print('Give me name and phone please')
                    else:
                        result = commands[command](*command_parts[1:])
                        print(result)
                elif command == 'change':
                    if len(command_parts) < 3:
                        print('Give me name and phone please')
                    else:
                        result = commands[command](*command_parts[1:])
                        print(result)
                elif command == 'phone':
                    if len(command_parts) < 2:
                        print('Enter user name')
                    else:
                        result = commands[command](*command_parts[1:])
                        print(result)
                else:
                    result = commands[command]()
                    print(result)
            except IndexError:
                print('Give me name and phone please')
        else:
            print('Unknown command.')


if __name__ == '__main__':
    main()
