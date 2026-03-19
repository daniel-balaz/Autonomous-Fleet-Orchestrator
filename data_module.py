from dataclasses import dataclass

@dataclass(frozen=True)
class Config:
    ID: str = "ROBOT-DEFAULT"

class Data:
# TEMP
    internal_temp: float = 20.0 # Na základě toho budeme ochlazovat vrták a celkově roboty, cim větší internal_temp tim větší machine temp