import torch
import torch.nn.functional as F
import numpy as np

class DataLoader:
    def __init__(self, images, labels, transforms=[]):
        self.images = images
        self.labels = labels
        self.transforms = transforms

        self.preprocess()

    def __getitem__(self, item):
        return self.images[item], self.labels[item]

    def get_batch(self, batch_size, transform=True):
        indices = np.arange(0, len(self.images))
        np.random.shuffle(indices)
        for i in range(0, len(indices), batch_size): 
            images, labels = self.__getitem__(indices[i:i+batch_size])
            if len(self.transforms) > 0 :
                transform = np.random.choice(self.transforms)
                images = transform(images)
            yield images, labels
        return None, None

    def preprocess(self):
        self.images -= self.images.mean(axis=0)
        self.images /= self.images.std(axis=0)
        self.images = torch.tensor(self.images.reshape(-1,3,100,100)).float()

        self.labels = torch.tensor(self.labels).long()


