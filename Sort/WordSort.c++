#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

bool compare(string a, string b){
    if (a.size() == b.size()){
        for (int i = 0; i < a.size(); i++){
            if (a[i] != b[i])
                return a[i] < b[i];
        }
    }
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
    cout << vec_str[0] << "\n";
    for (int i = 1; i < cnt; i++){
        if (vec_str[i - 1] == vec_str[i])
            continue;
        cout << vec_str[i] << "\n";
    }
}