import pygame
from pygame.constants import K_LEFT, K_RIGHT
from random import *

# 똥 피하기 게임.

# 보안하기 (1. 똥을 3개까지 늘리기[enemy를 3까지 늘리는 방법 ??])
# 2. 3개까지 늘리지만 서로 겹치지 않게하기.
# 3. 띵킹.  
        # 우선 리스트로 하는거 말고 걍 노가다로 복붙하는 형식으로 enemy3개 늘려서 겹치지 않게 해서 해보기.


################################################
#반드시 해야하는 초기화
pygame.init() 

# 화면 크기 설정
screen_width = 480 ## 가로크기
screen_height = 640 ## 세로크기
screen = pygame.display.set_mode((screen_width,screen_height)) 



# 화면 타이틀 설정 (2. background 시작)
pygame.display.set_caption("avoid poops") 

background = pygame.image.load("C:\\Users\\kang\\Desktop\\Pythonworkspace\\pygame_basic\\background.png")

character = pygame.image.load("C:\\Users\\kang\\Desktop\\Pythonworkspace\\pygame_basic\\character.png")

enemy_images = [
    pygame.image.load("C:\\Users\\kang\\Desktop\\Pythonworkspace\\pygame_basic\\enemy.png"),
    pygame.image.load("C:\\Users\\kang\\Desktop\\Pythonworkspace\\pygame_basic\\enemy.png"),
    pygame.image.load("C:\\Users\\kang\\Desktop\\Pythonworkspace\\pygame_basic\\enemy.png")
]

# FPS(5. frame_per_second 시작)
clock = pygame.time.Clock()

total_time = 100
start_time = pygame.time.get_ticks()

################################################

# 1. 사용자 게임 초기화( 배경 화면, 게임, 이미지, 좌표, 폰트 등)

game_font = pygame.font.Font(None,20)

# 캐릭터 , 적 상세정보
character_size = character.get_rect().size # 가로 세로 값이 두개로 나온다... 
character_width = character_size[0]
character_height = character_size[1]

# enemy_size = enemy.get_rect().size
# enemy_width = enemy_size[0]
# enemy_height = enemy_size[1]

character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - character_height

enemy_speed_y = [0.3 , 0.375, 0.45]

# 적들
enemys = []


#적들 설정.
enemys.append({
    "pos_x" : randint(0,410), # 공의 x 좌표
    "pos_y" : 0, # 공의 y 좌표
    "img_idx" : 0, # 공의 이미지 index
    "init_spd_y" : enemy_speed_y[0] # y의 최초 속도
})



# enemy_x_pos = randint(0,int(480-enemy_width))
# enemy_y_pos = 0



to_x = 0
to_y = 0

character_speed = 0.5

# enemy_speed = 0.3


running = True 





while running:
    dt = clock.tick(30) 

     

    #2.  이벤트 처리( 키보드, 마우스 등)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            # elif event.key == pygame.K_UP:
            #     to_y -= 0
            # elif event.key == pygame.K_DOWN:
            #     to_y += 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            # elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            #     to_y = 0

        
            ##### 이렇게 하면 화면 일단 나가고 다시 끝으로 돌아간다. 재미있다.
            # for문 안에 있어서 한 사이클 돌리는데 화면 넘어가는 pygame.keyup보다 밑에 있어서 적용되지 않되나봄
            # for문 밖에 있으면 최대치를 미리 문구가 실행되고 포문 안에 있는것도 적용되서 그런가봄. 
    #     if character_x_pos <0:
    #         character_x_pos = 0
    #     elif character_x_pos > screen_width - character_width:
    #         character_x_pos = screen_width - character_width

    # character_x_pos += to_x * dt    
    # character_y_pos += to_y * dt
            #####

    character_x_pos += to_x * dt
    
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width: # 우측 끝 - 캐릭터 넓이만큼
        character_x_pos = screen_width - character_width



    # character_x_pos += to_x * dt # 방지턱 문구보다 밑에다가 쓰면 to_x * dt만큼 넘어가고 다시 돌아온다 .
    # 순서의 중요성.

    # enemy_y_pos += enemy_speed * dt


    # 3. 게임 캐릭터 위치 정의

    for enemy_idx, enemy_val in enumerate(enemys):
        enemy_pos_x = enemy_val["pos_x"]
        enemy_pos_y = enemy_val["pos_y"]
        enemy_img_idx = enemy_val["img_idx"]

        enemy_rect = enemy_images[enemy_img_idx].get_rect()
        enemy_size = enemy_images[enemy_img_idx].get_rect().size
        enemy_width = enemy_size[0]
        enemy_height = enemy_size[1]

    # if enemy_y_pos  + enemy_height >640:
    #     enemy_x_pos = randint(0,int(480-enemy_width))
    #     enemy_y_pos = 0



    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    # enemy_rect = enemy.get_rect()
    # enemy_rect.left = enemy_x_pos
    # enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        running = False
        break


    


    # 5. 화면 그리기
    screen.blit(background,(0,0))
    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000 # 좀 알아보기 .
    timer = game_font.render("Time : {}".format(int(total_time - elapsed_time)), True, (255,255,255))
    screen.blit(timer, (10, 10))
    screen.blit(character,(character_x_pos,character_y_pos))
    # screen.blit(enemy,(enemy_x_pos, enemy_y_pos))

    for idx, val in enumerate(enemys):
        enemy_pos_x = val["pos_x"]
        enemy_pos_y = val["pos_y"]
        enemy_img_idx = val["img_idx"]
        screen.blit(enemy_images[enemy_img_idx],(enemy_pos_x,enemy_pos_y))

    if total_time - elapsed_time < 0:
        running = False
    

    pygame.display.update() 

pygame.time.delay(2000)


# 게임 종료o
pygame.quit()
