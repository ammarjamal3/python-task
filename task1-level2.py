def upper_case(x):
    
    normal_list=[]
    for x in names:
        normal_list.append(x.upper())
        list_comprehension=[x.upper() for x in names]
    print(normal_list)
    print(list_comprehension)

def fuctional_program_upper(y):
    return(y.upper())


names=['mahmoud', 'farida', 'ali','hassan' , 'mohamed' , 'khaled' , 'taha']
upper_case(names); 
func_upper=map(fuctional_program_upper,names)
print(list(func_upper))
