class RandomizedCollection {
public:
    int n;
    vector<int> v;
    unordered_map<int, vector<int> > mp;
    RandomizedCollection() {
        n=0;
        v.clear();
        mp.clear();
    }
    
    bool insert(int val) {
        v.push_back(val);
        mp[val].push_back(n++);
        return mp[val].size()<2;
        
    }
    
    bool remove(int val) {
        if(mp[val].size()==0)return false;
        int index = mp[val][mp[val].size()-1];
        mp[val].pop_back();
        v[index]=v[n-1];
        v.pop_back();
        n--;
        if(n>index){ mp[v[index]][mp[v[index]].size()-1]=index;sort(mp[v[index]].begin(), mp[v[index]].end());}
        return true;
    }
    
    int getRandom() {
        int index = rand()%n;
        return v[index];
    }
};

/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * RandomizedCollection* obj = new RandomizedCollection();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */