#include <algorithm>
#include <iostream>
#include <vector>

using std::cout;
using std::endl;
using std::max;
using std::vector;

typedef unsigned int nat;
typedef vector<nat> set;

set solve(const set &input)
{
    set sizes(input.size(), 1);
    vector<int> parents(input.size(), -1);
    int starter = -1;
    nat max_count;
    for (nat i = 1; i < input.size(); i++)
    {
        nat prevcount = 0;
        nat parent = -1;
        for (nat j = 0; j < i; j++)
        {
            if (input.at(i) % input.at(j) == 0 || input.at(j) % input.at(i) == 0)
            {
                prevcount = max(prevcount, sizes.at(j));
                parent = j;
            }
        }
        nat count = prevcount + 1;
        sizes.at(i) = count;
        if (count > max_count)
        {
            max_count = count;
            starter = i;
        }
        parents.at(i) = parent;
    }
    set solution;
    while (starter != -1)
    {
        solution.push_back(input.at(starter));
        starter = parents.at(starter);
    }
    return solution;
}

int main()
{
    set test1{3, 5, 10, 20, 21};
    set test2{1, 3, 6, 24};
    set answer = solve(test2);
    for (auto x : answer)
    {
        cout << x << endl;
    }
}