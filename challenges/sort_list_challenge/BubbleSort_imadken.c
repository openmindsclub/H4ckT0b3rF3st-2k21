//Bubble sort in C


#include <stdio.h>
#include <stdlib.h>
#include<time.h>

//swap two adjacent elements
void permuter(int *x ,int *y)
{
    int temp;

    temp = *x;
    *x = *y;
    *y = temp;
}

// A function to implement bubble sort
void Bubble_Sort(int T[], int n){



   for (int i = 0; i <= n-2; i++)


       for (int j = 0; j < n-i-1; j++){

           if (T[j] > T[j+1]) {

                permuter(&T[j], &T[j+1]);
               }


            }

}


void Afficher_Tableau(int T[], int n)
{
    int i;

    printf("\n Affichage du Tableau : \n");

    for (i=0; i < n; i++) printf(" %d ", T[i]);


}


int main()// the main is just for testing  procedures
{
    int *T;

    int n ;

    printf("Donner le nombre d'elements du tableau :  ");

    scanf("%d",&n);

    getchar();

    printf("\n");

    T=(int*)malloc(n*(sizeof(int)));


    srand(time(0));

    for (int i=0;i<n;i++) T[i]=rand();

    Afficher_Tableau(T, n);


    Bubble_Sort(T, n);

    printf("\n Tableau triee \n\n");

    Afficher_Tableau(T, n);


    getchar();



    return 0;
}
