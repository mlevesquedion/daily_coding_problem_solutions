import qualified Data.Map   as Map
import           Data.Maybe (maybe)

solve :: [String] -> [Int] -> [String]
solve xs = map (maybe "" id . flip Map.lookup m)
  where
    m = Map.fromList (zip [0 ..] xs)

main = putStrLn . show $ solve ["a", "b", "c"] [2, 1, 0]
