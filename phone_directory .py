#phone_directory name and number

names = ["Amal", "Mohammed", "Khadijah", "Abdullah", "Rawan", "Faisal", "Layla"]
numbers = ["1111111111", "2222222222", "3333333333", "4444444444", "5555555555", "6666666666", "7777777777"]
phone_dirctory = dict(zip(numbers, names))

#fucation to search about users
def serchuser():
    id_number = input("Enter your phone number: ")
    if id_number not in phone_dirctory:
        print(f"{id_number} is not a valid phone number")
    else:
        print(phone_dirctory[id_number])
#fucation to add new  users
def newuser():
    id_number_user = input("Enter your phone number: ")
    name_user = input("Enter your name: ")
    phone_dirctory[id_number_user]=name_user
    print(phone_dirctory[id_number_user])

serchuser()
newuser()
