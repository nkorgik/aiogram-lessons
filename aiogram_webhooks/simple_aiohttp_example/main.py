import aiohttp
import asyncio 
import certifi
import ssl


ssl_context = ssl.create_default_context(cafile=certifi.where())


async def main():
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl_context)) as session:
        try:
            async with session.get('https://httpbin.org/get/') as response:
                response_text = await response.text()
                print(response_text)
        except aiohttp.ClientError as _ex:
            print(f'HTTP request error: {_ex}')
            
        except asyncio.TimeoutError:
            print('HTTP request timed out')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
