import tkinter
import pyautogui

if __name__ == '__main__':

    window = tkinter.Tk()
    window.title("Rocket Engine Design Software")

    screen_Width, screen_Height = pyautogui.size()
    print(screen_Width, screen_Height)

    center_x = int(screen_Width / 4)
    center_y = int(screen_Height / 4)

    # set the position of the window to the center of the screen
    window.geometry("800x500+{}+{}".format(center_x,center_y))

    window.mainloop()