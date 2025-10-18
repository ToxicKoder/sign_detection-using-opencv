import cv2

camera = cv2.VideoCapture(0)

# for adjusting the size of the camera to the laptop screen
width = 1280
height = 720

camera.set(cv2.CAP_PROP_FRAME_HEIGHT , height)
camera.set(cv2.CAP_PROP_FRAME_WIDTH , width)


actual_height = camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
actual_width = camera.get(cv2.CAP_PROP_FRAME_WIDTH)


print("Camera opening...")

while True:
    ret , frame = camera.read()
    if not ret:
        print("Failed to grab the frame..")
        break

    

    frame_h = cv2.flip(frame,1) # 1 is for horizontal flip
        
    cv2.putText(
        frame_h,
        "Hello Aditya Welcome to VS Code.",
        (740,50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255,0,0),
        2,
        cv2.LINE_AA
    )

    cv2.imshow("Camera feed",frame_h) 

    if cv2.waitKey(1) & 0xFF == ord(' '):
        break

if not camera.isOpened():
    print("Not able to open the camera....")

else:
    print(f"camera closed")

camera.release()
cv2.destroyAllWindows()
    