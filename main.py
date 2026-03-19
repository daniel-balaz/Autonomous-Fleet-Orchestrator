import asyncio
from data_module import Data, Config
from app.robots_module import Robot, Drill_Robot

async def main():
    data = Data()
    cfg = Config()



    robot_vrtac = Drill_Robot(data, cfg)
    while True:
        robot_vrtac.drilling()
        robot_vrtac.list_temp()
        print(robot_vrtac.last_temp_list)
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())