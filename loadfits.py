from astropy.io import fits
import numpy as np

def load_fits(filnam):
  hdulist = fits.open(filnam)
  data = hdulist[0].data
  maxx, maxy = data.shape
  return maxy, maxx


if __name__ == '__main__':
  # Run your `load_fits` function with examples:
  shape = load_fits('data/image1.fits')
  print(shape)

  # You can also confirm your result visually:
  from astropy.io import fits
  import matplotlib.pyplot as plt
  from matplotlib import cm

  hdulist = fits.open('data/image1.fits')
  data = hdulist[0].data

  # Plot the 2D image data
  plt.imshow(data.T)
  plt.colorbar()
  plt.show()
