import turtle

# Pencere ayarları / Window settings
window = turtle.Screen()
window.title("Saat Açısı Görselleştirme / Clock Angle Visualization")
window.bgcolor("white")
window.setup(width=600, height=600)


# Saat çerçevesini çizme fonksiyonu / Function to draw the clock face
def draw_clock():
    clock_face = turtle.Turtle()
    clock_face.hideturtle()
    clock_face.speed(0)
    clock_face.penup()
    clock_face.goto(0, -250)
    clock_face.pendown()
    clock_face.circle(250)

    # Saat numaralarını ekleme / Adding hour numbers
    clock_face.penup()
    clock_face.goto(0, 0)
    clock_face.setheading(90)
    for hour in range(12):
        clock_face.forward(200)
        clock_face.write(str(hour if hour != 0 else 12), align="center", font=("Courier", 18, "normal"))
        clock_face.backward(200)
        clock_face.right(30)


# Akrep ve yelkovanı çizme fonksiyonu / Function to draw hour and minute hands
def draw_hands(hour_angle, minute_angle):
    # Akrep (saat ibresi) / Hour hand
    hour_hand = turtle.Turtle()
    hour_hand.hideturtle()
    hour_hand.speed(0)
    hour_hand.color("black")
    hour_hand.penup()
    hour_hand.goto(0, 0)
    hour_hand.pendown()
    hour_hand.setheading(90 - hour_angle)
    hour_hand.forward(100)

    # Akrep açısını yazdırma / Displaying hour angle
    hour_hand.penup()
    hour_hand.goto(-150, 220)
    hour_hand.write(f"Akrep Açısı: {hour_angle}° / Hour Angle: {hour_angle}°", font=("Courier", 12, "normal"))

    # Yelkovan (dakika ibresi) / Minute hand
    minute_hand = turtle.Turtle()
    minute_hand.hideturtle()
    minute_hand.speed(0)
    minute_hand.color("blue")
    minute_hand.penup()
    minute_hand.goto(0, 0)
    minute_hand.pendown()
    minute_hand.setheading(90 - minute_angle)
    minute_hand.forward(150)

    # Yelkovan açısını yazdırma / Displaying minute angle
    minute_hand.penup()
    minute_hand.goto(-150, 190)
    minute_hand.write(f"Yelkovan Açısı: {minute_angle}° / Minute Angle: {minute_angle}°",
                      font=("Courier", 12, "normal"))

    # Açıklama yazdırma / Displaying explanation
    minute_hand.goto(-150, 150)
    minute_hand.write(
        f"Açıklama / Explanation:\n\n"
        f"1. Akrep açısı: {hour_angle}° / Hour hand angle: {hour_angle}°\n"
        f"   - Saat 1 saat döndüğünde 30 derece döner. Bu yüzden akrep açısı 30'un katıdır.\n"
        f"   - The hour hand turns 30° for every hour passed.\n\n"
        f"   - Saatin user_input for hour_angle % 30 = Saat başına kalan açı: {hour_angle % 30}°\n"
       
        f"2. Saat başına kalan açı: {hour_angle % 30}° / Remaining angle in hour: {hour_angle % 30}°\n"
        f"   - Geçerli saat içinde kalan açı.\n"
        f"   - This is the leftover angle within the current hour.\n\n"
        f"3. Yelkovan açısı = Saat başına kalan açı X 12 : {hour_angle % 30}° x 12 = {(hour_angle % 30) * 12}°\n"
        f"   - Akrep açısının her derecesi için, yelkovan 12 derece döner.\n"
        f"   - For each degree the hour hand moves, the minute hand moves 12°.\n",
        font=("Courier", 9, "normal"), align="right"
    )


# Kullanıcıdan açıyı (α) al / Get the angle (α) from the user
a = int(window.numinput("Açı Girişi / Angle Input",
                        "Akrep'in gece yarısından itibaren döndüğü açı (0-360): / Hour hand angle from midnight (0-360):",
                        minval=0, maxval=360))

# Saat çerçevesini çiz / Draw the clock face
draw_clock()

# Akrep ve yelkovanın açılarını hesapla / Calculate the angles for hour and minute hands
remaining_hour_angle = a % 30  # Akrebin mevcut saat içerisindeki açısı / Angle within the current hour
minute_hand_angle = remaining_hour_angle * 12  # Yelkovanın açısı / Minute hand angle

# Toplam saat açısını hesapla (akrep ibresi için) / Total hour angle (for hour hand)
hour_hand_angle = a

# Akrep ve yelkovanı çiz / Draw the hour and minute hands
draw_hands(hour_hand_angle, minute_hand_angle)

# Pencereyi açık tut / Keep the window open
turtle.done()
