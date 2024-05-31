class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> ans;
        int row = matrix.size();
        int col = matrix[0].size();

        int count = 0;
        int total = row*col;

        int startingR = 0;
        int startingC = 0;
        int endingR = row-1;
        int endingC = col-1;

        while(count<total){
            
            for(int i = startingC; count<total && i<=endingC; i++){
                ans.push_back(matrix[startingR][i]);
                count++;
            }
            startingR++;

            for(int i = startingR; count<total && i<=endingR; i++){
                ans.push_back(matrix[i][endingC]);
                count++;
            }
            endingC--;

            for(int i = endingC; count<total && i>=startingC; i--){
                ans.push_back(matrix[endingR][i]);
                count++;
            }
            endingR--;

            for(int i = endingR; count<total && i>=startingR; i--){
                ans.push_back(matrix[i][startingC]);
                count++;
            }
            startingC++;
        }
        return ans;
    }
};