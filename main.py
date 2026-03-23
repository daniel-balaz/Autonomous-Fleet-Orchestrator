import asyncio
from data_module import SharedData, Config, DataLoaderRobot, RobotState
#from app.robots.drill_robot_module import Drill_Robot
from app.robots.loader_robot_module import Loader_Robot
#from app.robots.carrier_robot_module import Carrier_Robot

"""Každé kolo bude simulovat 10 min realného běhu, to bude náš interval"""

async def main():
    shared_data = SharedData()
    loader_robot_data = DataLoaderRobot()
    loader_robot_state = RobotState(max_battery_capacity=1000, 
                                    battery_consume_interval=25, 
                                    current_battery=1000)
    
    cfg = Config()

    #drill_robot = Drill_Robot(shared_data, cfg)
    loader_robot = Loader_Robot(shared_data, cfg, loader_robot_state, loader_robot_data)

    while True:
        loader_robot.run()

        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())