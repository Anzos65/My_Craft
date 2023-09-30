from direct.showbase.ShowBase import ShowBase
from mycraftmanager import Mapmanager

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager()
        self.land.startNew()
        self.land.loadLand("land.txt")
        base.camLens.setFov(90)

game = Game()
game.run()