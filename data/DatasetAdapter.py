import os
from typing import Tuple

from data.utils import Triple, get_random_path, remove, write_triples, write_mapping


class DatasetAdapter:
    def __init__(self, triples: Tuple[Triple], relation_to_id: dict, entity_to_id: dict):
        # self.triples = tuple(
        #     read_triples(path)
        # )
        # self.entity_normalization_mapping = make_normalization_mapping(
        #     chain(
        #         map(lambda triple: triple.head, self.triples),
        #         map(lambda triple: triple.tail, self.triples)
        #     )
        # )
        # self.relationship_normalization_mapping = make_normalization_mapping(
        #     map(lambda triple: triple.relationship, self.triples)
        # )
        # print(self.entity_normalization_mapping)
        # print(self.relationship_normalization_mapping)
        self.path = get_random_path()

        os.makedirs(self.path)

        write_mapping(path=os.path.join(self.path, 'relation2id.txt'), mapping=relation_to_id)
        write_mapping(path=os.path.join(self.path, 'entity2id.txt'), mapping=entity_to_id)
        write_triples(path=os.path.join(self.path, 'train2id.txt'), triples=triples)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        remove(self.path)
