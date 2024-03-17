import time
import math
from termcolor import colored
from data import JOURNEY_IN_DAYS, COST_FOOD_HUMAN_COPPER_PER_DAY, COST_FOOD_HORSE_COPPER_PER_DAY, COST_TENT_GOLD_PER_WEEK, COST_HORSE_SILVER_PER_DAY

##################### O03 #####################

def copper2silver(amount: int) -> float:
    return amount / 10

def silver2gold(amount:int) -> float:
    return amount / 5

def copper2gold(amount: int) -> float:
    return silver2gold(copper2silver(amount))

def platinum2gold(amount: int) -> float:
    return amount * 25

def getPersonCashInGold(personCash: dict) -> float:
    total_gold = 0
    total_gold += copper2gold(personCash.get('copper', 0))
    total_gold += silver2gold(personCash.get('silver', 0))
    total_gold += personCash.get('gold', 0)
    total_gold += platinum2gold(personCash.get('platinum', 0))
    return round(total_gold, 2)

##################### O05 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    totaal_food_kosten_koper = people * COST_FOOD_HUMAN_COPPER_PER_DAY * JOURNEY_IN_DAYS
    totaal_food_kosten_koper += horses * COST_FOOD_HORSE_COPPER_PER_DAY * JOURNEY_IN_DAYS
    return round(copper2gold(totaal_food_kosten_koper), 2)


##################### O06 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    filtered_lijst = []

    for item in list:
        if item.get(key) == value:
            filtered_lijst.append(item)
        
    return filtered_lijst


def getAdventuringPeople(people: list) -> list:
    filtered_list = []

    for person in people:
        if person.get('adventuring') == True:
            filtered_list.append(person)

    return filtered_list

def getShareWithFriends(friends:list) -> list:
    filtered_list = []

    for friend in friends:
        if friend.get('shareWith') == True:
            filtered_list.append(friend)

    return filtered_list

def getAdventuringFriends(friends:list) -> list:
    filtered_list = []

    for friend in friends:
        if friend.get('shareWith') == True and friend.get('adventuring') == True:
            filtered_list.append(friend)

    return filtered_list

##################### O07 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    #  if people % 2 == 0:
    #     total_needed_horses = people // 2
    #     return total_needed_horses
    #  else:
    #     total_needed_horses = (people // 2) + 1
    #     return total_needed_horses
    return math.ceil(people / 2)

def getNumberOfTentsNeeded(people:int) -> int:
    # if people % 3 == 0:
    #     total_needed_tents = people // 3
    #     return total_needed_tents
    # else:
    #     total_needed_tents = (people // 3) + 1
    #     return total_needed_tents
    return math.ceil(people / 3)

def getTotalRentalCost(horses: int, tents: int) -> float:
    total_cost_horse_silver = (horses * COST_HORSE_SILVER_PER_DAY) * JOURNEY_IN_DAYS 

    total_cost_tent = (tents * COST_TENT_GOLD_PER_WEEK ) * math.ceil(JOURNEY_IN_DAYS/7) 

    total_cost = silver2gold(total_cost_horse_silver) + total_cost_tent
    return total_cost

##################### O08 #####################

def getItemsAsText(items:list) -> str:
    pass

def getItemsValueInGold(items:list) -> float:
    pass

##################### O09 #####################

def getCashInGoldFromPeople(people:list) -> float:
    pass

##################### O10 #####################

def getInterestingInvestors(investors:list) -> list:
    pass

def getAdventuringInvestors(investors:list) -> list:
    pass

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    pass

##################### O11 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    pass

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    pass

##################### O13 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    pass

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    pass

##################### O14 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

##################### view functions #####################

def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()