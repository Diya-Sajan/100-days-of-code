class Solution {
public:
    void reverseString(vector<char>& v) {
        int s = 0;
        int e = v.size()-1;
        while(s<e){
            swap(v[s++],v[e--]);
        }
    }
};