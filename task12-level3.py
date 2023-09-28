def email():
    while(True):
         email=input('enter email')
         if email.__contains__('@'):
            list=email.split('@')
            print(f'user name is : {list[0]}')
            print(f'domain is {list[1]}')
         else : print('enter valid email')
         x =input('press any key for continue  , press n for exit')
         if x =='n':
            break
       

email()