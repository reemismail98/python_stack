def clockAngle(second):
    hours = int(second/3600)
    minutes = int((second % 3600)/ 60)
    seconds = (second % 3600) % 60
    
    degreeHour = 30 * hours
    degreeMinutes = 6 * minutes
    degreeSecond = 6 * seconds
    
    print(f"{hours}:{minutes}:{seconds}")
    print(f"Hours: {degreeHour} Degrees \nMinutes: {degreeMinutes} Degrees \nSeconds: {degreeSecond} Degrees")

clockAngle(4000)

