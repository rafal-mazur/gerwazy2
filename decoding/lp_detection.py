import numpy as np
import depthai as dai
from utils.geometry import Rectangle

def decode(lpdet_output: dai.NNData):
    data = np.array(lpdet_output.getFirstLayerFp16()).reshape(1, 1, 200, 7)[0, 0]
    
    rects = []
    
    for _, label, conf, x_min, y_min, x_max, y_max in data:
        # rozważyć jakis softmax czy cos w tym stylu
        
        # label: 1 - vehicle, 2 - licence plate
        if label == 1:
            continue
        
        if conf > 0.5:
            rects.append(Rectangle(x_min, y_min, x_max, y_max))
    
    return rects
