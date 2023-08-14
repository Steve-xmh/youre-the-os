from os import path
import pygame
from random import randint

from lib.ui.color import Color
from game_objects.button import Button
from game_objects.how_to_play_part import HowToPlayPart
from lib.scene import Scene

_parts = [
    HowToPlayPart(
        [
            '在游戏中，你是一台电脑中的操作系统。',
            '你需要管理进程、内存，和输入输出（I/O）事件。'
        ], 
        [
            pygame.image.load(path.join('assets', 'how_to_play_0_0.png'))
        ]
    ),
    HowToPlayPart(
        [
            '在屏幕的顶部，你可以看到你的所有 CPU。'
        ],
        [
            pygame.image.load(path.join('assets', 'how_to_play_1_0.png'))
        ]
    ),
    HowToPlayPart(
        [
            '在 CPU 下面，你能看到有一些处于闲置状态的进程。'
        ],
        [
            pygame.image.load(path.join('assets', 'how_to_play_2_0.png'))
        ]
    ),
    HowToPlayPart(
        [
            '你可以点击一个闲置状态的进程将其加入到一个可用的 CPU 中。',
        ],
        [
            pygame.image.load(path.join('assets', 'how_to_play_3_0.png')),
            pygame.image.load(path.join('assets', 'how_to_play_3_1.png'))
        ]
    ),
    HowToPlayPart(
        [
            '同样，你可以点击 CPU 上的进程将其移出到闲置进程中。',
        ],
        [
            pygame.image.load(path.join('assets', 'how_to_play_4_0.png')),
            pygame.image.load(path.join('assets', 'how_to_play_4_1.png'))
        ]
    ),
    HowToPlayPart(
        [
            '随着时间流逝，闲置的进程会逐渐进入六种“饥饿”等级。'
        ],
        [
            pygame.image.load(path.join('assets', 'how_to_play_5_0.png')),
            pygame.image.load(path.join('assets', 'how_to_play_5_1.png')),
            pygame.image.load(path.join('assets', 'how_to_play_5_2.png')),
            pygame.image.load(path.join('assets', 'how_to_play_5_3.png')),
            pygame.image.load(path.join('assets', 'how_to_play_5_4.png')),
            pygame.image.load(path.join('assets', 'how_to_play_5_5.png'))
        ]
    ),
    HowToPlayPart(
        [
            '饥饿等级能帮助你了解哪些进程闲置了太长的时间。',
            '如果一个进程闲置了太长时间，用户就会失去耐心然后杀掉那个进程。',
        ],
        [
            pygame.image.load(path.join('assets', 'how_to_play_6_0.png')),
            pygame.image.load(path.join('assets', 'how_to_play_6_1.png'))
        ]
    ),
    HowToPlayPart(
        [
            '一个进程也会正常地终止，此时只需要点击对应的进程就能将其删除。'
        ],
        [
            pygame.image.load(path.join('assets', 'how_to_play_7_0.png'))
        ]
    ),
    HowToPlayPart(
        [
            '有时候，一个工作中的进程会因为等待一个输入输出事件（I/O 事件）而阻塞。',
            '阻塞中的进程会浪费 CPU 的工作时间。所以将其移出 CPU 让出工作时间是一个好办法。',
        ],
        [
            pygame.image.load(path.join('assets', 'how_to_play_8_0.png'))
        ]
    ),
    HowToPlayPart(
        [
            '如果你有阻塞中的进程，留意一下输入输出事件（I/O 事件）条。',
            '在有事件的时候要记得点击它们，否则你的进程会一直阻塞下去直到“饿死”被杀掉',
        ],
        [
            pygame.image.load(path.join('assets', 'how_to_play_9_0.png')),
            pygame.image.load(path.join('assets', 'how_to_play_9_1.png'))
        ]
    ),
    HowToPlayPart(
        [
            '你还需要管理内存！进程运行的时候会创建出内存页面。',
            '正在使用中的内存页面会显示成白色，当前尚未使用的内存则会显示成灰色。',
        ],
        [
            pygame.image.load(path.join('assets', 'how_to_play_10_0.png'))
        ]
    ),
    HowToPlayPart(
        [
            '有时候，你的内存会耗尽然后新的内存页面会被写入到磁盘中。',
            '你可以通过点击内存页面来将其在内存和磁盘间移动。',
        ],
        [
            pygame.image.load(path.join('assets', 'how_to_play_11_0.png')),
            pygame.image.load(path.join('assets', 'how_to_play_11_1.png'))
        ]
    ),
    HowToPlayPart(
        [
            '进程只能使用处于内存中的内存页面，如果进程需要一个处于磁盘中的内存页面的话进程就会闪烁。',
            '这时候你就需要交换页面了，进程所需要使用的内存页面也会一起闪烁。',
        ],
        [
            pygame.image.load(path.join('assets', 'how_to_play_12_0.png')),
            pygame.image.load(path.join('assets', 'how_to_play_12_1.png'))
        ],
        animation_interval=200
    ),
    HowToPlayPart(
        [
            "如果你不及时将进程所需的内存页面交换到内存中的话，那个进程最终也会“饿死”然后被用户杀死。",
        ],
        [
            pygame.image.load(path.join('assets', 'how_to_play_13_0.png'))
        ],
        animation_interval=200
    ),    
    HowToPlayPart(
        [
            '一旦被用户杀掉的进程数量达到 10 个，用户就会生气，然后把你重启了。',
            '游戏也就会结束，你的目标就是在被用户重启前尽可能存活下来！',
        ],
        [
            pygame.image.load(path.join('assets', 'how_to_play_14_0.png'))
        ]
    )
]

