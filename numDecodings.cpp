#include <map>
#include <iostream>

using namespace std;

class Solution {
public:
    map<int, int> m;
    int go(int i, string s) {
        if (m.find(i) != m.end()) {
            return m[i];
        }
        if (s[i] == '0') {
            return 0;
        }
        
        int ways = 0;
        ways += go(i+1, s);
        if (i+1 < s.length() && stoi(s.substr(i,2)) >= 1 && stoi(s.substr(i,2)) <= 26) {
            ways += go(i+2, s);
        }
        m[i] = ways;
        return ways;
    };
    int numDecodings(string s) {
        m[s.length()] = 1;
        return go(0, s);
    };
};