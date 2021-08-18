import pygame
from pygame.constants import K_LEFT, K_RIGHT
import os




################################################
#반드시 해야하는 초기화
pygame.init() 

# 화면 크기 설정
screen_width = 640 ## 가로크기
screen_height = 480 ## 세로크기
screen = pygame.display.set_mode((screen_width,screen_height)) 



# 화면 타이틀 설정 (2. background 시작)
pygame.display.set_caption("nado pang") 

# FPS(5. frame_per_second 시작)
clock = pygame.time.Clock()

################################################

# 1. 사용자 게임 초기화( 배경 화면, 게임, 이미지, 좌표, 폰트 등)

current_path = os.path.dirname(__file__) # 현재 파일의 위치 변환
image_path = os.path.join(current_path, "images") # images 폴더 위치 변환
 

#배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # 스테이지의 높이 위에 캐릭터를 두기 위해서

#캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height

#캐릭터 이동 방향 
character_to_x = 0


#캐릭터 이동 속도
character_speed = 5

# 무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0] ## 무기 발사는 캐릭터의 중앙에서만 발사하기에 가로크기만 구함

# 무기는 한번에 여러 발 발사 가능
weapons = []

# 무기 이동 속도
weapon_speed = 10





running = True


while running:
    dt = clock.tick(30) 

     

    #2.  이벤트 처리( 키보드, 마우스 등)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 
   

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + (character_width/2) - (weapon_width/2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos,weapon_y_pos]) ## 무기 여러번 발사하면 좌표가 그만큼 늘어나기에 설정 

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

   
    # 3. 게임 캐릭터 위치 정의
    character_x_pos += character_to_x

    if character_x_pos <0:
        character_x_pos = 0 
    
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 무기 위치 조정
    weapons = [[w[0],w[1]-weapon_speed] for w in weapons] # weapons에는 리스트로 x,y의 좌표가 있으며, 
    # 캐릭터의 움직임에 따라 초기 x값은 변하고 y값은 변하지 않는다. 만약 첫발을 쏘게되면
    # 초기 위치에 있고, 그 다음으로 옆에다가 쏘면 옆에 쏜건 초기위치지만, 첫발은 그 위로 진행시키기 위해 y좌표에 weapon_speed 만큼 뺸다.
    # 또한 그 진행시키는 값을 저장할 구간도 필요하기에 list로 묶은것이다. 그럼 업데이트 되면서 그 값이 list안에 들어가고 그걸 또 다음상황으로 이용이 된다.
    # 100, 200 > 100, 180 > 100, 160 으로 무기 발사체가 진행이 될 것이다.

    # 천장에 닿은 무기 없애기
    
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0] # if문을 먼저 조건 생각하고 for문을 실행
    # 즉 w[1]의 값이 0보다 클 경우 list값을 저장하고 그렇지 않은 경우는 list값을 저장하지 않기에 값이 없어진다. 즉 발사체가 사라진다.
      



    # 4. 충돌 처리



    # 5. 화면 그리기
    screen.blit(background,(0,0))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon,(weapon_x_pos,weapon_y_pos))

    screen.blit(stage,(0,screen_height- stage_height))

    screen.blit(character,(character_x_pos,character_y_pos))

    
    # for weapon_x_pos, weapon_y_pos in weapons:
    #     screen.blit(weapon,(weapon_x_pos,weapon_y_pos)) 
    # 만약 이걸 여기다가 쓰면 그 메이플 스토리처럼 펫이 캐릭터 앞에 있는것처럼 무기 발사체가 캐릭터 앞에 있게 된다.
    # 그걸 방지하기 위해 순서를 배경 > 무기발사 > 스테이지 땅 > 캐릭터로 바꾼것.
    # 좀 더 자세히 할려면 발사체의 y축 맨 밑을 기준으로 캐릭터의 크기만큼 올리면 좀 더 완벽해짐.

    pygame.display.update() 
    

# 게임 종료o
pygame.quit()

