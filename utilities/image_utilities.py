import matplotlib.pyplot as plt
import cv2

def show_channels(img, channels=3, type="RGB"):
    """
    Display the channels of an image
    :param img: image to display
    :param channels: number of channels to display
    :param type: type of channels
    :return: None
    """
    fig, axes = plt.subplots(1, channels, figsize=(20, 5*channels ))
    if channels == 1:
        axes.imshow(img, cmap="gray")
    else:
        for i in range(channels):
            img_i = img[:, :, i]
            axes[i].imshow(img_i, cmap="gray")
            axes[i].set_title(type[i])
    plt.show()
    
def show_channels_hist(img, channels=3, type="RGB"):
    """
    Display the histogram of the channels of an image
    :param img: image to display
    :param channels: number of channels to display
    :param type: type of channels
    :return: None
    """
    fig, axes = plt.subplots(1, channels, figsize=(20, 5*channels))
    for i in range(channels):
        img_i = img[:, :, i]
        hist = cv2.calcHist([img_i], [0], None, [256], [0, 256])
        axes[i].plot(hist)
        axes[i].set_title(type[i])
    plt.show()