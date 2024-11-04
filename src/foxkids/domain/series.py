from dataclasses import dataclass


@dataclass
class Series:
    name: str
    count: int = 1
    current: int = 1
    year: int | None = None
    genre: str = ""
    name_rus: str = ""
    description: str = ""

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        if isinstance(other, Series):
            return self.name == other.name
        return NotImplemented

    def __str__(self):
        return self.name

    def to_dict(self) -> dict:
        return {**self.__dict__}

    def increase_current_seria(self):
        self.current += 1
        if self.current > self.count:
            self.current = 1
