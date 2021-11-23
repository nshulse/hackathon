class Ok:
    x: int



    def __repr__(self):
        return f"{self.x}"



    def wow(self):
        self.x = 2
        return self.x


hmm: Ok = Ok()
hmm.x = 1
print(hmm.x)
print(hmm.wow)