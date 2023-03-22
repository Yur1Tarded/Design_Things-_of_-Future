import cv2

def video_proc():
    cap = cv2.VideoCapture('cam_video.mp4')
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21,21), 0)
        ret, thresh = cv2.threshold(gray, 105, 255, cv2.THRESH_BINARY_INV)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            x,y,w,h = cv2.boundingRect(c)
            centr = (x+(w//2), y+(h//2))
            print(centr)
            cv2.circle(frame, (centr), h//2, (0, 255, 0), 2)
        cv2.imshow('frame', frame)
        cv2.waitKey(15)

# def image_proc():
#     img = cv2.imread('img_test.jpg')
#     #cv2.imshow('frame', img)
#     #print(img.shape)
#     w, h = img.shape[:2]
#     (cX, cY) = (w // 2, h // 2)
#     M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
#     rotated = cv2.warpAffine(img, M, (w, h))
#     cv2.imshow('rotated', rotated)

if __name__ == '__main__':
    video_proc()

cv2.waitKey(15)
cv2.destroyAllWindows()