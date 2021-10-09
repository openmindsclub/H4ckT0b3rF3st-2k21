#include <stdio.h>
#include <stdlib.h>
#include <string.h>



/************************************************* Functions and procedures  ***************************************************/


/***************************************************************************************/
/*********** 1. The function that returns the length of a string  **********************/
int longueur(char string[])
{
    int length=0,i;

 for(i = 0; string[i] != '\0'; i++)
  {
      length++;
  }
   return(length);

}
/***************************************************************************************/


/************* 2. Function that counts the number of words in a string  ********************/
int nombreMots(char string[])
{
    int cpt=1,i;



 for(i = 0; string[i] != '\0'; i++)
  {
    if(string[i] == ' ' || string[i] == '\t' || string[i] == '\n' )
    {
      cpt++;
    }
  }
   return(cpt);

}
/**************************************************************************************************/


/***************** 3. Count the number of numeric characters in the text  ***************************/
int nbrCharNum(char ch[])
{
    int i=0;
    int cpt=0;
    for(i = 0; ch[i] != '\0'; i++)
  {
    if(ch[i] == '0' || ch[i] == '1' || ch[i] == '2' || ch[i] == '3' || ch[i] == '4' || ch[i] == '5' || ch[i] == '6' || ch[i] == '7' || ch[i] == '8' || ch[i] == '9')
    {
      cpt++;
    }
  }
   return(cpt);


}

/**************************************************************************************************/
/****************** 4. Replace one character with another  **********************************/
void remplacerChar(char c , char cr, char ch[])
{

    int i, trouv=0;
    for(i = 0; ch[i] != '\0'; i++)
  {
    if(ch[i] == c)
    {
    	trouv=1;
      ch[i]=cr;
    }
  }
  if(trouv == 1)
  {

   printf("The new string is %s\n\n",ch);
}
else
{
      printf("Warning !! This character does not exist in the text  \n\n");
}


}
/*****************************************************************************************/

 /************************* 5. Existence of a word in a text  ********************************/
 int chercherMot(char ch[], char ch1[])
  {
    int trouve=0;
    int i=0;
    int j=0;
    for (i = 0; ch[i]!='\0'; i++)
  {
      if (ch[i]==ch1[j])
      {

         j++;

         if ((ch1[j]=='\0')&&((ch[i+1]==' ')||(ch[i+1]=='\0') ))
      {


        trouve=1;
        break;
      }
      }
      else
        {

        j=0;
      }
  }
  return (trouve);
  }
   /****************** 6. Replace a word with another word  *****************************/
   void remplaceMot (char ch[], char mot[], char chRemp[])
   {
       int trouve=0;
       int pos=0;
    int i=0;
    int j=0;
    int k,u,longDiff,L=0;
    int l=0;
    int L1=0;
    for (i = 0; ch[i]!='\0'; i++)
  {
      if (trouve==0)
      {


      if (ch[i]==mot[j] )
      {
         j++;

         if (mot[j]=='\0')
      {
        trouve=1;
        pos=i-1;
      }
      }
      else
        {
        j=0;
      }
      }
  }

  if (trouve==1)
  {


  k=pos-strlen(mot)+2;

  L=k+strlen(mot);
  L1=k+strlen(chRemp);


  if (strlen(mot) == strlen(chRemp))
  {


  for (k=pos-strlen(mot)+2; k<L; k++)
  {

      ch[k]=chRemp[l];
      l++;
  }
  }if (strlen(mot) < strlen(chRemp)){
       longDiff=strlen(chRemp)-strlen(mot);
       for (k=i+longDiff; k>pos+longDiff; k--)
  {
     ch[k]=ch[i];
     i--;

  }
  for (u=pos-strlen(mot)+2; u<L1; u++)
  {


      ch[u]=chRemp[l];
      l++;
  }

  }if (strlen(mot) > strlen(chRemp)){
       longDiff=strlen(mot)-strlen(chRemp);

       for (k=pos-strlen(mot)+2; k<L1; k++)
  {
     ch[k]=chRemp[l];
     l++;

  }

  for (u=L1; u<(i+longDiff-1); u++)
  {


      ch[u]=ch[u+longDiff];

  }
  }

     printf("The new string is : %s\n\n",ch);
  }else{
      printf("Warning  !! This word does not exist in the text  \n\n");
  }

   }
   /**********************************************************************************/
  /****************** 7. Check if a word is written in the form wwR  *********************/
  int wwRMot(char ch[])
  {
    int trouve=0;
    int i=0;
    int L=strlen(ch);
    int j=L/2;

     if (L==1){
     	trouve=1;
	 }
	 else{

    for (i = 0; i<j; i++)
    {

      if (ch[i]==ch[L-1])
      {
         L--;
         trouve=1;

      }
      else
        {

            trouve=0;
            break;
      }
  }
}
  return (trouve);
  }
  /*******************************************************************************************/
  /************************ 8. Know the longest word  ************************/
   char* motPlusLong(char ch[])
  {

    int i=0;
    int cpt=0;
    int max=0;
    char *c="";
    char c1[100]="";
    char const*pc = strtok(ch, " \n\t");

     while (pc != NULL)
    {


        for (i = 0; pc[i]!='\0'; i++)
        {
         cpt++;
        }

         if (cpt>max)
         {
            max=cpt;
            cpt=0;
            c=pc;

         }
         else
             {

            cpt=0;

         }
pc = strtok(NULL, " \n\t");
    }

return (c);
  }
