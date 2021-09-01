import os ,sys
import time
from plyer import notification as nf

if __name__ == "__main__":

    icon = os.path.join(sys.path[0],"icon/glass-of-water.png")
    while True:    
        nf.notify(
            title = "Please Water Now !",
            message = "The U.S. National Academies of Sciences, Engineering,\n and Medicine determined that an adequate daily \nfluid intake is: About 15.5 cups (3.7 liters) of fluids a day for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
            app_icon = icon,
            timeout = 10
        )
        time.sleep(60*60)