import SaveWorker as sw

class exp:
    def __init__(self, x_p, y_p):
        self.x_p = x_p
        self.y_p = y_p
        sw.importSaves(self)


a = exp(-1, -1)
a.game_started = True

sw.exportSaves(a)
sw.importSaves(a)
print(a.game_started)





