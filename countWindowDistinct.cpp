#include <map>
#include <iostream>
#include <conio.h>
using namespace std;

void countWindowDistinct(int win[], int K, int N) {
    int dis_count = 0;
    map<int, int> hm;
    /**
     * If this element appears first time,
     * increment distinct element count
     */
    for (int i = 0; i < K; i++) {
        if (hm[win[i]] == 0) {
            dis_count++;
        }
        hm[win[i]] += 1;
    }
    cout << dis_count << endl;

    for (int i = K; i<N; i++){
        if (hm[win[i-K]] == 1) {
            dis_count -= 1;
        }
        hm[win[i-K]] -= 1;

        if (hm[win[i]] == 0) {
            dis_count += 1;
        }
        hm[win[i]] += 1;
        cout << dis_count << endl;
    }
}

int main() {
    cout << "Array: ";
    int arr[] = {1,9,4,31,2,3,1,2,3,4,5};
    int K;
    cout << "K: ";
    cin >> K;
    cout << arr;
    int N = sizeof(arr)/sizeof(int);
    countWindowDistinct(arr, K, N);
    getch();
    return 0;
}