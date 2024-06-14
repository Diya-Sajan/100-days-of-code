class Solution {
public:
    void func(vector<int>& ar,int ini, int target, vector<int> nu, vector<vector<int>> &res ){
        if(ini==ar.size()){
            if(target==0)
            { 
                res.push_back(nu);
            }
            return;
        }
        if(ar[ini]<=target)
        {   nu.push_back(ar[ini]);
            func(ar,ini,target-ar[ini],nu,res);
            nu.pop_back();
        }

        func(ar,ini+1,target,nu,res);
    }
    vector<vector<int>> combinationSum(vector<int>& ar, int target) {
        vector<int> nu;
        vector<vector<int>> res;
        func(ar,0,target,nu,res);
        return res;
    }
};