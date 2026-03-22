from data_module import SharedData, Config, RobotState
import random 

class Robot():
    def __init__(self, shared_data: SharedData, cfg: Config, robotstate: RobotState) -> None:
        # Dataclasses
        self.shared_data = shared_data
        self.cfg = cfg
        self.robotstate = robotstate

    def run(self) -> None:
        print("test")

    def charging(self) -> None:
        pass

    def battery_consume(self, data) -> int:
        battery_loss = self.robotstate.battery_consume_interval + random.randint(-self.cfg.battery_consume_noice, self.cfg.battery_consume_noice)
        return self.robotstate.current_battery_capacity - battery_loss