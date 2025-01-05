#include <iostream>
#include <vector>


int main() {
    int H, W, X, Y;
    std::cin >> H >> W >> X >> Y;
    
    std::vector<std::vector<int>> changed_vec(H + X, std::vector<int>(W + Y));
    std::vector<std::vector<int>> origin_vec(H, std::vector<int>(W));

    for (int i = 0; i < H + X; i++) {
        for (int j = 0; j < W + Y; j++) {
            std::cin >> changed_vec[i][j];
        }
    }
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            origin_vec[i][j] = changed_vec[i][j];
        }
    }

    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            if (i + X < H && j + Y < W) {
                int x = changed_vec[i + X][j + Y] - origin_vec[i][j];
                origin_vec[i + X][j + Y] = x;
            }
        }
    }

    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            std::cout << origin_vec[i][j] << " ";
        }
        std::cout << std::endl;
    }
}