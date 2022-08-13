#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	int case_num;
	cin >> case_num;
	string str;
	vector<char> st_v;
	cin.ignore();
	while (case_num--) {
		getline(cin, str);
		str += ' ';
		for (int i = 0; i < str.size(); i++) {
			if (str[i] == ' ') {
				while (!st_v.empty()) {
					cout << st_v.back();
					st_v.pop_back();
				}cout << ' ';
			}
			else{
				st_v.push_back(str[i]);
			}
		}cout << "\n";
	}
	return 0;
}