from Renamer import Renamer

if __name__ == '__main__':
    renamer = Renamer()
    renamer.get_info()

    confirmation = input("Enter \"Y\" if you wish to proceed: ")
    if (confirmation.upper() == "Y"):
        renamer.operate()
