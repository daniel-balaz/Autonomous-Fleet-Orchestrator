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

    def perform_task(self, robotstate: RobotState) -> int:
        
        battery_loss = robotstate.battery_consume_interval + random.randint(-self.cfg.battery_consume_noice, self.cfg.battery_consume_noice)
        battery_now = round((robotstate.current_battery - battery_loss) + (self.cfg.battery_consume_noice * robotstate.battery_consume_multiplier)) 
        return battery_now