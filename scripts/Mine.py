
class Mine:
    def __init__(self, game):
        self.game = game
        # self.pos = pos
        self.click = 0
        self.damage = 10
    
    def update(self, ore, mpos, clicking, render_scroll):
        if ore.rect(render_scroll).collidepoint(mpos) and clicking:
            ore.hp = max(0, ore.hp - self.damage)
            print(ore.hp)
            self.game.clicking = False
            ore.clicking = True

    def render(self, surf, offset):
        pass