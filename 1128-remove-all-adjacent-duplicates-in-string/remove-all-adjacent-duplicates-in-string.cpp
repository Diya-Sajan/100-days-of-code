#include <string.h>
using namespace std;
class Solution {
public:
    string removeDuplicates(string s) {
        
        string str = s;
        s = "\0";
        s.push_back(str[0]);

        for(int i = 1; i<str.length(); i++){
            cout<<str[i];
            if(!s.empty() && s.back()==str[i]){
                s.pop_back();
            }
            else{
                s.push_back(str[i]);
            }
        }
        
        return(s);
    }
};