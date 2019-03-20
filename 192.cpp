#include <vector>
#include <iostream>

using namespace std;
typedef unsigned int nat;

bool can_reach_end(const vector<nat> &jumps)
{
    vector<bool> reachable(jumps.size(), false);
    reachable.at(0) = true;
    for (nat i = 0; i < jumps.size(); i++)
    {
        if (reachable.at(i))
        {
            nat jump = jumps.at(i);
            nat max_jumped = min(jump + i, (nat)jumps.size() - 1);
            for (nat jumped = i + 1; jumped <= max_jumped; jumped++)
            {
                reachable.at(jumped) = true;
            }
        }
    }
    return *(reachable.end() - 1);
}

int main()
{
    vector<nat> yes{1, 3, 1, 2, 0, 1};
    vector<nat> no{1, 2, 1, 0, 0};
    cout << can_reach_end(yes) << endl;
    cout << can_reach_end(no) << endl;
}