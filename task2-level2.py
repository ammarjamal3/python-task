def get_name(names):
    
    normal_list=[]
    for word in names:
       if 'a'in word: 
             normal_list.append(word)
    list_comprehension=[word for word in names if 'a'in word]         
    print(normal_list)
    print(list_comprehension)

def fuctional_program_get_name(list):
    for word in list:
        if 'a'in word:
             return(word)


names=['mahmoud', 'farida', 'ali','hassan' , 'mohamed' , 'khaled' , 'taha']
get_name(names); 
func_upper=filter(fuctional_program_get_name,names)
print(list(func_upper))
