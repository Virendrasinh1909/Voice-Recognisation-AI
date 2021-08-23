import datetime
import re
time_now = datetime.datetime.now()
#-----------------------------------------------------Hotword------------------------------------------------------------------
def hotword(word):
    if word == "what is the year" or word == "what's the year":
        return time_now.year
    
    elif word == "what is the day today" or word == "what's the day today":
        return time_now.strftime("%A")
    
    elif word == "what is the month" or word == "what's the month":
        return time_now.strftime("%B")
    
    elif word == "what is the date today" or word == "what's the date today" or word == "what's the date":
        return time_now.strftime("%d") + "th " + time_now.strftime("%B") + " " + time_now.strftime("%Y")
    
    elif word == "what is the time now" or word == "what's the time now":
        return time_now.strftime("%I") + time_now.strftime("%p") + " " + time_now.strftime("%M") + " Minute and " + time_now.strftime("%S") + " Seconds"
    else:
        return "Sorry I don't know the Answer..!"
