#include <iostream>
#include <queue>
using namespace std;

int main(){
    int size, range;
    queue<int> v;
    cin >> size >> range;
    for (int i = 1; i <= size; i++){
        v.push(i);
    }
    cout << "<";
    for (int i = 0; i < size; i++){
        for (int k = 0; k < range - 1; k++){
            int front = v.front();
            v.pop();
            v.push(front);
        }
        cout << v.front();
        v.pop();
        if (v.size() == 0){
            break;
        }
        cout << ", ";
    }
    cout << ">";
}