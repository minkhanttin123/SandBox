No_Blank = False
blank= " "
def main():
    username = input("Enter your name: ")
    while username == "":
        username = input("Enter again: ")
    print(username[1:len(username):2])
main()







