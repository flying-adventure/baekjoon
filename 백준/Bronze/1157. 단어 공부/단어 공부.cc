#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(void){
    char word[1000001];
    scanf("%s",word);//입력
    
    int alpha[26];
    for(int i=0; i<26;i++){
        alpha[i]=0;
    }
    int len = strlen(word);
    for(int j=0;j<len; j++){
        char cur = toupper(word[j]);
        alpha[cur-'A']++;
    }
    int max =0, num=0, max_alpha=0;
    for(int k=0;k<26;k++){
        if(alpha[k]>max){
            max=alpha[k];
            num=1;
            max_alpha='A'+k;
        }
        else if(max!=0 && alpha[k]==max){
            num++;
        }
        else{continue;}
    }
    if(num==1){
        printf("%c\n",max_alpha);
    }
    else{printf("?");}
}