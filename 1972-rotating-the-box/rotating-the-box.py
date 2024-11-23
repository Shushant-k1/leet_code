class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        def tilt(row):
            bottom = len(row) - 1
            for i in reversed(range(len(row))):
                match row[i]:
                    case '*':
                        bottom = i - 1
                    case '#':
                        row[i], row[bottom] = '.', '#'
                        bottom = bottom - 1
            return row

        return zip(*map(tilt, reversed(box)))