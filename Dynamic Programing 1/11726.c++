#include <iostream>
using namespace std;


int fibonaci(int i)
{
    int number;
    if (i < 1 || i == 0)
        return 0;
    if (i == 1)
        return 1;
    return (fibonaci(i - 1) + fibonaci(i - 2));
}

int main()
{
    int width, count;
    cin >> width;
    count = fibonaci(width + 1);
    cout << count;
}