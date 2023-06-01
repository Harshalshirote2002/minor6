import tensorflow as tf
import cv2
import scipy.signal as sp
import numpy as np
import pywt


def process_array(ppg):
    demodulated = sp.detrend(ppg) 
    envelope = np.abs(sp.hilbert(demodulated)) 
    carrier_extracted = demodulated / envelope
    scales = np.arange(1, 201)  
    img = pywt.cwt(carrier_extracted, scales, 'gaus1')[0] 
    img= img + np.abs(img.min())
    img= img*255/ (np.abs(img.max()) - np.abs(img.min())) 
    model=tf.keras.models.load_model('trainedCNN_final')
    image=(cv2.resize(img, (100,100))) /255.0
    out=model.predict(image.reshape(1,100,100,1))
    out=(out*160) + 40
    print(out.tolist())
    return out.tolist()
