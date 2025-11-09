from dataclasses import dataclass

@dataclass()
class SecolodC:
    secolo: str

    def __str__(self):
        return self.secolo
    def __lt__(self, other):
        return self.secolo < other.secolo

@dataclass()
class SecoloaC:
    secolo: str

    def __str__(self):
        return self.secolo
    def __lt__(self, other):
        return self.secolo < other.secolo
