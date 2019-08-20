#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
from scipy import ndimage
import numpy as np

import imagedegrade.im


def jpeg( input, jpeg_quality, intensity_range = (0,1), **kwargs ):
    if( not isinstance( input, np.ndarray) ):
        msg = 'The input should be numpy.ndarray.'
        raise TypeError( msg )

    if( input.dtype != np.uint8 ):
        ar = ( input - intensity_range[0] ) / ( intensity_range[1] - intensity_range[0] ) * 255.
        img = Image.fromarray( ar.astype(np.uint8) )
        img = imagedegrade.im.jpeg( img, jpeg_quality = jpeg_quality, **kwargs )
        ar = np.asarray( img, dtype=input.dtype )
        return ar / 255.0 * ( intensity_range[1] - intensity_range[0] ) + intensity_range[0]

    else:
        img = Image.fromarray( input )
        img = imagedegrade.im.jpeg( img, jpeg_quality = jpeg_quality, **kwargs )
        return np.asarray( img, dtype=input.dtype )

def noise( input, noise_sigma ):
    if( not isinstance( input, np.ndarray) ):
        msg = 'The input should be numpy.ndarray.'
        raise TypeError( msg )
    return input + np.random.normal(0., noise_sigma, input.shape )

def saltpepper( input, p, intensity_range = (0,1) ):
    if( not isinstance( input, np.ndarray) ):
        msg = 'The input should be numpy.ndarray.'
        raise TypeError( msg )

    output = input

    msk = np.random.binomial( 1, p/2, input.shape )
    output = msk * intensity_range[0] + (1-msk) * output

    msk = np.random.binomial( 1, p/2, input.shape )
    output = msk * intensity_range[1] + (1-msk) * output

    return output

def blur( input, blur_sigma ):
    if( not isinstance( input, np.ndarray) ):
        msg = 'The input should be numpy.ndarray.'
        raise TypeError( msg )
    return ndimage.gaussian_filter(input, sigma=[blur_sigma,blur_sigma,0], truncate=3.0, mode='nearest' )

def blur_noise_jpeg( input, blur_sigma, noise_sigma, jpeg_quality, intensity_range = (0,1) ):
    if( not isinstance( input, np.ndarray) ):
        msg = 'The input should be numpy.ndarray.'
        raise TypeError( msg )
    output = input

    if( blur_sigma > 0 ):
        output = blur( output, blur_sigma )

    if( noise_sigma > 0 ):
        output = noise( output, noise_sigma )

    output = jpeg( input, jpeg_quality, intensity_range )

    return output
