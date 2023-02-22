    #include <iostream>
    #include <algorithm>
    #include <vector>
    using namespace std;


    int arr[1000001];

    int func(int target)
    {
        arr[1] = 0;
        for (int i = 2; i <= target; i++)
        {   
            arr[i] = arr[i - 1] + 1;
            if (i % 2 == 0)
                arr[i] = min(arr[i], arr[i/2]+1);
            else if (i % 3 == 0)
                arr[i] = min(arr[i], arr[i/3]+1);
        }
        return (arr[target]);
    }

    int main()
    {
        int target, number = 0;

        cin >> target;
        number = func(target);
        cout << number;
    }