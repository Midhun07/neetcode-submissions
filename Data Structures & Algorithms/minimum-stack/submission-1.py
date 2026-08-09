class MinStack:
    # lets implement this using a list
    # Save a list of minimums till each index of the list
    # [2, 1, 5, 7, 3]
    # [2, 1, 1, 1, 1]

    def __init__(self):
        self.stack_list = []
        self.min_list = []

    def push(self, val: int) -> None:
        self.stack_list.append(val)
        min_val = min(self.min_list[-1], val) if len(self.min_list) > 0 else val
        self.min_list.append(min_val)

    def pop(self) -> None:
        del self.stack_list[-1]
        del self.min_list[-1]

    def top(self) -> int:
        return self.stack_list[-1]

    def getMin(self) -> int:
        return self.min_list[-1]
