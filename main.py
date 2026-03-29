import asyncio
from data_module import SharedData, Config, DataLoaderRobot, DataDrillRobot, RobotState
from app.robots.drill_robot_module import Drill_Robot
from app.robots.loader_robot_module import Loader_Robot
#from app.robots.carrier_robot_module import Carrier_Robot

async def main():
    shared_data = SharedData()
    cfg = Config()

    loader_robot_data = DataLoaderRobot()
    driller_robot_data = DataDrillRobot()

    loader_robot_state = RobotState(max_battery_capacity=1300, 
                                    battery_consume_interval=25, 
                                    current_battery=300)
    
    driller_robot_state = RobotState(max_battery_capacity=2000, 
                                    battery_consume_interval=45, 
                                    current_battery=2000)

    drill_robot = Drill_Robot(shared_data, cfg, driller_robot_state, driller_robot_data)
    loader_robot = Loader_Robot(shared_data, cfg, loader_robot_state, loader_robot_data)

    while True:
        await loader_robot.run()
        await drill_robot.run()
        #print("-" * 20)
        print(f"Weight_Left: {shared_data.drilled_weight}")

        await asyncio.sleep(5)


if __name__ == "__main__":
    asyncio.run(main())
