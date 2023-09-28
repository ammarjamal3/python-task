def get_string_contain2(names):
    
    normal_list=[]
    for word in names:
        if len(word) > 1: 
             normal_list.append(word)
    list_comprehension=[word for word in names if len(word)>1]  
    print(normal_list)
    print(list_comprehension)

def fuctional_program_get_name(names):
   
        if len(names) > 1:
          return(names)
      

names=['mahmoud', 'farida', 'ali','hassan' , 'mohamed' , 'khaled' , 'taha','a']
get_string_contain2(names); 
func_upper=filter(fuctional_program_get_name,names)
print(list(func_upper))
