import random
def gen_password():    
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" 
    count_user = int(input('укажите количество символов в пароле: '))
    new_password = '' 
    for i in range(count_user): 
        new_password += random.choice(letters)
    print("Сгенерированный пароль:", new_password)
