def temperature():
    temp=int(input("Enter temperature of body in Celcius:"))
    if (temp>99):
        print("you are suffering from mild fever")
    elif (temp<99 and temp>101):
            print("you fever is high")
    elif (temp<101 and temp>102):
            print("you are suffering from hard fever medications to be taken")
    elif (temp<102 and temp>103):
            print("you are suffering from extreme fever doctor help is needed")
    elif (temp>99):
            print("you are fine")
temperature()
                        
