#include <iostream>
#include <algorithm>
using namespace std;


int main(){
    int *arr, size;;
    cin >> size;;
    arr = (int *)malloc(sizeof(int) * size);
    for (int i = 0; i < size; i++){
        int num;
        cin >> num;
        arr[i] = num;
    }
    sort(arr, arr + size);
    for (int i = 0; i < size; i++){
        cout << arr[i] << "\n";
    }
}