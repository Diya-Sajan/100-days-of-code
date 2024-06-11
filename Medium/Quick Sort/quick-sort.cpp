//{ Driver Code Starts
#include <stdio.h>
#include <bits/stdc++.h>
using namespace std;

/* Function to print an array */
void printArray(int arr[], int size)
{
    int i;
    for (i=0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

// } Driver Code Ends
class Solution
{
    public:
    //Function to sort an array using quick sort algorithm.
    void quickSort(int ar[], int low, int high){
        if(low<high){
            int pivInd = func(ar,low,high);
    
            quickSort(ar,low,pivInd-1);
            quickSort(ar,pivInd+1,high);
        }
    }
    
    public:
    int func(int ar[], int low, int high){
    int pivot = ar[low];
    int i=low;
    int j=high;
    while(i<j){
        while(ar[i]<=pivot && i<=high-1){
            i++;
        }
        while(ar[j]>pivot && j>=low+1){
            j--;
        }
        if(i<j){swap(ar[i],ar[j]);}
    }
    swap(ar[low],ar[j]);
    return j;
    }
};


//{ Driver Code Starts.
int main()
{
    int arr[1000],n,T,i;
    scanf("%d",&T);
    while(T--){
    scanf("%d",&n);
    for(i=0;i<n;i++)
      scanf("%d",&arr[i]);
      Solution ob;
    ob.quickSort(arr, 0, n-1);
    printArray(arr, n);
    }
    return 0;
}
// } Driver Code Ends