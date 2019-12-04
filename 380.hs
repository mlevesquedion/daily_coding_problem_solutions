import           Debug.Trace
import           Prelude     hiding (div, divMod, mod)

divMod :: Integer -> Integer -> (Integer, Integer)
divMod n d = (div, mod)
  where e = exp 1
        log' = log . fromIntegral
        div = floor $ e**(log' n  - log' d)
        mod = n - div * d

main :: IO ()
main = do
  print $ divMod 10 3
