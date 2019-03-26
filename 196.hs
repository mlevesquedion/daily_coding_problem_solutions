import qualified Data.Map.Strict as Map

data Tree = Node Int Tree Tree | Leaf Int deriving (Show)

tree = Node 5 (Leaf 2) (Leaf (-5))

bumpCount k m =
    case Map.lookup k m of
        Nothing -> Map.insert k 1 m
        Just c -> Map.insert k (c + 1) m

count (Leaf v) m = (v, bumpCount v m)
count (Node val left right) m =
    let (leftVal, leftM) = count left m in
    let (rightVal, rightM) = count right leftM in
    let v = val + leftVal + rightVal in
        (v, bumpCount v rightM)

solve tree = maybe (-1, -1) id . Map.lookupMax . snd $ count tree (Map.empty)

main = putStrLn . show $ solve tree