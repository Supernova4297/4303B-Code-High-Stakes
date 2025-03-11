import turtle as tutel
b = tutel.Turtle()
b.shape("turtle")
b.setheading(180) # heading 0
b.back(12)
b.setheading(0) # heading 180
b.forward(24)
b.setheading(270) # heading 90
b.forward(24)
b.setheading(180) # heading 0
b.forward(24)
b.forward(12)
b.setheading(180 + 135)
b.forward(16.97) 
b.setheading(180 - 153.435) # heading -153.435
b.back(13.8)
b.dot() # Marks the end of the first goal
# finished coding 

b.color("red")
b.forward(14.333)
b.right(333.435) # heading 180
b.forward(48)
b.left(90) # heading 90
b.dot("#FFD700") # Marks Lady Brown Usage
b.right(146.31) # heading -123.69
b.forward(43.2666)
b.left(11.31) # heading -135
b.forward(33.9411255)
b.right(90) # heading -45
b.forward(33.9411255)
b.left(45) # heading -90
b.forward(24)
b.left(90) # heading 180
b.forward(24)
b.forward(12)
b.right(135) # heading -45
b.forward(16.97)
b.left(296.565) # heading -161.565
b.back(14.0)
b.dot() # End of Goal 2

b.color("#009999")
b.forward(13.8)
b.left(90) # heading 108.435
b.back(37.947332)
b.left(11.32) # heading 97.025
b.back(90.7471)
b.dot() # end of goal 3

b.color("#CC0099")
b.right(37.975) # heading -45
b.forward(97.5807358)
b.left(161.56505) # heading 26.56505
b.back(53.66563)
b.right(26.56505) # heading 180
b.forward(24)
b.right(90) # heading 90
b.forward(24)
b.right(90) # heading 0
b.forward(24)
b.forward(12)
b.left(135) # heading 135
b.forward(16.97056)
b.right(288.435) # heading 153.435
b.back(13.8)
b.dot() # Marks the end of the last goal

b.color("#0000ff")
b.forward(14.333)
b.left(333.435) # heading 180
b.forward(48)
b.right(90) # heading -90
b.dot("#FFD700") # Marks Lady Brown Usage
b.left(146.30993) # heading 33.69007
b.forward(43.2666153)
b.left(78.69006) # heading 135
b.forward(16.97056)

input("This is the end! ")