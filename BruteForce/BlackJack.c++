#include <iostream>
#include <vector>
using namespace std;


int main()
{
    int try_num, total, num, cnt = 0;
    cin >> try_num >> total;
    vector<int> box, sum;

    for (int i = 0; i < try_num; i++){
        cin >> num;
        box.push_back(num);
    }

    for (int i = 0; i < try_num - 2; i++){
        for (int j = i + 1; j < try_num - 1; j++){
            for (int k = j + 1; k < try_num; k++){
                sum.push_back(box[i] + box[j] + box[k]);
                cnt++;
            }
        }
    }

    int target = 0;
    for (int i = 0; i < cnt; i++){
        if (sum[i] <= total){
            if (target < sum[i])
                target = sum[i];
        }
    }
    cout << target;
}