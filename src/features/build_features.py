from PIL import Image
from sklearn.model_selection import train_test_split
from torch.utils.data import Dataset, DataLoader
from sklearn.preprocessing import LabelEncoder
from PIL import Image
import pickle

class BrainDataset(Dataset):
    """
    A dataset class that loads images from directories, applies scaling,
    and converts them into PyTorch tensors for model training and testing.
    It expects a list of file paths and corresponding labels.
    """
    def __init__(self, files, mode, transforms_train = None):
        super().__init__()
        # List of files
        self.files = sorted(files)
        #print(self.files)
        # Mode
        self.mode = mode

        if self.mode not in DATA_MODES:
            print(f"{self.mode} is not correct; correct modes: {DATA_MODES}")
            raise NameError

        self.len_ = len(self.files)

        self.label_encoder = LabelEncoder()

        if self.mode != 'test':
            self.labels = [path.parent.name for path in self.files]
            self.label_encoder.fit(self.labels)

            with open('label_encoder.pkl', 'wb') as le_dump_file:
                  pickle.dump(self.label_encoder, le_dump_file)

    def __len__(self):
        return self.len_

    def load_sample(self, file):
        try:
            image = Image.open(file).convert('RGB')
            image.load()
            return image
        except IOError as e:
            print(f"Error loading image {file}: {e}")
            return None

    def __getitem__(self, index):
        file_path = self.files[index]
        sample = self.load_sample(file_path)
        if sample is None:
            return None

        if self.mode == "train":
            transform = transforms_train
        else:
            transform = transforms.Compose([
                transforms.Resize(size=(RESCALE_SIZE, RESCALE_SIZE)),
                transforms.ToTensor(),
                transforms.Normalize([0.1852, 0.1852, 0.1853], [0.2031, 0.2031, 0.2031])
            ])

        x = transform(sample)

        if self.mode == "test":
            return x
        else:
            label = self.labels[index]
            label_id = self.label_encoder.transform([label])
            y = label_id.item()
            return x, y