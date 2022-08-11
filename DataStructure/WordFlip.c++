#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int main(){
    int num;
    vector<string> Vst;
    cin >> num;
    for (int i = 0; i < num; i++){
        string st;
        cin >> st;
        Vst.push_back(st);
    }
}