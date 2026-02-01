class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # #####################
        #   sorting solution  #
        # #####################

        # if not citations:
        #     return 0
        #
        # x = sorted(citations) # O(n log n) time + O(n) space
        # n = len(x)
        #
        # for i in range(n): # O(n)
        #     h = n - i
        #     if x[i] >= h:
        #         return h
        #
        # return 0
        #
        # total time O(n log n)
        # total space O(n)

        # #####################
        #  counting solution  #
        # #####################

        n = len(citations)
        papers_count = [0] * (n + 1) # this creates an array of zeros; each position/index is a count of citations
        # [count of articles with O citations, count of articles with 1 citation, count of articles with 2 citations, etc]
        # this is O(n) space

        for c in citations: # this is O(n) time
            papers_count[min(c, n)] += 1

        print(f"papers count: {papers_count}")

        h = n
        papers = papers_count[n]
        while papers < h:
            print(f"h={h}; papers count: {papers}")
            h -= 1
            papers += papers_count[h]

        # total time: O(n)
        # total space: O(n)

        return h

