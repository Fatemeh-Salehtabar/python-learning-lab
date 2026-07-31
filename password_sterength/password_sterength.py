user_name :str =input("Enter username: ")
password :str =input("Enter password: ")
PASWORD_STERENGTH :int= 7
score:int= 0
erorr_list = []

def contain_alpha(password:str):
    for char in password:
        if char.isalpha():
            return True
    return False

def contain_special_charecter(password: str):
    for char in password:
        if char == "!" or char == "@" or char == "$":
            return True
    return False            

def contain_common_password(password: str):
    forbidden= ["123456", "12345678", "12345", "111111", "123456789", "quwerty", "asdfgh", "zxcvbnm", "admin", "password","p@s$w0rd"]
    for item in forbidden:
        if item == password:
            return True
    return False
    



if len(password) > 8:
    score+=1
else:
    erorr_list.append("length of password less than 8")
    
if contain_alpha(password) and contain_special_charecter(password):
    score+=1
else:
    erorr_list.append("passwod dosent have english char and (@,!, $) ")
    
if password != user_name:
    score+=1
else:
    erorr_list.append("password simillar to the username")

if password != password.upper() and password != password.lower():
    score+=1
else:
    erorr_list.append("Password must contain both uppercase or lowercase letters.")

if password.swapcase() != user_name:
    score+=1
else:
    erorr_list.append("pasword is swapcase version of username")

if not contain_common_password(password):
    score+=1
else:
    erorr_list.append("password is contain common password")
    
    print(f"Password Sterength: {score}/{PASWORD_STERENGTH}")
    
    if score>=5 :
        print("Level: Strong")
    elif 3<=score<5:
        print("Level: Normal")
    else:
        print("Level: weak")
    
    print("Faild Checks")
    print(erorr_list)
        
    

 