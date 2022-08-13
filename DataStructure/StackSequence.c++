#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    vector<int> vec;
    vector<char> result;
    int cnt = 1;
    int num;
    cin >> num;

    for (int i = 0; i < num; i++){
        int x;
        cin >> x;
        while (cnt <= x){
            vec.push_back(cnt);
            cnt++;
            result.push_back('+');
        }
        if (vec.back() == x){
            vec.pop_back();
            result.push_back('-');
        }
        else{
            cout << "NO";
            return (0);
        }
    }

    for (int i = 0; i < result.size(); i++){
        cout << result[i] << "\n";
    }
}