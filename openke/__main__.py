import click

from .api import train as train_
from .data.PersistedDatasetAdapter import PersistedDatasetAdapter
from .models import TransE, TransH, TransD, TransR, RESCAL, DistMult, HolE, ComplEx, Analogy


@click.group()
def main():
    pass


@main.command()
@click.argument('model', type=click.Choice([model.key for model in {TransE, TransH, TransD, TransR, RESCAL, DistMult, HolE, ComplEx, Analogy}]))
@click.option('--dataset', type=str)
@click.option('--n-threads', '-t', type=int, default=8)
@click.option('--n-epochs', '-e', type=int, default=1000)
@click.option('--n-batches', '-b', type=int, default=100)
@click.option('--alpha', '-a', type=float, default=0.5)
@click.option('--margin', type=float, default=5.0)
@click.option('--bern', type=int, default=1)
@click.option('--embeddings-dimensionality', '-ed', type=int, default=100)
@click.option('--entity-negative-rate', '-enr', type=int, default=25)
@click.option('--relationship-negative-rate', '-rnr', type=int, default=0)
@click.option('--gpu', '-g', is_flag=True)
def train(model, dataset: str, n_threads: int = 8, n_epochs: int = 1000, n_batches: int = 100,
          alpha: float = 0.5, margin: float = 5.0, bern: int = 1, embeddings_dimensionality: int = 100,
          entity_negative_rate: int = 25, relationship_negative_rate: int = 0, gpu: bool = False):
    dataset = PersistedDatasetAdapter(path=dataset)
    train_(
        model=model,
        triples=tuple(dataset.normalized_triples),
        relation_to_id=dataset.relationship_normalization_mapping,
        entity_to_id=dataset.entity_normalization_mapping,
        n_threads=n_threads,
        n_epochs=n_epochs,
        n_batches=n_batches,
        n_alpha=alpha,
        margin=margin,
        bern=bern,
        embeddings_dimensionality=embeddings_dimensionality,
        ent_neg_rate=entity_negative_rate,
        rel_neg_rate=relationship_negative_rate,
        gpu=gpu
    )


main()
