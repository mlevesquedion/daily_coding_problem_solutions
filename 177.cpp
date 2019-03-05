#include <iostream>
#include <list>

using namespace std;

class Node
{
  public:
    Node(int val, Node *next = nullptr) : val(val), next(next) {}
    int val;
    Node *next;
};

list<int> doubly_from_singly(Node *singly)
{
    list<int> doubly;
    while (singly != nullptr)
    {
        doubly.push_back(singly->val);
        singly = singly->next;
    }
    return doubly;
}

Node *singly_from_doubly(list<int> doubly)
{
    Node *singly = nullptr;
    while (!doubly.empty())
    {
        singly = new Node(doubly.back(), singly);
        doubly.pop_back();
    }
    return singly;
}

void rotate(list<int> &L, int K)
{
    for (unsigned int i = 0; i < K; i++)
    {
        L.push_back(L.front());
        L.pop_front();
    }
}

Node *rotate(Node *L, int K)
{
    list<int> doubly = doubly_from_singly(L);
    rotate(doubly, K);
    return singly_from_doubly(doubly);
}

int main()
{
    Node *linkedList = new Node(7, new Node(7, new Node(3, new Node(5))));
    linkedList = rotate(linkedList, 6);
    while (true)
    {
        cout << linkedList->val;
        linkedList = linkedList->next;
        if (linkedList != nullptr)
            cout << " -> ";
        else
            break;
    }
}