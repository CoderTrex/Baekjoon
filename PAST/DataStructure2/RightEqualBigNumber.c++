#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;


int main(){
    ios::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
    vector<int> vec_input, vec_count;
    int cnt;
    cin >> cnt;
    for (int i = 0; i < cnt; i++){
        int num;
        cin >> num;
        vec_input.push_back(num);
    }
    for (int i = 0; i < cnt; i++){
        int num_input = vec_input[i];
        int num = count(vec_input.begin(), vec_input.end(), num_input);
        vec_count.push_back(num);
    }

    for (int i = 0; i < cnt - 1; i++){
        int count = 0;
        for (int j = i + 1; j < cnt; j++){
            if (vec_count[j] > vec_count[i]){
                count++;
            }
        }
        if (count == 0)
            cout << -1 << " ";
        else
            cout << count << " ";
    }
    cout << -1;
}