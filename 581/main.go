package main

import "fmt"

type Point struct {
	X, Y int
}

type Dimensions struct {
	Width, Height int
}

type Rectangle struct {
	Point
	Dimensions
}

func fromPoints(topLeft, bottomRight Point) Rectangle {
	width := bottomRight.X - topLeft.X
	height := topLeft.Y - bottomRight.Y

	if width < 0 || height < 0 {
		return Rectangle{topLeft, Dimensions{0, 0}}
	}

	return Rectangle{
		topLeft,
		Dimensions{width, height},
	}
}

func (r Rectangle) topLeft() Point {
	return Point{
		r.X, r.Y,
	}
}

func (r Rectangle) bottomRight() Point {
	return Point{
		r.X + r.Width,
		r.Y - r.Height,
	}
}

func (r1 Rectangle) Intersect(r2 Rectangle) Rectangle {
	if r2.X < r1.X {
		r1, r2 = r2, r1
	}
	return fromPoints(r2.topLeft(), r1.bottomRight())
}

func (r Rectangle) Area() int {
	return r.Width * r.Height
}

func main() {
	r1 := Rectangle{Point{1, 4}, Dimensions{3, 3}}
	r2 := Rectangle{Point{0, 5}, Dimensions{4, 3}}
	fmt.Println(r1.Intersect(r2).Area())
}
