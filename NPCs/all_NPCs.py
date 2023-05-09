class NPC:
    def __init__(self, name = 'NoName', lvl = 1, HP = 100, color = '#999999', position = [-1, -1, -1]):
        self.name = name + f'_{lvl}lvl'
        self.HP = HP + HP * lvl * 0.5
        self.color = color
        self.position = position[0:3]
    
    '''def __init__(self, dict):
        self.name = dict['name']
        self.HP = dict['HP']
        self.color = dict['color']
        self.position = dict['position']'''
    
    def __str__(self):
        return self.name

def SetBlackSwarm(lvl = 1, position = [-1, -1, -1]):
    return NPC('Black Sworm', lvl, 10, '#444444', position)


