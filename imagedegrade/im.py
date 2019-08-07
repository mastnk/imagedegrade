#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    # python 2
    from StringIO import StringIO as io_memory
except ImportError:
    # python 3
    from io import BytesIO as io_memory

from PIL import Image
import numpy as np

import imagedegrade.np

def jpeg( input, jpeg_quality ):
    if( not isinstance(input, Image.Image) ):
        msg = 'The input should be Image.Image.'
        raise TypeError( msg )

    buffer = io_memory()
    input.save( buffer, 'JPEG', quality = jpeg_quality )
    buffer.seek(0)
    return Image.open( buffer )

def noise( input, noise_sigma ):
    if( not isinstance(input, Image.Image) ):
        msg = 'The input should be Image.Image.'
        raise TypeError( msg )

    array = np.asarray( input )
    array = imagedegrade.np.noise( array, noise_sigma )
    return Image.fromarray( array )

def saltpepper( input, p, intensity_range = (0,1) ):
    if( not isinstance(input, Image.Image) ):
        msg = 'The input should be Image.Image.'
        raise TypeError( msg )

    array = np.asarray( input )
    array = imagedegrade.np.saltpepper( array, p, intensity_range )
    return Image.fromarray( array )

def blur( input, blur_sigma ):
    if( not isinstance(input, Image.Image) ):
        msg = 'The input should be Image.Image.'
        raise TypeError( msg )

    array = np.asarray( input )
    array = imagedegrade.np.blur( array, blur_sigma )
    return Image.fromarray( array )
