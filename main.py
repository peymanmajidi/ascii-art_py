import PIL
try:
    import Image
except ImportError:
    from PIL import Image


# List of characters gonna replaced with pixel: darker to lighter
# '@':0 BLACK ==> '*':125 GRAY ==> '.':255 WHITE
ASCII_CHARS = ["@", "#", "S", "X", "?", "*", "+", ";", ":", ",", "."]

# import cv2
# stream = cv2.VideoCapture('rtsp://admin:12345@192.168.1.1/1')  


# First step: Resize to fit in terminal window
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height/width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)

# Second step: Make a black&white(gray scale) image 'cause terminal is grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)
    
# Third step: Represent each pixel by a ASCII Character
def pixels_to_ascii(image):
    pixels = image.getdata()

    characters = ""
    for pixel in pixels:
        code = ASCII_CHARS[pixel//24]
        characters+= code
        #print(f"::{pixel} => {code}")

    return(characters)    


# Main Function
def main(new_width=100):
    path = "sample.png"
    image = PIL.Image.open(path)
     
    new_image_data = pixels_to_ascii(grayify(resize_image(image)))
    
    pixel_count = len(new_image_data) 
    # Make a new line after each 100 character: new width
    ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, pixel_count, new_width)])

    print(ascii_image)
    
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)
 

if __name__ == "__main__":
    main()