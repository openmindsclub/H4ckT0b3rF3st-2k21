#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<stdbool.h>


bool  isPrime(int x){

    if(x>=2){

    for (int i = 2;i <= sqrt(x);i++){

        if (x % i == 0) return false;

            }

    return true;
    }
}

unsigned long long  mil(int x){

   unsigned long long sum=2;

   for (int i=3;i<x;i+=2){

	   if (isPrime(i)) sum+=i;
   }

   return sum;


}




main(){

printf("%llu",mil(2000000));


}
