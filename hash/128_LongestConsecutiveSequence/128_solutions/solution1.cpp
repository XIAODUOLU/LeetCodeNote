#include <vector>
#include <unordered_map>
#include <iostream>
using namespace std;

class Solution
{
public:
    int longestConsecutive(vector<int> &nums)
    {
        unordered_map<int, int> numSequenceMap = {};
        for (int value : nums)
        {
            // 使用 find 方法，不存在该值才需要操作
            auto it = numSequenceMap.find(value);
            if (it == numSequenceMap.end())
            {
                int temp_value;

                // 如果不存在，先存进map，并赋值
                auto itBigger = numSequenceMap.find(value + 1);
                if (itBigger == numSequenceMap.end())
                {
                    // 不存在比自己大1的值，需要赋值为1
                    temp_value = 1;
                }
                else
                {
                    // 赋值为1+比自己大1的key的值,代表从该值启动的长度
                    temp_value = 1 + itBigger->second;
                }
                numSequenceMap[value] = temp_value;

                // 迭代循环找到比当前小1的值直到跳出，并赋值加自己的长度
                auto itSmaller = numSequenceMap.find(value - 1);
                while (itSmaller != numSequenceMap.end())
                {
                    numSequenceMap[itSmaller->first] = itSmaller->second + temp_value;
                    itSmaller = numSequenceMap.find(itSmaller->first - 1);
                }
            }
        }
        // 如果不存在，则为0
        int sequenceLength = 0;
        for (const auto &pair : numSequenceMap)
        {
            sequenceLength = (sequenceLength > pair.second) ? sequenceLength : pair.second;
        }
        return sequenceLength;
    }
};

int main()
{
    // {0}
    // {}

    vector<int> nums = {0, 1, 3, 4, 2, 6, 4, 7, 5};
    Solution solution = Solution();
    int output = solution.longestConsecutive(nums);
    cout << "the result is " << output << endl;
    return 0;
}
