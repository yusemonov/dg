from PIL import Image

# Create an Image Object from an Image
im = Image.open("input/s.png")

# Display actual image
im.show()

# Make the new image half the width and half the height of the original image
resized_im = im.resize((round(im.size[0]*0.5), round(im.size[1]*0.5)))

# Display the resized imaged
resized_im.show()

# Save the cropped image
resized_im.save('resizedBeach1.jpg')
