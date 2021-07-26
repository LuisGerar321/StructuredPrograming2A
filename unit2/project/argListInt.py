from sys import argv


print( argv )

# input  = []

# for i in range(1, len(argv)):
#         input.append(  int( argv[i]  ) )
# print(input)

listNumber  = [ int( argv[i])  for i in range( 1, len(argv) ) ] 



print(listNumber)

print( sum(listNumber))