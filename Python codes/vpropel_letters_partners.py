word=input()
import string
pre_letters=list(string.ascii_lowercase[:13])
post_letters=list(string.ascii_lowercase[13:])

bool=True

temp_list = [] 
for i in list(word): 
    if i in pre_letters: 
        temp_list.append(i) 
    elif i in post_letters:
        pos = post_letters.index(i) 
        if ((len(temp_list) > 0) and
            (pre_letters[pos] == temp_list[len(temp_list)-1])): 
            temp_list.pop() 
        else: 
            print('Lost')
            bool=not bool
if bool:
    if len(temp_list) == 0: 
        print("Won")
    else: 
        print('Lost')
  






            
            

        
            



           
       