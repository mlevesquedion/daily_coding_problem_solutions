#include <deque>
#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

int main()
{
    deque<int> subarray;
    unordered_set<int> cache;
    // vector<int> elements{5, 5, 5, 5, 5, 5, 5, 5};
    // vector<int> elements{1, 2, 3, 4, 5, 6, 7, 8};
    // vector<int> elements{1, 2, 3, 4, 5, 6, 7, 6};
    vector<int> elements{5, 1, 3, 5, 2, 3, 4, 1};
    size_t longest = 0;
    for (int x : elements)
    {
        if (cache.find(x) != cache.end())
        {
            while (subarray.front() != x)
            {
                cache.erase(subarray.front());
                subarray.pop_front();
            }
            cache.erase(subarray.front());
            subarray.pop_front();
        }
        subarray.push_back(x);
        cache.insert(x);
        longest = max(longest, subarray.size());
    }
    cout << longest << endl;
}