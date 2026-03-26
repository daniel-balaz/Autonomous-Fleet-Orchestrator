from robots_module import Robot
from data_module import SharedData, Config, DataLoaderRobot, RobotState, DataDrillRobot
import statistics


class Drill_Robot(Robot):
    """Tento robot bude simulovat vrtaní do horniny"""
    """--- Robotu se bude zahřívat vrtak a celkove cely robot jak bude vrtat, take při vrtání spotřebuje více baterie než kdyz jenom jede nebo stoji ---"""

    def __init__(self, shared_data: SharedData, cfg: Config, robotstate: RobotState, data: DataDrillRobot) -> None:
        super().__init__(shared_data, cfg, robotstate)
        self.data = data

    def run(self) -> None:
        self.robotstate.battery_consume_multiplier = self.drilling()        #ziskam o kolik % se bude baterka vybijet rychleji
        self.robotstate.current_battery = self.perform_task(self.robotstate)  #vybijeni baterky

    def drilling(self) -> float:
        dif = self.shared_data.internal_temp - self.drill_temp                     #delam si rozdil mezi vnitrni teplotou a  teplotou drillu
        self.drill_temp += dif * self.data.temp_cooling_multiplicator              #ochlazovani drillu okolim
        self.drill_temp += self.drill_temp * self.data.temp_heating_multiplicator  #oteplovani drillu trenim
        #self.shared_data.internal_temp =  rozdelana teplota uvnitr robota pomoci promenych, jako (motor_heat, batery_heat)
        return (abs(dif) / self.shared_data.internal_temp) / 100         #vypocitani o kolik % se bude baterka vybijet rychleji   #pouzivam dif, nvm jestli nebude lepsi drill_temp, musi se vyzkouset

    def list_temp(self) -> None:
        self.drill_temp = round(self.drill_temp, 2)
        self.robotstate.last_temp_list.append(self.drill_temp)
        if len(self.robotstate.last_temp_list) > 10:                    #zapisuji si poslednich 10 teplot drillu
            self.robotstate.last_temp_list.pop(0)
        median = statistics.median(self.robotstate.last_temp_list)      #vytvarim z nich median (pravy stred)
        print(f"Median {median}")

    def health_score(self) -> int:
        pass