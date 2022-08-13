#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

int main(){
    int cnt;
    cin >> cnt;
    vector<string> result;
    for (int i = 0; i < cnt; i++){
        string st;
        int total = 0;
        cin >> st;
        for (int j = 0; j < st.size(); j++){
            if (st[j] == '('){
                total++;
            }
            else if (st[j] == ')'){
                total--;
            }
            if (total < 0){
                result.push_back("NO");
                break;
            }
            if ((j == st.size() - 1) && total == 0){
                result.push_back("YES");
            }
            else if ((j == st.size() - 1) && total != 0){
                result.push_back("NO");
            }
        }
    }

    for (int i = 0; i < result.size(); i++){
        cout << result[i] << "\n";
    }
}