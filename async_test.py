import asyncio
import aiohttp

async def fetch_url(session, url):
    async with session.get(url, headers={'Accept': 'application/json'}) as response:
        if response.status == 200:
            return await response.json()

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in requests:
            tasks.append(fetch_url(session, url))
        responses = await asyncio.gather(*tasks)
        return responses
requests = ["https://us.api.blizzard.com/profile/wow/character/illidan/stadman/pvp-bracket/shuffle-evoker-preservation?namespace=profile-us&locale=en_US&access_token=US8hNyvIX13PiJImsfoAD7nkpbN0f2OLrk",
"https://us.api.blizzard.com/profile/wow/character/stormrage/scaliihead/pvp-bracket/shuffle-evoker-preservation?namespace=profile-us&locale=en_US&access_token=US8hNyvIX13PiJImsfoAD7nkpbN0f2OLrk",
"https://us.api.blizzard.com/profile/wow/character/azralon/dracthonyr/pvp-bracket/shuffle-evoker-preservation?namespace=profile-us&locale=en_US&access_token=US8hNyvIX13PiJImsfoAD7nkpbN0f2OLrk",
"https://us.api.blizzard.com/profile/wow/character/illidan/trillvoker/pvp-bracket/shuffle-evoker-devastation?namespace=profile-us&locale=en_US&access_token=US8hNyvIX13PiJImsfoAD7nkpbN0f2OLrk",
"https://us.api.blizzard.com/profile/wow/character/stormrage/sleepiiheadx/pvp-bracket/shuffle-evoker-preservation?namespace=profile-us&locale=en_US&access_token=US8hNyvIX13PiJImsfoAD7nkpbN0f2OLrk",
"https://us.api.blizzard.com/profile/wow/character/azralon/azrealz/pvp-bracket/shuffle-evoker-preservation?namespace=profile-us&locale=en_US&access_token=US8hNyvIX13PiJImsfoAD7nkpbN0f2OLrk",
"https://us.api.blizzard.com/profile/wow/character/tichondrius/kwebab/pvp-bracket/shuffle-evoker-preservation?namespace=profile-us&locale=en_US&access_token=US8hNyvIX13PiJImsfoAD7nkpbN0f2OLrk",
"https://us.api.blizzard.com/profile/wow/character/scilla/garbagevoker/pvp-bracket/shuffle-evoker-preservation?namespace=profile-us&locale=en_US&access_token=US8hNyvIX13PiJImsfoAD7nkpbN0f2OLrk",
"https://us.api.blizzard.com/profile/wow/character/illidan/lucardeht/pvp-bracket/shuffle-evoker-preservation?namespace=profile-us&locale=en_US&access_token=US8hNyvIX13PiJImsfoAD7nkpbN0f2OLrk",
"https://us.api.blizzard.com/profile/wow/character/proudmoore/caedalade/pvp-bracket/shuffle-evoker-devastation?namespace=profile-us&locale=en_US&access_token=US8hNyvIX13PiJImsfoAD7nkpbN0f2OLrk",
"https://us.api.blizzard.com/profile/wow/character/arthas/shamblewing/pvp-bracket/shuffle-evoker-devastation?namespace=profile-us&locale=en_US&access_token=US8hNyvIX13PiJImsfoAD7nkpbN0f2OLrk",
"https://us.api.blizzard.com/profile/wow/character/kelthuzad/shambly/pvp-bracket/shuffle-evoker-devastation?namespace=profile-us&locale=en_US&access_token=US8hNyvIX13PiJImsfoAD7nkpbN0f2OLrk",
"https://us.api.blizzard.com/profile/wow/character/kelthuzad/rvrbz/pvp-bracket/shuffle-evoker-preservation?namespace=profile-us&locale=en_US&access_token=US8hNyvIX13PiJImsfoAD7nkpbN0f2OLrk",
"https://us.api.blizzard.com/profile/wow/character/area52/lieferant/pvp-bracket/shuffle-evoker-preservation?namespace=profile-us&locale=en_US&access_token=US8hNyvIX13PiJImsfoAD7nkpbN0f2OLrk",
"https://us.api.blizzard.com/profile/wow/character/tichondrius/ggdwagon/pvp-bracket/shuffle-evoker-preservation?namespace=profile-us&locale=en_US&access_token=US8hNyvIX13PiJImsfoAD7nkpbN0f2OLrk",
"https://us.api.blizzard.com/profile/wow/character/illidan/zarrantevo/pvp-bracket/shuffle-evoker-preservation?namespace=profile-us&locale=en_US&access_token=US8hNyvIX13PiJImsfoAD7nkpbN0f2OLrk",
"https://us.api.blizzard.com/profile/wow/character/silverhand/ryü/pvp-bracket/shuffle-evoker-devastation?namespace=profile-us&locale=en_US&access_token=US8hNyvIX13PiJImsfoAD7nkpbN0f2OLrk",
"https://us.api.blizzard.com/profile/wow/character/tichondrius/gaslightqt/pvp-bracket/shuffle-evoker-preservation?namespace=profile-us&locale=en_US&access_token=US8hNyvIX13PiJImsfoAD7nkpbN0f2OLrk",
"https://us.api.blizzard.com/profile/wow/character/malganis/rvrbzx/pvp-bracket/shuffle-evoker-preservation?namespace=profile-us&locale=en_US&access_token=US8hNyvIX13PiJImsfoAD7nkpbN0f2OLrk",
"https://us.api.blizzard.com/profile/wow/character/blackhand/uda/pvp-bracket/shuffle-evoker-devastation?namespace=profile-us&locale=en_US&access_token=US8hNyvIX13PiJImsfoAD7nkpbN0f2OLrk"]


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(main())
    for r in results:
        print(r)
    print(len(results))