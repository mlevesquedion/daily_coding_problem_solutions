import           Data.List       (intercalate)
import           Data.List.Split (splitOn)

catDirs ds "."      = ds
catDirs (d:ds) ".." = ds
catDirs ds d        = (d : ds)

solve = intercalate "/" . reverse . foldl catDirs [] . splitOn "/"

path = "/usr/bin/../bin/./scripts/../"
