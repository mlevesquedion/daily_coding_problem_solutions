#include "iostream"
#include <vector>
#include <deque>

using namespace std;

typedef unsigned int uint;

template <typename T>
class BinTree
{
    typedef typename vector<T>::const_iterator iter;

  public:
    T value;
    BinTree *left;
    BinTree *right;
    BinTree(T value, BinTree *left = nullptr, BinTree *right = nullptr)
        : value(value), left(left), right(right) {}
    virtual ~BinTree()
    {
        delete left;
        delete right;
    }
    vector<T> level_order() const
    {
        vector<T> elements;
        deque<BinTree const *> todo{this};
        while (!todo.empty())
        {
            BinTree const *current = todo.front();
            todo.pop_front();
            elements.push_back(current->value);
            if (current->left)
            {
                todo.push_back(current->left);
            }
            if (current->right)
            {
                todo.push_back(current->right);
            }
        }
        return elements;
    }
    static BinTree *from_postorder(iter begin, iter end)
    {
        if (begin == end)
        {
            return nullptr;
        }
        T rootVal = *--end;
        iter leftBegin = begin;
        iter rightBegin = begin;
        while (rightBegin != end && *++rightBegin < rootVal)
        {
        }
        BinTree *left = from_postorder(leftBegin, rightBegin);
        BinTree *right = from_postorder(rightBegin, end);
        return new BinTree(rootVal, left, right);
    }
};

int main()
{
    vector<uint> nums{2, 4, 3, 8, 7, 5};
    BinTree<uint> *bst = BinTree<uint>::from_postorder(nums.begin(), nums.end());
    for (auto x : bst->level_order())
    {
        cout << x << endl;
    }
}