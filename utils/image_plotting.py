import matplotlib.pyplot as plt

def plot_image(sample): 
    plt.imshow(sample.reshape(20,20,3))
    plt.show()