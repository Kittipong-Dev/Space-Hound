import pygame
import sys
from scripts.Animation import Animation
from scripts.Gui.InventoryGui import InventoryGui
from scripts.Player import Player
from scripts.Tilemap import Tilemap
from scripts.utils import load_image, load_images, transform_images
from scripts.PhysicsEntity import PhysicsEntity
from scripts.Ores import Ores
from scripts.Mine import Mine
from scripts.Gui.MainGui import MainGui
from scripts.Text import Text
from scripts.Database.Character import Character
from scripts.Database.Inventory import Inventory
from scripts.Gui.CreateCharacterGui import CreateCharacterGui
from scripts.Gui.LoadingGui import LoadingGui
from scripts.Gui.SpinPlayerGui import SpinPlayerGui
from scripts.InputBox import InputBox
from scripts.Level import Level

RENDER_SCALE = 4.0

# The Game class represents a game in which the player controls a character and interacts with the
# environment.
class Game:
    def __init__(self):
        """
        This function initializes the game by setting up the display window, loading images, creating
        the tilemap, spawning ores, creating the player, and setting up the GUI.
        """
        pygame.init()

        # Display
        # The code snippet is setting up the display window for the game using the Pygame library.
        pygame.display.set_caption('Space Hound')
        self.screen = pygame.display.set_mode((1024, 579), pygame.RESIZABLE)
        self.display = pygame.Surface((256, 144), pygame.SRCALPHA)
        self.minimap = pygame.Surface((256, 256))
        self.clock = pygame.time.Clock()

        # Images
        self.assets = {
            'grass' : transform_images(load_images('tiles/grass'), (16, 16)),
            'stone' : transform_images(load_images('tiles/stone'), (16, 16)),
            'ores' : transform_images(load_images('tiles/ores', 'a'), (16, 16)),
            'decor' : load_images('tiles/decor', 'a'),
            'water' : load_images('tiles/water'),
            'gui/main' : load_images('gui/main/', 'a'),
            'gui/inventory': load_images('gui/inventory/','a'),
            'player/idley+1' : Animation(load_images('entities/player/idley+1', 'a'), img_dur=4),
            'player/idley-1' : Animation(load_images('entities/player/idley-1', 'a'), img_dur=4),
            'player/idlex' : Animation(load_images('entities/player/idlex', 'a'), img_dur=4),
            'player/runx' : Animation(load_images('entities/player/runx', 'a'), img_dur=7),
            'player/runy-1' : Animation(load_images('entities/player/runy-1', 'a'), img_dur=11),
            'player/runy+1' : Animation(load_images('entities/player/runy+1', 'a'), img_dur=11),
            'items/ore extractor/0' : load_image('items/ore extractor/0.png', 'a'),
            'gui/create character' : load_images('gui/create character', 'a'),
            'gui/loading' : load_images('gui/loading', 'a'),
            'gui/spin player' : load_images('gui/spin player', 'a'),
            'gui/input box' : load_images('gui/input box'),
        }

        # Tilemap
        self.tilemap = Tilemap(self, tile_size=16)

        # Load map
        try:
            self.tilemap.load('data/map/0.json')
        except FileNotFoundError:
            pass

        # Ore
        self.ores = []
        max_ore = len(self.tilemap.extract([('ores', 1)], keep=True))
        for ore in self.tilemap.extract([('ores', 0), ('ores', 1)], keep=False):
            self.ores.append(Ores(self, ore['pos'], ore['variant'], max_ore))

        # Char id
        self.char_id = int()

        # Player
        self.movement = [False, False, False, False]
        self.player = Player(self, (150, 120), (16, 17))

        # Ore extractor
        self.mine = Mine(self)

        # Event
        self.clicking = False

        # Camera movement
        self.scroll = [0, 0]

        # Minimap
        self.miniscroll = [0, 0]

        # Start game
        self.playing = False

        # Gui
        # Main
        self.on_main_gui = True
        self.main_gui = MainGui(self)
        # Inventory
        self.on_inventory = False
        self.inventory = InventoryGui(self)
        # Create character
        self.create_btns = list()
        y = 2
        for i in range(3):
            self.create_btns.append(CreateCharacterGui(self, (self.display.get_width() - 100, y), i))
            y += 48
        # Loading
        self.loading_gui = LoadingGui(self)
        self.spin_player_gui = SpinPlayerGui(self)
        # Input box
        self.inputing = False
        self.input_box = ''


        # Test database #####
        self.replace = False

        self.level = Level(self)

    def run(self):
        """
        The above function is a game loop that updates and renders various game elements such as the
        tilemap, player, ores, minimap, and GUI.
        """
        while True:

            # Display
            self.display.fill((84, 154, 204))

            # Mouse position
            mpos = pygame.mouse.get_pos()
            mpos = (mpos[0] / RENDER_SCALE, mpos[1] / RENDER_SCALE)
            # if self.clicking:
            #     print(mpos)
            #     self.clicking = False

            if self.playing:
                # Camera movement
                self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 5
                self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1]) / 5
                render_scroll = (int(self.scroll[0]), int(self.scroll[1]))

                # Tilemap
                self.tilemap.render(self.display, render_scroll)

                # Ore
                for ore in self.ores.copy():
                    Mine(self).update(ore, mpos, self.clicking, render_scroll)
                    ore.update()
                    ore.render(self.display, render_scroll)
                    ore.respawn(ore, self.ores, self.display, render_scroll)

                # Player
                spd_factor = 2
                # Movement keys are [A D W S]
                self.player.update(self.tilemap, movement=((self.movement[1] - self.movement[0]) * spd_factor, (self.movement[3] - self.movement[2]) * spd_factor))
                self.player.render(self.display, render_scroll)

                # Minimap:
                self.miniscroll[0] += (self.player.rect().centerx - self.minimap.get_width() / 2 - self.miniscroll[0])
                self.miniscroll[1] += (self.player.rect().centery - self.minimap.get_height() / 2 - self.miniscroll[1])
                mini_scroll = (int(self.miniscroll[0]), int(self.miniscroll[1]))

                self.minimap.fill((84, 154, 204))
                self.tilemap.render(self.minimap, mini_scroll)
                for ore in self.ores.copy():
                    ore.render(self.minimap, mini_scroll)
                self.player.render(self.minimap, mini_scroll)
                transition_surf = pygame.Surface((self.minimap.get_size()))
                transition_surf.fill((119, 0, 255))
                pygame.draw.circle(transition_surf, (255, 255, 255), (self.minimap.get_width() // 2, self.minimap.get_height() // 2), 104)
                transition_surf.set_colorkey((255, 255, 255))
                self.minimap.blit(transition_surf, (0, 0))
                self.minimap.set_colorkey((119, 0, 255))
                self.display.blit(pygame.transform.scale(self.minimap, (32, 32)), (self.display.get_width() - 37, 5))

                # Gui
                # Main
                level = Character().load(self.char_id)[Character().INDEXPAIR['level']]
                self.main_gui.update(self.display, mpos, self.on_main_gui, level)
                self.main_gui.render(self.display)
                # Inventory
                if self.on_inventory:
                    self.inventory.update()
                    self.inventory.render(self.display)
                    self.on_main_gui = False
                else:
                    self.on_main_gui = True
                    self.inventory.y = 0

                # test database
                # new_level = Character().load(self.char_id)[Character().INDEXPAIR['level']] + 1 ##
                # new_exp = 30.324
            
                self.level.update()

            if not self.playing:
                # Gui
                # loading
                self.loading_gui.update()
                self.loading_gui.render(self.display)
                self.spin_player_gui.update()
                self.spin_player_gui.render(self.display)
                for create_btn in self.create_btns:
                    create_btn.update(self.clicking, mpos)
                    create_btn.render(self.display)

                if self.inputing:
                    # Input Box
                    self.input_box.update(self.clicking, mpos)
                    self.input_box.render(self.display)
            
            # test database ##############
            # self.show_query = Text(f"{Character().query()}", 16, pos=(0, 50))
            # i = 60
            # self.datas = list()
            # for char_id in Character().query():
            #     i += 10
            #     self.datas.append(Text(str(Character().load(char_id)), 16, pos=(0, i)))
            # for data in self.datas:
            #     data.render(self.display)

            # self.show_query.render(self.display)

        
            try:
                delete_id = Character().query()[0]
            except IndexError:
                pass

            # Event
            for event in pygame.event.get():
                if self.inputing:
                    self.input_box.event(event)

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.clicking = True

                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.clicking = False

                if event.type == pygame.KEYDOWN:

                    if self.playing:
                        if event.key == pygame.K_s:
                            self.movement[3] = True
                        if event.key == pygame.K_w:
                            self.movement[2] = True
                        if event.key == pygame.K_d:
                            self.movement[1] = True
                        if event.key == pygame.K_a:
                            self.movement[0] = True

                        if self.on_main_gui:
                            if event.key == pygame.K_1:
                                print('1')
                            if event.key == pygame.K_2:
                                print('2')
                            if event.key == pygame.K_3:
                                print('3')
                            if event.key == pygame.K_4:
                                print('4')
                            if event.key == pygame.K_5:
                                print('5')
                            if event.key == pygame.K_6:
                                print('6')
                            if event.key == pygame.K_7:
                                print('7')
                            if event.key == pygame.K_8:
                                print('8')
                            if event.key == pygame.K_9:
                                print('9')
                            if event.key == pygame.K_0:
                                print('0')
                        if event.key == pygame.K_ESCAPE:
                            self.playing = False
                    
                        # test database ########
                        if self.on_inventory:
                            
                            if event.key == pygame.K_1:
                                Inventory().place('gold', 0, self.char_id)
                            if event.key == pygame.K_2:
                                Inventory().place('gold', 1, self.char_id)
                            if event.key == pygame.K_3:
                                Inventory().place('diamond', 2, self.char_id)
        

                            if event.key == pygame.K_r:
                                self.replace = not self.replace

                            if self.replace:
                                if event.key == pygame.K_1:
                                    Inventory().replace('diamond', 0, self.char_id)
                                if event.key == pygame.K_2:
                                    Inventory().replace('ruby', 1, self.char_id)
                                if event.key == pygame.K_3:
                                    Inventory().replace('gold', 2, self.char_id)

                            if event.key == pygame.K_g:
                                print(Inventory().load(self.char_id))



                        if event.key == pygame.K_e:
                            self.on_inventory = not self.on_inventory

                    # if event.key == pygame.K_b:
                    #     Character().save(self.char_id, new_level, new_exp)

                if event.type == pygame.KEYUP:
                    if self.playing:
                        if event.key == pygame.K_s:
                            self.movement[3] = False
                        if event.key == pygame.K_w:
                            self.movement[2] = False
                        if event.key == pygame.K_d:
                            self.movement[1] = False
                        if event.key == pygame.K_a:
                            self.movement[0] = False

            # Display
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))

            pygame.display.update()
            self.clock.tick(60)

Game().run()