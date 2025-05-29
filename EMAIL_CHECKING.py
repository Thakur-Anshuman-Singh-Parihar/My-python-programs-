def check_email(email):
    valid_char = set('abcdefghijklmnopqrstuvwxyz0123456789-+_@. ')
    if len(email)<6:
        print("Invalid Email : it is to short ")
    elif not email[0].isalpha() :
        print("Invalid Email : 1st letter should be an alphabet")
    elif '..' in email :
        print("Invalid Email : consecutive dots")
    elif ' ' in email :
        print("Invalid Email : spaces are not allowed")
    elif email.count('@') != 1 :
        print("Invalid Email : missing or multiple @ symble")
    elif email[-3] != '.' and email[-4] != '.':
        print("Invalid Email : Invalid syntax")
    elif not set(email).issubset(valid_char):
        print("Invalid Email : used invalid upper case character or invalid symbol")
    else:
        print("valid email")
email = input("Enter Your Email: ")
check_email(email)