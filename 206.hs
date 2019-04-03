solve :: [String] -> [Int] -> [String]
solve xs = map (uncurry (!!)) . zip (repeat xs)

main = putStrLn . show $ solve ["a", "b", "c"] [2, 1, 0]
