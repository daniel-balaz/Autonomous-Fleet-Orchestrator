import asyncio
from data_module import Data
from app.robots_module import Robot

async def main():
    data = Data()
    print(data.cena)

if __name__ == "__main__":
    asyncio.run(main())
