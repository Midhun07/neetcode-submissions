class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.time_map.get(key) is None:
            self.time_map[key] = [(key, value, timestamp)]
        else:
            self.time_map[key].append((key, value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        lst = self.time_map.get(key)
        if lst is None or not lst:
            return ""
        ele = ("", -1)
        l, r = 0, len(lst) - 1
        while l <= r:
            mid = (l + r) // 2
            if lst[mid][2] <= timestamp:
                ele = (lst[mid][1], lst[mid][2]) if lst[mid][2] == max(lst[mid][2], ele[1]) else ele
                l = mid + 1
            else:
                r = mid - 1
        return ele[0]