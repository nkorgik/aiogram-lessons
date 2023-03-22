"""Faster and more responsive applications"""
import asyncio 
import logging


async def fetch_data(uri: str) -> None:
    logging.info(f'Waiting for response -- {uri}')
    await asyncio.sleep(2) # blocking this coroutine, pass the workflow to the main thread
    print(f'Get result from {uri}')
    

async def main() -> None:
    tasks = [
        asyncio.create_task(fetch_data('https://meow.org')),
        asyncio.create_task(fetch_data('https://gooooooglejump.org')),
        asyncio.create_task(fetch_data('https://httpbin.org/get?query=sure#anchor_1')),
    ]
    
    return tasks


if __name__ == "__main__":
    asyncio.run(main())

