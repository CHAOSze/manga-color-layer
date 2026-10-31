"""Small, CPU-only motion QA helpers; these do not emulate AE's Puppet solver."""
import cv2
import numpy as np
from scipy.interpolate import RBFInterpolator


def rgba_float(image):
    a = np.asarray(image).astype(np.float32) / 255
    a[:, :, :3] *= a[:, :, 3:4]
    return a


def rgba_byte(a):
    a = a.copy()
    a[:, :, :3] /= np.maximum(a[:, :, 3:4], 1e-6)
    return np.uint8(np.clip(a*255, 0, 255))


def rigid_matrix(pivot, degrees, translation=(0,0)):
    M = cv2.getRotationMatrix2D(tuple(pivot), degrees, 1)
    M[:, 2] += translation
    return M


def transform_points(points, matrix):
    p = np.asarray(points, dtype=np.float64)
    return p @ matrix[:, :2].T + matrix[:, 2]


class PinField:
    """Precompute a smooth pin interpolator, then reuse it for different poses.

    A zero mobility map marks protected pixels. It is separate from the part's
    alpha: adding rigidity is not the same as cutting the artwork into layers.
    """
    def __init__(self, size, points, mobility=None):
        self.size = size
        self.points = np.asarray(points, dtype=np.float64)
        if len(np.unique(self.points, axis=0)) != len(self.points):
            raise ValueError('Duplicate control points')
        h, w = size[1], size[0]
        self.y, self.x = np.indices((h,w), dtype=np.float32)
        query = np.stack([self.x.ravel(), self.y.ravel()], axis=1)
        # Thin-plate spline needs a non-collinear set for a degree-one tail.
        rank = np.linalg.matrix_rank(np.column_stack([np.ones(len(points)), self.points]))
        degree = 1 if rank == 3 else 0
        interpolator = RBFInterpolator(self.points, np.eye(len(points)),
                                      kernel='thin_plate_spline', degree=degree, smoothing=0)
        self.basis = interpolator(query).reshape(h,w,len(points)).astype(np.float32)
        self.mobility = np.ones((h,w),np.float32) if mobility is None else np.asarray(mobility,dtype=np.float32)

    def displacement(self, deltas):
        return np.einsum('hwn,nc->hwc',self.basis,np.asarray(deltas,dtype=np.float32))*self.mobility[:,:,None]

    def deform(self, image, deltas):
        flow = self.displacement(deltas)
        return cv2.remap(image,self.x-flow[:,:,0],self.y-flow[:,:,1],cv2.INTER_LINEAR,borderMode=cv2.BORDER_CONSTANT)


def attachment_overlap(first, second):
    """Pixel overlap of already transformed alpha plates, not a quality score."""
    return int(((first[:,:,3]>.5)&(second[:,:,3]>.5)).sum())
