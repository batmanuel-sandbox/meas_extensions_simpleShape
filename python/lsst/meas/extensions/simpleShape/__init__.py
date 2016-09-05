import lsst.meas.base as measBase

from .simpleShapeLib import *
from .version import *   # generated by sconsUtils

measBase.wrapSimpleAlgorithm(SimpleShape, name="ext_simpleShape_SimpleShape",
                             Control=SimpleShapeControl, executionOrder=measBase.BasePlugin.SHAPE_ORDER)
