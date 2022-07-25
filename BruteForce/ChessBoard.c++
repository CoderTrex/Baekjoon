#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int width, height;
    cin >> height >> width;
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
    int cnt = 0;

    for (int start_h = 0; start_h < height - 7; start_h++){
        for (int start_w = 0; start_w < width - 7; start_w++){

            for (int i = start_h; i < start_h + 8; i++){
                for (int j = start_w; j < start_w + 8; j++){
                    cout << arr[i][j];
                }
                cout <<  "\n";
            }
            cout << "----------------------";
            cout << "start: " << ++cnt;
            cout <<  "\n";
        }
    }
}