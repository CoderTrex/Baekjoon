#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int size, *arr;
    cin >> size;
    arr = (int *)malloc(sizeof(int) * size);

    for (int i = 0; i < size; i++){
        int num;
        cin >> num;
        arr[i] = num;
    }

    for (int i = 0; i < size - 1; i++){
        for (int j = 0; j < size - i - 1; j++){
            if (arr[j] > arr[j+1]){
                swap(arr[j], arr[j+1]);
            }
        }
    }

    for (int i = 0; i<size; i++){
        cout << arr[i] << "\n";
    }
}