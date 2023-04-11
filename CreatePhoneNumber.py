def create_phone_number(n):
    #your code here
    phone_num = '('
    for index in range(0,3):
        phone_num+=str(n[index])
    phone_num += ') '
    for index in range(3,6):
        phone_num+=str(n[index])
    phone_num += '-'
    for index in range(6,10):
        phone_num+=str(n[index])
    return phone_num