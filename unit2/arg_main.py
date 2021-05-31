import sys

##Variables Globales##
my_int = 0 
my_str =  ""
my_float =  0.0
my_bool = True ##False
my_list = [] ## list() 


if __name__ == "__main__":
        
        my_int = int(  sys.argv[1]   )
        my_str =  str(  sys.argv[2]  )
        my_bool = bool( sys.argv[3]  )
        my_list = sys.argv

        print(   my_int * 2     , my_str*2, my_float, my_bool, my_list  )
        


