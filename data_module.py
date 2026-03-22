from dataclasses import dataclass

@dataclass(frozen=True)
class Config:
    ID: str = "ROBOT-DEFAULT"

    battery_consume_noice: int = 5

class Data:
    internal_temp: float = 20.0