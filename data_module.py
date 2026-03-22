from dataclasses import dataclass, field

@dataclass(frozen=True)
class Config:
    ID: str = "ROBOT-DEFAULT"

    battery_consume_noice: int = 5

@dataclass
class SharedData:
    """Data co zdílí všichni roboti"""
    internal_temp: float = 20.0

@dataclass
class RobotState:
    """Data co používají všichni roboti"""
    # Battery
    max_battery_capacity: int
    current_battery_capacity: int
    battery_consume_interval: int

    # Temp
    robot_temp: float = 20.0
    last_temp_list: list = field(default_factory=list)

    # Else
    round: int = 0

@dataclass
class DataLoaderRobot:
    # Config
    max_weight: float = 25
    min_pos_weight: float = 15
    max_pos_weight: float = 25

    # Data
    loading_weight: float = 0


@dataclass
class DataDrillRobot:
    drill_temp: float = 70.0
    max_temp: int = 250
    temp_cooling_multiplicator: float = 0.1
    temp_heating_multiplicator: float = 0.11


@dataclass
class DataCarrierRobot:
    pass