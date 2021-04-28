#include<stdio.h>
#include<stdlib.h>
void main(int argc, char* argv[])
{
	int inicio, final, i, j, bandera;
	inicio = atoi(argv[1]);
	final =atoi(argv[2]);
	
	for(i=inicio; i<=final; i++)
	{
		bandera=0;
		for(j=2; j<i/2; j++)
		{
			if(i%j==0)
			{
				bandera=1;
				break;
			}
		}	
	/*
	if (bandera==0)
	
		printf("%d ", i);*/
	}
	
}
