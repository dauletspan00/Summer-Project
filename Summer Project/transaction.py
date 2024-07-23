class TransactionStack:
    def __init__(self):
        self.stack = []
        self.history = []

    def push(self, transaction):
        self.stack.append(transaction)
        self.history.append(transaction)

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    def undo(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop();