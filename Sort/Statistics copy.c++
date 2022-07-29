#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

// 산술 중앙 최빈 범위
int main(){
    double result = 0;
    int size, num;
    vector<int> vec, vec_most;
    cin >> size;
    for (int i = 0; i < size; i++){
        cin >> num;
        result += num;
        vec.push_back(num);
    }
    result = floor(result/size + 0.5);
    // 산술 평균
    cout << (int)result << "\n";
    sort(vec.begin(), vec.end());
    // 중앙 값
    cout << vec[size / 2] << "\n";
    // 최빈값
    int cnt = 0, cnt_high = 1, cnt_mode;
    if (size > 1){
        for (int i = 1; i <= size; i++){
            cnt++;
            if (i == size || vec[i] != vec[i + 1]){
                if (cnt >= cnt_high){
                    cnt_high = cnt;
                    vec_most.push_back(vec[i]);
                }
                cnt = 0;
            }
        }
        sort(vec_most.begin(), vec_most.end());
        if (vec_most.size() > 1){
            cout << vec_most[1] << "\n";
        }else{
            cout << vec_most[0] << "\n";
        }
    }else{
        cnt_mode = vec[0];
        cout << cnt_mode << "\n";
    }
    // 범위
    cout << vec.back() - vec.front();
}
