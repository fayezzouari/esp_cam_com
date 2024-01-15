import cv2
import urllib.request
import numpy as np


url = "http://192.168.0.51/cam-hi.jpg"
im = None


def run1():
    while True:
        img_resp = urllib.request.urlopen(url)
        imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
        im = cv2.imdecode(imgnp, -1)

        cv2.imshow("live transmission", im)
        key = cv2.waitKey(5)
        if key == ord("q"):
            break

    cv2.destroyAllWindows()


def main():
    print("started")
    run1()


if __name__ == "__main__":
    main()
