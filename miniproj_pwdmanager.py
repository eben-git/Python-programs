'''def write_key():
    key = Fernet.generate_key()
    with open("Key.key", "w") as key_file:
        key_file.write(key)'''

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User: ",user, "| Password: ", passw)


def add():
    name = input("Account name: ")
    passwd = input("Password: ")
    with open("passwords.txt", "a") as f:
        f.write(name + "|" + passwd + "\n")


while True:
    mode = input("would you like to add or view existing passwords (view, add), type q to quit: ").lower()
    if mode == "q":
        break
    elif mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("invalid response!!")
        continue
