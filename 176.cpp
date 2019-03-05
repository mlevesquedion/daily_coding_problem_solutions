#include <assert.h>
#include <unordered_set>

using namespace std;

unsigned long unique_char_count(const string &s)
{
    unordered_set<char> chars;
    for (const char c : s)
    {
        chars.insert(c);
    }
    return chars.size();
}

bool bijection_exists(const string &a, const string &b)
{
    return unique_char_count(a) == unique_char_count(b);
}

int main()
{
    assert(bijection_exists("abc", "bcd"));
    assert(!bijection_exists("foo", "bar"));
}
