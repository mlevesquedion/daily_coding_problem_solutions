import           Data.Bool     (bool)
import           Data.Function (on)
import           Data.List     (group, maximumBy)

toBin :: Word -> String
toBin 0 = []
toBin n = (bool '1' '0' (m == 0)) : (toBin d)
  where
    (d, m) = divMod n 2

solve :: Word -> Int
solve =
  length .
  maximumBy (compare `on` length) . filter ((==) '1' . head) . group . toBin
