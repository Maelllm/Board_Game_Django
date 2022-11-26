import aiohttp
import asyncio
import time

start_time = time.time()

pokemon_list_1 = []
pokemon_list_2 = []


async def async_pokemon(num_1, num_2):
    async with aiohttp.ClientSession() as session:
        for number in range(num_1, num_2):
            pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            async with session.get(pokemon_url) as resp:
                pokemon = await resp.json()
                pokemon_list_1.append(pokemon['name'])
        print(pokemon_list_1)
