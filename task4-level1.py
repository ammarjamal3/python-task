def no_duplicated(x):
    list=[]
   
    for _ in x:
      list=x.split(' ')
    newlist=[]
    for q in list:
        if q not in newlist:
          newlist.append(q)
    print(' '.join(list))    

x=input(' enter your sentence  ')

no_duplicated(x)