import pygame, sys
from pygame.locals import QUIT, MOUSEBUTTONDOWN
from state import State_2, UltimateTTT_Move, State
import time
from importlib import import_module

color = {"black": pygame.Color(0, 0, 0),
         "white": pygame.Color(255, 255, 255),
         'blue': pygame.Color(50, 255, 255),
         'orange': pygame.Color(255, 120, 0)}
small_image = {1: pygame.image.load('images/small_x.png'), 
               -1: pygame.image.load('images/small_o.png')}
large_image = {1: pygame.image.load('images/large_x.png'), 
               -1: pygame.image.load('images/large_o.png')}

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Ultimate Tic-Tac-Toe')

def draw(state: State_2):
    screen.fill('white')
        
    for x in range(3):
        for y in range(3):
            pygame.draw.rect(screen, color["white"], (x*200, y*200, 200, 200))

    if state.previous_move != None:
        next_block = state.previous_move.x * 3 + state.previous_move.y
        if state.global_cells[next_block] == 0:  # Chỉ tô xanh nếu chưa thắng
            pygame.draw.rect(screen, color['blue'], 
                            ((next_block%3)*200, (next_block//3)*200, 200, 200))

        i = state.previous_move.index_local_board
        pygame.draw.rect(screen, color['orange'],
                        ((i%3)*200 + state.previous_move.y*50 + 25,
                         (i//3)*200 + state.previous_move.x*50 + 25,
                         50, 50))
    
    for k in range(9):
        value = state.global_cells[k]
        if value != 0:
            picture = large_image[value]
            picture = pygame.transform.scale(picture, (100, 100))
            screen.blit(picture, ((k%3)*200 + 50, (k//3)*200 + 50))            
    
    for x in range(3):
        for y in range(3):
            for i in [1, 2]:
                pygame.draw.line(screen, color["black"], 
                                (x*200 + i*50 + 25, y*200 + 25), 
                                (x*200 + i*50 + 25, y*200 + 175), 2)
                pygame.draw.line(screen, color["black"], 
                                (x*200 + 25, y*200 + i*50 + 25), 
                                (x*200 + 175, y*200 + i*50 + 25), 2)
    
    for i in range(9):
        local_board = state.blocks[i]
        for x in range(3):
            for y in range(3):
                value = local_board[x, y]
                if value != 0:
                    screen.blit(small_image[value],
                                ((i%3)*200 + y*50 + 35,
                                 (i//3)*200 + x*50 + 35))
    
    for i in [1, 2]:
        pygame.draw.line(screen, color["black"], (i*200, 0), (i*200, 600), 3)
        pygame.draw.line(screen, color["black"], (0, i*200), (600, i*200), 3)

    pygame.display.update()

def get_move_from_mouse(pos, state):
    """Chuyển tọa độ chuột thành nước đi hợp lệ"""
    y, x = pos
    print(f"Mouse position: {x}, {y}")
    valid_moves = state.get_valid_moves  # Lấy danh sách nước đi hợp lệ
    
    # Tính chỉ số bảng cục bộ và ô trong bảng dựa trên tọa độ chuột
    local_board_idx = (y // 200) + (x // 200) * 3
    
    local_x = ((x % 200) - 25) // 50
    local_y = ((y % 200) - 25) // 50
    print(f"local_board_idx: {local_board_idx}, local_x: {local_x}, local_y: {local_y}")
    if 0 <= local_x < 3 and 0 <= local_y < 3:
        # Tạo nước đi tiềm năng
        potential_move = UltimateTTT_Move(local_board_idx, local_x, local_y, -1)
        # Kiểm tra xem nước đi có trong danh sách hợp lệ không
        for move in valid_moves:
            if (move.index_local_board == potential_move.index_local_board and
                move.x == potential_move.x and
                move.y == potential_move.y):
                return potential_move
    return None

def play_human_vs_ai(ai_player_module, rule=2,playerFirst = 1):
    """Chơi với một người là AI (X) và một người là người dùng (O)"""
    ai_player = import_module(ai_player_module)
    state = State_2() if rule == 2 else State()
    turn = 0
    remain_time_ai = 120
    is_game_done = False
    state.player_to_move = playerFirst
    while True:
        draw(state)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            if state.game_over or is_game_done:
                continue
            
                    
            # Lượt của AI (X, player_to_move = 1)
            if state.player_to_move == 1:
                start_t = time.time()
                new_move = ai_player.select_move(state, remain_time_ai)
                elapsed_time = time.time() - start_t
                remain_time_ai -= elapsed_time
                
                if elapsed_time > 10 or not new_move or remain_time_ai < -0.1:
                    is_game_done = True
                    continue
                
                state.act_move(new_move)
                turn += 1
                draw(state)  # Cập nhật giao diện ngay sau nước đi của AI
                pygame.time.wait(500)  # Đợi 0.5 giây để người chơi thấy nước đi
            
            # Lượt của người chơi (O, player_to_move = -1)
            elif state.player_to_move == -1 and event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                new_move = get_move_from_mouse(pos, state)
                
                if new_move:
                    state.act_move(new_move)
                    turn += 1
                
            if turn >= 81:
                is_game_done = True

play_human_vs_ai('botAI', 2,-1)