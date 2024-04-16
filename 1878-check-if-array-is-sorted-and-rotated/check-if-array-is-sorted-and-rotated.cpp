class Solution {
public:    
    bool check(vector<int>& arr) {
       int count = 0;
       for(int i=0; i<arr.size()-1; i++){
            if(arr[i+1] < arr[i]){
                count++;
            }
       }

        if(arr[0] < arr[arr.size()-1]){
            count++;
        } 
       if(count>1){
        return false;
       }
       return true;
    }
};