import torch 
import torchvision.transforms as t
import numpy as np

def rotate90(batch_images):
    # batch_images = batch_images.view(-1,20,20,3)
    # batch_images = torch.rot90(batch_images, dims=[2,3])
    # return batch_images.view(-1,3,20,20)
    rot = t.RandomRotation((0,90))
    return rot(batch_images)

def rotate180(batch_images):
    pass 

def rotate270(batch_images): 
    pass

def noTransform(batch_images):
    return batch_images