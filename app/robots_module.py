from data_module import Data, Config


class Robot():
    def __init__(self, data: Data, cfg: Config) -> None:
        self.data = data
        self.cfg = cfg
        self.battery: float = 1.0
        