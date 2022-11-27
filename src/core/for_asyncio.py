import asyncio
import random
import time

import aiohttp  # NOQA

start_time = time.time()

pokemon_list_1 = []
pokemon_list_2 = []


async def async_pokemon(num_1, num_2):
    async with aiohttp.ClientSession() as session:
        for number in range(num_1, num_2):
            print(f"Starting {number}")
            pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{number}"
            async with session.get(pokemon_url) as resp:
                pokemon = await resp.json()
                pokemon_list_1.append(pokemon["name"])


async def stop_event_loop(seconds):
    await asyncio.sleep(seconds)
    print("You cannot catch anyone more")
    asyncio.get_event_loop().stop()
    print(f"Trainer 1 has {len(pokemon_list_1)} pokemons. Trainer 2 has {len(pokemon_list_2)}.")
    print("Behold!")
    print(pokemon_list_1)
    print(pokemon_list_2)


async def resolve_future(future):
    print("Hello")
    await asyncio.sleep(random.randint(1, 5))
    print("Future has come")
    future.set_result(random.randint(10, 25))


async def async_pokemon_2(future):
    print("I a'm gonna be best pokemon master")
    result = await future
    print("Gonna catch them all")
    async with aiohttp.ClientSession() as session:
        for number in range(random.randint(30, 40), random.randint(40, 50) + result):
            print(f"Starting {number}")
            pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{number}"
            async with session.get(pokemon_url) as resp:
                pokemon = await resp.json()
                pokemon_list_2.append(pokemon["name"])
        print("Victory")


event_loop = asyncio.get_event_loop()

event_loop.create_task(async_pokemon(1, random.randint(35, 70)))
event_loop.create_task(async_pokemon(30, 60))

fut = asyncio.Future()

event_loop.create_task(stop_event_loop(random.randint(3, 6)))

event_loop.create_task(resolve_future(fut))

event_loop.create_task(async_pokemon_2(fut))
event_loop.create_task(async_pokemon_2(fut))

event_loop.run_forever()
event_loop.close()
