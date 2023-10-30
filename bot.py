def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except (ValueError, IndexError):
            return "Give me name and phone please"
    return wrapper

def handle_hello():
    return "How can I help you?"

@input_error
def handle_add(data, contacts):
    name, phone = data.split(" ")
    contacts[name] = phone
    return f"Contact {name} added."

@input_error
def handle_change(data, contacts):
    name, phone = data.split(" ")
    contacts[name] = phone
    return f"Phone for contact {name} changed."

@input_error
def handle_phone(name, contacts):
    if name not in contacts:
        return "No such contact"
    return contacts[name]

def handle_show_all(contacts):
    if not contacts:
        return "Contact list is empty."
    contact_list = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    return contact_list

def main():
    contacts = {}
    
    while True:
        command = input("Enter a command: ").lower()
        
        if command == "hello":
            response = handle_hello()
        elif command.startswith("add"):
            data = command[len("add"):].strip()
            response = handle_add(data, contacts)
        elif command.startswith("change"):
            data = command[len("change"):].strip()
            response = handle_change(data, contacts)
        elif command.startswith("phone"):
            name = command[len("phone"):].strip()
            response = handle_phone(name, contacts)
        elif command == "show all":
            response = handle_show_all(contacts)
        elif command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            response = "Unknown command. Please try again."
        
        print(response)

if __name__ == "__main__":
    main()
