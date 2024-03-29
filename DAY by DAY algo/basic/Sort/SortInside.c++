#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
    int num_str;
    vector<int> vec;
    cin >> num_str;
    int i = num_str, index = 0;
    while (i > 0){
        vec.push_back(i%10);
        i /= 10;
        index++;
    }
    sort(vec.begin(), vec.end());
    for (int i = index - 1; i >=0; i--){
        cout << vec[i];
    }
}