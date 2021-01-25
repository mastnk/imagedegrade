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

def im2np( im ):
    np = np.asarray( np ).astype( np.float32 )
    np.flags.writeable = True
    return np

def np2im( np ):
    return Image.fromarray( np.uint8(np.clip(0,255)) )

def jpeg( input, jpeg_quality, **kwargs ):
    if( not isinstance(input, Image.Image) ):
        msg = 'The input should be Image.Image.'
        raise TypeError( msg )

    buffer = io_memory()
    input.save( buffer, 'JPEG', quality = jpeg_quality, **kwargs )
    buffer.seek(0)
    return Image.open( buffer )

def noise( input, noise_sigma ):
    if( not isinstance(input, Image.Image) ):
        msg = 'The input should be Image.Image.'
        raise TypeError( msg )

    array = np.asarray( input ).astype( np.float32 )
    array.flags.writeable = True

    array = imagedegrade.np.noise( array, noise_sigma )

    return Image.fromarray( np.uint8(array) )

def saltpepper( input, p ):
    if( not isinstance(input, Image.Image) ):
        msg = 'The input should be Image.Image.'
        raise TypeError( msg )

    array = np.asarray( input )
    array = imagedegrade.np.saltpepper( array, p, (0,255) )
    return Image.fromarray( np.uint8(array) )

def blur( input, blur_sigma ):
    if( not isinstance(input, Image.Image) ):
        msg = 'The input should be Image.Image.'
        raise TypeError( msg )

    array = np.asarray( input )
    array = imagedegrade.np.blur( array, blur_sigma )
    return Image.fromarray( np.uint8(array) )
