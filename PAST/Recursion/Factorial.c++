#include <iostream>
using namespace std;


int func_rec(int num)
{
    int result = 1;
    while (num > 0)
    {
        result *= num;
        num--;
    }
    return result;
}

int main()
{
    int num;
    cin >> num;
    int result = func_rec(num);
    cout << result;
}