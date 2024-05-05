#include <stdlib.h>
#include <string.h>
#include "concatenate.h"

char* concatenate_strings(const char* str1, const char* str2) {
    char * str3 = (char *) malloc(1 + strlen(str1)+ strlen(str2) );
    strcpy(str3, str1);
    strcat(str3, str2);
    return str3;
}
