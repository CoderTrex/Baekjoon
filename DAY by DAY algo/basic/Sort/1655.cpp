#include <iostream>
#include <queue>
#include <algorithm>

int main() {
    std::ios_base::sync_with_stdio(0);
	std::cin.tie(0);
    // <자료형, 구현체, 비교연산자>
    std::priority_queue<int, std::vector<int>, std::less<int>> maxheap;
    std::priority_queue<int, std::vector<int>, std::greater<int>> minheap;

    int size, num;
    std::cin >> size;


    for (int i = 0; i < size; i++) {
        std::cin >> num;
        if (maxheap.empty()) {
            maxheap.push(num);
        }
        else {
            if (maxheap.size() > minheap.size()) {
                minheap.push(num);
            }
            else {
                maxheap.push(num);
            }
            if (maxheap.top() > minheap.top()) {
                int maxValue = maxheap.top();
                int minValue = minheap.top();
                maxheap.pop();
                minheap.pop();
                maxheap.push(minValue);
                minheap.push(maxValue);
            }
        }
        std::cout << maxheap.top() << "\n";
    }
}