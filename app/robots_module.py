from data_module import Data, Config
import statistics


class Robot():
    def __init__(self, data: Data, cfg: Config) -> None:
        self.data = data
        self.cfg = cfg
        self.battery: float = 1.0
        self.temp: float = self.data.internal_temp
        self.round: int = 0
        

    def charging(self) -> None:
        pass

    def moving(self) -> None:
        pass


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
        self.weight: float = 0