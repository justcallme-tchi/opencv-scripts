import cv2
img = cv2.imread('code.png')        # put a sample image in your folder
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 1.5)
edges = cv2.Canny(blur, 50, 150)
cv2.imwrite('edges.jpg', edges)

# ORB keypoints
orb = cv2.ORB_create()
kp = orb.detect(gray, None)
img_kp = cv2.drawKeypoints(img, kp, None, flags=0)
cv2.imwrite('orb_keypoints.jpg', img_kp)
