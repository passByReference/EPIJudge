import asyncio
from time import sleep

"""
Coroutines (with asyncio)

    Single-threaded by default: All coroutines run in a single thread

    Cooperative multitasking: Coroutines voluntarily yield control with await

    I/O-bound focus: Ideal for network operations, file I/O (when using async libraries)

    Low overhead: No thread creation/context switching costs

Multithreading

    Preemptive multitasking: OS decides when to switch threads

    True parallelism: Can utilize multiple CPU cores (with GIL limitations in Python)

    Higher overhead: Thread creation and context switching is expensive

    Good for: Mixed I/O and CPU-bound work (though Python's GIL complicates this)
"""
async def test(x):
    await asyncio.sleep(x)
    return x

def test_sync(x):
    sleep(x)
    return x

def main():
    res = 0
    for i in range(10):
        res += test_sync(i)
    print(res)
# async def main():
#     tasks = []
#     for i in range(10):
#         tasks.append(test(i))
#     res = await asyncio.gather(*tasks)
#     print(sum(res))

    
# asyncio.run(main())

main()

