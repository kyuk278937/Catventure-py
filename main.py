import asyncio
import pygame
import TestScene

async def main():
    TestScene.TestScene()
    await asyncio.sleep(0)  # Пездець важлива хуйня НЕ ЧІПАТИ БЛЯТЬ

if __name__ == '__main__':
    asyncio.run(main())