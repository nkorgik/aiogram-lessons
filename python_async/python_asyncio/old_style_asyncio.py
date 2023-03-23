import asyncio # this program will not work on python above 3.4.4 probably =D


async def cor_1(count: int) -> None:
    while count:
        print('Current value for the first coroutine --', count)
        await asyncio.sleep(1)
        count -= 1
        

async def cor_2(count: int) -> None:
    while count:
        print('Current value for the second coroutine --', count)
        await asyncio.sleep(1)
        count -= 1
        
        
async def main() -> None: # ENTRY POINT: you don't need to worry about the details of event loop management
    
    # Future object only provides a way to represent the eventual result of an asynchronous operation. 
    # It does not provide any mechanism for scheduling or executing the operation within the event loop, or managing its execution.
    # In general, you should try to avoid working directly with futures and lower-level constructs, unless you have a specific need to do so.

    # this code-style is strongly not recommended - do not use ensure_futures for coroutines
    # instead you could use this method for futures in order to schedule them in our event loop -- fut = asyncio.Future() --> asyncio.ensure_future(fut)
    future_1 = asyncio.ensure_future(cor_1) # In the old-style asyncio, ensure_future() was designed to work with both coroutines and futures
    future_2 = asyncio.ensure_future(cor_2)
    
    done, pending = await asyncio.wait([future_1, future_2]) # you could pass here tasks, it will return done and pending tasks/futures
    # it's still used in a case when you need completed futures/tasks that have been executed as soon as possible. It is worht noting that raised error will not broke our program
    
    for task_futures in done:
        print(task_futures.result()) # task is a subclass of future, read above ⬆︎⬆︎⬆︎
        
    
if __name__ == "__main__":
    # using this condition, you can ensure that your asynchronous code is only executed when it is intended to be executed
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
    except Exception as _ex:
        print('Error occured during workflow', _ex)
    finally:
        loop.close()
    # we should predict all memory/descriptors leaks and et cetera