class HowToPlay(Scene):
    def __init__(self, screen, scenes):
        super().__init__(screen, scenes, background_color=Color.LIGHT_GREY)
        
        self._parts = []
        self._current_part_id = 0
        self._previous_button = None
        self._next_button = None
        
    def setup(self):       
        self._scene_objects = []
        
        self._parts = _parts
        
        self._current_part_id = 0
        self._scene_objects.append(self._parts[self._current_part_id])
        
        self._previous_button = Button('<', self._go_to_previous_part)
        self._previous_button.view.set_xy(
            52,
            self._screen.get_height() - 78
        )
        self._scene_objects.append(self._previous_button)
        
        self._next_button = Button('>', self._go_to_next_part)
        self._next_button.view.set_xy(
            self._screen.get_width() - self._next_button.view.width - 52,
            self._screen.get_height() - 78
        )
        self._scene_objects.append(self._next_button)
        
    def _go_to_previous_part(self):
        if self._current_part_id == 0:
            self._return_to_main_menu()
        else:
            self._scene_objects.remove(self._previous_button)
            self._scene_objects.remove(self._next_button)
            self._scene_objects.remove(self._parts[self._current_part_id])
            
            self._current_part_id -= 1
            self._parts[self._current_part_id].initial_time = self.current_time
            
            self._scene_objects.append(self._parts[self._current_part_id])
            self._scene_objects.append(self._previous_button)
            self._scene_objects.append(self._next_button)
        
    def _go_to_next_part(self):
        if self._current_part_id == len(self._parts) - 1:
            self._return_to_main_menu()
        else:
            self._scene_objects.remove(self._previous_button)
            self._scene_objects.remove(self._next_button)
            self._scene_objects.remove(self._parts[self._current_part_id])
            
            self._current_part_id += 1
            self._parts[self._current_part_id].initial_time = self.current_time
            
            self._scene_objects.append(self._parts[self._current_part_id])
            self._scene_objects.append(self._previous_button)
            self._scene_objects.append(self._next_button)
    
    def _return_to_main_menu(self):
        self._scenes['main_menu'].start()
    
    def update(self, current_time, events):
        for game_object in self._scene_objects:
            game_object.update(current_time, events)
