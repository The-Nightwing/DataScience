import numpy as np
import cv2
import matplotlib.pyplot as plt
import pandas as pd

pic3 = cv2.imread('bottom_left.jpg')
pic3 = cv2.resize(pic3, (200, 200))
pic4 = cv2.imread('bottom_right.jpg')
pic4 = cv2.resize(pic4, (200, 200))
pic5 = cv2.imread('center.jpeg')
pic5 = cv2.resize(pic5, (100, 100))
pic1 = cv2.imread('top_left.jpg')
pic1 = cv2.resize(pic1, (200, 200))
pic2 = cv2.imread('top_right.jpg')
pic2 = cv2.resize(pic2, (200, 200))


pic3 = cv2.cvtColor(pic3, cv2.COLOR_BGR2RGB)
pic4 = cv2.cvtColor(pic4, cv2.COLOR_BGR2RGB)
pic5 = cv2.cvtColor(pic5, cv2.COLOR_BGR2RGB)
pic1 = cv2.cvtColor(pic1, cv2.COLOR_BGR2RGB)
pic2 = cv2.cvtColor(pic2, cv2.COLOR_BGR2RGB)

pic5_h = np.zeros((120, 10, 3), dtype='uint8')
pic5_v = np.zeros((10, 100, 3), dtype='uint8')
pic5 = np.vstack([pic5_v, pic5, pic5_v])
pic5 = np.hstack([pic5_h, pic5, pic5_h])

border_vertical = np.zeros((10, 430, 3), dtype="uint8")
border_horizontal = np.zeros((200, 10, 3), dtype="uint8")

print(pic5.shape, pic2.shape)

pokemon12 = np.hstack([border_horizontal, pic1, border_horizontal, pic2, border_horizontal])
pokemon34 = np.hstack([border_horizontal, pic3, border_horizontal, pic4, border_horizontal])

collage = np.vstack([border_vertical, pokemon12, border_vertical, pokemon34, border_vertical])

collage[155:155 + pic5.shape[0], 155:155 + pic5.shape[1]] = pic5

plt.imshow(collage)  # to see the collage
plt.show()

r = []
g = []
b = []

for row in range(collage.shape[0]):
    for col in range(collage.shape[1]):
        r.append(collage[row][col][0])
        g.append(collage[row][col][1])
        b.append(collage[row][col][2])

df = pd.DataFrame({'r': r, 'g': g, 'b': b})
print(df.shape)
df.to_csv("submission.csv", index=False)

cv2.waitKey(0)
cv2.destroyAllWindows()
