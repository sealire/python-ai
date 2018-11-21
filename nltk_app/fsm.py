# 状态机


class StateMachine:

    # Initialize
    def start(self):
        self.state = self.startState

    # Step through the input
    def step(self, inp):
        (s, o) = self.getNextValues(self.state, inp)
        self.state = s
        return o

    # Loop through the input
    def feeder(self, inputs):
        self.start()
        return [(self.state, inp, self.step(inp), self.state) for inp in inputs]


# Determine the TRUE or FALSE state
class TextSeq(StateMachine):
    startState = 1

    def getNextValues(self, state, inp):
        if inp == 'A':
            return (self.state, True)
        elif inp == 'E':
            return (4, False)
        elif inp == 'F':
            return ((self.state) % 3 + 1, True)
        elif inp == 'B':
            return ((self.state + 1) % 3 + 1, True)
            return (4, False)


InSeq = TextSeq()

x = InSeq.feeder(['A', 'A', 'A'])
print(x)

y = InSeq.feeder(['A', 'B', 'F', 'A', 'F', 'F', 'E'])
print(y)
