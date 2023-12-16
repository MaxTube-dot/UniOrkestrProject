import cv2

# Load the BMP image
image_path = 'D:/AtomicHack/UniProject/ModelYolo/train/images/4387_frame0006.bmp'
image = cv2.imread(image_path)

height, width, _ = image.shape

# Load the COCO format annotation from the text file
annotation_path = 'D:/AtomicHack/UniProject/ModelYolo/train/labels/4387_frame0006.txt'
with open(annotation_path, 'r') as f:
    annotation_lines = f.readlines()

# Iterate over the annotation lines
for line in annotation_lines:
    # Parse the bounding box coordinates
    t = line.strip().split(' ')
    classes, x1, y1, x2, y2 = map(float, line.strip().split(' '))


    x, y, w, h = int(abs(x1 - x2) * width / 2), int(abs(y1 - y2) * height/2), 80, 80

    pt1 = (int(x1 * width),int( y1 * height))
    pt2 = (int(x2 * width), int( y2 * height))
    # Draw the bounding box on the image
    if classes == 8:
        cv2.rectangle(image, pt1, pt2, (129, 255, 0), 4)
    else:
        cv2.rectangle(image, pt1, pt2, (0, 255, 0), 2)


# Display the image with the bounding boxes
cv2.imshow('Image with Bounding Boxes', image)
cv2.waitKey(0)
cv2.destroyAllWindows()