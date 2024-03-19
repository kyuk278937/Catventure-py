import asyncio
import pygame
import TestScene

async def main():
    TestScene.TestScene()
    await asyncio.sleep(0)

if __name__ == '__main__':
    asyncio.run(main())

# http://localhost:8000#debug