import torch
import numpy as np

class DataLoader:
    def __init__(self, images, labels, transforms=[], preprocess=True):
        self.images = images
        self.labels = labels
        self.transforms = transforms

        if preprocess:
            self.preprocess()

    def __getitem__(self, item):
        return self.images[item], self.labels[item]

    def get_batch(self, batch_size, transform=True):
        indices = np.arange(0, len(self.images))
        indices = np.random.shuffle(indices)
        pass

    def preprocess(self):
        pass
