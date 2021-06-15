import sys
#global
num1 = 9

def isPrime(   ):
        # def message(): ##Local
        #         print("It is fucntion")
        global num1
        num1 = 3
        def localFunction( ):
                print("This is a local function")
        # localFunction() ##Local
        # message() ## Local
        # message( "This is a function..."   )
        num_div = 1
        count = 2 ##dos cuentas
        if(num1 == 1):
                print("it is not a prime")
                exit()

        while( count <= num1  ):
                
                if( num1 %  count == 0 ):
                        num_div += 1
                count +=1
                
        if(num_div>2):
                
                return False
        else:
                return True

def message(    ): ##Global
        print( "GLobal var" )


def powTwoNumbers(  num1, num2    ):
        powNum1 =  pow( num1, 2  )
        powNum2   = pow( num2, 2  )
        return (   powNum1,  powNum2   )



if __name__ == "__main__":


        print(  f'num1: {num1} ')

        print(  isPrime(  )    )

        print(  f'num1: {num1} ')


        (x, y) = powTwoNumbers(  2, 3 )

        print (    f' x:  {x }  , y: {y}...  '  )












