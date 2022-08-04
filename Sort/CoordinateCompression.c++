#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    vector<pair<int, int>> vec;
    int num_try, ele;
    cin >> num_try;
    for (int i = 0; i < num_try; i++){
        cin >> ele;
        vec.push_back({ele, i});
    }
    sort(vec.begin(), vec.end());
    vec.push_back({vec[0].second, 0});
    
}