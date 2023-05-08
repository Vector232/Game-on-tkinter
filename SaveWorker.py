# Читает файл сохранения
import json
import all_maps as am

def importSaves(main):
    with open('save0.json', 'r', encoding='utf8') as f:
        data = json.load(f)
        # загружаем состояние игры
        main.game_started = data['game']['game_started']
        main.free_action_points = data['game']['AP']
        # загружаем состояние игрока
        main.player.position = data['player']['player_position']
        main.player.HP = data['player']['player_HP']
        # загружаем состояние всех игровых карт
        am.all_maps = data['maps']
        
       

    print('Sim-Loaded')

# Пишет файл сохранения
def exportSaves(main):
    data = {}
    with open('save0.json', 'w', encoding='utf8') as f:
        # сохраняем игры
        data['game'] = {}
        data['game']['game_started'] = main.game_started
        data['game']['AP'] = main.free_action_points
        # сохраняем состояние игрока
        data['player'] = {}
        data['player']['name'] = 'AlfaNPC'
        data['player']['player_position'] = [main.player.position[0], main.player.position[1]]
        data['player']['player_HP'] = main.player.HP
        # сохраняем состояние всех игровых карт
        data['maps'] = am.all_maps
        json.dump(data, f)
    print('Sim-Saved')