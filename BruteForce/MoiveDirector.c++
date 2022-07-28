#include <iostream>
#include <vector>
using namespace std;

int  main(){
    int num, result = 0;
    cin >> num;

    // 만의 자리 처리
    int num_cp = num;
    while ((num_cp -= 280) > 280){
        result += 100000;
    }


    // 천의 자리 처리
    int cnt_th = 0;
    while ((num_cp -= 19) > 19 || cnt_th < 6){
        result += 10000;
        cnt_th++;
    }
    if ((num_cp - 100) > 0){
        num_cp -= 100;
        result += 10000;
    }
    else{
        // 출력;
    }
    while ((num_cp -= 19) > 19){
        result += 10000;
    }

    // 백의 자리 처리
    int cnt_hd = 0;
    while ((num_cp -=  6) > 6 || cnt_hd < 6){
        
    }
}