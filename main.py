import asyncio
from data_module import Data, Config
from app.robots_module import Robot, Drill_Robot, Loader_Robot

"""Každé kolo bude simulovat 10 min realného běhu, to bude náš interval"""

async def main():
    data = Data()
    cfg = Config()

    drill_robot = Drill_Robot(data, cfg)
    loader_robot = Loader_Robot(data, cfg)
    while True:
        drill_robot.drilling()
        drill_robot.list_temp()
        loader_robot.transform_weight()

        print(f"Loading Weight: {loader_robot.loading_weight} Kg")
        print(f"Battery: |{loader_robot.current_battery_capacity}/{loader_robot.max_battery_capacity}| Wh")

        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())