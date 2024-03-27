#include <iostream> 
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    vector<char> cv;
    string st;
    cin >> st;
    for (int i = 0; i < st.size(); i++){
        cv.push_back(st[i]);
    }

    int cnt, cursor = cv.size();
    cin >> cnt;
    for (int i = 0; i < cnt; i++){
        char c;
        cin >> c;
        if (c == 'L'){
            if (cursor > 0){
                cursor--;
            }
        }
        else if (c == 'D'){
            if (cursor < cv.size()){
                cursor++;
            }
        }
        else if (c == 'B'){
            if (cursor <= cv.size() && cursor != 0){
                cv.erase(cv.begin() + cursor - 1);
                cursor--;
            }
        }
        else if (c == 'P'){
            char in;
            cin >> in;
            cv.insert(cv.begin() + cursor, in);
            cursor++;
        }
    }
    
    for (int i = 0; i < cv.size(); i++){
        cout << cv[i];
    }
}