#include <iostream>
using namespace std;

int main(){
    int cnt, result, tmp, num;
	cin >> cnt;
	result = 0; 
	num = 0;
	while (num != cnt){
		result++;
		tmp = result;
		while (tmp != 0){
			if (tmp % 1000 == 666){
				num++;
				break;
			}
			else tmp /= 10;
		}
	}
	cout << result;
}