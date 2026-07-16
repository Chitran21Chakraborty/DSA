class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        columns = ord(coordinates[0])
        row = int(coordinates[1])
        return (columns - row) % 2 == 1 # if (columns-row) is even it is black else white