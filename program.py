import os

def program(program):
    if program == "camera":
        os.startfile("C:/Users/New/Desktop/RawData/Speech To Text/ASLAN/ASLAN0.2/programs/Camera.lnk")
        return "Camera is Open Now.."

    elif program == "vs code" or program == "code" or program == "Visual Studio code":
        os.system("code")
        return "Visual Studio Code is Open Now.."

    elif program == "Paint":
        os.startfile("C:/Users/New/Desktop/RawData/Speech To Text/ASLAN/ASLAN0.2/programs/Paint.lnk")
        return "Paint is Open Now.."

    elif program == "Notepad":
        os.startfile("C:/Users/New/Desktop/RawData/Speech To Text/ASLAN/ASLAN0.2/programs/Notepad.lnk")
        return "Notepad is Open Now.."

    elif program == "WordPad":
        os.startfile("C:/Users/New/Desktop/RawData/Speech To Text/ASLAN/ASLAN0.2/programs/Wordpad.lnk")
        return "WordPad is Open Now.."

    elif program == "Photoshop":
        os.startfile("C:/Users/New/Desktop/RawData/Speech To Text/ASLAN/ASLAN0.2/programs/Adobe Photoshop 2020.lnk")
        return "PhotoShop is Opening Now.."

    elif program == "calculator":
        os.startfile("C:/Users/New/Desktop/RawData/Speech To Text/ASLAN/ASLAN0.2/programs/Calculator.lnk")
        return "Calculator is Open Now.."

    elif program == "calendar":
        os.startfile("C:/Users/New/Desktop/RawData/Speech To Text/ASLAN/ASLAN0.2/programs/Calendar.lnk")
        return "Calendar is Open Now.."

    elif program == "Word":
        os.startfile("C:/Users/New/Desktop/RawData/Speech To Text/ASLAN/ASLAN0.2/programs/Word 2013.lnk")
        return "MicroSoft Word is Open Now.."

    elif program == "Excel":
        os.startfile("C:/Users/New/Desktop/RawData/Speech To Text/ASLAN/ASLAN0.2/programs/Excel 2013.lnk")
        return "MicroSoft Excel is Open Now.."

    elif program == "PowerPoint":
        os.startfile("C:/Users/New/Desktop/RawData/Speech To Text/ASLAN/ASLAN0.2/programs/PowerPoint 2013.lnk")
        return "MicroSoft PowerPoint is Open Now.."

    elif program == "music":
        os.startfile("C:/Users/New/Desktop/RawData/Speech To Text/ASLAN/ASLAN0.2/programs/Groove Music.lnk")
        return "Groove Music is Open Now.."

    else:
        return "Sorry I don't know the Answer..!"
