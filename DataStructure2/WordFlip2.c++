#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int main(){
	ios::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	vector<char> st_v;
	int i = 0;
    string st;
	getline(cin, st);
	
	for (int i = 0; i < st.size(); i++){
		st_v.push_back(st[i]);
	}
	
	vector<char> st_v_2;
	for (int i = 0; i <= st_v.size(); i++){
		if (st_v[i] == '<'){
			while (!st_v_2.empty()) {
					cout << st_v_2.back();
					st_v_2.pop_back();
			}
			while (st_v[i] != '>'){
				cout << st_v[i];
				i++;
			}
			cout << '>';
		}
		else{
			if (st_v[i] == ' ') {
				while (!st_v_2.empty()) {
					cout << st_v_2.back();
					st_v_2.pop_back();
				}cout << ' ';
			}
			else if (i == st_v.size()){
				while (!st_v_2.empty()) {
					cout << st_v_2.back();
					st_v_2.pop_back();
				}
			}
			else{
				st_v_2.push_back(st_v[i]);
			}
		}
	}
}