from data_module import Data, Config


class Robot():
    def __init__(self, data: Data, cfg: Config) -> None:
        self.data = data
        self.cfg = cfg
        self.battery: float = 1.0

class Drill_Robot(Robot):
    """Tento robot bude simulovat vrtaní do horniny"""
    """--- Robotu se bude zahřívat vrtak a celkove cely robot jak bude vrtat, take při vrtání spotřebuje více baterie než kdyz jenom jede nebo stoji ---"""

    def __init__(self, data: Data, cfg: Config) -> None:
        """Projede jenom na začátku neboli při inicializaci"""
        """
        To -> None je tu čistě jenom pro typing, tim říkaš co ta funkce vlastne vrací,tady nevraci nic takže dáme None, 
        tim zabráníme tomu aby nekdo z nás v budoucnu zkoušel vytahnout z funkce která vrací str například číslo
        """
        super().__init__(data, cfg)
        self.drill_temp: float = self.data.internal_temp

    def vypis_battery_a_id(self) -> tuple[float, str]: # to pak smaž, je to jenom pro ukázku jak typovat funkci co vrací vice věci, ale musi je vracet presne v poradi
        battery = self.battery
        id = self.cfg.ID
        return battery, id
        # return id, battery # tohle by ti vyhodilo chybu protoze to neni v poradi jake rikas
        # pokud to chapes tak smaz tuhle funkci

class Carrier_Robot(Robot):
    def __init__(self, data: Data, cfg: Config) -> None:
        super().__init__(data, cfg)
        self.max_load: int = 500
        self.weight: float = 0

class Loader_Robot(Robot):
    def __init__(self, data: Data, cfg: Config) -> None:
        super().__init__(data, cfg)
        self.weight: float = 0


