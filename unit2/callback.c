#include <stdio.h>
#include <string.h>
#include <stdio.h>
#include "./folderTest/utils.h"
#include "stdbool.h"

void SecurityCameraA( void (*__) (int number),  int  EmergencyNumber );
void SecurityCameraB();

void callToNumber(int number){

        printf("Llamando al %d...!\n", number   );
}

int main(){
        //Some code to call functions
        return 0;
}

void SecurityCameraB(){

        //Logica Compleja//
        bool thief = false;
        if(thief){ //Si detecta ladron debe hacer algo!
                // Ejecutar un calback
                callToNumber(999);
        }
}
void SecurityCameraA( void (*__) (int number), int EmergencyNumber   ){
        //Logica Compleja//
        bool thief = false;
        if(thief){ //Si detecta ladron debe hacer algo!
                // Ejecutar un calback
                __(EmergencyNumber);
        }
}


