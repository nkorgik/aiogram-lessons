# The main concepts of any Asyncio program. Any specialist should know these principles --

## Call Stack: 

_The call stack is a data structure that keeps track of the order in which functions are called in a program._
When a function is called, its execution is added to the top of the call stack, and when it returns, its execution is removed from the stack. 
This allows the program to keep track of where it is in the execution of nested functions.

When you call a function or method in Python (including async functions in aiogram), a new stack frame is pushed onto the call stack. This stack frame contains information about the function call, such as the function arguments, local variables, and the return address (i.e., the location in the code where the function call was made).

When the function returns, the stack frame is popped from the call stack and control returns to the caller. Any return values or exceptions are passed back up the call stack to the calling function.

_Asynchronous code in aiogram uses coroutines and event loops to manage the execution of multiple tasks in a single thread. When createtask function is called, it is scheduled for execution on the event loop. The event loop manages the execution of multiple coroutines by interleaving their execution in a cooperative manner._

When a coroutine awaits a future, such as an I/O operation or another coroutine, it suspends its execution and allows other coroutines to run. When the future is ready, the coroutine is resumed and continues executing from where it left off.

In this way, the event loop manages the execution of multiple coroutines by scheduling them for execution on the call stack in a cooperative manner. As a result, the call stack in aiogram may look different from a typical call stack in synchronous code, but the underlying principles are the same.


## Event Loop: 

_The event loop is the central component of asynchronous programming in Python._ It is a loop that continuously checks for events, such as incoming I/O operations, and dispatches them to the appropriate handler. When an event occurs, the event loop schedules the associated coroutine to be executed, and returns control to the program's main loop.


## Futures:

_Futures are objects that represent the eventual result of an asynchronous operation._ They are created when an asynchronous function is called, and are returned immediately, before the function has completed. The future is then scheduled for execution by the event loop. When the operation is completed, the future is marked as "done", and the result is made available to the program.


## Tasks:

_Tasks are objects that represent the execution of a coroutine._ They are created by the event loop when a coroutine is scheduled for execution, and are responsible for keeping track of the coroutine's state and progress. When a task is completed, its associated coroutine is removed from the event loop. Task is a type of futures, e.g ensure_future will always return task.


### FAQ About Tasks & Futures: 

*What is the difference between tasks and futures?*

_Futures were introduced in Python's concurrent.futures module in Python 3.2 as a way to represent the results of asynchronous operations that may not have completed yet. Futures are a way to represent the outcome of a computation that may not have completed yet, but can be waited on (i.e., blocked on) until it has completed._

Tasks, on the other hand, were introduced in Python's asyncio module in Python 3.4 as a way to manage the execution of coroutines in an asynchronous event loop. Tasks are a subclass of futures that are specifically designed to manage the execution of coroutines in an event loop.

Tasks in asyncio are similar to futures in concurrent.futures, but they provide additional functionality specific to managing the execution of coroutines in an event loop. For example, tasks can be cancelled, scheduled for execution on an event loop, and chained together using the asyncio.gather() function.

So while futures came before tasks in Python, tasks are specifically designed to manage the execution of coroutines in an event loop and are an essential part of asynchronous programming in asyncio.

_Schema of Asyncio:_

                                Main Thread
                                     |
                                     v
      +-------------------------------------------------------+
      |                  Event Loop                            |
      |                                                       |
      |  +-----------------+           +-----------------+   |
      |  |   Task Queue    |  <------- |    Event Queue  |   |
      |  +-----------------+           +-----------------+   |
      |          |                             |               |
      |          v                             v               |
      |  +-----------------+           +-----------------+   |
      |  | Task (Coroutine)|  <------- |      Event      |   |
      |  +-----------------+           | (I/O, Timer, ..) |   |
      |                                 +-----------------+   |
      +-------------------------------------------------------+


*Is this paradigm shared-memory? And all bags that are inherent to this threads are the same for coroutines?*

_No, the asynchronous programming paradigm in Python is not shared-memory. In fact, it is designed to avoid the use of shared memory and traditional thread synchronization mechanisms (such as locks and semaphores), which can be difficult to use correctly and can lead to race conditions and other concurrency issues._

In asynchronous programming, coroutines (also known as "tasks") are scheduled by the event loop to run concurrently, but they do not share memory or other resources directly. Instead, they communicate and synchronize using a set of built-in primitives, such as asyncio.Queue, asyncio.Event, and asyncio.Lock, which are designed to work in an asynchronous context.

While it is true that all coroutines run in the same thread and therefore share the same resources (such as the call stack and event loop), they are designed to be isolated from each other and to avoid conflicts through the use of these built-in primitives.

For example, if two coroutines need to access a shared resource, they can use a Lock object to synchronize their access and avoid conflicts. Similarly, if one coroutine needs to notify another coroutine that an event has occurred, it can use an Event object to signal the other coroutine to wake up and respond.

Overall, the asynchronous programming paradigm in Python is designed to provide a lightweight and efficient way to perform concurrent I/O operations, without the overhead and complexity of traditional multi-threaded programming.


*Are there any disadventages of using Aioschedule*

For simple use cases where performance and scalability are not a major concern, aioschedule can be a very useful and lightweight library for scheduling coroutines. It's important to carefully evaluate your requirements and the available libraries before deciding which one to use. 