from app.robots.robots_module import Robot
from data_module import SharedData, Config, DataLoaderRobot, RobotState, DataDrillRobot

import statistics
import random

class Loader_Robot(Robot):
    def __init__(self, shared_data: SharedData, cfg: Config, robotstate: RobotState, data: DataLoaderRobot) -> None:
        super().__init__(shared_data, cfg, robotstate)
        self.data = data

    def run(self) -> None:
        super().run()
        self.transform_weight()

    def transform_weight(self) -> None:
        self.loading_weight = random.uniform(self.data.min_pos_weight, self.data.max_pos_weight)
        self.robotstate.current_battery_capacity = self.battery_consume(self.data)