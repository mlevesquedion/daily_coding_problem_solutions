import qualified Data.Map   as M
import           Data.Maybe
import           Prelude    hiding (id, lookup)

data Action = Pickup | Dropoff deriving Eq

type Id = Int

type Timestamp = Int

data Delivery = Delivery { id :: Id, ts :: Timestamp, act :: Action }

lookup :: (Ord a) => M.Map a b -> a -> b
lookup map = fromJust . flip M.lookup map

solve :: [Delivery] -> Int
solve deliveries = sum $ map (\id -> lookup dropoffById id - lookup pickupById id) ids
  where ids = map id deliveries
        pickups = filter (\(Delivery _ _ a) -> a == Pickup) deliveries
        dropoffs = filter (\(Delivery _ _ a) -> a == Dropoff) deliveries
        pickupById = M.fromList $ map (\(Delivery id ts _) -> (id, ts)) pickups
        dropoffById = M.fromList $ map (\(Delivery id ts _) -> (id, ts)) dropoffs

deliveries :: [Delivery]
deliveries = [
  Delivery 1 1570320047 Pickup,
  Delivery 1 1570320725 Dropoff,
  Delivery 2 1570321092 Pickup,
  Delivery 3 1570321212 Pickup,
  Delivery 3 1570322352 Dropoff,
  Delivery 2 1570323012 Dropoff
             ]

main :: IO ()
main = do
  putStrLn $ show $ solve deliveries
