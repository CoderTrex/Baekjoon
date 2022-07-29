#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

// 산술 중앙 최빈 범위
int main(){
    double result = 0;
    int size, *arr;
    cin >> size;
    arr = (int *)malloc(sizeof(int) * size);

    for (int i = 0; i < size; i++){
        int num;
        cin >> num;
        arr[i] = num;
        result += num;
    }
    result = floor(result /size + 0.5);
    sort(arr, arr + size);

    int cur_fre = 0, high_fre = 1, data_most = arr[0];
    vector<int> most_fre;
    if (size > 1){
        for (int i = 1; i <= size; i++){
            cur_fre++;
            if (i == size || arr[i] != arr[i + 1]){
                if (cur_fre >= high_fre){
                    high_fre = cur_fre;
                    data_most = arr[i];
                    most_fre.push_back(arr[i]);
                }
                cur_fre = 0;
            }
        }
        if (most_fre.size() > 1){
            sort(most_fre.begin(), most_fre.end());
            data_most = most_fre[1];
        }
    }

    // 산술 평균
    cout << result << "\n";
    // 중앙 값
    cout << arr[size / 2] << "\n";
    // 최빈값
    cout << data_most << "\n";
    // 범위
    cout << arr[size - 1] - arr[0] << "\n";
}
