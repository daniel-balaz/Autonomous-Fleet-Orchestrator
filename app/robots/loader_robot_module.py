from app.robots.robots_module import Robot
from data_module import SharedData, Config, DataLoaderRobot, RobotState

import statistics
import random

class Loader_Robot(Robot):
    def __init__(self, shared_data: SharedData, cfg: Config, robotstate: RobotState, data: DataLoaderRobot) -> None:
        super().__init__(shared_data, cfg, robotstate)
        self.data = data

    async def run(self) -> None:
        if self.shared_data.driller_working or self.shared_data.drilled_weight > self.cfg.weight_left: 
            self.charging()
            self.shared_data.loader_working = False

        if not self.shared_data.driller_working: 
            while self.shared_data.drilled_weight > self.cfg.weight_left:
                self.shared_data.loader_working = True
                self.robotstate.battery_consume_multiplier = self.transform_weight()
                await super().run() 

            print("--- Loader Robot ---")
            print(f"Battery: {self.robotstate.current_battery} | {round((self.robotstate.current_battery / self.robotstate.max_battery_capacity) * 100, 1)}%")
            print(f"Health Score: {self.robotstate.health_score}")
            print(f"Working: {self.shared_data.driller_working}")
            print("-" * 20)

        
    def transform_weight(self) -> float:
        loading_weight = random.uniform(self.data.min_pos_weight, self.data.max_pos_weight)
        self.shared_data.drilled_weight -= min(random.uniform(self.data.min_pos_weight, self.data.max_pos_weight), 0)
        return loading_weight / self.data.max_pos_weight