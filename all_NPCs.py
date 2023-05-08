class NPC:
    def __init__(self, name = str, lvl = int, HP = int, color = str, position = list):
        self.name = name + f'_{lvl}lvl'
        self.HP = HP + HP * lvl * 0.5
        self.color = color
        self.position = position[0:3]
    
    def __str__(self):
        return self.name



black_swarm = NPC('black_swarm', 1, 10, '#444444', [5, 5, 5])
