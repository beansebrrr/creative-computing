userList = {
    'Vince' : 'myballs'

}
username = input("Enter your username: ")
password = input("Enter your password: ")

if username in userList:
    if password != userList[username]:
        print("die.")
        exit
    print("Sup my g.")
    
    