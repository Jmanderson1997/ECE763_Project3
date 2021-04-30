import torch 
import torch.nn as nn

class Flatten(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, X): 
        return X.view(X.shape[0], -1)


class ConvBlock(nn.Module):
    def __init__(self, in_channels, out_channels): 
        super().__init__() 
        self.conv1 = nn.Conv2d(in_channels, out_channels, 3, padding=1)
        self.conv2 = nn.Conv2d(out_channels, out_channels, 3, padding=1)
        self.batch_norm = nn.BatchNorm2d(out_channels)
        self.act1 = nn.LeakyReLU()
        self.act2 = nn.LeakyReLU()
        self.pool = nn.MaxPool2d(2)

    def forward(self, X): 
        X = self.conv1(X)
        X = self.act1(X)
        X = self.pool(X)
        X = self.conv2(X)
        X = self.batch_norm(X)
        X = self.act2(X)
        return X


class MLP(nn.Module):

    def __init__(self, features_in, layer_sizes, nonlinear_act=nn.LeakyReLU, act_last_layer=True, dropout=True):
        super().__init__()
        layers = nn.ModuleList()

        for i, hidden in enumerate(layer_sizes):
            layers.append(nn.Linear(features_in, hidden))
            if dropout and i !=len(layer_sizes)-1: 
                layers.append(nn.Dropout(.4))
            if i == len(layer_sizes)-1 and not act_last_layer:
                break
            layers.append(nonlinear_act())
            features_in = hidden

        # self.mlp = nn.Sequential(*layers)
        self.mlp = layers

    def forward(self, X):
        # return self.mlp(X)
        for layer in self.mlp: 
            X = layer(X)

        return X


class FaceClassifier(nn.Module): 
    def __init__(self, in_channels, conv_layers, linear_layers): 
        super().__init__()
        self.model = nn.ModuleList()
        for i, layer in enumerate(conv_layers): 
            self.model.append(ConvBlock(in_channels, layer))
            in_channels = layer

        view_size = 100//(2**(i+1))
        self.model.append(Flatten())
        self.model.append(MLP(in_channels*view_size*view_size, linear_layers, act_last_layer=False))
        self.model.append(nn.Softmax(dim=-1))

    def forward(self, X):
        for block in self.model: 
            X = block(X)
        return X
