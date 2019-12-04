import           Debug.Trace
import           Prelude     hiding (div, divMod, mod)

-- |
-- >>> log10 10
-- 1
-- >>> log10 100
-- 2
-- >>> log10 1
-- 0
log10 :: Floating a => Integer -> a
log10 = logBase 10 . fromIntegral

-- |
-- >>> divMod 10 3
-- (3,1)
divMod :: Integer -> Integer -> (Integer, Integer)
divMod n d = (div, mod)
  where div = floor $ 10**(log10 n  - log10 d)
        mod = n - div * d

main :: IO ()
main = do
  print $ divMod 10 3
