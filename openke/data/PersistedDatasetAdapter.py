from itertools import chain

from ..data.utils import read_triples, make_normalization_mapping


class PersistedDatasetAdapter:
    def __init__(self, path: str):
        self.triples = tuple(
            read_triples(path)
        )
        self.entity_normalization_mapping = make_normalization_mapping(
            chain(
                map(lambda triple: triple.head, self.triples),
                map(lambda triple: triple.tail, self.triples)
            )
        )
        self.relationship_normalization_mapping = make_normalization_mapping(
            map(lambda triple: triple.relationship, self.triples)
        )

    @property
    def normalized_triples(self):
        for triple in self.triples:
            yield (
                self.entity_normalization_mapping[triple[0]],
                self.entity_normalization_mapping[triple[1]],
                self.relationship_normalization_mapping[triple[2]]
            )
