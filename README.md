imagedegrade
====

It is a python package to degrade image data.

## Usage

### Import sample
`import imagedegrade.np as degrade`

### imagedegrade.np.blur( input, blur_sigma )
Blur input data by Gaussian kernel.It simply calls:
`scipy.ndimage.gaussian_filter(input, sigma=[blur_sigma,blur_sigma,0], truncate=3.0, mode='nearest' )`

- **input** *numpy.ndarray*
Three dimensional array of [height, width, channel]. Note that it should be three dimensional array even if it is a gray image data.

- **blur_sigma** *float*
It specifies the standard deviation of Gaussian blur kernel.

- **output** *numpy.ndarray*
Blurred data.

### imagedegrade.np.noise( input, noise_sigma )

Add Gaussian noise to input data. It simply calls:
`input + numpy.random.normal(0., noise_sigma, input.shape )`

- **input** *numpy.ndarray*

- **noise_sigma** *float*
It specifies the standard deviaion of Gaussian noise. 

- **output** *numpy.ndarray*
Noisy data.

### imagedegrade.np.jpeg( input, jpeg_quality, intensity_range = (0,1) )

Add JPEG compression distortion. Gray image version is not debugged.

- **input** *numpy.ndarray*
Three dimensional array of [height, width, channel]. Note that it should be three dimensional array even if it is a gray image data.

- **jpeg_quality** *int*
It specifys jpeg quality. The range is 1 to 100. 
Note that even if you specify 100, the output is included some JPEG compression distortion.

- **intensity_range** *tuple of floats*
It specifys intensity range of the input image data.
JPEG compression is caluclated in uint8. 
Before JPEG compression, data is applied:
`( data - intensity_range[0] ) / ( intensity_range[1] - intensity_range[0] ) * 255.0`
After JPEG compression, data is applied:
`data / 255.0 * ( intensity_range[1] - intensity_range[0] ) + intensity_range[0]`
If dtype of input is uint8, those calculation is not applied.

- **output** *numpy.ndarray*
The image data with JPEG compression distortion.


### imagedegrade.np.blur_noise_jpeg( input, blur_sigma, noise_sigma, jpeg_quality, intensity_range = (0,1) )

It sequentially applys blur, noise, and jpeg compression distortion. Please check the above descriptions for the parameters.

## Install

`% pip install git+https://github.com/mastnk/imagedegrade`

## Author

[Masayuki Tanaka](https://github.com/mastnk)
