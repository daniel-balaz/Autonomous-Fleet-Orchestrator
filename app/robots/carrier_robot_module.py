from robots_module import Robot
from data_module import SharedData, Config, RobotState, DataCarrierRobot
import statistics

class Carrier_Robot(Robot):
    def __init__(self, shared_data: SharedData, cfg: Config, robotstate: RobotState) -> None:
        super().__init__(shared_data, cfg, robotstate)