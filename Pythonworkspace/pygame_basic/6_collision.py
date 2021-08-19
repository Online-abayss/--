import pygame
from pygame.constants import K_LEFT, K_RIGHT

pygame.init() # 초가화작업 (무조건 필수) (클래스 정의할떄도 self.init 하는것처럼 그런듯)

# 화면 크기 설정
screen_width = 480 ## 가로크기
screen_height = 640 ## 세로크기
screen = pygame.display.set_mode((screen_width,screen_height)) ## 게임 화면 크기 설정



# 화면 타이틀 설정 (2. background 시작)
pygame.display.set_caption("Test Game") # 게임 타이틀 제작

# FPS(5. frame_per_second 시작)
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\kang\\Desktop\\Pythonworkspace\\pygame_basic\\background.png")

# 캐릭터(스프라이트) 불러오기 (3.man sprite 시작)
character = pygame.image.load("C:\\Users\\kang\\Desktop\\Pythonworkspace\\pygame_basic\\character.png")
character_size = character.get_rect().size ## 캐릭터의 이미지의 가로 및 세로 크기값을 알수있음.
character_width = character_size[0] # 캐릭터의 가로 크기
character_heigth = character_size[1] # 캐릭터의 세로 크기

# 캐릭터 움직임의 관한 좌표를 설정
# 좌표는 11시 꼭짓점 기준으로 0,0을 잡고 우측 밑으로 증가한다.

# y좌표를 바로 밑에껏처럼 하면 캐릭터가 안보인다. 왜냐하면 캐릭터도 마찬가지로 좌표는 11시 꼭짓점을 기준으로 잡아주기에
# 캐릭터의 크기를 생각하고 그만큼 위로 올려서 보이게 해야한다. 또한 중앙으로 캐릭터를 옮기고 싶으면 그냥 화면 가로/2가 아닌 캐릭터 크기의 절반만큼 더 왼쪽으로 옮겨야한다.
 
character_x_pos = (screen_width/2) -(character_width/2)#  x위치를 설정

character_y_pos = screen_height - character_heigth# Y위치를 설정


# 이동 할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6



# 적 캐릭터 (6. collision)

enemy = pygame.image.load("C:\\Users\\kang\\Desktop\\Pythonworkspace\\pygame_basic\\enemy.png")
enemy_size = enemy.get_rect().size ## 캐릭터의 이미지의 가로 및 세로 크기값을 알수있음.
enemy_width = enemy_size[0] # 캐릭터의 가로 크기
enemy_heigth = enemy_size[1] # 캐릭터의 세로 크기
 
enemy_x_pos = (screen_width/2) -(enemy_width/2)#  x위치를 설정

enemy_y_pos = (screen_height/2) - (enemy_heigth/2)# Y위치를 설정

# 이벤트 루프 
# 키보드 입력에 따른 이동 여부 설정(4. keyboard_event 시작)
running = True # 게임이 계속 진행중인지? 파악
while running:
    dt = clock.tick(30) # 게임화면 초당 프레임수를 결정

    #print("fps : " + str(clock.get_fps())) # 초당 프레임이 몇인지 글로 보여줌 


    for event in pygame.event.get(): # 키보드 및 마우스 입력이 들어올경우 그 값에 대응으로 처리 (이벤트 발생 여부)
        if event.type == pygame.QUIT: ## 1시 방향 X 표시의 창끄기 표시 명령어
            running = False ## 내가 실수로 = 한개만 할걸 두개로 해서 확정이 아닌 조건으로 되서 무한루프로 빠져나오지 못했음.
        
        if event.type == pygame.KEYDOWN: #키가 눌려졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터를 좌측으로 이동
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT: # 캐릭터를 우측으로 이동
                to_x += character_speed
            elif event.key == pygame.K_UP: # 캐릭터를 위로 이동
                to_y -= character_speed
            elif event.key == pygame.K_DOWN: # 캐릭터를 밑으로 이동
                to_y += character_speed
        
        if event.type == pygame.KEYUP: # 키보드를 때면 멈추기.
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    character_x_pos += to_x * dt #  이동속도에 데이터 프레임 수를 곱해서 좀더 자연스럽게 만듦
    character_y_pos += to_y * dt

    # 화면 밖으로 넘어가는걸 방지

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width: # 우측 끝 - 캐릭터 넓이만큼
        character_x_pos = screen_width - character_width
    
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_heigth: # 스크린 맨밑 - 캐릭터 높이만큼
        character_y_pos =  screen_height - character_heigth

    # 충돌 처리 ( rect 정보 업데이트 )
    character_rect = character.get_rect() # 캐릭터의 가로 세로 값을 변수명에 지정 (위의 .size랑 조금 다름 size는 값 자체를 알려주는 듯)
    character_rect.left = character_x_pos # 캐릭터 rect값을 변동시키기 위해 좌측과 위쪽만 바꾸면된다.
    character_rect.top = character_y_pos # 이렇게 하면 화면상에 캐릭터의 위치로 계속 데이터가 변동된다.

    # 충돌 처리 적 버전
    enemy_rect = enemy.get_rect()    
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    # 위의 enemy.rect.left와 top을 설정 안해서 충돌해도 종료가 안된다.
    # 왜냐하면 현재 이미지만 불러서 그 위치에 보이게끔 이미지만 구축했지, 내용은 없다. 그래서 주석을 풀어서 적의 최종위치를 설정
    if character_rect.colliderect(enemy_rect): #clliderect 사격형 기준으로 충돌여부가 있는지 확인하는 문구
        print("충돌했어요")
        running = False

    screen.blit(background, (0,0)) #배경 그리기 ## 여기까지만 하면 반영을 하지 않는다. 
    #rgb값을 이용하여 배경을 넣을수 있다.
    #screen.fill((0,0,255)
    
    screen.blit(character, (character_x_pos,character_y_pos)) # 캐릭터 그리기 및 위치 설정한 값으로 지정

    screen.blit(enemy, (enemy_x_pos,enemy_y_pos)) # 적 그리기

    pygame.display.update() # 매 프레임마다 배경을 그려줘야 하기에 설정함
    

# 게임 종료o
pygame.quit()
