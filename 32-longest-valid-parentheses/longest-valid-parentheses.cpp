class Solution {
public:
    int longestValidParentheses(string s) {
        stack<int>st; // Using Stack...
        st.push(-1); // Invalid parentheses check krne k liye -1 insert kr do...
        int maxi = 0;
        for(int i = 0; i < s.length(); ++i){
            char ch = s[i];
            if(ch == '('){ // for opening brackets...
                st.push(i); // index push krna h...
            }
            else{
                st.pop(); // atfirst, toh pop kr do...
                if(st.empty()){ // for closing bracket agar opening bracket cancel ho rhi h but stack mein toh sirf invalid index h na mtlb invalid parentheses h yeh...
                    
                    st.push(i);
                }
                else{
                    int length = i - st.top(); // then, length find kr lo...
                    maxi = max(length, maxi);
                }
            }
        }
        return maxi;
    }
};