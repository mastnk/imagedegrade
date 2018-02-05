#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
from scipy import ndimage
import numpy as np

import degrade.im


def jpeg( input, jpeg_quality, intensity_range = (0,1) ):
	assert( isinstance( input, np.ndarray) )
	
	if( input.dtype != np.uint8 ):
		ar = ( input - intensity_range[0] ) / ( intensity_range[1] - intensity_range[0] ) * 255.
		img = Image.fromarray( ar.astype(np.uint8) )
		img = degrade.im.jpeg( img, jpeg_quality = jpeg_quality )
		ar = np.asarray( img, dtype=input.dtype )
		return ar / 255.0 * ( intensity_range[1] - intensity_range[0] ) + intensity_range[0]
		
	else:
		img = Image.fromarray( input )
		img = degrade.im.jpeg( img, jpeg_quality = jpeg_quality )
		return np.asarray( img, dtype=input.dtype )

def noise( input, noise_sigma ):
	assert( isinstance( input, np.ndarray) )
	return input + np.random.normal(0., noise_sigma, input.shape )

def blur( input, blur_sigma ):
	assert( isinstance( input, np.ndarray) )
	return ndimage.gaussian_filter(input, sigma=[blur_sigma,blur_sigma,0], truncate=3.0, mode='nearest' )

def blur_noise_blur( input, blur_sigma, noise_sigma, jpeg_quality, intensity_range = (0,1) ):
	output = input
	
	if( blur_sigma > 0 ):
		output = blur( output, blur_sigma )
	
	if( noise_sigma > 0 ):
		output = noise( output, noise_sigma )
	
	output = jpeg( input, jpeg_quality, intensity_range )
	
	return output
