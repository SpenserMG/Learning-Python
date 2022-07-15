import qrcode
import time

# First discovering how to make a qr code
# dest = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

# img = qrcode.make(dest)

# img.save(f"C:/Users/smgre/OneDrive/Desktop/qrcodes/qrcode.png")


# Making a little program to create your own QR Code, giving it a url and then 
userInput = ""
userQRName = ""
keepGoing = True
qrGoing = True

print("Make your own qrcode with an image from the web or a video.\nWe'll need first the source url for the image or video, and then what you wish to name the file.")

userInput = input("Please provide the url of the image or video you would like to embed: ")
userQRName = input("Please provide what you would like to name this QR code(just provide the name, it will be saved as a .png file): ")

img = qrcode.make('{}'.format(userInput))
img.save('C:/Users/smgre/OneDrive/Desktop/qrcodes/{}.png'.format(userQRName))

time.sleep(1)

while qrGoing:
    userInput = ''
    userQRName = ''

    print("Your new QR code has been saved. Would you like to make another Y/N?")
    answer = input()

    if answer == 'Y':
        while keepGoing:
            userInput = input("Please provide the url of the image or video you would like to embed: ")
            userQRName = input("Please provide what you would like to name this QR code(just provide the name, it will be saved as a .png file): ")

            img = qrcode.make('{}'.format(userInput))
            img.save('C:/Users/smgre/OneDrive/Desktop/qrcodes/{}.png'.format(userQRName))
    elif answer == "N":
        qrGoing = False
    else:
        print("Incorrect input, please provide an approved respone of Y or N.")