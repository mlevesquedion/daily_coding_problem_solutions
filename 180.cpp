#include <iostream>
#include <vector>
#include <deque>

using namespace std;

int main()
{
    vector<int> stack{1, 2, 3, 4, 5};
    // vector<int> stack{1, 2, 3, 4};
    deque<int> queue;
    int to_take = stack.size() - 1;
    for (int i = to_take; i > 0; i--)
    {
        for (int j = 0; j < i; j++)
        {
            queue.push_back(stack.back());
            stack.pop_back();
        }
        for (int j = 0; j < i; j++)
        {
            stack.push_back(queue.front());
            queue.pop_front();
        }
    }
    for (auto x : stack)
    {
        cout << x << endl;
    }
}