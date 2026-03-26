from dataclasses import dataclass, field
from collections import deque
from typing import Deque

@dataclass(frozen=True)
class Config:
    ID: str = "ROBOT-DEFAULT"

    battery_consume_noice: int = 5
    batter_charging_noise: int = 170

    # BATTERY INFO
    BATTERY_THRESHOLD_WARNING: float = 0.4
    BATTERY_THRESHOLD_LOW: float= 0.2
    BATTERY_THRESHOLD_CRITICAL: float = 0.1


@dataclass
class SharedData:
    """Data co sdílí všichni roboti"""
    internal_temp: float = 20.0

@dataclass
class RobotState:
    """Data co používají všichni roboti"""
    # Battery
    max_battery_capacity: int
    current_battery: int
    battery_consume_interval: int
    battery_consume_multiplier: float = 0

    battery_score: float = 0
    last_battery_list: Deque[int] = field(default_factory=lambda: deque(maxlen=10))
    last_battery_diff: Deque[int] = field(default_factory=lambda: deque(maxlen=10))
    # Temp
    robot_temp: float = 20.0
    last_temp_list: Deque[int] = field(default_factory=lambda: deque(maxlen=10))

    # Else
    round: int = 0

@dataclass
class DataLoaderRobot:
    # Config
    min_pos_weight: float = 15
    max_pos_weight: float = 25

    # Data

@dataclass
class DataDrillRobot:
    drill_temp: float = 30.0
    max_temp: int = 250
    temp_cooling_multiplicator: float = 0.1
    temp_heating_multiplicator: float = 0.11


@dataclass
class DataCarrierRobot:
    pass