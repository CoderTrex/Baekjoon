#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main(){
    int cnt, num;
    string st;
    vector<int> vec;
    cin >> cnt;
    for (int i = 0; i < cnt; i++){
        cin >> st;
        if (st == "push"){
            cin >> num;
            vec.push_back(num);
        }
        else if (st == "pop"){
            if (vec.size() == 0){
                cout << -1 << "\n";
            }
            else{
                cout << vec.back() << "\n";
                vec.pop_back();
            }
        }
        else if (st == "size"){
            cout << vec.size() << "\n";
        }
        else if (st == "empty"){
            if (vec.size() == 0){
                cout << 1 << "\n";
            }
            else{
                cout << 0 << "\n";
            }
        }
        else if (st == "top"){
            if (vec.size() == 0)
                cout << -1 << "\n";
            else{
                cout << vec[vec.size() - 1] << "\n";
            }
        }
    }
}