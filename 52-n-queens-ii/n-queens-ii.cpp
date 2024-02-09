class Solution {
public:
    bool isValid(vector<vector<int>> &board, int row, int col, int n) {
        // col Checker
        for(int i = 0; i < n; i++) {
            if(board[i][col] == 1) return false;
        }

        // Left Diagonal Checker 
        int x = row;
        int y = col;
        while(x >= 0 && y >= 0) {
            if(board[x][y] == 1) return false;
            x--;
            y--; 
        }

        // Right Diagonal Checker
        x = row;
        y = col;
        while(x >= 0 && y < n) {
            if(board[x][y] == 1) return false;
            x--;
            y++;
        }
        return true;
    }
    int solveNQueens(vector<vector<int>> &board, int n, int i) {
        // Base Case
        if(i == n) {
            return 1;
        }
        // Recursive case
        int ways = 0;
        for(int j = 0; j < n ; j++) {
            if(isValid(board, i , j, n)) {
                board[i][j] = 1;
                ways += solveNQueens(board, n, i+1);
                board[i][j] = 0;
            }
        }
        return ways;
    }
    int totalNQueens(int n) {
        vector<vector<int>> board (n, vector<int> (n));
        return solveNQueens(board, n , 0);
    }
};