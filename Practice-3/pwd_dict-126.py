users = {
    'naresh': 'n123',
    'ramesh': 'r456',
    'kishore': 'k478'
}
c=0

while True:
    uname = input("UserName: ")
    pwd = input("Password: ")
    if uname in users and pwd == users[uname]:
        print(f'{uname} welcome,')
        break
    else:
        c += 1
        if c >= 3:
            print("You have entered wrong credentials 3 times, please try again later")
            break
        print("Invalid username or password")
