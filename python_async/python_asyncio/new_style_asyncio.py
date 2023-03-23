"""Faster and more responsive applications"""
import asyncio 
import logging


async def fetch_data(uri: str) -> None: # this asynchronous function will be coroutine
    logging.info(f'Waiting for response -- {uri}')
    await asyncio.sleep(2) # blocking this coroutine, pass the workflow to the main thread
    print(f'Get result from {uri}')
    

async def main() -> None:
    tasks = [ # here we create our tasks that are going to be executed duruing our code
        asyncio.create_task(fetch_data('https://meow.org')), # register/schedule our task in event_loop
        asyncio.create_task(fetch_data('https://gooooooglejump.org')),
        asyncio.create_task(fetch_data('https://httpbin.org/get?query=sure#anchor_1')),
    ]
    # this is worth noting that we could place here just coroutines but it's less explicit
    
    # our tasks won't be scheduled at the specific time (other words -- invoked) untill we explicitly call gather, wait or create_future
    await asyncio.gather(*tasks) # we gather our tasks into our event loop and make tasks queue
    # you could use here not only tasks but also coroutines, it's up to u anyways they are going to be wrapped into tasks heheheh 


if __name__ == "__main__":
    # highly recommend you using this idiom
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s: %(message)s',
    )
    asyncio.run(main()) # run event_loop
