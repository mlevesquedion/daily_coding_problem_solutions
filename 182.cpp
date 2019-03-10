#include <iostream>
#include <list>
#include <vector>
#include <unordered_set>

using namespace std;
typedef vector<list<size_t>> graph;

struct pair_hash
{
    inline std::size_t operator()(const std::pair<int, int> &v) const
    {
        return v.first * 31 + v.second;
    }
};

bool is_minimally_connected(const graph &G)
{
    if (G.empty())
        return true;
    vector<size_t> to_visit{0};
    unordered_set<size_t> visited;
    vector<unordered_set<size_t>> bi_edges(G.size());
    while (!to_visit.empty())
    {
        size_t current = to_visit.back();
        if (visited.find(current) != visited.end())
        {
            return false;
        }
        visited.insert(current);
        to_visit.pop_back();
        for (size_t n : G[current])
        {
            if (bi_edges[n].find(current) != bi_edges[n].end())
            {
                continue;
            }
            to_visit.push_back(n);
            bi_edges[current].insert(n);
        }
    }
    return visited.size() == G.size();
}

int main()
{
    // A graph is minimally connected iif a DFS of said graph visits every node exactly once
    graph complete = {
        {1, 2},
        {0, 2},
        {0, 1}};
    cout << "Complete graph is not minimally connected: "
         << is_minimally_connected(complete) << endl;
    graph minimal = {
        {1, 2},
        {0},
        {0}};
    cout << "Not complete graph is minimally connected: "
         << is_minimally_connected(minimal) << endl;
    graph not_connected = {
        {1},
        {0},
        {}};
    cout << "Not connected graph is not minimally connected: "
         << is_minimally_connected(not_connected) << endl;
}