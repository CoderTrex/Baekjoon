#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int trial;
    cin >> trial;

    vector<int> weight, height;
    for (int i = 0; i < trial; i++){
        int num_1, num_2;
        cin >> num_1 >> num_2;
        weight.push_back(num_1);
        height.push_back(num_2);
    }

    vector<int> rank_w, rank_h;
    for (int i = 0; i < trial; i++){
        int cnt_w = 0, cnt_h = 0;
        for (int j = 0; j < trial; j++){
            if (weight[i] < weight[j])
                cnt_w++;
            if (height[i] < height[j])
                cnt_h++;
        }
        rank_w.push_back(cnt_w);
        rank_h.push_back(cnt_h);
    }

    vector<int> rank_total, rank_cout;
    for(int i = 0; i < trial; i++){
        rank_total.push_back(rank_w[i] + rank_h[i]);
        rank_cout.insert(rank_cout.begin() + i, 1);
    }
    for (int i = 0; i < trial; i++){
        for (int j = 0; j < trial; j++){
            if (rank_total[i] > rank_total[j]){
                rank_cout[i]++;
            }
        }
    }
    for (int i = 0; i < trial; i++){
        cout << rank_cout[i] << " ";
    }
    cout << "\n";
}