class Solution:
    def findCommonResponse(self, responses: list[list[str]]) -> str:
        count = defaultdict(int)

        for daily in responses:
            for response in set(daily):
                count[response] += 1

        max_count = max(count.values())
        most_common = min(key for key, value in count.items() if value == max_count)
        print(max_count )

        return most_common