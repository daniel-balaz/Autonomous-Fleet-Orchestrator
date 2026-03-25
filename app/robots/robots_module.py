from data_module import SharedData, Config, RobotState
import random 

class Robot():
    def __init__(self, shared_data: SharedData, cfg: Config, robotstate: RobotState) -> None:
        # Dataclasses
        self.shared_data = shared_data
        self.cfg = cfg
        self.robotstate = robotstate

    def run(self) -> None:
        self.perform_task()

    def charging(self) -> None:
        while self.robotstate.current_battery < self.robotstate.max_battery_capacity:   #nabijej pokud akt_baterie < max_baterie
            self.robotstate.current_battery += self.cfg.batter_charging_noise

    def do_battery_state(self) -> float:
        pass

    def perform_task(self, robotstate: RobotState) -> int:
        battery_loss = robotstate.battery_consume_interval + random.randint(-self.cfg.battery_consume_noice, self.cfg.battery_consume_noice)
        battery_now = round((robotstate.current_battery - battery_loss) + (self.cfg.battery_consume_noice * robotstate.battery_consume_multiplier)) 
        return battery_now