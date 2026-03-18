import asyncio
from data_module import Data

async def main():
    data = Data()
    print(data.cena)

if __name__ == "__main__":
    asyncio.run(main())
