import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi
import cv2
import random

param_rand=6

for num_points in [1000,5000,10000,15000,20000,25000,30000,35000,40000,45000,50000,100000]:
#for num_points in [1000]:
    for image_file in ['Norris','Sil','Sil2']:
    #for image_file in ['Sil3']:
        image=cv2.imread(image_file + '.jpg')
        height, width, _ = image.shape

        img_blue,img_green,img_red=cv2.split(image)
        image=cv2.merge((img_red, img_green, img_blue))

        points=np.random.randint([width,height],size=(num_points,2))

        # compute Voronoi tesselation
        vor = Voronoi(points)
        plt.figure(figsize=(width/100,height/100),frameon=False)
        for i, region in enumerate(vor.regions):
            if not -1 in region and len(region)>2:
                polygon = [vor.vertices[i] for i in region]
                polycolor=image[height-points[list(vor.point_region).index(i)][1],points[list(vor.point_region).index(i)][0],:]/255+[(random.random()-0.5)/param_rand,(random.random()-0.5)/param_rand,(random.random()-0.5)/param_rand]
                polycolor=[min(1,max(0,i)) for i in polycolor]
                plt.fill(*zip(*polygon),color=polycolor)

        #plt.plot(points[:,0], points[:,1], 'ko')
        #plt.axis('equal')
        plt.xlim(0, width)
        plt.ylim(0, height)
        plt.axis('off')
        plt.savefig(image_file + '_' + str(num_points) + '_' + str(param_rand) + '.jpg')
        print(image_file + '_' + str(num_points) + '.jpg   - DONE!')
        #plt.show()
        plt.clf()




