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
    int *arr_b = (int *)calloc((height - 7) * (width - 7), sizeof(int));
    int *arr_w = (int *)calloc((height - 7) * (width - 7), sizeof(int));

    for (int start_h = 0; start_h < height - 7; start_h++){
        for (int start_w = 0; start_w < width - 7; start_w++){
            for (int i = start_h; i < start_h + 8; i++){
                for (int j = start_w; j < start_w + 8; j++){
                    if (j % 2 == 1){
                        if (arr[i][j] == 'W')
                            arr_b[start_w + start_h]++;
                    }
                    else{    
                        if (arr[i][j] == 'W')
                            arr_w[start_w + start_h]++;
                    }
                }
            }
        }
    }
    for (int i = 0; i < (height - 7) * (width - 7); i++)
    {
        cout << "sample one: " << arr_b[i];  
        cout << " sample two: " << arr_w[i];
        cout << "\n";  
    }
}