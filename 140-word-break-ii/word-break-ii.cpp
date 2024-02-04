#pragma GCC optimize("03")
static int __star = []{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL), cout.tie(NULL);
    return 0;
}();

class Solution {
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        vector<string> r;
        dp(s,wordDict,r,0);
        return r;
    }

    void dp(string s, vector<string>& dict, vector<string>& r, int index) {
        if(s.size() == index) {
            s.pop_back();
            r.push_back(s);
        }
        for(string& word : dict) {
            int s1 = s.size(), d1 = word.size();
            if(d1 > s1-index) continue;
            if(word == s.substr(index,d1)) {
                string ret = s.substr(0,index+d1) + " " + s.substr(index+d1,s1-d1);
                dp(ret,dict,r,index+d1+1);
            }
        }
    }
};