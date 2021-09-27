WIDTH = 1287
HEIGHT = 700
main_box = Rect(0, 0, 820, 240)
timer_box = Rect(0, 0, 320, 240)

answer1 = Rect(0, 0, 495, 165)
answer2 = Rect(0, 0, 495, 165)
answer3 = Rect(0, 0, 495, 165)
answer4 = Rect(0, 0, 495, 165)

main_box.move_ip(50, 40)
timer_box.move_ip(990, 40)

answer1.move_ip(50, 358)
answer2.move_ip(735, 358)
answer3.move_ip(50, 538)
answer4.move_ip(735, 528)

answers = [answer1, answer2, answer3, answer4]

score = 0
time_left = 15

q1 = ["what is the capital of France?",
    "London", "Paris", "Berlin", "Tokyo", 2]

q2 = ["what is 7+27?",
    "22", "40", "36", "34", 3]

q3 = ["what is the seventh month of the year?",
    "June", "April", "May", "July", 4]

q4 = ["which planet is closest to the sun?",
    "Mercury", "Saturn", "Neptune", "Venus", 1]

q5 = ["what is a quarter of 200?",
    "37", "50", "46", "150", 2]

q6 = ["what is the name of my sister?",
    "mary", "ava", "sofia", "mia", 4]

q7 = ["how much lego sets do I have?",
    "74", "16", "100+", "50", 3]

questions = [q1, q2, q3, q4, q5, q6, q7]
question = questions.pop(0)

def draw():
    screen.fill("dim gray")
    screen.draw.filled_rect(main_box, "sky blue")
    screen.draw.filled_rect(timer_box, "sky blue")
    
    for answer in answers:
        screen.draw.filled_rect(answer, "orange")
        
    screen.draw.textbox(str(time_left), timer_box, color=("black"))
    screen.draw.textbox(question[0], main_box, color=("black"))
    
    index = 1
    for answer in answers:
        screen.draw.textbox(question[index], answer, color=("black"))
        index = index + 1
        
def game_over():
    global question, time_left
    message = "Game over! you got %s questions correct" % str(score)
    question = [message, "-", "-", "-", "-", 5]
    time_left = 0
    
def correct_answer():
    global question, score, time_left
    
    score = score + 1
    if questions:
        question = questions.pop(0)
        time_left = 10
    else:
        game_over()

def on_mouse_down(pos):
    index = 1
    for answer in answers:
        if answer.collidepoint(pos):
            if index == question[5]:
                correct_answer()
            else:
                game_over()
        index = index + 1
        
def upadate_time_left():
    global time_left
    
    if time_left:
        time_left = time_left - 1
    else:
        game_over()
        
clock.schedule_interval(upadate_time_left, 1.0)
