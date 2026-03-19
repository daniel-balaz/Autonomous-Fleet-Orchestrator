from dataclasses import dataclass

@dataclass(frozen=True)
class Config:
    ID: str = "ROBOT-DEFAULT"

class Data:
    internal_temp: float = 20.0