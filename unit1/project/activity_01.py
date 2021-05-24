print("Prime program")
num_div = 1
count = 2

number =    int(input( "Enter a number to validate: " ))

if(number == 1):
        print("it is not a prime")
        exit()

while( count <= number  ):
        
        if( number %  count == 0 ):
                num_div += 1
        count +=1
        
if(num_div>2):
        
        print("it is not a prime")
else:
        print("it is a prime")




