import ColabTurtle.Turtle as t
import math
import random
import matplotlib.pyplot as plt

#ブロッコリーなんだから緑色だよね
cm = plt.get_cmap('YlGn', 20)

# 初期化
t.initializeTurtle(initial_speed=10, initial_window_size=(400, 400))
t.shape(shape='circle')
t.bgcolor('black')

# パラメータ(色々調べて構成)
color_offset = 2
init_length = 60
init_width = 14
max_level = 5

# 俗にいう手で食べるときに持つところ
branches = [((200, 360), -90, init_length, init_width, 0)]

for level in range(max_level):
    next_branches = []

    # 1層の枝をここで処理
    for pos, heading, length, width, current_level in branches:

        # ペンの移動
        t.up()
        t.goto(pos[0], pos[1])
        t.face(heading)

        #乱数部分
        current_length = max(1, int(length + (length * random.randint(-10, 10) * 0.01)))
        t.down()
        t.width(width)
        t.color(*map(lambda p: int(p * 255), cm(color_offset + current_level)[:3]))
        t.forward(current_length)

        # 枝の伸び先は？
        new_pos = (t.xcor(), t.ycor())

        #各枝の先端から、さらに3本の枝を生やす
        num_branches = 3
        spread_angle = 50  # 枝が広がる角度
        start_angle = heading - (spread_angle / 2)
        angle_step = spread_angle / (num_branches - 1)

        for i in range(num_branches):
            branch_heading = start_angle + (i * angle_step) + random.randint(-3, 3)

            next_branches.append((
                new_pos,
                branch_heading,
                math.ceil(current_length * 0.65), # 短く
                math.ceil(width * 0.60),          # 補足
                current_level + 1
            ))

    # 次の層
    branches = next_branches

# 要するにわさわさしてるつぼみ部分を作る
for pos, heading, length, width, current_level in branches:
    t.up()
    t.goto(pos[0], pos[1])
    t.down()
    t.width(8)  # つぼみのサイズ
    t.color(*map(lambda p: int(p * 255), cm(color_offset + current_level)[:3]))
    t.forward(1)
