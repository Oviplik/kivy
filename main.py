from kivy.app import App
from kivy.uix.label import Label
from kivy.core.text import LabelBase
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.video import Video
import time
import random
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.config import Config
#Config.set('graphics', 'fullscreen', 1)
Window.size = (800, 480)
class MainApp(App):
    def build(self):
        self.super_box = BoxLayout(orientation='vertical')
        self.horizontal_box_btn = BoxLayout(orientation='horizontal', size_hint=(1.0, .1))
        self.vertical_box = BoxLayout(orientation='vertical', size_hint=(1.0, .9))
        self.horizontal_box = BoxLayout(orientation='horizontal', size_hint=(1.0, .0001))
        self.dict_video = {
                            'slide0': {'duration': 99999, 'source': ''},
                            'slide1': {'duration': 195, 'source': 'media/video/video_part1.mp4'},
                            'slide2': {'duration': 177, 'source': 'media/video/video_part2.mp4'},
                            'slide3': {'duration': 94.2, 'source': 'media/video/video_part3.mp4'},
                            'slide4': {'duration': 99999, 'source': ''},
                            'slide5': {'duration': 232, 'source': 'media/video/video_part4.mp4'},
                            'slide6': {'duration': 85, 'source': 'media/video/video_part5.mp4'},
                            'slide7': {'duration': 99999, 'source': ''},
                            'slide8': {'duration': 29.5, 'source': 'media/video/video_part6.mp4'},
                            'slide9': {'duration': 99999, 'source': ''},
                            'slide10': {'duration': 214, 'source': 'media/video/video_part7.mp4'},
                            'slide11': {'duration': 99999, 'source': ''},
                            'slide12': {'duration': 15.5, 'source': 'media/video/video_part8.mp4'},
                            'slide13': {'duration': 99999, 'source': ''},
                            'slide14': {'duration': 62, 'source': 'media/video/video_part9.mp4'},
                            'slide15': {'duration': 86, 'source': 'media/video/video_part10.mp4'},
                            'slide16': {'duration': 99999, 'source': ''},
                            'slide17': {'duration': 99999, 'source': ''},
                            'slide18': {'duration': 99999, 'source': ''},
                            'slide19': {'duration': 73, 'source': 'media/video/video_part11.mp4'},
                            'slide20': {'duration': 99999, 'source': ''},#конец
                            'slide21': {'duration': 78, 'source': 'media/video/video_part12.mp4'},
                            'slide22': {'duration': 99999, 'source': ''},  # конец
                            'slide23': {'duration': 112, 'source': 'media/video/video_part13.mp4'},
                            'slide24': {'duration': 99999, 'source': ''},
                            'slide25': {'duration': 134, 'source': 'media/video/video_part14.mp4'},
                            'slide26': {'duration': 99999, 'source': ''},  # конец
                            'slide27': {'duration': 108, 'source': 'media/video/video_part15.mp4'},
                            'slide28': {'duration': 99999, 'source': ''},
                            'slide29': {'duration': 91, 'source': 'media/video/video_part16.mp4'},
                            'slide30': {'duration': 99999, 'source': ''},  # переход на 14 слайд
                        }
        self.slide_count = 1
        self.score = 0
        self.win_term = ['вправо', 'вверх', 'вправо', 'влево', 'вниз', 'вверх', 'влево', 'вниз']
        self.correct_answer = ['btn_quest_2_3', 'btn_quest_2_1', 'btn_quest_2_2']
        self.slide = 'slide' + str(self.slide_count)
        self.sec = self.dict_video[self.slide]['duration']
        self.duration = self.dict_video[self.slide]['duration']
        Clock.schedule_interval(self.time_clock, 1)
        self.left_img = Image(source='media/img/battle_wolf_man_left.jpg', size_hint=(.001, .001), opacity=0)
        self.right_img = Image(source='media/img/battle_wolf_man_right.jpg', size_hint=(.001, .001), opacity=0)
        self.back_img = Image(source='media/img/background.jpg', size_hint=(.001, .001), pos_hint={'center_x': .5, 'center_y': .5}, opacity=0)
        self.btn_img = Button(background_normal = 'media/img/target.png', size_hint=(.001,.001), opacity=0, disabled=True)
        self.btn_img.bind(on_press=self.game_touch)
        self.btn_quest_1_1 = Button(text='Отправиться за стену спасать монаха', font_name='cyrillicold', halign='center',valign='center', size_hint=(.001, .001), opacity=0, pos_hint={'center_x': .5, 'center_y': .5}, background_color=(13,13,13,0.13),
                              color='#DFD064', disabled=True, on_press=lambda *args: self.quest('answer_1_1', *args))
        self.btn_quest_1_2 = Button(text='Остаться и восстанавливать стену', font_name='cyrillicold', halign='center',valign='center', size_hint=(.001, .001), opacity=0, pos_hint={'center_x': .5, 'center_y': .5}, background_color=(13,13,13,0.13),
                                 color='#DFD064', disabled=True, on_press=lambda *args: self.quest('answer_1_2', *args))
        self.btn_quest_2_1 = Button(text='Используя пистолет,\nсветовые гранаты,\nсократить дистанцию с врагом', font_name='cyrillicold', halign='center',valign='center', size_hint=(.001, .001), background_color=(13,13,13,0.13),
                                    color='#DFD064', opacity=0, disabled=True, on_press=lambda *args: self.quest('btn_quest_2_1', *args))
        self.btn_quest_2_2 = Button(text='Кромсать врага мечом/топором', font_name='cyrillicold', halign='center',valign='center', size_hint=(.001, .001), background_color=(13,13,13,0.13),
                                    color='#DFD064', opacity=0, disabled=True, on_press=lambda *args: self.quest('btn_quest_2_2', *args))
        self.btn_quest_2_3 = Button(text='Применить импульсный заряд', font_name='cyrillicold', halign='center',valign='center', size_hint=(.001, .001), background_color=(13,13,13,0.13),
                                    color='#DFD064', opacity=0, disabled=True, on_press=lambda *args: self.quest('btn_quest_2_3', *args))
        self.lab = Label(text='Проведите\nпальцем', halign='center',valign='center', font_name='cyrillicold', pos_hint={'center_x': .5, 'center_y': .5}, size_hint=(.001,.001), opacity=0, color='#DFD064')
        self.lab_steps = Label(text='Твой порядок действий', halign='center', valign='center', font_name='cyrillicold',
                          size_hint=(.001, .001), opacity=0, color='#DFD064')
        self.video = Video(source='', state='stop', options={'eos': 'loop'}, size_hint = (.001, .001))
        self.button_pause = Button(text='Меню', font_name='cyrillicold', size_hint = (.001, .001), pos_hint={'right': .0, 'top': 1.0}, opacity=0, disabled=True, background_color=(13,13,13,0.13))
        self.button_pause.bind(on_press=self.stop_video)
        self.button_next = Button(text='Пропустить', font_name='cyrillicold', size_hint = (.001, .001), pos_hint={'left': .0, 'top': 1.0}, opacity=0, disabled=True, background_color=(13,13,13,0.13), color=(13,13,13,0.13))
        self.button_next.bind(on_press=self.next_video)
        self.button_menu_start = Button(text='Начать с начала', font_name='cyrillicold', background_color=(13, 13, 13, 0.13), size_hint=(1.0,.3), opacity=1, disabled=False)
        self.button_menu_start.bind(on_press=self.start)
        self.button_menu_continue = Button(text='Продолжить', font_name='cyrillicold', background_color=(13, 13, 13, 0.13), size_hint=(1.0,.3), opacity=1, disabled=True)
        self.button_menu_continue.bind(on_press=self.stop_video)
        self.button_menu_exit = Button(text='Выход', font_name='cyrillicold', background_color=(13, 13, 13, 0.13), size_hint=(1.0,.3), opacity=1, disabled=False)
        self.button_menu_exit.bind(on_press=self.exit)
        self.horizontal_box_btn.add_widget(self.button_pause)
        self.horizontal_box_btn.add_widget(self.button_next)
        self.vertical_box.add_widget(self.button_menu_start)
        self.vertical_box.add_widget(self.button_menu_continue)
        self.vertical_box.add_widget(self.button_menu_exit)
        self.vertical_box.add_widget(self.video)
        self.vertical_box.add_widget(self.back_img)
        self.vertical_box.add_widget(self.btn_img)
        self.vertical_box.add_widget(self.btn_quest_1_1)
        self.vertical_box.add_widget(self.btn_quest_1_2)
        self.vertical_box.add_widget(self.lab_steps)
        self.horizontal_box.add_widget(self.left_img)
        self.horizontal_box.add_widget(self.lab)
        self.horizontal_box.add_widget(self.right_img)
        self.horizontal_box.add_widget(self.btn_quest_2_1)
        self.horizontal_box.add_widget(self.btn_quest_2_2)
        self.horizontal_box.add_widget(self.btn_quest_2_3)
        self.super_box.add_widget(self.horizontal_box_btn)
        self.super_box.add_widget(self.vertical_box)
        self.super_box.add_widget(self.horizontal_box)
        return self.super_box

    def just_func(self,dt):
        pass

    def start(self, instance):
        Clock.schedule_interval(self.just_func, 1)
        self.score = 0
        self.slide_count = 1
        self.slide = 'slide' + str(self.slide_count)
        self.sec = self.dict_video[self.slide]['duration']
        self.duration = self.dict_video[self.slide]['duration']
        self.video.source = 'media/video/video_part1.mp4'
        self.btn_quest_1_1.text='Отправиться за стену спасать монаха'
        self.btn_quest_1_2.text='Остаться и восстанавливать стену'
        self.back_img.source = 'media/img/background.jpg'
        self.left_img.source='media/img/battle_wolf_man_left.jpg'
        self.right_img.source='media/img/battle_wolf_man_right.jpg'
        self.win_term = ['вправо', 'вверх', 'вправо', 'влево', 'вниз', 'вверх', 'влево', 'вниз']
        self.correct_answer = ['btn_quest_2_3', 'btn_quest_2_1', 'btn_quest_2_2']
        self.lab.text='Проведите\nпальцем'
        self.button_pause.size_hint=(.5, 1.0)
        self.button_next.size_hint = (.5, 1.0)
        self.button_pause.opacity = 1
        self.button_next.opacity = 1
        self.button_pause.disabled = False
        self.button_next.disabled = False
        self.video.state = 'stop'
        self.stop_video('play')

    def exit(self, instance):
        app.stop()

    def stop_video(self, instance):
        self.button_next.disabled = True
        if self.video.state == 'play' and self.slide_count in [1,2,3,5,6,8,10,12,14,15,19,20,21,22,23,25,26,27,29]:
            self.video.state = 'pause'
            self.video.size_hint = (.001, .001)
            self.button_menu_start.size_hint = (1.0,.3)
            self.button_menu_start.opacity = 1
            self.button_menu_start.disabled = False
            self.button_menu_continue.size_hint = (1.0,.3)
            self.button_menu_continue.opacity = 1
            self.button_menu_continue.disabled = False
            self.button_menu_exit.size_hint = (1.0,.3)
            self.button_menu_exit.opacity = 1
            self.button_menu_exit.disabled = False
        elif self.slide_count in [4,7,11] and self.button_menu_continue.disabled == True:
            self.btn_quest_1_1.size_hint = (.001, .001)
            self.btn_quest_1_2.size_hint = (.001, .001)
            self.btn_quest_1_1.opacity = 0
            self.btn_quest_1_2.opacity = 0
            self.btn_quest_1_1.disabled = True
            self.btn_quest_1_2.disabled = True
            self.button_menu_start.size_hint = (1.0,.3)
            self.button_menu_start.opacity = 1
            self.button_menu_start.disabled = False
            self.button_menu_continue.size_hint = (1.0,.3)
            self.button_menu_continue.opacity = 1
            self.button_menu_continue.disabled = False
            self.button_menu_exit.size_hint = (1.0,.3)
            self.button_menu_exit.opacity = 1
            self.button_menu_exit.disabled = False
        elif self.slide_count in [4, 7, 11] and self.button_menu_continue.disabled == False:
            self.btn_quest_1_1.size_hint=(1.0, .3)
            self.btn_quest_1_2.size_hint=(1.0, .3)
            self.btn_quest_1_1.opacity=1
            self.btn_quest_1_2.opacity=1
            self.btn_quest_1_1.disabled = False
            self.btn_quest_1_2.disabled = False
            self.button_menu_start.size_hint = (.001,.001)
            self.button_menu_start.opacity = 0
            self.button_menu_start.disabled = True
            self.button_menu_continue.size_hint = (.001,.001)
            self.button_menu_continue.opacity = 0
            self.button_menu_continue.disabled = True
            self.button_menu_exit.size_hint = (.001,.001)
            self.button_menu_exit.opacity = 0
            self.button_menu_exit.disabled = True
        elif self.slide_count==16 and self.button_menu_continue.disabled == True:
            self.lab_steps.size_hint = (.001, .001)
            self.lab_steps.opacity = 0
            self.vertical_box.size_hint = (1.0, .9)
            self.horizontal_box.size_hint = (1.0, .001)
            self.horizontal_box.padding = (.0,.0,3.5,.0)
            self.btn_quest_2_1.size_hint = (.001, .001)
            self.btn_quest_2_2.size_hint = (.001, .001)
            self.btn_quest_2_3.size_hint = (.001, .001)
            self.btn_quest_2_1.opacity = 0
            self.btn_quest_2_2.opacity = 0
            self.btn_quest_2_3.opacity = 0
            self.btn_quest_2_1.disabled = True
            self.btn_quest_2_2.disabled = True
            self.btn_quest_2_3.disabled = True
            self.button_menu_start.size_hint = (1.0,.3)
            self.button_menu_start.opacity = 1
            self.button_menu_start.disabled = False
            self.button_menu_continue.size_hint = (1.0,.3)
            self.button_menu_continue.opacity = 1
            self.button_menu_continue.disabled = False
            self.button_menu_exit.size_hint = (1.0,.3)
            self.button_menu_exit.opacity = 1
            self.button_menu_exit.disabled = False
        elif self.slide_count==16 and self.button_menu_continue.disabled == False:
            self.vertical_box.size_hint = (1.0, .1)
            self.lab_steps.size_hint = (1., 1.)
            self.lab_steps.opacity = 1
            self.horizontal_box.size_hint = (1.0, .9)
            self.horizontal_box.padding = (.0, .0, 3.5, .0)
            self.btn_quest_2_1.size_hint=(.3, 1.0)
            self.btn_quest_2_2.size_hint=(.3, 1.0)
            self.btn_quest_2_3.size_hint=(.3, 1.0)
            self.btn_quest_2_1.opacity=1
            self.btn_quest_2_2.opacity=1
            self.btn_quest_2_3.opacity=1
            self.btn_quest_2_1.disabled = False
            self.btn_quest_2_2.disabled = False
            self.btn_quest_2_3.disabled = False
            self.button_menu_start.size_hint = (.001,.001)
            self.button_menu_start.opacity = 0
            self.button_menu_start.disabled = True
            self.button_menu_continue.size_hint = (.001,.001)
            self.button_menu_continue.opacity = 0
            self.button_menu_continue.disabled = True
            self.button_menu_exit.size_hint = (.001,.001)
            self.button_menu_exit.opacity = 0
            self.button_menu_exit.disabled = True
            self.correct_answer = ['btn_quest_2_3', 'btn_quest_2_1', 'btn_quest_2_2']
        elif self.slide_count in [9,18] and self.button_menu_continue.disabled == True:
            self.video.size_hint = (.001, .001)
            self.win_term.insert(0, 'pause')
            self.vertical_box.size_hint = (1.0, .9)
            self.horizontal_box.size_hint=(1.0, .001)
            self.left_img.size_hint = (.001,.001)
            self.left_img.opacity = 0
            self.right_img.size_hint = (.001,.001)
            self.right_img.opacity = 0
            self.lab.size_hint = (.001,.001)
            self.lab.opacity = 0
            self.sound_bg.stop()
            self.button_menu_start.size_hint = (1.0,.3)
            self.button_menu_start.opacity = 1
            self.button_menu_start.disabled = False
            self.button_menu_continue.size_hint = (1.0,.3)
            self.button_menu_continue.opacity = 1
            self.button_menu_continue.disabled = False
            self.button_menu_exit.size_hint = (1.0,.3)
            self.button_menu_exit.opacity = 1
            self.button_menu_exit.disabled = False
        elif self.slide_count in [9,18] and self.button_menu_continue.disabled == False:
            self.win_term.pop(0)
            self.vertical_box.size_hint = (1.0, .001)
            self.horizontal_box.size_hint = (1.0, .9)
            self.left_img.size_hint = (1.0, 1.0)
            self.left_img.opacity = 1
            self.right_img.size_hint = (1.0, 1.0)
            self.right_img.opacity = 1
            self.lab.size_hint = (.3, 1)
            self.lab.opacity = 1
            self.lab.text = self.win_term[0]
            self.sound_bg.play()
            self.button_menu_start.size_hint = (.001,.001)
            self.button_menu_start.opacity = 0
            self.button_menu_start.disabled = True
            self.button_menu_continue.size_hint = (.001,.001)
            self.button_menu_continue.opacity = 0
            self.button_menu_continue.disabled = True
            self.button_menu_exit.size_hint = (.001,.001)
            self.button_menu_exit.opacity = 0
            self.button_menu_exit.disabled = True
        elif self.slide_count in [13,17,24,28] and self.button_menu_continue.disabled == True:
            self.back_img.size_hint = (.001, .001)
            self.back_img.opacity = 0
            self.btn_img.size_hint = (.001, .001)
            self.btn_img.opacity = 0
            self.btn_img.disabled = True
            self.sound_bg.stop()
            self.button_menu_start.size_hint = (1.0,.3)
            self.button_menu_start.opacity = 1
            self.button_menu_start.disabled = False
            self.button_menu_continue.size_hint = (1.0,.3)
            self.button_menu_continue.opacity = 1
            self.button_menu_continue.disabled = False
            self.button_menu_exit.size_hint = (1.0,.3)
            self.button_menu_exit.opacity = 1
            self.button_menu_exit.disabled = False
        elif self.slide_count in [13,17,24,28] and self.button_menu_continue.disabled == False:
            self.back_img.size_hint = (1.0, 1.0)
            self.back_img.opacity = 1
            self.btn_img.size_hint = (.09, .18)
            self.btn_img.opacity = 1
            self.btn_img.disabled = False
            self.sound_bg.play()
            self.button_menu_start.size_hint = (.001,.001)
            self.button_menu_start.opacity = 0
            self.button_menu_start.disabled = True
            self.button_menu_continue.size_hint = (.001,.001)
            self.button_menu_continue.opacity = 0
            self.button_menu_continue.disabled = True
            self.button_menu_exit.size_hint = (.001,.001)
            self.button_menu_exit.opacity = 0
            self.button_menu_exit.disabled = True
        else:
            self.video.state = 'play'
            self.video.size_hint = (1.0, 1.0)
            self.button_menu_start.size_hint = (.001,.001)
            self.button_menu_start.opacity = 0
            self.button_menu_start.disabled = True
            self.button_menu_continue.size_hint = (.001,.001)
            self.button_menu_continue.opacity = 0
            self.button_menu_continue.disabled = True
            self.button_menu_exit.size_hint = (.001,.001)
            self.button_menu_exit.opacity = 0
            self.button_menu_exit.disabled = True

    def time_clock(self,dt):
        self.sec -= 1
        self.button_next.disabled = True
        if self.duration-self.sec >= 1:
            self.button_next.color='white'
            self.button_next.disabled = False
        if self.sec <= 0:
            self.next_video('next')
        if self.video.state == 'pause':
            self.button_next.disabled = True
            self.sec+=1


    def next_video(self,instance):
        self.button_next.disabled = True
        self.slide_count += 1
        self.slide = 'slide' + str(self.slide_count)
        self.sec = self.dict_video[self.slide]['duration']
        self.duration = self.dict_video[self.slide]['duration']
        if self.slide == 'slide4':
            self.sec = self.dict_video[self.slide]['duration']
            self.video.state = 'pause'
            self.video.size_hint = (.001, .001)
            self.btn_quest_1_1.size_hint=(1.0, .3)
            self.btn_quest_1_2.size_hint=(1.0, .3)
            self.btn_quest_1_1.opacity=1
            self.btn_quest_1_2.opacity=1
            self.btn_quest_1_1.disabled = False
            self.btn_quest_1_2.disabled = False
        elif self.slide == 'slide7':
            self.sec = self.dict_video[self.slide]['duration']
            self.video.state = 'pause'
            self.video.size_hint = (.001, .001)
            self.btn_quest_1_1.text = 'Скрытно наблюдать за происходящим и не вмешиваться'
            self.btn_quest_1_2.text = 'Неожиданно и стремительно атаковать бездушных'
            self.btn_quest_1_1.size_hint=(1.0, .3)
            self.btn_quest_1_2.size_hint=(1.0, .3)
            self.btn_quest_1_1.opacity=1
            self.btn_quest_1_2.opacity=1
            self.btn_quest_1_1.disabled = False
            self.btn_quest_1_2.disabled = False
        elif self.slide == 'slide9':
            self.sec = self.dict_video[self.slide]['duration']
            self.video.state = 'pause'
            self.video.size_hint = (.001, .001)
            self.sward_battle()
        elif self.slide == 'slide11':
            self.sec = self.dict_video[self.slide]['duration']
            self.video.state = 'pause'
            self.video.size_hint = (.001, .001)
            self.btn_quest_1_1.text = 'Да, абсолютно! Только так у нас есть шанс живыми добраться до стены...'
            self.btn_quest_1_2.text = 'Нет... всё-таки ты прав, будем держаться вместе!'
            self.btn_quest_1_1.size_hint=(1.0, .3)
            self.btn_quest_1_2.size_hint=(1.0, .3)
            self.btn_quest_1_1.opacity=1
            self.btn_quest_1_2.opacity=1
            self.btn_quest_1_1.disabled = False
            self.btn_quest_1_2.disabled = False
        elif self.slide == 'slide13':
            self.sec = self.dict_video[self.slide]['duration']
            self.video.state = 'pause'
            self.game()
        elif self.slide == 'slide16':
            self.sec = self.dict_video[self.slide]['duration']
            self.video.state = 'pause'
            self.video.size_hint = (.001, .001)
            self.vertical_box.size_hint = (1.0, .1)
            self.lab_steps.size_hint = (1.,1.)
            self.lab_steps.opacity = 1
            self.horizontal_box.size_hint = (1.0, .9)
            self.horizontal_box.padding = (.0,.0,3.5,.0)
            self.btn_quest_2_1.size_hint=(.3, 1.0)
            self.btn_quest_2_2.size_hint=(.3, 1.0)
            self.btn_quest_2_3.size_hint=(.3, 1.0)
            self.btn_quest_2_1.opacity=1
            self.btn_quest_2_2.opacity=1
            self.btn_quest_2_3.opacity=1
            self.btn_quest_2_1.disabled = False
            self.btn_quest_2_2.disabled = False
            self.btn_quest_2_3.disabled = False
        elif self.slide == 'slide17':
            self.sec = self.dict_video[self.slide]['duration']
            self.back_img.source='media/img/background2.jpg'
            self.score = 0
            self.video.state = 'pause'
            self.game()
        elif self.slide == 'slide18':
            self.sec = self.dict_video[self.slide]['duration']
            self.left_img.source='media/img/battle_knights_left.jpg'
            self.right_img.source='media/img/battle_knights_right.jpg'
            self.win_term = ['вверх', 'вправо', 'вверх', 'влево', 'вверх', 'вниз', 'влево', 'вниз', 'вправо']
            self.sward_battle()
        elif self.slide == 'slide24':
            self.sec = self.dict_video[self.slide]['duration']
            self.back_img.source = 'media/img/background3.jpg'
            self.video.state = 'pause'
            self.game()
        elif self.slide == 'slide28':
            self.sec = self.dict_video[self.slide]['duration']
            self.back_img.source = 'media/img/background4.jpg'
            self.video.state = 'pause'
            self.game()
        elif self.slide in ['slide20', 'slide22', 'slide26']:
            self.stop_video('stop')
            self.button_menu_continue.disabled = True
            self.button_pause.disabled = True
        elif self.slide == 'slide30':
            self.slide_count = 14
            self.next_video('next')
        else:
            self.sec = self.dict_video[self.slide]['duration']
            self.duration = self.dict_video[self.slide]['duration']
            self.video.source = self.dict_video[self.slide]['source']
            self.video.state = 'play'


    def game(self):
        if self.slide_count == 28:
            self.btn_img.background_normal = 'media/img/flash.png'
        else:
            self.btn_img.background_normal = 'media/img/target.png'
        self.sound_bg = SoundLoader.load('media/sounds/archivo.mp3')
        self.sound_bg.loop = True
        self.sound_bg.play()
        self.video.size_hint=(.001,.001)
        self.back_img.size_hint = (1.0, 1.0)
        self.back_img.opacity = 1
        self.btn_img.size_hint = (.09, .18)
        self.btn_img.opacity = 1
        self.btn_img.disabled = False
        event=Clock.schedule_interval(self.update, 0.5)

    def game_touch(self, touch):
        self.score += 1
        self.list_times1 = [3,7]
        self.list_times2 = [4,8]
        if self.score in self.list_times1 and self.slide_count == 17 or self.score in self.list_times1 and self.slide_count == 24:
            self.btn_img.background_normal = 'media/img/flash.png'
            sound = SoundLoader.load('media/sounds/shot.mp3')
            sound.play()
        elif self.score in self.list_times2 and self.slide_count == 24:
            self.btn_img.background_normal = 'media/img/target.png'
            self.back_img.source = 'media/img/background3_flash.jpg'
            sound = SoundLoader.load('media/sounds/flash.mp3')
            sound.play()
        elif self.score in self.list_times2 and self.slide_count == 17:
            self.btn_img.background_normal = 'media/img/target.png'
            self.back_img.source = 'media/img/background2_flash.jpg'
            sound = SoundLoader.load('media/sounds/flash.mp3')
            sound.play()
        elif self.slide_count == 28:
            self.btn_img.background_normal = 'media/img/flash.png'
            self.back_img.source = 'media/img/background4_flash.jpg'
            sound = SoundLoader.load('media/sounds/flash.mp3')
            sound.play()
        else:
            self.btn_img.background_normal = 'media/img/target.png'
            sound = SoundLoader.load('media/sounds/shot.mp3')
            sound.play()

    def update(self, dt):
        if self.slide_count == 17:
            self.back_img.source = 'media/img/background2.jpg'
        elif self.slide_count == 24:
            self.back_img.source = 'media/img/background3.jpg'
        elif self.slide_count == 28:
            self.back_img.source = 'media/img/background4.jpg'
        if self.score >= 10:
            self.sound_bg.stop()
            self.video.size_hint = (1.0, 1.0)
            self.btn_img.size_hint = (.001, .001)
            self.btn_img.opacity = 0
            self.btn_img.disabled = True
            self.back_img.size_hint = (.001, .001)
            self.back_img.opacity = 0
            Clock.unschedule(self.update)
            self.next_video('next')
            return
        else:
            self.width = Window.size[0]
            self.height = Window.size[1]
            x = round(random.uniform(0.1, 0.8), 1)
            y = round(random.uniform(0.3, 0.7), 1)
            self.btn_img.pos = (self.width*x,self.height*y)


    def quest(self, answer, args):
        if self.slide_count == 4 and answer == 'answer_1_1':
            self.btn_quest_1_1.size_hint=(.001, .001)
            self.btn_quest_1_2.size_hint=(.001, .001)
            self.btn_quest_1_1.opacity=0
            self.btn_quest_1_2.opacity=0
            self.btn_quest_1_1.disabled = True
            self.btn_quest_1_2.disabled = True
            self.video.size_hint = (1., 1.)
            self.next_video('next')
        elif self.slide_count == 4 and answer == 'answer_1_2':
            self.btn_quest_1_1.size_hint = (.001, .001)
            self.btn_quest_1_2.size_hint = (.001, .001)
            self.btn_quest_1_1.opacity = 0
            self.btn_quest_1_2.opacity = 0
            self.btn_quest_1_1.disabled = True
            self.btn_quest_1_2.disabled = True
            self.video.size_hint = (1., 1.)
            self.slide_count = 20
            self.next_video('next')
        elif self.slide_count == 7 and answer == 'answer_1_1':
            self.btn_quest_1_1.size_hint = (.001, .001)
            self.btn_quest_1_2.size_hint = (.001, .001)
            self.btn_quest_1_1.opacity = 0
            self.btn_quest_1_2.opacity = 0
            self.btn_quest_1_1.disabled = True
            self.btn_quest_1_2.disabled = True
            self.video.size_hint = (1., 1.)
            self.slide_count = 22
            self.next_video('next')
        elif self.slide_count == 7 and answer == 'answer_1_2':
            self.btn_quest_1_1.size_hint=(.001, .001)
            self.btn_quest_1_2.size_hint=(.001, .001)
            self.btn_quest_1_1.opacity=0
            self.btn_quest_1_2.opacity=0
            self.btn_quest_1_1.disabled = True
            self.btn_quest_1_2.disabled = True
            self.video.size_hint = (1., 1.)
            self.next_video('next')
        elif self.slide_count == 11 and answer == 'answer_1_1':
            self.btn_quest_1_1.size_hint=(.001, .001)
            self.btn_quest_1_2.size_hint=(.001, .001)
            self.btn_quest_1_1.opacity=0
            self.btn_quest_1_2.opacity=0
            self.btn_quest_1_1.disabled = True
            self.btn_quest_1_2.disabled = True
            self.video.size_hint = (1., 1.)
            self.next_video('next')
        elif self.slide_count == 11 and answer == 'answer_1_2':
            self.btn_quest_1_1.size_hint = (.001, .001)
            self.btn_quest_1_2.size_hint = (.001, .001)
            self.btn_quest_1_1.opacity = 0
            self.btn_quest_1_2.opacity = 0
            self.btn_quest_1_1.disabled = True
            self.btn_quest_1_2.disabled = True
            self.video.size_hint = (1., 1.)
            self.slide_count = 26
            self.next_video('next')
        elif self.slide_count == 16:
            if answer == self.correct_answer[0] and answer == 'btn_quest_2_3':
                self.btn_quest_2_3.size_hint=(.001, .001)
                self.btn_quest_2_3.opacity=0
                self.btn_quest_2_3.disabled = True
                self.correct_answer.pop(0)
            elif answer == self.correct_answer[0] and answer == 'btn_quest_2_2':
                self.btn_quest_2_2.size_hint = (.001, .001)
                self.btn_quest_2_2.opacity = 0
                self.btn_quest_2_2.disabled = True
                self.correct_answer.pop(0)
            elif answer == self.correct_answer[0] and answer == 'btn_quest_2_1':
                self.btn_quest_2_1.size_hint = (.001, .001)
                self.btn_quest_2_1.opacity = 0
                self.btn_quest_2_1.disabled = True
                self.correct_answer.pop(0)
            if len(self.correct_answer) == 0:
                self.lab_steps.size_hint = (.001, .001)
                self.lab_steps.opacity = 0
                self.vertical_box.size_hint = (1.0, .9)
                self.horizontal_box.size_hint = (1.0, .001)
                self.next_video('next')


    def sward_battle(self):
        self.vertical_box.size_hint=(1.0, .0001)
        self.horizontal_box.size_hint=(1.0, .9)
        self.left_img.size_hint = (1.0, 1.0)
        self.left_img.opacity = 1
        self.right_img.size_hint = (1.0, 1.0)
        self.right_img.opacity = 1
        self.lab.bind(on_touch_move=lambda x, y: self.touch_slide(y))
        self.lab.size_hint = (.3,1)
        self.lab.opacity = 1
        self.sound_bg = SoundLoader.load('media/sounds/archivo.mp3')
        self.sound_bg.loop = True
        self.sound_bg.play()


    def touch_slide(self, y):
        if len(self.win_term)>0:
            self.lab.text = self.win_term[0]
            self.side = ''
            if abs(y.dx) > abs(y.dy):
                if y.dx > 0:
                    self.side = 'вправо'
                    if self.side == self.win_term[0]:
                        self.win_term.pop(0)
                else:
                    self.side = 'влево'
                    if self.side == self.win_term[0]:
                        self.win_term.pop(0)
            else:
                if y.dy > 0:
                    self.side = 'вверх'
                    if self.side == self.win_term[0]:
                        self.win_term.pop(0)
                else:
                    self.side = 'вниз'
                    if self.side == self.win_term[0]:
                        self.win_term.pop(0)
        else:
            self.left_img.size_hint = (.001, .001)
            self.left_img.opacity = 0
            self.right_img.size_hint = (.001, .001)
            self.right_img.opacity = 0
            self.sound_bg.stop()
            self.lab.size_hint = (.001, .001)
            self.lab.opacity = 0
            self.win_term.append('Проведите\nпальцем')
            self.next_video('next')
            self.video.size_hint = (1., 1.)
            self.vertical_box.size_hint = (1.0, .9)
            self.horizontal_box.size_hint = (1.0, .001)

    LabelBase.register(name='cyrillicold',
                       fn_regular='./media/fonts/Cyrillicold.otf')


if __name__ == '__main__':
    app = MainApp()
    app.run()

