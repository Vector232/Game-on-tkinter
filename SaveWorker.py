# Читает файл сохранения
import json
import pickle
import maps.all_maps as AM

def importSaves(main):
    with open('saves/save0.pickle', 'rb') as f:
        data = pickle.load(f)
        # загружаем состояние игры
        main.game_started = data['game']['game_started']
        main.free_action_points = data['game']['AP']
        # загружаем состояние игрока
        main.player.position = data['player']['player_position']
        main.player.HP = data['player']['player_HP']
        # загружаем состояние всех игровых карт
        AM.all_levels = data['maps']
        
       

    print('Sim-Loaded')

# Пишет файл сохранения
def exportSaves(main):
    data = {}
    with open('saves/save0.pickle', 'wb') as f:
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
        data['maps'] = AM.all_levels
        pickle.dump(data, f)
    print('Sim-Saved')