from tkinter import *
from tkinter.messagebox import askyesno
from random import *
from winsound import *
import SaveWorker as sw
import player as p
import all_maps as am

class Main_Class:
    #Создаем основное окно
    def __init__(self):
        self.focus_on = "start_menu"

        self.window = Tk()
        self.window["bg"] = "white"
        self.window.geometry('600x500')
        self.window.title("Симуляция А101")
        self.window.attributes('-fullscreen', True)

        self.global_event = 'none'
        self.bg_color = "#000000"
        self.text_size = 35

        self.game_started = False
        self.free_action_points = 0
        self.player = p.Player()
        
        try:
            sw.importSaves(self)
        except:
            sw.exportSaves(self)

        self.height = self.window.winfo_screenheight()
        self.width = self.window.winfo_screenwidth()
        
        self.window.bind("<F11>", self.FullscreenChanger)
        self.window.bind("<Escape>", self.ExitProtocol)
        self.window.bind("<F1>", self.logInfo)
        self.window.bind("<F5>", self.QuickSave)
        self.window.bind("<F9>", self.QuickLoad)

        self.StartMenu()
        self.window.mainloop()
    
    #Создаем стартовое меню и запускаем анимацию на фоне
    def StartMenu(self):
        
        if not self.focus_on in ("setting_menu"):
            PlaySound(None, SND_PURGE)
            PlaySound('NewComposition1.wav', SND_ASYNC | SND_NOSTOP)

        self.focus_on = "start_menu"

        self.startMenuCanvas = Canvas(self.window, bg="black", highlightthickness=0, height=self.height, width=self.width)
        self.startMenuCanvas.pack()

        self.animation_start()

        self.mainFrame = LabelFrame(self.startMenuCanvas, text="Симуляция А101", fg="green", bg=self.bg_color, bd="0", font=('Comic Sans MS', self.text_size))
            
        self.mainFrame.place(relx=0.35, rely=0.3)

        if not self.game_started:
            buttonNewGame = Button(self.mainFrame, text="ЗАПУСТИТЬ СИМУЛЯЦИЮ", fg="green", activebackground='#003300', bg=self.bg_color, bd="0", font=('Comic Sans MS', self.text_size), command=self.click_NewGame)
            buttonNewGame.pack()
        else:
            buttonRestartGame = Button(self.mainFrame, text="ПЕРЕЗАПУСТИТЬ СИМУЛЯЦИЮ", fg="green", activebackground='#003300', bg=self.bg_color, bd="0", font=('Comic Sans MS', self.text_size), command=self.click_RestartGame)
            buttonRestartGame.pack()
            buttonContinue = Button(self.mainFrame, text="ПРОДОЛЖИТЬ СИМУЛЯЦИЮ", fg="green", activebackground='#003300', bg=self.bg_color, bd="0", font=('Comic Sans MS', self.text_size), command=self.click_Continue)
            buttonContinue.pack()

        buttonSettings = Button(self.mainFrame, text="НАСТРОИТЬ СИМУЛЯЦИЮ", fg="green", activebackground='#003300', bg=self.bg_color, bd="0", font=('Comic Sans MS', self.text_size), command=self.click_Settings)
        buttonSettings.pack()

        buttonExit = Button(self.mainFrame, text="ПРЕРВАТЬ СИМУЛЯЦИЮ", fg="green", bg=self.bg_color, activebackground='#003300', bd="0", font=('Comic Sans MS', self.text_size), command=self.ExitMessagebox)
        buttonExit.pack()


    def SettingMenu(self):
        self.focus_on = "setting_menu"

        self.settingMenuFrame = LabelFrame(self.startMenuCanvas, text="Симуляция А101 -> Настройки", fg="green", bg=self.bg_color, bd="0", font=('Comic Sans MS', self.text_size))
        self.settingMenuFrame.place(relx=0.35, rely=0.3)

        buttonSettings = Button(self.settingMenuFrame, text="НАСТРОИТЬ 1", fg="green", bg=self.bg_color, activebackground='#003300', bd="0", font=('Comic Sans MS', self.text_size))
        buttonSettings.pack()
        scaleTextSizeSetting = Scale(self.settingMenuFrame, from_=20, to=50, orient=HORIZONTAL, label='РАЗМЕР ТЕКСТА', fg='green', activebackground='#003300', bg=self.bg_color, 
                               bd=0, font=('Comic Sans MS', self.text_size), troughcolor='#001100', length=500, highlightbackground=self.bg_color, command=self.ChangeTextSize)
        scaleTextSizeSetting.pack()
        buttonSettings = Button(self.settingMenuFrame, text="НАСТРОИТЬ 3", fg="green", bg=self.bg_color, activebackground='#003300', bd="0", font=('Comic Sans MS', self.text_size))
        buttonSettings.pack()
        buttonSettings = Button(self.settingMenuFrame, text="НАЗАД", fg="green", bg=self.bg_color, activebackground='#003300', bd="0", font=('Comic Sans MS', self.text_size), command=self.click_back_set_to_main)
        buttonSettings.pack()

    def click_NewGame(self):
        print("click_NewGame")
        self.startMenuCanvas.pack_forget()
        self.game_started = True
        self.TheGame()
        Beep(400,  200)

    def click_RestartGame(self):
        print("click_RestartGame")
        self.startMenuCanvas.pack_forget()
        self.game_started = True
        self.player.position = [-1, -1]
        self.TheGame()
        Beep(400,  200)
    
    def click_Continue(self):
        print("click_Continue")
        self.startMenuCanvas.pack_forget()
        sw.importSaves(self)
        self.TheGame()
        Beep(400,  200)

    def click_Settings(self):
        self.mainFrame.place_forget()
        self.SettingMenu()
        print("click_Settings -> ", self.focus_on)
        Beep(400,  200)

    def click_back_set_to_main(self):
        print("click_back_set_to_main ->", self.focus_on)
        self.startMenuCanvas.pack_forget()
        self.StartMenu()
        Beep(400,  200)

    def QuickSave(self, event):
        print('press -> QuickSave')
        if self.focus_on == 'mini_game':
            sw.exportSaves(self)

    def QuickLoad(self, event):
        print('press -> QuickLoad')
        if self.focus_on == 'mini_game':
            self.GameCanvas.pack_forget()
            sw.importSaves(self)
            self.TheGame(True)


    def ChangeTextSize(self, val):
        self.text_size = val
        print("text_size =", self.text_size)

    def ExitProtocol(self, event = None):
        if self.focus_on == "start_menu":
            self.ExitMessagebox()
        elif self.focus_on == "setting_menu":
            self.click_back_set_to_main()
        elif self.focus_on == "mini_game":
            sw.exportSaves(self)
            self.GameCanvas.pack_forget()
            self.global_event = 'back'
            self.StartMenu()
        else:
            print("menu not faund!")
            self.ExitMessagebox()

    def ExitMessagebox(self, event = None):
            Beep(400,  200)
            answer = askyesno("Покинуть симуляцию?", "Вы действительно желаете покинуть симуляцию?")
            if answer:
                print("ExitMessagebox -> YES")
                self.window.destroy()
            else: print("ExitMessagebox -> NO")

    def FullscreenChanger(self, event = None):
        print("FullscreenChanger")
        self.window.attributes("-fullscreen", not self.window.attributes("-fullscreen"))

    #Анимация на фоне меню
    def animation_start(self = None):
        digits = "1234567890йцукенгшщзхъ\фывапролджэячсмитьбю.,ЮБЬТИМСЧЯЭЖДЛОРПАВЫФ/ЪХЗЩШГНЕКУЦЙ!№;%:?*()_+"
        h = randint(0, 100)
        h = int(h/10)
        self.startMenuCanvas.delete('t' + str(h))
        for _ in range(randint(30, 40)):
            self.startMenuCanvas.create_text(randint(0, self.width), randint(0, self.height), font=('Comic Sans MS', randint(10, 20)), fill="#004100", text=choice(digits), tag="t" + str(h))   
        self.startMenuCanvas.update()

        self.window.after(100, self.animation_start)

    #Основное игровое поле
    def TheGame(self, quickload = False):
        print('Game -> Starting')
        self.focus_on = "mini_game"

        self.GameCanvas = Canvas(self.window, bg="black", highlightthickness=0, height=self.height, width=self.width)
        self.GameCanvas.pack()

        PlaySound(None, SND_PURGE)
        # Размеры игрового поля
        self.scale = 40
        self.scale_x = self.height / self.scale
        self.scale_y = self.height / self.scale

        if self.player.position == [-1, -1]:
            self.player.position = [self.scale_x * 20,  self.scale_y * 20]

        print('game_field -> Expanding')
        self.HP_bar()

        self.game_field(am.all_maps['level_1'][0])
        self.InfoOnUI()

        self.window.bind("<Up>", self.player_move)
        self.window.bind("<Down>", self.player_move)
        self.window.bind("<Left>", self.player_move)
        self.window.bind("<Right>", self.player_move)
        self.window.bind("<space>", self.player_move)
    
    def HP_bar(self):
        self.GameCanvas.delete('hp_bar')
        x = 0
        hp = self.player.HP

        if hp == 0:
            print('YOU DEAD')
        while x < self.width and hp > 0:
            self.GameCanvas.create_rectangle(x, 0, x + self.scale_x, self.scale_y, fill='#550000', tag = 'hp_bar')
            x += self.scale_x
            hp -= 100/self.scale

    # Рисует игровое поле по умолчанию или заданное поле
    def game_field(self, map_ = None):
        # Поле по умолчанию
        if map_ == None:
            colors = ['#001100', '#002200', '#003300', '#004400', '#000000']
            self.all_plates = {}
            NPC_list = []
            x, y = [0, self.scale_y]

            self.GameCanvas.delete('gamefild', 'player', 'NPC')

            for _ in range(40):
                for _ in range(40):
                    plate_color = choice(colors)
                    self.all_plates.setdefault(plate_color, []).append([x, y])# сразу пополняем словарь плиток
                    self.GameCanvas.create_rectangle(x, y, x + self.scale_x, y + self.scale_y, fill=plate_color, tag = 'gamefild')
                    y += self.scale_y
                y = self.scale_y
                x += self.scale_x

            self.player_icon = self.GameCanvas.create_rectangle(self.player.position[0], self.player.position[1], self.player.position[0] + self.scale_x, self.player.position[1] + self.scale_y, fill='#00FF00', tags='player')
            for NPC in NPC_list:
                self.GameCanvas.create_rectangle(self.NPC.position[0], self.NPC.position[1], self.NPC.position[0] + self.scale_x, self.NPC.position[1] + self.scale_y, fill=self.NPC.color, tags='NPC')
            print('game_field -> expanded')

        # Заданное поле
        else:
            colors = ['#005500', '#555555', '#999999', '#999999', '#999999', '#999999', '#999999', '#553300', '#999999']
            self.all_plates = {}
            NPC_dict = map_['NPCs']
            x, y = [0, self.scale_y]

            self.GameCanvas.delete('gamefild', 'player', 'NPC')

            for line in map_['game_field']:
                for plate in line:
                    self.all_plates.setdefault(plate, []).append([x, y])
                    self.GameCanvas.create_rectangle(x, y, x + self.scale_x, y + self.scale_y, fill=colors[plate], tag='gamefild')
                    x += self.scale_x
                x = 0
                y += self.scale_y

            self.player_icon = self.GameCanvas.create_rectangle(self.player.position[0], self.player.position[1],\
                                                                self.player.position[0] + self.scale_x, self.player.position[1] + self.scale_y,\
                                                                fill='#992200', tag = 'player')
            
            for NPC in NPC_dict:
                self.GameCanvas.create_rectangle(NPC_dict[NPC]['position'][0], NPC_dict[NPC]['position'][1], NPC_dict[NPC]['position'][0] + self.scale_x,\
                                                 NPC_dict[NPC]['position'][1] + self.scale_y, fill=NPC_dict[NPC]['color'], tag='NPC')
            
            print('game_field -> expanded')

        #if not quickload: self.minigame_loop()

        
        
    #перемещение игрока по полю
    def player_move(self, command):
        print('PRESS ->', command.keysym)
        
        move_x = 0
        move_y = 0
        
        if command.keysym == 'Up':                                                                              
            move_y = -self.scale_y
            move_x, move_y = self.next_turn_check([self.player.position[0], self.player.position[1] + move_y], [move_x, move_y])

        elif command.keysym == 'Down':
            move_y = self.scale_y
            move_x, move_y = self.next_turn_check([self.player.position[0], self.player.position[1] + move_y], [move_x, move_y])

        elif command.keysym == 'Left':
            move_x = -self.scale_x
            move_x, move_y = self.next_turn_check([self.player.position[0] + move_x, self.player.position[1]], [move_x, move_y])

        elif command.keysym == 'Right':
            move_x = self.scale_x
            move_x, move_y = self.next_turn_check([self.player.position[0] + move_x, self.player.position[1]], [move_x, move_y])
        
        elif command.keysym == 'space':
            move_x, move_y = self.next_turn_check([self.player.position[0], self.player.position[1]], [move_x, move_y])

        self.GameCanvas.move(self.player_icon, move_x, move_y)

        print('Player coord ->', self.GameCanvas.coords(self.player_icon))
        self.GameCanvas.update()
        #Beep(400, 200)

    #проверяет возможность или последствия следующего хода
    def next_turn_check(self, new_xy, move_xy):

        self.free_action_points += 100
        if self.free_action_points > 10000: self.free_action_points -= 10000

        x, y = new_xy
        move_x, move_y = move_xy

        if new_xy in self.all_plates[7]:
            print("Dont stand in the lava!")
            self.player.HP -= 10
            self.HP_bar()


        if new_xy in self.all_plates[1]:
            print("Wall in the way!")
            move_x, move_y = 0, 0
        
        elif x > self.height - self.scale_x:
            move_x = -self.height + self.scale_x

        elif x < 0:
            move_x = self.height - self.scale_x

        elif y > self.height - self.scale_y:
            move_y = -self.height + (2 * self.scale_y)

        elif y < self.scale_y:
            move_y = self.height - (2 * self.scale_y)

        self.player.position[0] += move_x
        self.player.position[1] += move_y

        self.InfoOnUI()

        return [move_x, move_y]

    def logInfo(self, event):
        print(self.game_started)
    
    def InfoOnUI(self, event = None):
            self.GameCanvas.delete('InfoOnUI')
            self.GameCanvas.create_text(self.scale_x*45, self.scale_y, font=('Comic Sans MS', self.text_size), fill="#004100", text="Information", tag='InfoOnUI')
            self.GameCanvas.create_text(self.scale_x*45, self.scale_y*4, font=('Comic Sans MS', self.text_size), fill="#004100", text="HP:  " + str(self.player.HP), tag='InfoOnUI')
            self.GameCanvas.create_text(self.scale_x*45, self.scale_y*8, font=('Comic Sans MS', self.text_size), fill="#004100", text="AP: " + str(self.free_action_points), tag='InfoOnUI')

        

app = Main_Class()