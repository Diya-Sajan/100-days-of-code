class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int maxArea = 0;
        stack<pair<int, int>> stk;
        int n = heights.size();

        // Iterate through each index and height in the heights array
        for (int i = 0; i < heights.size(); ++i) {
            int start = i;

            // Check if the stack is not empty and the height at the top of the stack is greater than the current height
            while (!stk.empty() && stk.top().second > heights[i]) {
                int index = stk.top().first;
                int height = stk.top().second;
                stk.pop();
                // Calculate the area for the popped element and update maxArea if needed
                maxArea = max(maxArea, (i - index) * height);
                start = index;
            }

            // Push the current index and height onto the stack
            stk.push({start, heights[i]});
        }

        // Process any remaining elements in the stack
        while (!stk.empty()) {
            int index = stk.top().first;
            int height = stk.top().second;
            stk.pop();
            // Calculate the area for the popped element and update maxArea if needed
            maxArea = max(maxArea, (n - index) * height);
        }

        return maxArea;
    }
};