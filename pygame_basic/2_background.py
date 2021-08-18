import pygame

pygame.init() # 초가화작업 (무조건 필수) (클래스 정의할떄도 self.init 하는것처럼 그런듯)

# 화면 크기 설정
screen_width = 480 ## 가로크기
screen_height = 640 ## 세로크기
screen = pygame.display.set_mode((screen_width,screen_height)) ## 게임 화면 크기 설정



# 화면 타이틀 설정 (2. background 시작)
pygame.display.set_caption("Test Game") # 게임 타이틀 제작

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\kang\\Desktop\\Pythonworkspace\\pygame_basic\\background.png")

# 이벤트 루프
running = True # 게임이 계속 진행중인지? 파악
while running:
    for event in pygame.event.get(): # 키보드 및 마우스 입력이 들어올경우 그 값에 대응으로 처리 (이벤트 발생 여부)
        if event.type == pygame.QUIT: ## 1시 방향 X 표시의 창끄기 표시 명령어
            running = False ## 내가 실수로 = 한개만 할걸 두개로 해서 확정이 아닌 조건으로 되서 무한루프로 빠져나오지 못했음.

    screen.blit(background, (0,0)) #배경 그리기 ## 여기까지만 하면 반영을 하지 않는다. 
    #rgb값을 이용하여 배경을 넣을수 있다.
    #screen.fill((0,0,255))

    pygame.display.update() # 매 프레임마다 배경을 그려줘야 하기에 설정함
    

# 게임 종료
pygame.quit()
