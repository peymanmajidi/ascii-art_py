import PIL
try:
    import Image
except ImportError:
    from PIL import Image

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", ".", " "]

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height/width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)


def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)
    

def pixels_to_ascii(image):
    pixels = image.getdata()

    characters = ""
    for pixel in pixels:
        code = ASCII_CHARS[pixel//22]
        characters+= code

        print(f"char:'{chr(pixel)}'")

    return(characters)    

def main(new_width=100):
    # path = "pey.jpg"
    path = "sample.png"
    image = PIL.Image.open(path)
     
    new_image_data = pixels_to_ascii(grayify(resize_image(image)))
    
    pixel_count = len(new_image_data)  
    ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, pixel_count, new_width)])

    print(ascii_image)
    
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)
 

if __name__ == "__main__":
    main()