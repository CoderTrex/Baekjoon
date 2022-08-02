#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

bool compare(string a, string b){
    return a.size() < b.size();
}


int main(){
    int cnt;
    cin >> cnt;
    vector<string> vec_str;
    for (int i = 0; i < cnt; i++){
        string str;
        cin >> str;
        vec_str.push_back(str);
    }
    sort(vec_str.begin(), vec_str.end(), compare);
    for (int i = 0; i < cnt; i++){
        cout << vec_str[i] << "\n";
    }
}