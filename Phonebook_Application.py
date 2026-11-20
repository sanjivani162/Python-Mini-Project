phonebook = {}
def show_menu():
    print("\n--- PHONE BOOK MENU---")
    print("1.Add New Contact")
    print("2.View All Contact")
    print("3.Search Contact")
    print("4.Delete Contact")
    print("5.Exit")
while True:
    show_menu()
    choice=input("Enter your choice (1-5):")
    if choice == '1':
        name = input("Enter Name:").lower()
        phone = input("Enter Phone Number:")
        phonebook[name]=phone
        print(f"Contact {name} saved!")
    elif choice == '2':
        if not phonebook:
            print("phone book is empty!")
        else:
            print("\n---All Contacts---")
            for name,phone in phonebook.items():
                print(f"{name} : {phone}")
    elif choice =='3':
        search_name = input("Enter name to search: ").lower()
        if search_name in phonebook:
            print(f"{search_name} : {phonebook[search_name]}")
        else:
             print(f"sorry,{search_name} not found.")
    elif choice == '4':
            del_name = input("Enter name to delete:").lower()
            if del_name in phonebook:
                del phonebook[del_name]
                print("f{del_name} deleted!")
            else:
                print("Name not found.")
    elif choice == '5':
            print("Thank You! Phone Book Closed.")
            break
    else:
            print("Invalid choice! please enter 1-5.")