from robots_module import Robot
from data_module import SharedData, Config, DataLoaderRobot, RobotState, DataDrillRobot
import statistics


class Drill_Robot(Robot):
    """Tento robot bude simulovat vrtaní do horniny"""
    """--- Robotu se bude zahřívat vrtak a celkove cely robot jak bude vrtat, take při vrtání spotřebuje více baterie než kdyz jenom jede nebo stoji ---"""

    def __init__(self, shared_data: SharedData, cfg: Config, robotstate: RobotState, data: DataDrillRobot) -> None:
        super().__init__(shared_data, cfg, robotstate)
        self.data = data

    def drilling(self) -> None:
        dif = self.shared_data.internal_temp - self.drill_temp
        self.drill_temp += dif * self.data.temp_cooling_multiplicator
        
        self.drill_temp += self.drill_temp * self.data.temp_heating_multiplicator

    def list_temp(self) -> None:
        self.drill_temp = round(self.drill_temp, 2)
        self.robotstate.last_temp_list.append(self.drill_temp)
        if len(self.robotstate.last_temp_list) > 10:
            self.robotstate.last_temp_list.pop(0)
        median = statistics.median(self.robotstate.last_temp_list)
        print(f"Median {median}")