#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int width, height;
    cin >> width >> height;
    char **arr;
    arr = (char **)malloc(sizeof(char *) * height);
    for (int i=0; i < height; i++){
        arr[i] = (char *)malloc(sizeof(char) *width);
    }
    for (int i = 0; i < height; i++){
        for (int j = 0; j < width; j++){
            char num;
            cin >> num;
            arr[i][j] = num;
        }
    }
    for (int i = 0; i < height; i++){
        for (int j = 0; j < width; j++){
            cout << arr[i][j] << " ";
        }
        cout << "\n";
    }
}