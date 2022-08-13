#include <iostream> 
#include <vector>
#include <string>
#include <algorithm>
using namespace std;



// L : 커서를 왼쪽으로 한 칸 옮김
// D : 커서를 오른쪽으로 한 칸 옮김
// B : 커서 왼쪽에 있는 문자를 삭제함
// P $ : 뒤에 적은 $라는 문자를 왼쪽에 추가함.

int main(){
    vector<char> cv;
    cin >> cv;
    int cnt, cursor = cv.size();
    cin >> cnt;
    for (int i = 0; i < cnt; i++){
        char c;
        cin >> c;
        if (c == 'L'){
            if (cursor > 1){
                cursor--;
            }
        }
        else if (c == 'D'){
            if (cursor < st.size()){
                cursor++;
            }
        }
        else if (c == 'B'){
            if (cursor < st.size()){
                
            }
        }
        else if (c == 'P'){}
    }
}