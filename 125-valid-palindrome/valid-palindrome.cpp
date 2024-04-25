class Solution {
public:
    char low(char ch){
        if(ch>='A' && ch<='Z'){
            ch = ch -'A'+'a';
        }
        return ch;
    }
    bool isValid(char ch){
        if(ch>='a' && ch<='z' || ch>='0' && ch<='9'){
            return true;
        }
        return false;
    }
    bool isPalindrome(string s) {
        
        int st = 0;
        int e = s.length()-1;

        while(st<e){
        
            s[st] = low(s[st]);
            s[e] = low(s[e]);

            if (not isValid(s[st])){
                st++;
            }
            else if(not isValid(s[e])) {
                e--;
            }

            else if(s[st]!=s[e]){
                return false;
            }
            else{
                st++;
                e--;
            }
        }
        return true;
    }
};