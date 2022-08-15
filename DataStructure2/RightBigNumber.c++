#include <iostream>
#include <stdlib.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
    int *vec;
    int cnt;
    cin >> cnt;
    vec = (int * )malloc(sizeof(int) * cnt);
    for (int i = 0; i < cnt; i++){
        int num;
        cin >> num;
        vec[i] = num;
    }

    for (int i = 0; i < cnt - 1; i++){
        int big = -1;
        for (int j = i + 1; j < cnt; j++){
            if (vec[i] < vec[j]){
                big = vec[j];
                break;
            }
        }
        cout << big << " ";
    }
    cout << -1;
}