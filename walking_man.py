#made by malcolm
#shows man walking across screen, in a loop
import ui
import time

@ui.in_background

def walk():
    counter = 1
    while(counter<=10):
        if counter == 1:
            view['imageview1'].image = ui.Image.named('./assets/walking_man_1.BMP')
        elif counter == 2:
            view['imageview1'].image = ui.Image.named('./assets/walking_man_2.BMP') 
        elif counter == 3:
            view['imageview1'].image = ui.Image.named('./assets/walking_man_3.BMP')
        elif counter == 4:
            view['imageview1'].image = ui.Image.named('./assets/walking_man_4.BMP')
        elif counter == 5:
            view['imageview1'].image = ui.Image.named('./assets/walking_man_5.BMP')
        elif counter == 6:
            view['imageview1'].image = ui.Image.named('./assets/walking_man_6.BMP')
        elif counter == 7:
            view['imageview1'].image = ui.Image.named('./assets/walking_man_7.BMP')
        elif counter == 8:
            view['imageview1'].image = ui.Image.named('./assets/walking_man_8.BMP')
        elif counter == 9:
       	    view['imageview1'].image = ui.Image.named('./assets/walking_man_9.BMP')
        elif counter == 10:
            view['imageview1'].image = ui.Image.named('./assets/walking_man_10.BMP')
            if counter >= 10:
                counter = 0
        
        view['imageview1'].x = view['imageview1'].x  - 10
  
        counter = counter + 1
        time.sleep(.25)
walk()

view = ui.load_view()
view.present('sheet')
