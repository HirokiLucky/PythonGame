#ピンボールゲーム
import pygame

FPS = 60     # Frame per Second 毎秒のフレーム数
loop = True
score = 0
gamemode = 0
x, y= (100, 100)   # ボールの初期位置
vx = 5    # ボールの速度
vy = 5
paddle_x, paddle_y= (400, 700) # パドルの初期位置
paddle_vx = 10                 # パドルの速度
g = 0.1
life = 3

# ボールの描画関数
def draw_ball(screen, x, y, radius=10):
    return pygame.draw.circle(screen, (255, 255, 0), (x, y), radius)

# パドルの描画関数
def draw_paddle(screen, x, y):
    return pygame.draw.rect(screen, (0, 255, 255), (x, y, 200, 30))

def draw_block(screen):
    block_list = []
    for i in range(3):
        block = pygame.draw.rect(screen, (255, 0, 255), (i * 200 + 150, 200, 80, 80))
        block2 = pygame.draw.rect(screen, (255, 0, 255), (i * 200 + 150, 400, 80, 80))
        block_list.append(block)
        block_list.append(block2)
    return block_list

def draw_score():
    pygame.init()
    score_print = font.render(("score:"+ str(score)), True, (255,255,255))
    screen.blit(score_print, (350,100))

def draw_life():
    pygame.init()
    life_print = font.render(("LIFE:"+ str(life)), True, (255,255,255))
    screen.blit(life_print, (350,150))

def credit():
    global gamemode
    screen.fill((0, 0, 0))
    screen.blit(text7, (200, 400))
    pygame.draw.rect(screen, (255,255,255), button3)
    screen.blit(text8, (350, 600))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 終了イベント
                pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.type == pygame.QUIT:  # 終了イベント
                pygame.quit()
            if button3.collidepoint(event.pos):
                gamemode = 0

def menu(screen):
    global gamemode
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255,255,0), button)
    pygame.draw.rect(screen, (255,0,255), button2)
    screen.blit(text, (350, 400))
    screen.blit(text1, (250, 100))
    screen.blit(text3, (100, 200))
    screen.blit(text4, (100, 250))
    screen.blit(text5, (100, 300))
    screen.blit(text6, (100, 400))
    pygame.display.update()
    pygame.mixer.init()    # 初期設定
    pygame.mixer.music.load('music.mp3')     # 音楽ファイルの読み込み（mp3を挿入。メニュー画面の音楽）
    pygame.mixer.music.play(1)
    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 終了イベント
                pygame.quit()  #pygameのウィンドウを閉じる
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.collidepoint(event.pos):
                    gamemode = 1
                    return
                if button2.collidepoint(event.pos):
                    gamemode = 3
                    return
    pygame.mixer.music.stop()             

def gameover():
    global loop, gamemode,life, score
    print("あなたのscoreは：" + str(score) + "点でした！")
    screen.fill((0, 0, 0))
    screen.blit(text2, (200, 400))
    pygame.draw.rect(screen, (0, 0, 255), button4)
    pygame.draw.rect(screen, (255, 0, 0), button5)
    screen.blit(text9, (200, 600))
    screen.blit(text10, (550, 600))
    pygame.display.flip()
    pygame.mixer.init()    # 初期設定
    pygame.mixer.music.load('music1.mp3')     # 音楽ファイルの読み込み（mp3を挿入。GameOver画面の音楽）
    pygame.mixer.music.play(1)
    while(1):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button4.collidepoint(event.pos):
                    life = 4
                    score = 0
                    gamemode = 0
                    return
                if button5.collidepoint(event.pos):
                    loop = False
                    pygame.quit()
            if event.type == pygame.QUIT:  # 終了イベント
                loop = False
                pygame.quit()
    pygame.mixer.music.stop()

                
