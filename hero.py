class Hero():
    def __init__(self,pos,land):
        self.land = land
        self.hero = loader.loadModel("smiley")
        self.hero.setPos(pos)
        self.hero.setScale(0.3)
        self.hero.reparentTo(render)
        self.mode = True
        self.cameraBind()
        self.accept_events()

    def cameraBind(self):
        base.disableMouse()
        base.camera.setR(0)
        base.camera.setP(0)
        base.camera.setH(180)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0,0,1.5)

    def spectate(self):
        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos(-pos[0],-pos[1],-pos[2]-3)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn = False

    def changeView(self):
        if self.cameraOn:
            self.spectate()
        else:
            self.cameraBind()

    def turnLeft(self):
        self.hero.setH((self.hero.getH() + 5) % 360)

    def turnRight(self):
        self.hero.setH((self.hero.getH() - 5) % 360)

    def justMove(self,angle):
        pos = self.lookAt(angle)
        self.hero.setPos(pos)

    def tryMove(self,angle):
        pass

    def moveTo(self,angle):
        if self.mode == True:
            self.justMove(angle)
        else:
            self.tryMove(angle)

    def lookAt(self,angle):
        fromX = round(self.hero.getX())
        fromY = round(self.hero.getY())
        fromZ = round(self.hero.getZ())
        dx, dy = self.checkDir(angle)
        return fromX + dx, fromY + dy, fromZ

    def checkDir(self,angle):
        if 0 >= angle <= 20:
            return (0, -1)
        elif 20 >= angle <= 65:
            return (1, -1)
        elif 65 >= angle <= 110:
            return (1, 0)
        elif 110 >= angle <= 155:
            return (1, 1)
        elif 155 >= angle <= 200:
            return (0, 1)
        elif 200 >= angle <= 245:
            return (-1, 1)
        elif 245 >= angle <= 290:
            return (-1, 0)
        elif 290 >= angle <= 335:
            return (-1, -1)
        
    def back(self):
        angle = (self.hero.getH() + 180) % 360
        self.moveTo(angle)

    def forward(self):
        angle = self.hero.getH()
        self.moveTo(angle)

    def left(self):
        angle = (self.hero.getH() + 90) % 360
        self.moveTo(angle)

    def right(self):
        angle = (self.hero.getH() - 90) % 360
        self.moveTo(angle)

    def accept_events(self):
        base.accept("p", self.spectate)
        base.accept("j", self.turnLeft)
        base.accept("j"+"-repeat", self.turnLeft)
        base.accept("l", self.turnRight)
        base.accept("l"+"-repeat", self.turnRight)
        base.accept("w",self.forward)
        base.accept("s", self.back)
        base.accept("a", self.left)
        base.accept("d", self.right)