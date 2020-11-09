import os
from typing import Tuple

from . import config
from . import models
from .data.RuntimeDatasetAdapter import RuntimeDatasetAdapter
from .data.utils import Triple


def train(model: str, triples: Tuple[Triple], relation_to_id: dict, entity_to_id: dict, n_threads: int = 8, n_epochs: int = 1000, n_batches: int = 100,
          n_alpha: float = 0.5, margin: float = 5.0, bern: int = 1, embeddings_dimensionality: int = 100, ent_neg_rate: int = 25, rel_neg_rate: int = 0,
          gpu: bool = False):
    with RuntimeDatasetAdapter(triples=triples, relation_to_id=relation_to_id, entity_to_id=entity_to_id) as dataset:
        os.environ['CUDA_VISIBLE_DEVICES'] = '0' if gpu else 'none'
        # Input training files from benchmarks/FB15K/ folder.
        con = config.Config()
        # True: Input test files from the same folder.
        con.set_in_path(f"{dataset.path}/")
        con.set_test_link_prediction(True)
        # con.set_test_triple_classification(True)
        con.set_work_threads(n_threads)
        con.set_train_times(n_epochs)
        con.set_nbatches(n_batches)
        con.set_alpha(n_alpha)
        con.set_margin(margin)
        con.set_bern(bern)
        con.set_dimension(embeddings_dimensionality)
        con.set_ent_neg_rate(ent_neg_rate)
        con.set_rel_neg_rate(rel_neg_rate)
        con.set_opt_method("SGD")

        # Models will be exported via tf.Saver() automatically.
        con.set_export_files("./res/model.vec.tf", 0)
        # Model parameters will be exported to json files automatically.
        con.set_out_files("./res/embedding.vec.json")
        # Initialize experimental settings.
        con.init()
        con.set_model(
            models.TransE if model == models.TransE.key else
            models.TransH if model == models.TransH.key else
            models.TransD if model == models.TransD.key else
            models.TransR if model == models.TransR.key else
            models.RESCAL if model == models.RESCAL.key else
            models.DistMult if model == models.DistMult.key else
            models.HolE if model == models.HolE.key else
            models.ComplEx if model == models.ComplEx.key else
            models.Analogy if model == models.Analogy.key else
            None
        )
        # Train the model.
        con.run()
        return con

# con = train(triples=(Triple(0, 1, 0), Triple(1, 0, 0)), relation_to_id={'a': 0}, entity_to_id={'0': 0, '1': 1}, n_epochs=10)
