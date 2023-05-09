import maps.level_1.map_1 as LVL1_MAP1
import maps.level_1.map_2 as LVL1_MAP2
class Map:
    def __init__(self, name = str, NPCs = dict, game_field = list):
        self.name = name
        self.NPCs = NPCs
        self.game_field = game_field

    def __init__(self, dict):
        self.name = dict['name']
        self.NPCs = dict['NPCs']
        self.game_field = dict['game_field']

    def __str__(self) -> str:
        return f'map: {self.name}'


all_levels = {'level_1': [Map(LVL1_MAP1.map_1), Map(LVL1_MAP2.map_2)]}

#Правила формирования игрового поля:
# от 0 до 9  -> тайлы карты где:
# 6 - пропасть убивает
# 7 - лава вредит
# 8 глубокая вода сильно замедляет
# 9 вода замедляет
# 0 трава без эффектов
# 1 стена не дает пройти
# 2 лестница поднимает на уровень выше
# 3 - ... высшие уровни замка
# A - глубый моб





