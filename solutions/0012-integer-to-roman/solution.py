class Solution:
    def intToRoman(self, num: int) -> str:
        # map = {
        #     1000: "M",
        #     900:  "CM",
        #     500:  "D",
        #     400:  "CD",
        #     100:  "C",
        #     90:   "XC",
        #     50:   "L",
        #     40:   "XL",
        #     10:   "X",
        #     9:    "IX",
        #     5:    "V",
        #     4:    "IV",
        #     1:    "I",
        # }

        # res = ""
        # for k, v in map.items():
        #     val = int(num / k)
        #     if val > 0:
        #         res += val * v
        #         num = num % k

        # return res

        result = []

        def encode(d, one, five, ten):
            if d == 9:
                return one + ten
            if d == 4:
                return one + five
            if d >= 5:
                return five + one * (d - 5)
            return one * d

        thousands = num // 1000
        hundreds  = (num // 100) % 10
        tens      = (num // 10) % 10
        ones      = num % 10

        result.append("M" * thousands)
        result.append(encode(hundreds, "C", "D", "M"))
        result.append(encode(tens, "X", "L", "C"))
        result.append(encode(ones, "I", "V", "X"))

        return "".join(result)





