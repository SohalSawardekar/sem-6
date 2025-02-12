import cv2

# Load the image
image_path = 'C:/Users/sohal/OneDrive/Pictures/Screenshots/Screenshot 2025-01-04 225820.png'
image = cv2.imread(image_path)
print(image)

# Apply grayscale filter
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(grayscale_image)

# Apply blur filter
blurred_image = cv2.GaussianBlur(image, (15, 15), 0)
print(blurred_image)

# Apply edge detection
edges = cv2.Canny(image, 100, 200)
print(edges)

# Display the images
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", grayscale_image)
cv2.imshow("Blurred Image", blurred_image)
cv2.imshow("Edges", edges)

# Wait for a key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
