import asyncio
from data_module import Data, Config
from app.robots_module import Drill_Robot, Robot

async def main():
    data = Data()
    cfg = Config()

    drill_robot = Drill_Robot(data, cfg)
    battery, id = drill_robot.vypis_battery_a_id

if __name__ == "__main__":
    asyncio.run(main())
