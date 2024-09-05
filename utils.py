import cv2
import matplotlib.pyplot as plt

import glob
import random


class AverageMeter(object):
    """Computes and stores the average and current value"""

    def __init__(self):
        self.reset()

    def reset(self):
        self.val = 0
        self.avg = 0
        self.sum = 0
        self.count = 0

    def update(self, val, n=1):
        self.val = val
        self.sum += val * n
        self.count += n
        self.avg = self.sum / self.count

def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise ValueError('Boolean value expected.')


# def visualize(sample_class, webcam, amazon, dslr):
    	
#     webcam_sample = glob.glob(f'{webcam}/{sample_class}/*')
#     amazon_sample = glob.glob(f'{amazon}/{sample_class}/*')
#     dslr_sample = glob.glob(f'{dslr}/{sample_class}/*')
#     wsam = cv2.resize(cv2.imread(webcam_sample[random.randint(0, len(webcam_sample)-1)]), (512,512))[...,[2,1,0]]
#     asam = cv2.resize(cv2.imread(amazon_sample[random.randint(0, len(amazon_sample)-1)]), (512,512))[...,[2,1,0]]
#     dsam = cv2.resize(cv2.imread(dslr_sample[random.randint(0, len(dslr_sample)-1)]), (512,512))[...,[2,1,0]]

#     plt.subplots(figsize=(15,5))
#     plt.subplot(1,3,1)
#     plt.imshow(wsam)
#     plt.gca().axes.xaxis.set_visible(False)
#     plt.gca().axes.yaxis.set_visible(False)
#     plt.title("webcam",fontsize=15)

#     plt.subplot(1,3,2)
#     plt.imshow(asam)
#     plt.gca().axes.xaxis.set_visible(False)
#     plt.gca().axes.yaxis.set_visible(False)
#     plt.title("amazon",fontsize=15)

#     plt.subplot(1,3,3)
#     plt.imshow(dsam)
#     plt.gca().axes.xaxis.set_visible(False)
#     plt.gca().axes.yaxis.set_visible(False)
#     plt.title("dslr",fontsize=15)
    
#     plt.suptitle(sample_class,fontsize=15)
    
#     plt.show()
