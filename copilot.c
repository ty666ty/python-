#include <stdio.h>

 void InsertionSort(int *array, int size)
 {
     int i, j, temp;
     for (i = 1; i < size; i++)
     {
         temp = array[i];
         for (j = i - 1; j >= 0 && array[j] > temp; j--)
         {
             array[j + 1] = array[j];
         }
         array[j + 1] = temp;
     }
 }

 typedef struct
 {
     int *array;
     struct copilot_task *next;
    
     ;
 } Array;

 //冒泡排序
void BubbleSort(int *array, int size)
{
    int i, j, temp;
    for (i = 0; i < size; i++)
    {
        for (j = 0; j < size - 1 - i; j++)
        {
            if (array[j] > array[j + 1])
            {
                temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;
            }
        }
    }
}

//两数之和
void sum2(int *array, int size)
{
    int i, j, temp;
    for (i = 0; i < size; i++)
    {
        for (j = i + 1; j < size; j++)
        {
            if (array[i] + array[j] == 0)
            {
                printf("%d %d\n", array[i], array[j]);
            }
        }
    }
}
//三数之和
void sum3(int *array, int size)
{
    int i, j, k, temp;
    for (i = 0; i < size; i++)
    {
        for (j = i + 1; j < size; j++)
        {
            for (k = j + 1; k < size; k++)
            {
                if (array[i] + array[j] + array[k] == 0)
                {
                    printf("%d %d %d\n", array[i], array[j], array[k]);
                }
            }
        }
    }
}

int main()
{   
  
   
    


}