import asyncio

async def main():
    task1 = asyncio.create_task(par())
    task2 = asyncio.create_task(impar())
    await par()
    await impar()
    print("terminanos")

async def par():
    for x in range(0, 11, 2):
        x = x + 2
        print(x) 
    await asyncio.sleep(2)

async def impar():
    for x in range(1, 11, 2):
        x = x + 2
        print(x)
    await asyncio.sleep(2)

asyncio.run(main())