#include <iostream>
#include <queue>
#include <string>
using namespace std;

// push x: x를 넣는다
// pop : 가장 앞에 있는 정수 빼고 출력 / 없으면 -1
// size : 갯수
// empty : 큐가 비어있으면 1 아니면 0
// front : 맨앞의 정수 출력 / 없으면 -1
// back : 맨뒤의 정수 출력 / 없으면 -1

int main(){
    cin.tie(NULL);
	ios::sync_with_stdio(false);
    int cnt;
    queue<int> que;
    cin >> cnt;
    for (int i = 0; i < cnt; i++){
        string st;
        cin >> st;
        if (st == "push"){
            int num;
            cin >> num;
            que.push(num);
        }
        else if (st == "pop"){
            if (que.size() != 0){
                cout << que.front() << "\n";
                que.pop();
            }
            else
                cout << -1 << "\n";
        }
        else if (st == "size"){
            cout << que.size() << "\n";
        }
        else if (st == "empty"){
            if (que.size() == 0){
                cout << 1 << "\n";
            }
            else{
                cout << 0 << "\n";
            }
        }
        else if (st == "front"){
            if (que.size() != 0){
                cout << que.front() << "\n";
            }
            else
                cout << -1 << "\n";
        }
        else if (st == "back"){
            if (que.size() != 0){
                cout << que.back() << "\n";
            }
            else
                cout << -1 << "\n";
        }
    }
}