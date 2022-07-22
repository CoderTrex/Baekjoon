#include <iostream>
#include <vector>
using namespace std;


int find_de(int num){
    int re = 0;
    int total;
    for (int t = num; t > 0; t--){
        total = 0;
        for (int i = t; i > 0; i/=10){
            total += (i % 10);
        }
        if (total + t == num)
            re = t;
    }
    return (re);
}

int main(){
    int num, num_try, i;
    cin >> num;
    i = find_de(num);
    cout << i;
}