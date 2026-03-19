from dataclasses import dataclass

@dataclass(frozen=True)
class Config:
    ID: str = "ROBOT-DEFAULT"

class Data:
    cena: int = 100