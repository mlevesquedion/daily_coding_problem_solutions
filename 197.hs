removeDanglingRighties :: String -> Int -> String -> (String, Int)
removeDanglingRighties [] leftOpens acc = ((reverse acc), leftOpens)
removeDanglingRighties (h:t) leftOpens acc =
  case (h, leftOpens) of
    (')', 0) -> removeDanglingRighties t 0 acc
    (')', n) -> removeDanglingRighties t (n - 1) (h : acc)
    ('(', n) -> removeDanglingRighties t (n + 1) (h : acc)

closeDanglingLefties :: (String, Int) -> String
closeDanglingLefties (parens, opens) = parens ++ (replicate opens ')')

solve :: String -> String
solve parens = closeDanglingLefties $ removeDanglingRighties parens 0 []
