print("Prime program")
num_div = 1
count = 2

number =    int(input( "Enter a number to validate: " ))

while( count <= number  ):
        
        if( number %  count == 0 ):
                
                # print(count)
                num_div += 1
                # print("div:",  count,"num_div: ", num_div)
        count +=1
        
if(num_div>2):
        print("it is not a prime")
else:
        print("it is a prime")




