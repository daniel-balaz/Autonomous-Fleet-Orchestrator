from app.robots.robots_module import Robot
from data_module import SharedData, Config, DataLoaderRobot, RobotState, DataDrillRobot

import statistics
import random

class Loader_Robot(Robot):
    def __init__(self, shared_data: SharedData, cfg: Config, robotstate: RobotState, data: DataLoaderRobot) -> None:
        super().__init__(shared_data, cfg, robotstate)
        self.data = data

    def run(self) -> None:
        self.robotstate.battery_consume_multiplier = self.transform_weight()
        self.robotstate.current_battery = self.perform_task(self.robotstate)
        print(self.robotstate.current_battery)
        super().run()
        

    def transform_weight(self) -> float:
        loading_weight = random.uniform(self.data.min_pos_weight, self.data.max_pos_weight)
        return loading_weight / self.data.max_pos_weight
        
