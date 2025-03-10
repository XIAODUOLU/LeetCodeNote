#include <vector>
#include <unordered_set>
#include <iostream>
using namespace std;

class Solution
{
public:
    int longestConsecutive(vector<int> &nums)
    {
        unordered_set<int> numSequence = {};
        for (int value : nums)
        {
            numSequence.insert(value);
        }
        int longestValue = 0;
        for (const int num : numSequence)
        {
            if (!numSequence.count(num - 1))
            {
                int currentNum = num;
                int tempLongestValue = 1;
                while (numSequence.count(currentNum + 1))
                {
                    currentNum += 1;
                    tempLongestValue += 1;
                }
                longestValue = longestValue > tempLongestValue ? longestValue : tempLongestValue;
            }
        }
        return longestValue;
    }
};

int main()
{
    vector<int> nums = {0, 1, 3, 4, 2, 6, 4, 7, 5};
    Solution solution = Solution();
    int output = solution.longestConsecutive(nums);
    cout << "the result is " << output << endl;
    return 0;
}
