#include <iostream>
#include <optional>

using std::cout;
using std::endl;
using std::make_optional;
using std::nullopt;
using std::optional;
using std::pair;

typedef unsigned long nat;
typedef pair<int, int> point;
typedef pair<int, int> range;

class Rectangle
{
  public:
    const point topLeft;
    const nat width;
    const nat height;
    Rectangle(point topLeft, nat width, nat height) : topLeft(topLeft), width(width), height(height) {}
    nat area() const
    {
        return width * height;
    };
    int x() const { return topLeft.first; };
    int y() const { return topLeft.second; };
    optional<Rectangle> intersect(const Rectangle &rhs) const
    {
        optional<range> x_overlap = overlap(this->x_range(), rhs.x_range());
        optional<range> y_overlap = overlap(this->y_range(), rhs.y_range());
        if (x_overlap == nullopt || y_overlap == nullopt)
        {
            return nullopt;
        }
        nat width = x_overlap->second - x_overlap->first;
        nat height = y_overlap->second - y_overlap->first;
        return optional<Rectangle>(Rectangle({x_overlap->first, y_overlap->first}, width, height));
    };

  private:
    range x_range() const
    {
        int x_begin = this->topLeft.first;
        return {x_begin, x_begin + this->width};
    };
    range y_range() const
    {
        int y_begin = this->topLeft.second;
        return {y_begin, y_begin + this->height};
    };
    optional<range> overlap(range a, range b) const
    {
        range first = (a.first < b.first) ? a : b;
        range second = (first == a) ? b : a;
        if (first.second > second.first)
        {
            return optional<range>({second.first, first.second});
        }
        return nullopt;
    }
};

int main()
{
    Rectangle A({1, 4}, 3, 3);
    Rectangle B({0, 5}, 4, 3);
    cout << A.intersect(B)->area() << endl;
}