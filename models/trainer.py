import sys
import torch
import matplotlib.pyplot as plt
import numpy as np

class Trainer():

    def __init__(self, model, train_loader, test_loader=None, loss=torch.nn.CrossEntropyLoss, optimizer=torch.optim.Adam):
        self.model = model
        self.train_loader = train_loader
        self.test_loader = test_loader

        self.train_losses = []
        self.test_losses = []
        self.train_accs = []
        self.test_accs = []

        self.loss = loss()
        self.optimizer = optimizer(model.parameters(), lr=1e-4)
        self.scheduler = torch.optim.lr_scheduler.StepLR(self.optimizer, step_size=5, gamma=.3)

        self.device = 'cuda' if torch.has_cuda else 'cpu'


    def fit(self, epochs, batch_size):
        print("Training using "+ self.device)
        self.model.to(self.device)
        for i in range(epochs): 
            train_loss = 0
            val_loss = 0
            train_correct = 0
            val_correct = 0 
            self.model.train()
            for j, batch in enumerate(self.train_loader.get_batch(batch_size)):

                self.optimizer.zero_grad()
                
                images, labels = batch
                images = images.to(self.device)
                labels = labels.squeeze().to(self.device)
                pred = self.model(images)
                loss = self.loss(pred, labels)
                loss.backward()
                self.optimizer.step() 

                decisions = pred.detach().argmax(dim=1)
                train_correct += sum(torch.eq(decisions, labels))
                train_loss += loss.detach().item()

            train_loss /= j+1 
            train_acc = train_correct/ ((j+1)*batch_size)
            self.train_losses.append(train_loss)
            self.train_accs.append(train_acc)


            self.model.eval()
            for j, batch in enumerate(self.test_loader.get_batch(batch_size)):
                
                images, labels = batch
                images = images.to(self.device)
                labels = labels.squeeze().to(self.device)
                pred = self.model(images)
                loss = self.loss(pred, labels)

                decisions = decisions = pred.detach().argmax(dim=1)
                val_correct += sum(torch.eq(decisions, labels))
                val_loss += loss.detach().item()

            val_loss /= j+1 
            val_acc = val_correct/ ((j+1)*batch_size)
            self.test_losses.append(val_loss)
            self.test_accs.append(val_acc)

            self.scheduler.step()
            print("Epoch " + str(i+1)+ '/'+ str(epochs)+ ', Train_loss: ' + str(train_loss) + ', Val_loss:'+str(val_loss))
            

    def plot_loss(self):
        epochs = np.arange(0, len(self.train_losses), 1)
        plt.plot(epochs, self.train_losses, label="Train")
        plt.plot(epochs, self.test_losses, label="Validation")
        plt.title("Training Loss")
        plt.xlabel("Epoch")
        plt.ylabel("Loss")
        plt.legend()
        plt.show()

    def plot_acc(self):
        epochs = np.arange(0, len(self.train_accs), 1)
        plt.plot(epochs, self.train_accs, label="Train")
        plt.plot(epochs, self.test_accs, label="Validation")
        plt.title("Training Accuracy")
        plt.xlabel("Epoch")
        plt.ylabel("Accuracy")
        plt.legend()
        plt.show()
