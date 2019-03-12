#include <iostream>
#include <numeric>
#include <vector>

using namespace std;

int greatest_common_divisor(int p, int q)
{
    while (q != 0)
    {
        int tmp = p;
        p = q;
        q = tmp % q;
    }
    return p;
}

int greatest_common_denominator(const vector<int> &numbers)
{
    if (numbers.empty())
        return 0;
    return accumulate(
        numbers.begin(),
        numbers.end(),
        numbers.front(),
        greatest_common_divisor);
}

int main()
{
    vector<int> numbers{42, 56, 14};
    cout << greatest_common_denominator(numbers) << endl;
}