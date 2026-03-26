from data_module import SharedData, Config, RobotState
import random 
import statistics

class Robot():
    def __init__(self, shared_data: SharedData, cfg: Config, robotstate: RobotState) -> None:
        # Dataclasses
        self.shared_data = shared_data
        self.cfg = cfg
        self.robotstate = robotstate

    def run(self) -> None:
        self.robotstate.current_battery = self.perform_task()
        self.do_battery_state()
        if len(self.robotstate.last_battery_list) > 1: self.robotstate.health_score = self.health_score()

    def charging(self) -> None:
        while self.robotstate.current_battery < self.robotstate.max_battery_capacity:   #nabijej pokud akt_baterie < max_baterie
            self.robotstate.current_battery += self.cfg.batter_charging_noise

    def health_score(self) -> float:
        rounds_left = self.robotstate.rounds_left
        diff = self.robotstate.step_diff
        battery = round((self.robotstate.max_battery_capacity / self.robotstate.current_battery) * 100)
        print((battery * self.cfg.BATTERY_WEIGHT), "+", (diff * self.cfg.DIFF_WEIGHT) ,"-", rounds_left)
        score = (battery * self.cfg.BATTERY_WEIGHT) + (diff * self.cfg.DIFF_WEIGHT) - rounds_left
        return score

    def do_battery_state(self) -> None:
        # 
        self.robotstate.last_battery_list.append(self.robotstate.current_battery)
        
        if len(self.robotstate.last_battery_list) > 1:
            self.robotstate.step_diff = 0
            battery_diff = self.robotstate.last_battery_list[-2] - self.robotstate.last_battery_list[-1]
            self.robotstate.last_battery_diff.append(battery_diff)
            if len(self.robotstate.last_battery_diff) > 1: 
                step_diff = self.robotstate.last_battery_diff[-2] - self.robotstate.last_battery_diff[-1]
                self.robotstate.step_diff_list.append(step_diff)
                for diff in self.robotstate.step_diff_list:
                    self.robotstate.step_diff += diff
    
            median_of_battery_diff = statistics.median(self.robotstate.last_battery_diff)
            self.robotstate.rounds_left = self.robotstate.current_battery / median_of_battery_diff if median_of_battery_diff != 0 else 0
        

    def perform_task(self) -> int:
        battery_loss = self.robotstate.battery_consume_interval + random.randint(-self.cfg.battery_consume_noice, self.cfg.battery_consume_noice)
        battery_now = max(round((self.robotstate.current_battery - battery_loss) - (self.cfg.battery_consume_noice * self.robotstate.battery_consume_multiplier)), 0) 
        return battery_now