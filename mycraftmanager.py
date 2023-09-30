class Mapmanager():
    def __init__(self):
        self.model = "gfx/models/block.egg"
        self.texture = "gfx/textures/block.png"
        self.color = (0,1,0,1)

    def startNew(self):
        self.land = render.attachNewNode("Land")

    def addBlock(self,position):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.block.setColor(self.color)
        self.block.reparentTo(self.land)

    def clear(self):
        self.land.removeNode()
        self.startNew()

    def loadLand(self, filename):
        self.clear()
        with open(filename, "r") as file:
            y = 0
            for string in file:
                x = 0
                string = string.split(" ")
                for number in string:
                    for z in range(int(number)+1):
                        block = self.addBlock((x, y, z))
                    x += 1
                y += 1


