from wordcloud import WordCloud , STOPWORDS , ImageColorGenerator
import matplotlib.pyplot as plt #to display our world cloud
from PIL import Image #to load our image
import numpy as np #to get the color of our image

#Content-Related
text = open('batman.txt','r').read()
stopwords = set(STOPWORDS)

#Apperence-Related
custom_mask = np.array(Image.open('kakashi.png'))
wc = WordCloud(background_color = 'white',
	           stopwords = stopwords,
	           mask = custom_mask,
	           contour_width = 1,
	           contour_color = 'black')

wc.generate(text)
#Plotting
plt.imshow(wc, interpolation = 'bilinear')
plt.axis('off')
plt.show()

