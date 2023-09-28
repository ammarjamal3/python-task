def changecurrency():
    while(True):

         print(''' press 1 for convert from IQ Dinar to Dollar
         pres 2 for convert from IQ Dinar to euro''')
         convert_input=int(input())
         dinnar=int(input('enter Dinnar '))
         if  convert_input == 1:
             dollar=dinnar / 1500
             print(f'dollar is : {dollar}')

         elif convert_input == 2:
              euro=dinnar/1800
              print(f'euro is : {euro}')
     
         else : print('please enter 1 or 2')

         x =input('press any key for continue  , press n for exit')
         if x =='n':
              break


changecurrency()