def main():
    global loop, score,x, y, paddle_x, paddle_y, vx, vy, paddle_vx, gamemode, life
    for event in pygame.event.get():      # 「閉じる」ボタンを処理する
        if event.type == pygame.QUIT:
            pygame.quit()

    clock.tick(FPS)      # 毎秒の呼び出し回数に合わせて遅延
    draw_score()
    draw_life()
    pressed_keys = pygame.key.get_pressed() # キー情報を取得
    if pressed_keys[pygame.K_RIGHT]:    
        paddle_x += paddle_vx        
    if pressed_keys[pygame.K_LEFT]:  
        paddle_x -= paddle_vx        
        
    # パドルを取得する
    paddle_rect = draw_paddle(screen, paddle_x, paddle_y)

    vy = vy + g
    x += vx          # ボールの移動
    y += vy
    if not (0 <= x <= 800):  # 画面の外に出たら、向きを変える
        vx = -vx
    if(0 >= y):  # 画面の外に出たら、向きを変える
        vy = -vy
    if (800 <= y):
        life = life - 1
        if life != 0:
            vy = 5
            x, y= (100, 100)
        elif life == 0:
            gamemode = 2
            return gamemode
        
    ball_rect = draw_ball(screen, x, y)   # ボールの取得
    
    if (ball_rect.colliderect(paddle_rect)):
        vy = -vy - 0.1   # パドルと衝突したら、ボールを反転
        
    if (paddle_x <= 0):  #壁とパドルの当たり判定
        paddle_x = 0
    if (paddle_x >= 600):  
        paddle_x = 600

    block_rect = draw_block(screen)            #ブロックの取得
    for block in block_rect:
        if (ball_rect.colliderect(block)):#ブロックとボールの当たり判定
            if (200 < y < 280):
                vx = -vx
                score = score + 100
            if (400 < y < 480):
                vx = -vx
                score = score + 100
            if (150 < x < 230):
                vy = -vy - 0.1
                score = score + 100
            if (350 < x < 430):
                vy = -vy - 0.1
                score = score + 100
            if (550 < x < 630):
                vy = -vy - 0.1
                score = score + 100
            
    pygame.display.flip() # パドルとボールの描画を画面に反映
    screen.fill((0, 0, 0))  # 塗潰し：次の flip まで反映されない

screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()   # 時計オブジェクト
pygame.init()
font = pygame.font.SysFont('Helvetica', 30)
font1 = pygame.font.SysFont('Times New Roman', 50)
blocks = pygame.sprite.RenderUpdates()
button = pygame.Rect(350,400, 100, 50)
button2 = pygame.Rect(100, 400, 100, 50)
button3 = pygame.Rect(350, 600, 100, 50)
button4 = pygame.Rect(200, 600, 200, 50)
button5 = pygame.Rect(500, 600, 200, 50)
myfont = pygame.font.Font("ipag.ttf", 30)
text = font.render("PLAY!!", True, (255,0,255))
text1 = font1.render("MAIN GAME", True, (255,0,0))
text2 = font1.render("Thank you for playing", True, (255,255,255))
text3 = myfont.render("説明：「PLAY!!」ボタンを押してスタート!", True, (0,255,0))
text4 = myfont.render("＜－、－＞ボタンでパドルを動かしましょう", True, (0,255,0))
text5 = myfont.render("ボールをブロックに当ててscore獲得！", True, (0,255,0))
text6 = font.render("credit", True, (0,0,0))
text7 = myfont.render("提供：HirokiLucky", True, (0,255,0))
text8 = font.render("Back", True, (255,0,0))
text9 = myfont.render("continueする！", True, (255,255,0))
text10 = myfont.render("諦める", True, (0,0,0))

while loop:
    if gamemode == 0:
        menu(screen)
    elif gamemode == 1:
        pygame.mixer.init()    # 初期設定
        pygame.mixer.music.load('music2.mp3')     # 音楽ファイルの読み込み（mp3を挿入。ゲーム中の音楽）
        pygame.mixer.music.play(3)
        while(1):
            next_step = main()
            if next_step == 2:
                break
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # 終了イベント
                    loop = False
                    pygame.quit()
        pygame.mixer.music.stop()
    elif gamemode == 2:
        gameover()
    elif gamemode == 3:
        credit()



