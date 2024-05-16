import numpy as np
import torch
from PIL import Image
from pathlib import Path
from torchvision import transforms
import matplotlib.pyplot as plt
from src import Config as cfg


class Utils():

    @staticmethod
    def get_files_and_labels(root_dir):
        """Method use to collect image files root paths and labels"""
        root_dir = Path(root_dir)
        file_paths = []
        #labels = []

        for class_dir in root_dir.iterdir():
            if class_dir.is_dir():
                for file in class_dir.glob('*.jpg'):
                    file_paths.append(file)
                    #labels.append(class_dir.name)
        return file_paths

    @staticmethod
    def imshow(inp, title=None, plt_ax=plt, default=False):
          """Imshow for tensors"""

          inp = inp.numpy().transpose((1, 2, 0))
          #Calculated by imagenet
          #mean = np.array(MEANS)
          #std = np.array(STD)
          #[output[channel] = (input[channel] - mean[channel]) / std[channel]
          #inp = std * inp + mean
          inp = np.clip(inp, 0, 1)
          plt_ax.imshow(inp)
          if title is not None:
              plt_ax.set_title(title)
          plt_ax.grid(False)

    @staticmethod
    def my_mean(file, RESCALE_SIZE):
        image = Image.open(file).convert('RGB')
        image.load()
        image = image.resize((RESCALE_SIZE, RESCALE_SIZE))
        return torch.sum(transforms.ToTensor()(image),dim=(1,2))

    @staticmethod
    def my_std(file, means, RESCALE_SIZE):
        assert len(means)==3
        image = Image.open(file).convert('RGB')
        image.load()
        image = image.resize((RESCALE_SIZE, RESCALE_SIZE))
        image = transforms.ToTensor()(image)
        for i in range(3):
            image[i,:,:]=(image[i,:,:]-means[i])**2
        return torch.mean(image,dim=(1,2))

    @staticmethod
    def display_random_images(dataset, nrows=3, ncols=3):
      """
      Displays a grid of random images from a dataset with labels.
      """
      fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=(8, 8), sharey=True, sharex=True)

      for fig_x in ax.flatten():
          random_index = int(np.random.uniform(0, len(dataset)))
          im_val, label = dataset[random_index]
          img_label = " ".join(map(lambda x: x.capitalize(), dataset.label_encoder.inverse_transform([label])[0].split('_')))

          Utils.imshow(im_val.data.cpu(), title=img_label, plt_ax=fig_x)

      plt.show()
