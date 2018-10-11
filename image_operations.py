import image_rotation
import image_crop
import image_enhance
import image_resize
import image_erase


def rotate(str):
    img_rotate(str)
def crop(str):
    img_crop(str)
def enhance(str):
    img_enhance(str)
def resize(str):
    img_resize(str)
def erase(str):
    img_erase(str)
def img_opt():
    str=raw_input("Enter the image ")
    ch_int=1
    while ch_int != 6:
        print("-----------------------OPTIONS-----------------------")
        print("1.Rotate")
        print("2.crop")
        print("3.enhance")
        print("4.resize")
        print("5.erase")
        print("6.exit")
        ch=raw_input("Enter your choice: ")
        ch_int=int(ch)

        switcher = {
            1: rotate,
            2: crop,
            3: enhance,
            4: resize,
            5: erase
        }
        # Get the function from switcher dictionary
        func = switcher.get(ch_int, "Invalid operation")
