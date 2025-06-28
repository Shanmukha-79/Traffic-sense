import cv2
import numpy as np

cap = cv2.VideoCapture('traffic.mp4')

if not cap.isOpened():
    print("Error: Cannot open video.")
    exit()

fgbg = cv2.createBackgroundSubtractorMOG2(history=1000, varThreshold=50, detectShadows=True)

violation_line_y = 220

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (640, 360))

    enhanced = cv2.GaussianBlur(frame, (5,5), 0)
    enhanced = cv2.convertScaleAbs(enhanced, alpha=1.5, beta=30)

    fgmask = fgbg.apply(enhanced)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, np.ones((5,5), np.uint8))

    contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    violation_detected = False

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 2500:
            x, y, w, h = cv2.boundingRect(cnt)
            center_y = y + h // 2
            if center_y > violation_line_y:
                violation_detected = True
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
                cv2.putText(frame, 'Violation', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)
            else:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    line_color = (0, 0, 255) if violation_detected else (0, 255, 0)
    cv2.line(frame, (0, violation_line_y), (frame.shape[1], violation_line_y), line_color, 3)

    cv2.imshow('Traffic Rule Detection', frame)

    if cv2.waitKey(600) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
