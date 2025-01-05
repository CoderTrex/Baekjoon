#include <iostream>
#include <algorithm>
#include <deque>

int main( ) {
    int N, temp = 0;
    std::cin >> N;
    std::deque<int> card;

    for (int i = 1; i <= N; i++) {
        card.push_back(i);
    }

    while (card.size() > 1) {
        card.pop_front();
        temp = card.front();
        card.pop_front();
        card.push_back(temp);
    }

    std::cout << card.front();
}