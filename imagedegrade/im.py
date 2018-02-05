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

import degrade.np

def jpeg( input, jpeg_quality ):
	assert( isinstance(input, Image.Image) )

	buffer = io_memory()
	input.save( buffer, 'JPEG', quality = jpeg_quality )
	buffer.seek(0)
	return Image.open( buffer )

def noise( input, noise_sigma ):
	assert( isinstance(input, Image.Image) )

	array = np.asarray( input )
	array = degrade.np.noise( array, noise_sigma )
	return Image.fromarray( array )

def blur( input, blur_sigma ):
	assert( isinstance(input, Image.Image) )

	array = np.asarray( input )
	array = degrade.np.blur( array, blur_sigma )
	return Image.fromarray( array )
