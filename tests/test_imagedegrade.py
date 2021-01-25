#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

import sys

from imagedegrade import im as imagedegrade_im
from imagedegrade import np as imagedegrade_np

import numpy as np
from PIL import Image, ImageDraw

import os
import glob

from scipy import misc

class tests( unittest.TestCase ):
###################################################################
    @classmethod
    def setUpClass(cls): # it is called before test starting
        pass

    @classmethod
    def tearDownClass(cls): # it is called before test ending
        #for file in glob.glob('__tests__*'):
        #   os.remove(file)
        pass

    def setUp(self): # it is called before each test
        self.np = misc.face()
        self.im = Image.fromarray( self.np )
        self.im.save( '__tests__face.png' )
        pass

    def tearDown(self): # it is called after each test
        pass

###################################################################
    def test_jpg(self):
        q = 5
        filename = '__tests__jpg.jpg'
        self.im.save( filename, quality = q, subsampling='4:4:4' )
        im0 = Image.open( filename )
        #os.remove( filename )

        im1 = imagedegrade_im.jpeg( self.im, jpeg_quality = q, subsampling='4:4:4' )

        np0 = np.asarray( im0 )
        np1 = np.asarray( im1 )

        self.assertTrue( ( np0 == np1 ).all() )

        np2 = imagedegrade_np.jpeg( self.np, jpeg_quality = q, subsampling='4:4:4' )
        self.assertTrue( ( np0 == np2 ).all() )

    def test_noise(self):
        np0 = self.np.astype(np.float32)
        np1 = imagedegrade_np.noise( np0, noise_sigma = 50 )
        np1 = np.clip(np1, 0, 255)
        Image.fromarray( np1.astype(np.uint8) ).save('__tests_noise.png')

    def test_saltpepper(self):
        np0 = self.np.astype(np.float32)
        np1 = imagedegrade_np.saltpepper( np0, 0.01, (0,255) )
        np1 = np.clip(np1, 0, 255)
        Image.fromarray( np1.astype(np.uint8) ).save('__tests_saltpepper.png')

    def test_blur(self):
        np0 = self.np.astype(np.float32)
        np1 = imagedegrade_np.blur( np0, blur_sigma = 5 )
        np1 = np.clip(np1, 0, 255)
        Image.fromarray( np1.astype(np.uint8) ).save('__tests_color_blur.png')

        np0 = self.np.astype(np.float32)
        np0 = np.mean( np0, axis=2, keepdims=True )
        np1 = imagedegrade_np.blur( np0, blur_sigma = 5 )
        np1 = np.clip(np1, 0, 255)

        np1 = np.reshape( np1, (np1.shape[0], np1.shape[1]) )
        Image.fromarray( np1.astype(np.uint8) ).save('__tests_gray_blur.png')



###################################################################
    def suite():
        suite = unittest.TestSuite()
        suite.addTests(unittest.makeSuite(tests))
        return suite

if( __name__ == '__main__' ):
    unittest.main()
