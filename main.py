# ----- Average Speed Calculation -----

# time conversion function
def time_conversion(time):
    mins = round(time)
    if mins < 60:
        return str(mins) + " minutes"
    else:
        minutes = 0
        if mins % 60 == 0:
            hours = mins / 60
        else:
            minutes = mins % 60
            hours = (mins-minutes)/60
        return str(round(hours)) + " hour(s), " + str(minutes) + " minute(s)"


# main calc function
def avg_speed_calc():
    num = int(input("How many tracks do you want to calculate: "))
    total_dis = total_time = 0.0
    for x in range(num):
        dis = float(input("Track " + str(x+1) + " Distance (in km): "))
        total_dis += dis
        speed = float(input("Track " + str(x+1) + " Speed (in km/h): "))
        # Time in hours
        time = round((dis / speed), 2)
        total_time += time
        # Time in minutes for printing
        minutes = (dis*1000)/(speed/3.6)/60
        print("Time: " + time_conversion(minutes) + "\n")
    avg_speed = round((total_dis / total_time), 2)
    print("Your average speed was " + str(avg_speed) + "km/h.")


# Call main func to calc avg speed
if __name__ == '__main__':
    avg_speed_calc()
