import pygame
from pygame.constants import K_LEFT, K_RIGHT





################################################
#반드시 해야하는 초기화
pygame.init() 

# 화면 크기 설정
screen_width = 480 ## 가로크기
screen_height = 640 ## 세로크기
screen = pygame.display.set_mode((screen_width,screen_height)) 



# 화면 타이틀 설정 (2. background 시작)
pygame.display.set_caption("게임 이름") 

# FPS(5. frame_per_second 시작)
clock = pygame.time.Clock()

################################################

# 1. 사용자 게임 초기화( 배경 화면, 게임, 이미지, 좌표, 폰트 등)


running = True 

while running:
    dt = clock.tick(30) 

     

    #2.  이벤트 처리( 키보드, 마우스 등)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 
   
   
   
    # 3. 게임 캐릭터 위치 정의


    # 4. 충돌 처리



    # 5. 화면 그리기
    

    pygame.display.update() 
    

# 게임 종료o
pygame.quit()
