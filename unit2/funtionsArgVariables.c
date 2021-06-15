#include <stdio.h>
#include "/mnt/d/StructuredPrograming2A/unit2/folderTest/utils.h"
#include <stdlib.h>


int var1 = 10;
int var2  = 20;


int main ( int argc, char** argv){
        printf( "var1 =  %d, var2 =%d\n",  var1, var2 );
        printf("Funtion was executed:\n");
        //Paso de argumentos por direccion//
        modifyVariables(  var1, var2  );
        printf("var1=  %d, var2= %d\n",  var1, var2 );


        //Get the address of var1 and var2
        // & = "La direccion de" --> &x00879fb
        int * myptr1 =  &var1;
        int * myptr2 = &var2;

        ShowIntAdress( myptr1 );
        ShowIntAdress(myptr2);
        

        printf("Pointer has modificaded the var1:\n");
        // *myptr1  = "El valor de" --> &x00879fb = x;
        myptr1 = &var1; 
        *myptr1 = 20;
        // *0x7f49efa01014 = 20;
        var2 = 40;

       

        printf("///////////////////Pointers into functions /////\n");

        printf( "var1 =  %d, var2 =%d\n",  var1, var2 );
        printf("Funtion address was executed:\n");
        //Paso de argumentos por direccion
        modifyVariablesAddress(  &var1, &var2,  3 );
        //Decodificado humano: modifyVariablesAddress( 0x7ff150a01014 , 0x7ff150a01018);
        printf("var1=  %d, var2= %d\n",  var1, var2 );
        //Dentro del codigo debe ir algo asi:
                // *0x7ff150a01018 = 1000;

        return 0;
}