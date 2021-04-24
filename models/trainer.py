
class Trainer():

    def __init__(self, name, model, train_loader, test_loader=None):
        self.name = name
        self.model = model
        self.train_loader = train_loader
        self.test_loader = test_loader

        self.train_loss = []
        self.test_loss = []
        self.train_acc = []
        self.test_acc = []

    def train(self, lr, batch_size):
        pass

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