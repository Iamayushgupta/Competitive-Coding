n=int(input())

def check_beautiful(input_number):
    default_list = [8,9]

    while True:
        
        temp = []
        for i in default_list:

            if (input_number %i) == 0:
                return "beautiful"
            
            temp.append(int('8')+str(i))
            temp.append(int('9')+str(i))


        default_list = temp    
        
        if (i > input_number):
            break

    return -1

print(check_beautiful(n))