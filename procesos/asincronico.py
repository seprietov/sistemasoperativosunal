import asyncio

async def par():
    for x in range(2, 11, 2):
        print(x) 
        x = x + 2
        await asyncio.sleep(0.2)
    

async def impar():
    for x in range(1, 10, 2):
        print(x)
        x = x + 2
        await asyncio.sleep(0.2)

async def main():
    task1 = asyncio.create_task(impar())
    task2 = asyncio.create_task(par())
    await task1
    print("terminanos")

asyncio.run(main())
