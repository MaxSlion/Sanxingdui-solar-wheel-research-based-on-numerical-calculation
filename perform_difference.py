import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np

def read_images(image1_path, image2_path):
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)
    return image1, image2

def resize_image(image, width, height):
    return cv2.resize(image, (width, height))

def overlay_images(image1, image2, coordinates):
    x, y = coordinates
    height, width, _ = image2.shape
    image1[y:y+height, x:x+width] = image2
    return image1

def perform_difference(image1, image2):
    global difference
    difference = cv2.absdiff(image1, image2)
    return difference

def show_image_on_gui(image, title="Image"):
    global photo
    root = tk.Tk()
    root.title(title)

    # Convert image to PhotoImage format for tkinter
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_pil = Image.fromarray(np.uint8(image))
    # Convert the PIL Image to PhotoImage for tkinter and create a reference
    photo = ImageTk.PhotoImage(image_pil)
    # Display the image on a label
    image_pil.save(r"./1111.png")
    label = tk.Label(root, image=photo)
    label.pack()

    # Function to save the image
    # def save_image():
    #     save_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg")])
    #     if save_path:
    #         image_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    #         cv2.imwrite(save_path, image_bgr)
    #         print("Image saved successfully!")

    # Add a Save button
    # save_button = tk.Button(root, text="Save", command=save_image)
    # save_button.pack()

    root.mainloop()

if __name__ == "__main__":
    image1_path = "./repair-mask-half.png"  # Replace with the actual path of your first image
    image2_path = "./origin-mask.png"  # Replace with the actual path of your second image

    # Step 1: Read the images
    image1, image2 = read_images(image1_path, image2_path)

    # Step 2: Resize the images to the same dimensions
    height, width = 751, 751  # Set the desired dimensions
    image1_resized = resize_image(image1, width, height)
    image2_resized = resize_image(image2, width, height)

    # Step 3: Overlay the images at specified coordinates (x, y)
    coordinates = (0, 0)  # Replace with the desired coordinates
    combined_image = overlay_images(image1_resized.copy(), image2_resized, coordinates)

    # Step 4: Perform difference operation
    difference_image = perform_difference(image1_resized, image2_resized)

    # Step 5: Display the difference image with a Save button on GUI
    show_image_on_gui(difference_image, "Difference Image")
