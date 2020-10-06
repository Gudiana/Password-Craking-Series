char_arr = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x",
"y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W",
"X","Y","Z","á","é","ú","ó","Á","É","Ú","Ó","ç","Ç","1","2","3","4","5","6","7","8","9","0",".","+",
"*","-","/","<",">",",",";",":","-","_","º","ª","~","^","´","`","'","?","«","»","=",")","(","&","%",
"$","#","\"","!","\\","|","@","£","§","{","[","]"," ","}"];
def split(password):
    return [char for char in password]

def check_if_exist_on_list(list,num):
    if num >= len(list) and num < 0:
        return False
    else:
        return True
def create_new_password(length):
    new_password = ""
    for i in range(length):
        new_password += char_arr[0]
    return new_password

def find_number_on_char_arr(char):
    for i in range(len(char_arr)):
        if char_arr[i] == char:
            return i

def translate_number_list_to_char_list(newPassword_number_list):
    newPassword_char_list = []
    for i in range(len(newPassword_number_list)):
        assossiated_char = char_arr[newPassword_number_list[i]]
        newPassword_char_list.append(assossiated_char);

    return newPassword_char_list


def create_new_password_number_list(newPassword_char_list):
    newPassword_number_list =  [];
    for newPassword_char in newPassword_char_list:
        newPassword_number_list.append(find_number_on_char_arr(newPassword_char))
    return newPassword_number_list

def create_new_password_char_list(newPassword):
    return split(newPassword)




def password_crack(truePassword):
    true_password_length = len(truePassword);
    new_password = create_new_password(true_password_length);
    new_password_char_list = create_new_password_char_list(new_password);
    new_password_number_list = create_new_password_number_list(new_password_char_list)
    continue_password_craking = True
    while continue_password_craking:
        if new_password_number_list[len(new_password_number_list)-1] == 113:
            new_password_number_list[len(new_password_number_list)-1] = 0
            if check_if_exist_on_list(new_password_number_list,len(new_password_number_list)-2):
                new_password_number_list[len(new_password_number_list)-2] += 1
            else:
                print("End")
                exit()
        for i in range(len(new_password_number_list)-1):
            if new_password_number_list[i] == 113:
                if i != 0 and len(new_password_number_list) > 1:
                    new_password_number_list[i] = 0
                    new_password_number_list[i-1] += 1
                else:
                    print("End")
                    continue_password_craking = False

        if continue_password_craking:
            new_password_char_arr_try = translate_number_list_to_char_list(new_password_number_list)
            new_password_string_try = ''.join(new_password_char_arr_try)
            if new_password_string_try == truePassword:
                print("Your password is " + new_password_string_try)
                continue_password_craking = False
            else:
                print(new_password_string_try)
                new_password_number_list[len(new_password_number_list)-1] += 1








true_password = input("Enter your password: ");
if len(true_password) > 1:
    password_crack(true_password);
else:
    print("Not a valid password");
