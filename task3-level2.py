def get_name_start(names):
    
    normal_list=[]
    for word in names:
        letter1,*letter_rest=word 
        if letter1=='a':
             normal_list.append(word)
             list_comprehension=[word]         
    print(normal_list)
    print(list_comprehension)

def fuctional_program_get_name(names):
       letter1,*letter_rest=names
       if letter1=='a':
          return(names)
      

names=['mahmoud', 'farida', 'ali','hassan' , 'mohamed' , 'khaled' , 'taha']
get_name_start(names); 
func_upper=filter(fuctional_program_get_name,names)
print(list(func_upper))
