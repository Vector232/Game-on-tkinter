# Читает файл сохранения
def importSaves(main):
    with open('save0.txt', 'r', encoding='utf8') as f:
        for line in f:
            main.game_started = True if line.split('=')[1].strip() == 'True' else False
            print(main.game_started)
            main.player.position = list(map(float, f.readline().split('=')[1].split(',')))
    print('Sim-Loaded')

# Пишет файл сохранения
def exportSaves(main):
    with open('save0.txt', 'w', encoding='utf8') as f:
        f.write(f'game_started={main.game_started}\n')
        f.write(f'player_position={main.player.position[0]},{main.player.position[1]}\n')
    print('Sim-Saved')