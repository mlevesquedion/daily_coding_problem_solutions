#include <iostream>
#include <unordered_map>
#include <tuple>
#include <vector>

using namespace std;

typedef char state;
typedef tuple<state, state, double> transition;

state markov_step(vector<transition> &transitions, state current_state)
{
    // For better performance, it would be helpful to pre-group the transitions in a unordered_map indexed by state
    float probability = (float)rand() / RAND_MAX;
    float cumulative_probability = 0;
    for (auto trans : transitions)
    {
        if (get<0>(trans) == current_state)
        {
            cumulative_probability += get<2>(trans);
            if (cumulative_probability >= probability)
            {
                return get<1>(trans);
            }
        }
    }
}

void increment_count(unordered_map<state, unsigned int> &counts, state key)
{
    auto it = counts.find(key);
    if (it == counts.end())
    {
        counts[key] = 0;
    }
    else
    {
        counts[key] = (it->second + 1);
    }
}

unordered_map<state, unsigned int> markov_run(vector<transition> &transitions, state start_state, unsigned int steps)
{
    state current_state = start_state;
    unordered_map<state, unsigned int> counts;
    for (unsigned int step = 0; step < steps; step++)
    {
        current_state = markov_step(transitions, current_state);
        increment_count(counts, current_state);
    }
    return counts;
}

int main()
{
    vector<transition> transitions = {
        {'a', 'a', 0.9},
        {'a', 'b', 0.075},
        {'a', 'c', 0.025},
        {'b', 'a', 0.15},
        {'b', 'b', 0.8},
        {'b', 'c', 0.05},
        {'c', 'a', 0.25},
        {'c', 'b', 0.25},
        {'c', 'c', 0.5}};
    state start_state = 'a';
    unsigned int steps = 5000;
    unordered_map<state, unsigned int> counts = markov_run(transitions, start_state, steps);
    for (auto &p : counts)
    {
        cout << p.first << " => " << p.second << endl;
    }
}