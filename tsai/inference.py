# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/052a_inference.ipynb (unless otherwise specified).

__all__ = []

# Cell
from fastai.learner import load_learner
from fastai.callback.core import GatherPredsCallback
from fastai.learner import Learner
from fastcore.basics import patch
from fastcore.meta import delegates

# Cell
@patch
@delegates(GatherPredsCallback.__init__)
def get_X_preds(self: Learner, X, y=None, bs=64, with_input=False, with_decoded=True, with_loss=False, **kwargs):
    if with_loss and y is None:
        print('cannot find loss as y=None')
        with_loss = False
    dl = self.dls.valid.new_dl(X, y=y)
    dl.bs = self.dls.bs if bs is None else bs
    output = list(self.get_preds(dl=dl, with_input=with_input, with_decoded=with_decoded, with_loss=with_loss, **kwargs))
    if with_decoded and hasattr(self.dls.tls[-1], "tfms") and hasattr(self.dls.tls[-1].tfms, "decodes"):
        output[2 + with_input] = self.dls.tls[-1].tfms.decode(output[2 + with_input])
    return tuple(output)