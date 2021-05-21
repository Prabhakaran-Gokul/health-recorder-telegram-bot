import cv2
import imutils
from imutils.convenience import resize

class UrineAnalyser:
    def __init__(self):
        self.resize_ratio = None
        self.original_image = None
        self.original_image_resized = None

    def preprocess_image(self, image, threshold):
        grayed_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred_image = cv2.GaussianBlur(grayed_image, (5,5), 0)
        thresh_image = cv2.threshold(blurred_image, threshold, 255, cv2.THRESH_BINARY)[1]
        eroded_image = cv2.erode(thresh_image, None, iterations=5)
        dialated_image = cv2.dilate(eroded_image, None, iterations=5)
        return dialated_image

    def resize_image(self, image):
        resized_image = imutils.resize(image, width=300)
        self.original_image_resized = resized_image
        return resized_image

    def load_image(self, file_name):
        image = cv2.imread(filename = file_name)
        self.original_image = image
        return image

    def draw_contours(self, image):
        cnts = cv2.findContours(image, cv2.RETR_LIST)


def canny_threshold(value):
    low_threshold = value
    # img_blur = cv2.blur(grayed_image, (3,3))
    img_blur = cv2.GaussianBlur(grayed_image, (5,5), 0)
    detected_edges = cv2.Canny(img_blur, low_threshold, low_threshold*3, 3)
    mask = detected_edges != 0
    dst = image * (mask[:,:,None].astype(image.dtype))
    cv2.imshow("Edge Map", dst)

if __name__ == "__main__":
    UA = UrineAnalyser()
    image = UA.load_image("images/2015-01-21 20:48/cropped1.png")
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    
    # resized = UA.resize_image(image)
    # cv2.imshow("Resized", resized)
    # cv2.waitKey(0)
    
    # processed = UA.preprocess_image(resized, 150)
    # cv2.imshow("Processed", processed)
    # cv2.waitKey(0)

    # masked = cv2.bitwise_and(UA.original_image_resized, UA.original_image_resized, mask=processed)
    # cv2.imshow("Masked", masked)
    # cv2.waitKey(0)

    grayed_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.namedWindow("Edge Map")
    max_threshold = 100
    cv2.createTrackbar("Min Threshold:", "Edge Map", 0, max_threshold, canny_threshold)
    canny_threshold(0)
    cv2.waitKey(0)
    # grayed_image = cv2.cvtColor(masked, cv2.COLOR_BGR2GRAY)
    # blurred_image = cv2.GaussianBlur(grayed_image, (5,5), 0)
    # edged_image = cv2.Canny(blurred_image, 150 , 220)
    # thresh_image = cv2.threshold(blurred_image, 210, 255, cv2.THRESH_BINARY_INV)[1]
    # cv2.imshow("thresh_image", thresh_image)
    # cv2.waitKey(0)

    # fin = cv2.bitwise_and(UA.original_image_resized, UA.original_image_resized, mask=thresh_image)
    # cv2.imshow("fin", fin)
    # cv2.waitKey(0)


