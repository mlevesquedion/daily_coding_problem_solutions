const INFINITY: u32 = u32::max_value();

fn solve(jumps: Vec<u32>) -> Vec<u32> {
    let mut table = vec![0; jumps.len()];
    let mut parents = vec![0; jumps.len()];

    for i in 1..(jumps.len()) {
        let mut min = INFINITY;
        let mut min_parent = INFINITY;
        for j in 0..i {
            if j + jumps[j] as usize >= i && table[j] < min {
                min = table[j];
                min_parent = j as u32;
            }
        }
        table[i] = match min {
            INFINITY => INFINITY,
            _ => min + 1,
        };
        parents[i] = min_parent;
    }

    let mut solution = Vec::new();
    let mut current = table.len() - 1;
    while parents[current] != INFINITY {
        solution.push(jumps[current]);
        if current == 0 {
            break;
        }
        current = parents[current] as usize;
    }
    solution.into_iter().rev().collect()
}

fn main() {
    let example = vec![6, 2, 4, 0, 5, 1, 1, 4, 2, 9];
    assert_eq!(solve(example), vec![6, 5, 9]);
}
