class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # Count digits of the input number
        d = {}
        n = str(n)
        for ch in n:
            d[ch] = d.get(ch, 0) + 1

        leng = len(n)
        res = 1
        temp = set()

        # Collect powers of 2 with the same number of digits
        for i in range(31):  # 2^0 to 2^30
            res = 1 << i
            p = str(res)
            if len(p) == leng:
                temp.add(p)
            elif len(p) > leng:
                break

        # Compare digit counts with each candidate
        for j in temp:
            x = d.copy()
            valid = True
            for ch in j:
                if ch not in x or x[ch] == 0:
                    valid = False
                    break
                x[ch] -= 1

            # Check if all counts are used up
            if valid and all(v == 0 for v in x.values()):
                return True

        return False
