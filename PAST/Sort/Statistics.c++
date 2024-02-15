#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;


// 배열 사용
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



// // 백터 사용
// #include <iostream>
// #include <algorithm>
// #include <vector>
// #include <cmath>
// using namespace std;

// // 산술 중앙 최빈 범위
// int main(){
//     double result = 0;
//     int size, num;
//     vector<int> vec, vec_most;
//     cin >> size;
//     for (int i = 0; i < size; i++){
//         cin >> num;
//         result += num;
//         vec.push_back(num);
//     }
//     result = floor(result/size + 0.5);
//     // 산술 평균
//     cout << (int)result << "\n";
//     sort(vec.begin(), vec.end());
//     // 중앙 값
//     cout << vec[size / 2] << "\n";
//     // 최빈값
//     int cnt = 0, cnt_high = 1, cnt_mode;
//     if (size > 1){
//         for (int i = 1; i <= size; i++){
//             cnt++;
//             if (i == size || vec[i] != vec[i + 1]){
//                 if (cnt >= cnt_high){
//                     cnt_high = cnt;
//                     vec_most.push_back(vec[i]);
//                 }
//                 cnt = 0;
//             }
//         }
//         sort(vec_most.begin(), vec_most.end());
//         if (vec_most.size() > 1){
//             cout << vec_most[1] << "\n";
//         }else{
//             cout << vec_most[0] << "\n";
//         }
//     }else{
//         cnt_mode = vec[0];
//         cout << cnt_mode << "\n";
//     }
//     // 범위
//     cout << vec.back() - vec.front();
// }
