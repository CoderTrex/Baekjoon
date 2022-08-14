#include <algorithm>
#include <iostream>
#include <string>
#include <deque>
using namespace std;

int main(){
    int cnt;
    cin >> cnt;
    deque<int> d;
    for (int i = 0; i < cnt; i++){
        string st;
        int num;
        cin >> st;
        if (st == "push_front"){
            cin >> num;
            d.push_front(num);
        }
        else if (st == "push_back"){
            cin >> num;
            d.push_back(num);
        }
        else if (st == "pop_front"){
            if (d.size() != 0){
                cout << d.front() << "\n";
                d.pop_front();
            }
            else
                cout << -1 << "\n";
        }
        else if (st == "pop_back"){
            if (d.size() != 0){
                cout << d.back() << "\n";
                d.pop_back();
            }
            else
                cout << -1 << "\n";
        }
        else if (st == "size"){
            cout << d.size() << "\n";
        }
        else if (st == "empty"){
            if (d.size() == 0)
                cout << 1 << "\n";
            else
                cout << 0 << "\n";
        }
        else if (st == "front"){
            if (d.size() != 0)
                cout << d.front() << "\n";
            else
                cout << -1 << "\n";
        }
        else if (st == "back"){
            if (d.size() != 0)
                cout << d.back() << "\n";
            else
                cout << -1 << "\n";
        }
    }
}