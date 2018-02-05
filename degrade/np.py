#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
import numpy
import im

from scipy import ndimage

def jpeg( input, jpeg_quality, intensity_range = (0,1) ):
	assert( isinstance( input, numpy.ndarray) )
	
	if( input.dtype != numpy.uint8 ):
		ar = ( input - intensity_range[0] ) / ( intensity_range[1] - intensity_range[0] ) * 255.
		img = Image.fromarray( ar.astype(numpy.uint8) )
		img = im.jpeg( img, jpeg_quality = jpeg_quality )
		ar = numpy.asarray( img, dtype=input.dtype )
		return ar / 255.0 * ( intensity_range[1] - intensity_range[0] ) + intensity_range[0]
		
	else:
		img = Image.fromarray( input )
		img = im.jpeg( img, jpeg_quality = jpeg_quality )
		return numpy.asarray( img, dtype=input.dtype )

def noise( input, noise_sigma ):
	assert( isinstance( input, numpy.ndarray) )
	return input + numpy.random.normal(0., noise_sigma, input.shape )

def blur( input, blur_sigma ):
	assert( isinstance( input, numpy.ndarray) )
	return ndimage.gaussian_filter(input, sigma=[blur_sigma,blur_sigma,0], truncate=3.0, mode='nearest' )

def blur_noise_blur( input, blur_sigma, noise_sigma, jpeg_quality, intensity_range = (0,1) ):
	output = input
	
	if( blur_sigma > 0 ):
		output = blur( output, blur_sigma )
	
	if( noise_sigma > 0 ):
		output = noise( output, noise_sigma )
	
	output = jpeg( input, jpeg_quality, intensity_range )
	
	return output
