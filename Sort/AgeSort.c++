#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;


bool compare(pair<int, string> a, pair<int, string> b){
    return a.first < b.first;
}

int main(){
    vector<pair<int, string>> vec_sort; 
    int num;
    cin >> num;
    for (int i = 0; i < num; i++){
        int age;
        string name; 
        cin >> age >> name;
        vec_sort.push_back(make_pair(age, name));
    }
    stable_sort(vec_sort.begin(), vec_sort.end(), compare);
    for (int i = 0; i < num; i++){
        cout << vec_sort[i].first << " " << vec_sort[i].second << "\n";
    }
}