import cv2 
import numpy  

class VConvolutionFilter(object):
    """A filter that applies a convolution to V (or all of
    BGR)."""
    def __init__(self, kernel):
        self._kernel = kernel
    def apply(self, src, dst):
        """Apply the filter with a BGR or gray source/destination."""
        cv2.filter2D(src, -1, self._kernel, dst)
class SharpenFilter(VConvolutionFilter):
    """A sharpen filter with a 1-pixel radius."""
    def __init__(self):
        kernel = numpy.array([[-1, -1, -1],
        [-1, 9, -1],
        [-1, -1, -1]])
        VConvolutionFilter.__init__(self, kernel)

class FindEdgesFilter(VConvolutionFilter):
    """An edge-finding filter with a 1-pixel radius."""
    def __init__(self):
        kernel = numpy.array([[-1, -1, -1],
        [-1, 8, -1],
        [-1, -1, -1]])
        VConvolutionFilter.__init__(self, kernel)

class BlurFilter(VConvolutionFilter):
    """A blur filter with a 2-pixel radius."""
    def __init__(self):
        kernel = numpy.array([[0.04, 0.04, 0.04, 0.04, 0.04],
            [0.04, 0.04, 0.04, 0.04, 0.04],
            [0.04, 0.04, 0.04, 0.04, 0.04],
            [0.04, 0.04, 0.04, 0.04, 0.04],
            [0.04, 0.04, 0.04, 0.04, 0.04]])
        VConvolutionFilter.__init__(self, kernel)