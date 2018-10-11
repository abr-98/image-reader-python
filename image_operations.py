import image_rotation
import image_crop
import image_resize
import image_erase


def rotate(str):
    img_rotate(str)
def crop(str):
    img_crop(str)

def resize(str):
    img_resize(str)
def erase(str):
    img_erase(str)
def img_opt():
    str=raw_input("Enter the image ")
    ch_int=1
    while ch_int != 5:
        print("-----------------------OPTIONS-----------------------")
        print("1.Rotate")
        print("2.crop")

        print("3.resize")
        print("4.erase")
        print("5.exit")
        ch=raw_input("Enter your choice: ")
        ch_int=int(ch)

        switcher = {
            1: rotate,
            2: crop,

            3: resize,
            4: erase
        }
        # Get the function from switcher dictionary
        func = switcher.get(ch_int, "Invalid operation")
