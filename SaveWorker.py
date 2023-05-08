# Читает файл сохранения
import json

def importSaves(main):
    with open('save0.json', 'r', encoding='utf8') as f:
        data = json.load(f)
        main.game_started = data['game_started']
        main.free_action_points = data['AP']
        main.player.position = data['player_position']
        main.player.HP = data['player_HP']
    print('Sim-Loaded')

# Пишет файл сохранения
def exportSaves(main):
    data = {}
    with open('save0.json', 'w', encoding='utf8') as f:
        data['game_started'] = main.game_started
        data['AP'] = main.free_action_points
        data['player_position'] = [main.player.position[0], main.player.position[1]]
        data['player_HP'] = main.player.HP
        json.dump(data, f)
    print('Sim-Saved')