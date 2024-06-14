class Solution {
public:
    void func(vector<int> &ar, int ind, int target, vector<int> &nu, vector<vector<int>> &res){
        
        if(target==0){
            res.push_back(nu);
            return;
        }
        for(int i = ind; i<ar.size(); i++){
            if(i>ind && ar[i]==ar[i-1]) continue;
            if(ar[i]>target) break;
            
            nu.push_back(ar[i]);
            func(ar,i+1,target-ar[i],nu,res);
            nu.pop_back();
        }
    }

    vector<vector<int>> combinationSum2(vector<int>& ar, int target) {
    vector<vector<int>> res;
    vector<int> nu;
    sort(ar.begin(),ar.end());
    func(ar,0,target,nu,res);
    return res;
    }

};