def change_between_c_and_f():
    while(True):

         print(''' press 1 for convert from C to F
         pres 2 for convert from F to C''')
         convert_input=int(input())

         if  convert_input == 1:
             c_temp=int(input('enter c temp'))
             temp_f=(c_temp*1.8)+32
             print(f'temp in f is : {temp_f}')

         elif convert_input == 2:
              f_temp=int(input('enter c temp'))
              temp_c=(f_temp-32)*1.8
              print(f'temp in C is : {temp_c}')
     
         else : print('please enter 1 or 2')

         x =input('press any key for continue  , press n for exit')
         if x =='n':
              break


change_between_c_and_f()