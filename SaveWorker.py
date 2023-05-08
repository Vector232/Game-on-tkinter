# Читает файл сохранения
import json
import all_maps as am

def importSaves(main):
    with open('save0.json', 'r', encoding='utf8') as f:
        data = json.load(f)
        main.game_started = data['game_started']
        main.free_action_points = data['AP']
        main.player.position = data['player_position']
        main.player.HP = data['player_HP']
        am.map_1.NPSc = data['maps']['map_1']['NPCs']
        am.map_1.game_field = data['maps']['map_1']['game_field']
    print('Sim-Loaded')

# Пишет файл сохранения
def exportSaves(main):
    data = {}
    with open('save0.json', 'w', encoding='utf8') as f:
        data['game_started'] = main.game_started
        data['AP'] = main.free_action_points
        data['player_position'] = [main.player.position[0], main.player.position[1]]
        data['player_HP'] = main.player.HP
        # сохраняем состояние всех игровых карт
        data['maps'] = {} # создаем раздел с картами
        for map in am.maps: # перебираем карты в списке карт
            data['maps'][map.name] = {} # создаем раздел для каждой карты
            data['maps'][map.name]['NPCs'] = {} # создаем раздел для хранения состояний НИП
            for NPC in map.NPCs: # перебираем всех НИП
                data['maps'][map.name]['NPCs'] = {NPC: {'HP': map.NPCs[NPC].HP, 'color': map.NPCs[NPC].color, 'position': map.NPCs[NPC].position}}
            data['maps'][map.name]['game_field'] = map.game_field
        json.dump(data, f)
    print('Sim-Saved')