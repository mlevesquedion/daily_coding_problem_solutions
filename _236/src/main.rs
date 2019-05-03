#[derive(Clone, Copy)]
struct Point(f64, f64);

impl Point {
    fn distance(&self, other: &Point) -> f64 {
        ((self.0 - other.0).powf(2.0) + (self.1 - other.1).powf(2.0)).sqrt()
    }
}

#[derive(Clone, Copy)]
struct Triangle(Point, Point, Point);

impl Triangle {
    fn perimeter(&self) -> f64 {
        self.0.distance(&self.1) + self.1.distance(&self.2) + self.2.distance(&self.0)
    }

    fn contains(&self, p: &Point) -> bool {
        [self.0, self.1, self.2]
            .iter()
            .map(|tp| tp.distance(&p))
            .fold(0.0, |a, b| a + b)
            < self.perimeter()
    }
}

fn triangles(v: &Vec<Point>) -> Vec<Triangle> {
    if v.len() < 3 {
        panic!("Not a polygon!");
    }
    let first = &v[0];
    let second = &v[1];
    v.iter()
        .skip(2)
        .map(|p| Triangle(*first, *second, *p))
        .collect()
}

fn within(v: &Vec<Point>, p: &Point) -> bool {
    triangles(v).iter().any(|t| t.contains(&p))
}

fn main() {
    let points = vec![
        Point(0.0, 0.0),
        Point(0.0, 1.0),
        Point(1.0, 1.0),
        Point(1.0, 0.0),
    ];
    let outside = Point(2.0, 2.0);
    let inside = Point(0.5, 0.5);
    assert_eq!(within(&points, &outside), false);
    assert_eq!(within(&points, &inside), true);
}
