#include <iostream>
#include <algorithm>

int size, value;
int arr[101][100001];
int N[101];
int K[101];

int main() {
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(0);

    std::cin >> size >> value;

    for (int i = 1; i <= size; i++) {
        std::cin >> N[i] >> K[i];
    }


    for (int i = 1; i <= size; i++) {
        for (int j = 1; j <= value; j++) {
            if (j >= N[i])
                arr[i][j] = std::max(arr[i - 1][j], arr[i - 1][j - N[i]] + K[i]);
            else
                arr[i][j] = arr[i - 1][j];
        }
    }
    std::cout << arr[size][value] << "\n";
}