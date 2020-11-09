import os
import uuid
from collections import namedtuple
from typing import Iterable, Tuple

Triple = namedtuple('Triple', ('head', 'tail', 'relationship'))


def line_to_triple(line: str):
    return line[:-1].split('\t', maxsplit=2)


def triple_to_line(triple: Triple, sep: str = '\t'):
    return sep.join(map(str, triple)) + '\n'


def read_triples(path: str):
    with open(path, 'r') as file:
        for line in file:
            yield Triple(*line_to_triple(line))


def make_normalization_mapping(objects: Iterable):
    return {
        entity: i
        for i, entity in enumerate(
            set(
                objects
            )
        )
    }


def get_random_path(filename_pattern: str = None):
    parent_directory = '/tmp'
    os.makedirs(parent_directory, exist_ok=True)
    random_string = str(uuid.uuid1())
    return os.path.join(parent_directory, filename_pattern.format(name=random_string) if filename_pattern else random_string)


def remove(path: str):
    os.system(f'rm -rf {path}')


def write_mapping(path: str, mapping: dict, sep: str = '\t'):
    n_entries = len(mapping.keys())
    with open(path, 'w') as file:
        file.write(str(n_entries) + '\n')
        for key, value in mapping.items():
            file.write(str(key) + sep + str(value) + '\n')


def write_triples(path: str, triples: Tuple[Triple], sep: str = '\t'):
    n_entries = len(triples)
    with open(path, 'w') as file:
        file.write(str(n_entries) + '\n')
        for triple in triples:
            file.write(triple_to_line(triple, sep=sep))
