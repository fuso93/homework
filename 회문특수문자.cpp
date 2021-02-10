#include <stdio.h>

int checkPalindrome(char * head, char * tail) {
    while (head < tail) {
        if (*head == ' ' || *tail == ' ') {
            head += (*head == ' ');
            tail += (*tail == ' ');
        }
        if (*head <'A'||(*head >'Z'&&*head<'a')||*tail <'A'||(*tail >'Z'&&*tail<'a')){
        	head++;
        	tail++;
		}
        else {
        	
            int check = *head - *tail;
            if (check != 32 && check != -32 && check != 0 ) return 0;
             
        }
        head++; tail--;
        
    }
    
    return 1;
}

int strlen(char * c) {
    int len = 0;
    for (; *c; c++) len++;
    return len;
}

int main(void) {
    char word[100];
    gets(word);
    if (checkPalindrome(word, word + strlen(word) - 1)) printf("[%s] is palindrome\n", word);
    else printf("[%s] is not palindrome\n", word);
    return 0;
}