/*******************************************************************************/
/************************ 9. construction of two vectors  ***************************/
void construvtionVect(char ch[])
{
    int T[200];

    char V[200]="";
    int i ,k,trouv=0;
    int j=0;

   for (i = 0; ch[i]!='\0'; i++)
  {
      trouv=0;

      if (i==0)
      {
          trouv=0;
      }
      else
      {
          k = j;
      for (k = k; k>0; k--)
      {

         if ((ch[i]==V[k-1]) && (trouv==0))
         {
            T[k-1]=T[k-1]+1;
            trouv=1;
         }
      }
      }
      if (trouv==0)
      {
            V[j]=ch[i];
            T[j]=1;
            j++;
       }

  }
  printf("the array T contains the characters of a text without repetition \n");
  for (k = 0; k<j; k++)
      {

        printf("%c|",V[k]);

      }
printf("\n");
      printf("the array V contains the number of occurrences of characters in a text  \n");
  for (k = 0; k<j; k++)
      {

        printf("%i|",T[k]);

      }
printf("\n");
}
/******************************************************************************/




/*********** Main function **************************/

int main()
{

    /*********** Variable declaration  **************************/
      int boolean,k,i,choice,pos, num,Lstring, nbWord,trouv,j=0;
      char string[300]="";
      char tab[300];
      char mot[100]="";
      char motRemp[100]="";
      char string1[300]="";
      char *c,c1,c2;


    /****************************************************************/
     /************** Reading and saving a character string  ****************/
     printf("Enter the string you want:  ");
     scanf("%[^\n]s",string);
      for(i = 0; string[i] != '\0'; i++)
      {

          printf("%c",string[i]);

      }


       printf("\n");
    /****************** The menu  ****************************/
    etiq1:
    printf ("\t ------------------- Menu -------------------- \n \n \n");

         printf ("1. The length of the string \n");
         printf ("2. Number of word in text \n");
         printf ("3. Number of numeric characters in the text \n");
         printf ("4. Replace one character with another \n");
         printf ("5. Word exists in text \n");
         printf ("6. Replacing a word with another word \n");
         printf ("7. Check if a word is written as wwR \n");
         printf ("8. Know the longest word \n");
         printf ("9. Construction of two vectors \n");


        printf ("Enter the number of the operation you want to perform:");
        scanf("%d",&choice);
        system("cls");
        switch(choice)
        {
            case 1:
                 printf("\t*****************************************************************\n");
                 printf("\t*\t\t 1- Length of a character string  \t\t*\n");
                 printf("\t***************************************************************** \n\n\n");

                 printf("Your string is: %s\n",string);
                 Lstring=longueur(string);
                 printf("The length of this string is, %d\n\n",Lstring);

                 printf("Do you want to go back to the menu, (1: yes, 0: no) ");
                 scanf("%d",&boolean);
                 if (boolean==1)
                 {
                      system("cls");
                      goto etiq1;
                 }
                 else
                 {
                      exit(0);
                 }

                  break;

            case 2:
                 printf("\t*****************************************************************\n");
                 printf("\t*\t\t 2- Number of words in a string  \t\t*\n");
                 printf("\t***************************************************************** \n\n\n");

                 printf("Your string is: %s\n",string);
                 nbWord=nombreMots(string);
                 printf("The total number of words in this string is  = %d\n", nbWord);

                 printf("Do you want to go back to the menu, (1: yes, 0: no) ");
                 scanf("%d",&boolean);
                 if (boolean==1)
                 {
                      system("cls");
                      goto etiq1;
                 }
                 else
                 {
                      exit(0);
                 }
                break;


            case 3:
                 printf("\t*****************************************************************\n");
                 printf("\t*\t\t 3- Number of numeric characters in a string  \t*\n");
                 printf("\t***************************************************************** \n\n\n");

                 printf("Your string is: %s \n",string);
                 num=nbrCharNum(string);
                 printf("the number of numeric characters is:  %i\n",num);

                 printf("Do you want to go back to the menu, (1: yes, 0: no) ");
                 scanf("%d",&boolean);
                 if (boolean==1)
                 {
                      system("cls");
                      goto etiq1;
                 }else{
                      exit(0);
                 }

                break;
            case 4:
                 printf("\t*************************************************************************\n");
                 printf("\t*\t\t 4- Replace one character with another in a string  \t*\n");
                 printf("\t************************************************************************* \n\n\n");

                 printf("Your string is: %s\n",string);
                 printf("Enter the character to replace: ");
                 scanf(" %c",&c1);
                 printf("Enter the new character: ");
                 scanf(" %c",&c2);
                 remplacerChar(c1,c2,string);

                 printf("Do you want to go back to the menu, (1: yes, 0: no) ");
                 scanf("%d",&boolean);
                 if (boolean==1)
                 {
                      system("cls");
                      goto etiq1;
                 }else{
                      exit(0);
                 }

                 break;

            case 5:
                 printf("\t*****************************************************************\n");
                 printf("\t*\t\t 5- Search for a word in a string \t\t*\n");
                 printf("\t***************************************************************** \n\n\n");

                 printf("Your string is: %s\n",string);
                 printf("Enter the word to search for: ");
                 scanf(" %s",string1);

                 trouv=chercherMot(string,string1);
                  if(trouv==1)
                  {
                      printf("This word exists in the text \n");
                  }
                  else
                  {
                      printf("This word does not exist in the text \n");
                  }

                printf("Do you want to go back to the menu, (1: yes, 0: no) ");
                 scanf("%d",&boolean);
                 if (boolean==1)
                 {
                      system("cls");
                      goto etiq1;
                 }else{
                      exit(0);
                 }
                 break;

            case 6:
                 printf("\t*****************************************************************\n");
                 printf("\t*\t\t 6- Replace a word in a string  \t\t*\n");
                 printf("\t***************************************************************** \n\n\n");

                 printf("Your string is: %s\n",string);
                 printf("Enter the word you want to replace it:  ");
                 scanf(" %[^\n]s",&mot);
                 printf("Enter the replacement word:  ");
                 scanf(" %[^\n]s",&motRemp);
                 remplaceMot(string,mot,motRemp);

                 printf("Do you want to go back to the menu, (1: yes, 0: no) ");
                 scanf("%d",&boolean);
                 if (boolean==1)
                 {
                      system("cls");
                      goto etiq1;
                 }else{
                      exit(0);
                 }
                 break;

            case 7:
                 printf("\t*********************************************************************************\n");
                 printf("\t*\t\t 7- Check if a word is written in the form wwR  \t\t*\n");
                 printf("\t********************************************************************************* \n\n\n");

                 printf("Enter the string you want:  ");
                 scanf(" %[^\n]s",&tab);
                 trouv=wwRMot(tab);
                 if(trouv==1)
                  {
                      printf("This word is written in wwR form \n");
                  }
                  else
                  {
                      printf("This word is not written in the form wwR \n");
                  }

                 printf("Do you want to go back to the menu, (1: yes, 0: no) ");
                 scanf("%d",&boolean);
                 if (boolean==1)
                 {
                      system("cls");
                      goto etiq1;
                 }else{
                      exit(0);
                 }
                 break;

            case 8:
                 printf("\t*****************************************************************\n");
                 printf("\t*\t\t 8- the longest word in a string  \t\t*\n");
                 printf("\t***************************************************************** \n\n\n");

                 printf("Your string is: %s\n",string);
                 c=    motPlusLong(string);


                 printf("the longest word is : %s\n",c);


                 printf("Do you want to go back to the menu, (1: yes, 0: no) ");
                 scanf("%d",&boolean);
                if (boolean==1)
                 {
                      system("cls");
                      goto etiq1;
                 }else{
                      exit(0);
                 }

                 break;

            case 9:
                  printf ("\t ********************************************** ********************************************\n");
                  printf ("\t*\t\t 9- Construction of two vectors. \t\t\t\t\t*\n");
                  printf ("\t*\t\t The vector V contains the characters without repetition \t \t*\n");
                  printf ("\t*\t\t The vector T contains the occurrence of each character \t\t*\n");
                  printf ("\t ********************************************** ******************************************** \n\n\n ");

                 printf("Your string is:  %s\n",string);
                 construvtionVect(string);
                  printf("Do you want to go back to the menu, (1: yes, 0: no)");
                 scanf("%d",&boolean);
                if (boolean==1)
                 {
                      system("cls");
                      goto etiq1;
                 }else{
                      exit(0);
                 }
                  break;


            default:

               printf ("Warning !! Please choose a number between 1 and 9 \n \n");
               printf ("Do you want to return to the menu, (1: yes, 0: no)");
                 scanf("%d",&boolean);
                if (boolean==1)
                 {
                 	system("cls");
                      goto etiq1;
                 }else{
                      exit(0);
                 }
                 break;
                    // terminates the complete program execution
        }

    return 0;
}


