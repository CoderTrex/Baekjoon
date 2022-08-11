#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main () {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, temp; 
    cin >> n;
    vector<int> v, cv;
    vector<int>::iterator iter;

    for(int i = 0; i < n; i++) {
        cin >> temp;
        v.push_back(temp);
        cv.push_back(temp);
    }
    sort(cv.begin(), cv.end());
    cv.erase(unique(cv.begin(), cv.end()), cv.end());
    for(iter = v.begin(); iter != v.end(); iter++) {
        cout << lower_bound(cv.begin(), cv.end(), *iter) - cv.begin() << ' '; 
    }
}