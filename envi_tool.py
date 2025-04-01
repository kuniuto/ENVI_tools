# from pycocotools.coco import COCO
# from PIL import Image
import matplotlib.pyplot as plt
import cv2
import numpy as np
# import argparse
# import math
# import os
# import spectral.io.envi as envi
import spectral as sp
from random import randint
# import pandas as pd

import keyboard

color_wavelengths = [450, 550, 650]


def color_enhancement(envi_fname,color_wavelengths,band_width):
    hdr_fname = envi_fname+'.hdr'
    dat_fname = envi_fname+'.dat'

    ##################
    # read ENVI file #
    ##################
    hdr = sp.envi.open(hdr_fname)
    wavelengths_list = hdr.bands.centers
    height, width, bands = hdr.nrows, hdr.ncols, hdr.nbands

    color_bands = []
    for w in color_wavelengths:
        diff = np.absolute(np.array(wavelengths_list)-w)
        index = diff.argmin()
        color_bands.append(index)
    print(f'loading {envi_fname}')
    r_cube = hdr.load()

    color_range = []
    for w in color_wavelengths:
        w_temp = w-band_width/2
        diff = np.absolute(np.array(wavelengths_list)-w_temp)
        index_low = diff.argmin()
        w_temp = w+band_width/2
        diff = np.absolute(np.array(wavelengths_list)-w_temp)
        index_high = diff.argmin()
        color_range.append([index_low, index_high]) 

    r_color_image = r_cube.read_bands(color_bands)
    # r_color_image[r_color_image > 1.0] = 1.0
    
    for i, b_range in enumerate(color_range):
        cube_temp = r_cube[:,:,b_range[0]:b_range[1]]
        layer = np.mean(cube_temp,2)
        r_color_image[:,:,i] = layer

    r = cv2.selectROI("select White Diffuse Reflectance Standard", r_color_image[:,:,[2,1,0]]) 
    cv2.destroyWindow("select White Diffuse Reflectance Standard")

    cropped_cube = r_color_image[int(r[1]):int(r[1]+r[3]),  
                        int(r[0]):int(r[0]+r[2]),:] 
    

    max_value = np.amax(cropped_cube)
    print(f'max value = {max_value}')

    r_color_image_enhanced = r_color_image/max_value

    cv2.imwrite(f'{envi_fname}_original_color.png',r_color_image[:,:,[2,1,0]]*255)
    cv2.imwrite(f'{envi_fname}_enhanced_color.png',r_color_image_enhanced[:,:,[2,1,0]]*255)


    fig, axes = plt.subplots(1, 2, tight_layout=True)
    axes[0].imshow(r_color_image)
    axes[0].set_title('original reflectance color image')
    axes[1].imshow(r_color_image_enhanced)
    axes[1].set_title('enhanced reflectance color image')
    plt.show()

def sample_rois(fname):
    hdr_fname = fname+'.hdr'
    dat_fname = fname+'.dat'

    hdr = sp.envi.open(hdr_fname)

    wavelengths_list = hdr.bands.centers

    height, width, bands = hdr.nrows, hdr.ncols, hdr.nbands

    color_bands = []
    for w in color_wavelengths:
        diff = np.absolute(np.array(wavelengths_list)-w)
        index = diff.argmin()
        color_bands.append(index)

    print(f'loading {fname}')
    r_cube = hdr.load()


    r_color_image = r_cube.read_bands(color_bands)
    r_color_image[r_color_image > 1.0] = 1.0

    color_image_uint8_by_cv2 = cv2.normalize(r_color_image, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

    color_image_uint8_by_cv2_bboxes = color_image_uint8_by_cv2

    print("press ESCAPE to finish selecting RoIs")
    RoIs = []
    count = 0
    color_list = []
    while True:
        if keyboard.is_pressed('escape'):
            break
        else:
            r = cv2.selectROI("select RoI: press ESCAPE to finish selecting RoIs", color_image_uint8_by_cv2_bboxes)
            B, G, R = randint(0, 255), randint(0, 255), randint(0, 255)
            cv2.rectangle(color_image_uint8_by_cv2_bboxes,  (r[0],r[1]), (int(r[0]+r[2]), int(r[1]+r[3])), (B,G,R), 2)
            cv2.putText(color_image_uint8_by_cv2_bboxes, str(count), (r[0], r[1]-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (B,G,R))
            RoIs.append(r)
            color_list.append(tuple([float(R)/255.0,float(G)/255.0,float(B)/255.0]))
            count += 1
    cv2.destroyWindow("select RoI: press ESCAPE to finish selecting RoIs")

    plt.figure()
    plt.imshow(color_image_uint8_by_cv2_bboxes[:,:,[2,1,0]])

    RoIs.pop()
    color_list.pop()
    num_RoIs = len(RoIs)

    ref_matrix = np.zeros((bands,num_RoIs))
    for i,r in enumerate(RoIs):
        cropped_cube = r_cube[int(r[1]):int(r[1]+r[3]),  
                        int(r[0]):int(r[0]+r[2]),:] 
        ref_temp = []
        for k in range(bands):
            m = np.mean(cropped_cube[:,:,k].flatten())
            ref_temp.append(m)
        ref_matrix[:,i] = ref_temp


    plt.figure()
    for i,r in enumerate(RoIs):
        c = list(color_list[i])

        plt.plot(wavelengths_list, ref_matrix[:,i], color=c,label=str(i), linewidth = 2)
    plt.xlabel('Wavelength [nm]') 
    plt.ylabel('Reflectance')
    plt.legend()
    plt.show()
