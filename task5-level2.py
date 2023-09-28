def get_length_word(names):
    
    normal_list=[]
    for word in names: 
             normal_list.append(len(word))
    list_comprehension=[len(word) for word in names]  
    print(normal_list)
    print(list_comprehension)

def fuctional_program_get_name(names):
          return(len(names))
      

names=['mahmoud', 'farida', 'ali','hassan' , 'mohamed' , 'khaled' , 'taha']
get_length_word(names); 
func_upper=map(fuctional_program_get_name,names)
print(list(func_upper))