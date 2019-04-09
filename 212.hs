import           Data.Char (chr, ord)

startOffset :: Int
startOffset = ord 'A' - 1

toAlpha :: Int -> Char
toAlpha = chr . ((+) startOffset)

solve :: Int -> String
solve = snd . until (((==) 0) . fst) encode . (flip (,) "")
  where
    encode (n, s) =
      let (d, m) = divMod n 26
       in (d, ((toAlpha m) : s))
