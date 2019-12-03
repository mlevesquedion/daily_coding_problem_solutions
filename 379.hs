subsequences :: [a] -> [[a]]
subsequences [] = [[]]
subsequences (x:xs) = map (x:) next ++ next
  where next = subsequences xs

main :: IO ()
main = do
  mapM_ putStrLn $ subsequences "xyz"
