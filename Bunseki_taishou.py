import turtle
import colorsys

# 画面の設定
turtle.bgcolor("black")
turtle.speed(0)
turtle.tracer(10, 0)  # 描画速度を爆速にする設定
turtle.hideturtle()

# 美しい螺旋を描く
for i in range(400):
    # HSVからRGBへ変換して、滑らかなグラデーションを作る
    color = colorsys.hsv_to_rgb(i / 300, 1.0, 1.0)
    turtle.pencolor(color)

    # 芸術的な幾何学模様を作るための絶妙な角度と長さ
    turtle.forward(i * 1.2)
    turtle.right(149)  # この角度が美しい対称性を生み出します
    turtle.circle(i, 30)

turtle.done()