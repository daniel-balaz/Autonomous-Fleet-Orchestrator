from app.robots.robots_module import Robot
from data_module import SharedData, Config, RobotState, DataDrillRobot
import statistics


class Drill_Robot(Robot):
    """Tento robot bude simulovat vrtaní do horniny"""
    """--- Robotu se bude zahřívat vrtak a celkove cely robot jak bude vrtat, take při vrtání spotřebuje více baterie než kdyz jenom jede nebo stoji ---"""

    def __init__(self, shared_data: SharedData, cfg: Config, robotstate: RobotState, data: DataDrillRobot) -> None:
        super().__init__(shared_data, cfg, robotstate)
        self.data = data
        self.robotstate = robotstate

    def run(self) -> None:
        self.robotstate.battery_consume_multiplier = self.drilling()        #ziskam o kolik % se bude baterka vybijet rychleji
        for i in self.data.drill_intervals: super().run()
        print(f"Battery: {self.robotstate.current_battery} | {round((self.robotstate.current_battery / self.robotstate.max_battery_capacity) * 100, 1)}%")
        print(f"Health Score: {self.robotstate.health_score}")

    def drilling(self) -> float:
        dif = self.shared_data.internal_temp - self.data.drill_temp                     #delam si rozdil mezi vnitrni teplotou a  teplotou drillu
        self.data.drill_temp += dif * self.data.temp_cooling_multiplicator              #ochlazovani drillu okolim
        self.data.drill_temp += self.data.drill_temp * self.data.temp_heating_multiplicator  #oteplovani drillu trenim
        #self.shared_data.internal_temp =  rozdelana teplota uvnitr robota pomoci promenych, jako (motor_heat, batery_heat)
        return (abs(dif) / self.shared_data.internal_temp) / 100         #vypocitani o kolik % se bude baterka vybijet rychleji   #pouzivam dif, nvm jestli nebude lepsi drill_temp, musi se vyzkouset

    def list_temp(self) -> None:
        self.drill_temp = round(self.drill_temp, 2)
        self.robotstate.last_temp_list.append(self.drill_temp)

        median = statistics.median(self.robotstate.last_temp_list)      #vytvarim z nich median (pravy stred)
        print(f"Median {median}")
