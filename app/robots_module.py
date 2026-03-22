from data_module import Data, Config
import random
import statistics



class Robot():
    def __init__(self, data: Data, cfg: Config) -> None:
        # Dataclasses
        self.data = data
        self.cfg = cfg

        # Battery
        self.max_battery_capacity: int
        self.current_battery_capacity: int
        self.battery_consume_interval: int

        # Temp
        self.robot_temp: float = self.data.internal_temp

        # Else
        self.round: int = 0
        

    def charging(self) -> None:
        pass

    def battery_consume(self) -> int:
        battery_loss = self.battery_consume_interval + random.randint(-self.cfg.battery_consume_noice, self.cfg.battery_consume_noice)
        return self.current_battery_capacity - battery_loss


class Drill_Robot(Robot):
    """Tento robot bude simulovat vrtaní do horniny"""
    """--- Robotu se bude zahřívat vrtak a celkove cely robot jak bude vrtat, take při vrtání spotřebuje více baterie než kdyz jenom jede nebo stoji ---"""

    def __init__(self, data: Data, cfg: Config) -> None:
        super().__init__(data, cfg)
        self.drill_temp: float = 70.0
        self.temp_cooling_multiplicator: float = 0.1
        self.temp_heating_multiplicator: float = 0.11
        self.last_temp_list: list = []

    def drilling(self) -> None:
        dif = self.data.internal_temp - self.drill_temp
        self.drill_temp += dif * self.temp_cooling_multiplicator
        
        self.drill_temp += self.drill_temp * self.temp_heating_multiplicator
        max_temp: int = 250

    def list_temp(self) -> None:
        self.drill_temp = round(self.drill_temp, 2)
        self.last_temp_list.append(self.drill_temp)
        if len(self.last_temp_list) > 10:
            self.last_temp_list.pop(0)
        median = statistics.median(self.last_temp_list)
        print(f"Median {median}")
    
class Carrier_Robot(Robot):
    def __init__(self, data: Data, cfg: Config) -> None:
        super().__init__(data, cfg)
        self.max_load: int = 500
        self.weight: float = 0

class Loader_Robot(Robot):
    def __init__(self, data: Data, cfg: Config) -> None:
        super().__init__(data, cfg)
        # Config
        self.max_weight: float = 25
        self.min_pos_weight: float = 15
        self.max_pos_weight: float = 25
        self.max_battery_capacity = 1000 # Wh
        self.battery_consume_interval = 25 # Wh

        # Data
        self.loading_weight: float
        self.current_battery_capacity = self.max_battery_capacity

    def transform_weight(self) -> None:
        self.loading_weight = random.uniform(self.min_pos_weight, self.max_pos_weight)
        self.current_battery_capacity = self.battery_consume()
