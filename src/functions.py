import asyncio

from sc2.constants import *

async def fail():
    return "FAIL"

async def doNothing():
    await asyncio.sleep(0)
    return "OK"

async def trainUnit(obs, unit, supply):
    if (obs.can_afford(unit) and obs.units(LARVA).exists and obs.supply_left >= supply):
        await obs.do(obs.units(LARVA).random.train(unit))
        return "OK"
    else:
        return "FAIL"

async def trainQueen(obs):
    try:
        hatchery = obs.units(HATCHERY).idle
        if obs.can_afford(QUEEN):
            return await obs.do(hatchery[0].train(QUEEN))
        else:
            return "FAIL"
    except:
        return "FAIL"

async def trainDrone(obs):
    return await trainUnit(obs, DRONE, 1)

async def trainOverlord(obs):
    return await trainUnit(obs, OVERLORD, 1)

async def trainZergling(obs):
    sp = obs.units(SPAWNINGPOOL).ready
    if (sp.exists):
        return await trainUnit(obs, ZERGLING, 1)
    else:
        return "FAIL"

async def trainRoach(obs):
    rw = obs.units(ROACHWARREN).ready
    if (rw.exists):
        return await trainUnit(obs, ROACH, 2)
    else:
        return "FAIL"
    
async def buildHatchery(obs):
    if obs.minerals >= 300:
        await obs.expand_now()
        return "OK"
    else:
        return "FAIL"
 
async def prepareArmy(obs):
	if (len(obs.units(HATCHERY)) > 1):
		target = obs.game_info.map_center.towards(obs.units(HATCHERY)[1].position, 40)
		for unit in obs.units(ZERGLING).idle | obs.units(ROACH).idle:
			await obs.do(unit.attack(target))
	return "OK"

async def buildExtractor(obs):
	if obs.minerals >= 25:
		for drone in obs.workers:
			target = obs.state.vespene_geyser.closest_to(drone.position)
			if (await obs.can_place(EXTRACTOR, target.position)):
				await obs.do(drone.build(EXTRACTOR, target))
				break
			else:
				continue
		return "OK"
	else:
		return "FAIL"
    
async def buildSpawningPool(obs):
    if obs.minerals >= 200:
        hatchery = obs.units(HATCHERY).ready.first
        await obs.build(SPAWNINGPOOL, near=hatchery)
        return "OK"
    else:
        return "FAIL"
    
async def buildRoachWarren(obs):
    if obs.minerals >= 150:
        hatchery = obs.units(HATCHERY).ready.first
        await obs.build(ROACHWARREN, near=hatchery)
        return "OK"
    else:
        return "FAIL"
 
async def buildEvolutionChamber(obs):
    if obs.minerals >= 75:
        hatchery = obs.units(HATCHERY).ready.first
        await obs.build(EVOLUTIONCHAMBER, near=hatchery)
        return "OK"
    else:
        return "FAIL"

async def researchSpeedling(obs):
    sp = obs.units(SPAWNINGPOOL).ready
    if sp.exists and obs.minerals >= 100 and obs.vespene >= 100:
        await obs.do(sp.first(RESEARCH_ZERGLINGMETABOLICBOOST))
        return "OK"
    else:
        return "FAIL"

async def researchRangedAttackI(obs):
    ec = obs.units(EVOLUTIONCHAMBER).idle
    if ec.exists and obs.minerals >= 100 and obs.vespene >= 100:
        await obs.do(ec.first(RESEARCH_ZERGMISSILEWEAPONSLEVEL1))
        return "OK"
    else:
        return "FAIL"

async def researchArmorI(obs):
    ec = obs.units(EVOLUTIONCHAMBER).idle
    if ec.exists and obs.minerals >= 150 and obs.vespene >= 150:
        await obs.do(ec.first(RESEARCH_ZERGGROUNDARMORLEVEL1))
        return "OK"
    else:
        return "FAIL"


async def moveDronesToGas(obs):
	for extractor in obs.units(EXTRACTOR):
		if (extractor.assigned_harvesters < 3):
			for drone in obs.workers.random_group_of(3 - extractor.assigned_harvesters):
				await obs.do(drone.gather(extractor))
			return "OK"
	return "FAIL"

async def inject(obs):
    for queen in obs.units(QUEEN).idle:
        abilities = await obs.get_available_abilities(queen)
        if AbilityId.EFFECT_INJECTLARVA in abilities:
            await obs.do(queen(EFFECT_INJECTLARVA, obs.units(HATCHERY).closest_to(queen.position)))
                
async def attack(obs):
    target = obs.known_enemy_structures.random_or(obs.enemy_start_locations[0]).position
    for unit in obs.units(ZERGLING) | obs.units(ROACH):
        await obs.do(unit.attack(target))
    return "OK"

# TODO: Attack better. Zerglings arrive before roaches.
# TODO: Add rally point for hatcheries
# TODO: Move initial overlord








            
            