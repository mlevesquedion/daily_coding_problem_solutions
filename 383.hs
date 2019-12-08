module Main where

import           Data.List (isPrefixOf, sort)

-- | Dominated by findMatches, could be improved with better matching,
-- | e.g. Karp-Rabin or similar
-- >>> embolden "abcdefg" ["bc", "ef"]
-- "a<b>bc</b>d<b>ef</b>g"
-- >>> embolden "abcdefg" ["bcd", "def"]
-- "a<b>bcdef</b>g"
embolden :: String -> [String] -> String
embolden s = insertBolds s . merge . findMatchPositions s

-- O(|s| · |subs| · E(|subs_i|))
findMatchPositions :: String -> [String] -> [(Int, Int)]
findMatchPositions s subs = go 0 s
  where go _ [] = []
        go n s@(c:cs) = case matches s subs of
                               []  -> go (n + 1) cs
                               m:_ -> (n, n + length m):go (n + 1) cs
        matches s = filter (flip isPrefixOf s)

-- O(n)
merge :: [(Int, Int)] -> [(Int, Int)]
merge ((a1, b1):(a2, b2):rest)
  | a2 <= b1 = merge ((a1, b2):rest)
  | otherwise = (a1, b1):merge ((a2, b2):rest)
merge xs = xs

-- Could be faster using classic merge algorithm on open + close instead of sorting
-- O(|s| log |s|)
insertBolds :: String -> [(Int, Int)] -> String
insertBolds s positions = concat $ insert 0 bolds s
  where open = zip (map fst positions) (repeat "<b>")
        close = zip (map snd positions) (repeat "</b>")
        bolds = sort (open ++ close)
        insert _ [] suffix = [suffix]
        insert n bolds@((pos, bold):rest) suffix@(c:cs) = if pos == n then
                                        bold:[c]:(insert (n + 1) rest cs)
                                      else
                                        [c]:(insert (n + 1) bolds cs)

main :: IO ()
main = print "it compiles"
