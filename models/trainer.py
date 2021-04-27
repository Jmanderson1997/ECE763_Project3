import sys
import torch


class Trainer():

    def __init__(self, name, model, train_loader, test_loader=None, loss=torch.nn.CrossEntropyLoss):
        self.name = name
        self.model = model
        self.train_loader = train_loader
        self.test_loader = test_loader

        self.train_losses = []
        self.test_losses = []
        self.train_accs = []
        self.test_accs = []

        self.loss = loss()

    def fit(self, epochs, lr, batch_size):
        for i in range(epochs): 
            train_loss = 0
            val_loss = 0
            train_correct = 0
            val_correct = 0 
            for j, batch in enumerate(self.train_loader.get_batch(batch_size)):
                pass
                
                # images, labels = batch
                # pred = self.model(images)
                # loss = self.loss(pred, labels)
                # loss.backward()

                # decisions = pred.detach().argmax()
                # train_loss += loss.detach()
                
            train_loss /= j 
            self.train_losses.append(train_loss)


            sys.stdout.write("\r Epoch " + str(i+1)+ '/'+ str(epochs)+ ', Train_loss: ' + str(train_loss) + ', Val_loss:'+str(val_loss))
            

    def plot_loss(self):
        pass

    def plot_acc(self):
        pass

    def save_model(self):
        pass

    def save_history(self):
        pass

    def load_trainer(self, name):
        pass