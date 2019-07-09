import sc2
from sc2 import run_game, maps, Race, Difficulty, BotAI
from sc2.constants import *
from sc2.player import Bot, Computer

from BT import NodeFunctions
import functions

class Varg(sc2.BotAI):
    
    tree = NodeFunctions.main()

    async def on_step(self, iteration):

        if (iteration % 20 == 0):
            await self.distribute_workers()
        if (len(self.units(ROACH)) < 20):
            await functions.prepareArmy(self)
        else:
        	if(iteration % 100 == 0):
        		await functions.attack(self)

        await functions.inject(self)
        
        await self.tree.runTree(self)

# Note: Change step() in sc2/client for speeding up or slowing down the game. 1 is almost realtime.
# The larvae bug is "solved" when not enabling realtime.
def main():
    run_game(maps.get("Abyssal Reef LE"), [
        Bot(Race.Zerg, Varg()),
        Computer(Race.Zerg, Difficulty.Hard)
    ], realtime=False, save_replay_as="VargReplay.SC2Replay")

if __name__ == '__main__':
    main()