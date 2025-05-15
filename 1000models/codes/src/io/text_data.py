import json
from typing import List, Tuple
import _config as cfg


class TextDataLoader:
    def __init__(self, dataset_name):
        self.dataset_name = dataset_name
        self.data_path = cfg.get_texts_path(dataset_name)
        self.index_map = self._build_index_map()
    
    def _build_index_map(self):
        index_map = {}
        position = 0
        with open(self.data_path, 'r') as f:
            for line in f:
                item = json.loads(line)
                index_map[item["index"]] = position
                position += len(line)
        return index_map
    
    def get_texts(self, index_list: list) -> List[Tuple[int, str]]:
        index_list = sorted(index_list)
        texts = []
        with open(self.data_path, 'r', encoding='utf-8') as f:
            for idx in index_list:
                if idx in self.index_map:
                    f.seek(self.index_map[idx])
                    item = json.loads(f.readline())
                    texts.append((item["index"], item["text"]))
        texts.sort(key=lambda x: x[0])
        return texts