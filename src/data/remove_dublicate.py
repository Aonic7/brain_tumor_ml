import hashlib
import os

class DuplicateRemover:
    def __init__(self, project_dir, labels):
        self.project_dir = project_dir
        self.labels = labels

    def compute_hash(self, file):
        hasher = hashlib.md5()
        with open(file, 'rb') as f:
            buf = f.read()
            hasher.update(buf)
        return hasher.hexdigest()

    def list_files(self):
        hash_dict = {}
        for data_type in ['Training', 'Testing']:
            for label in self.labels:
                folder_path = os.path.join(self.project_dir, 'data', 'processed', data_type, label)
                for root, dirs, files in os.walk(folder_path):
                    for file in files:
                        if file.endswith(".jpg"):
                            file_path = os.path.join(root, file)
                            file_hash = self.compute_hash(file_path)
                            if file_hash in hash_dict:
                                hash_dict[file_hash].append(file_path)
                            else:
                                hash_dict[file_hash] = [file_path]
        return hash_dict

    def remove_duplicates(self, hash_dict):
        duplicate_count = 0
        for hash_value, file_paths in hash_dict.items():
            if len(file_paths) > 1:
                for file_path in file_paths[1:]:
                    print(f"Removing duplicate (hash : {hash_value}) : {file_path}")
                    os.remove(file_path)
                    duplicate_count += 1
        print(f"Number of duplicates removed: {duplicate_count}")

