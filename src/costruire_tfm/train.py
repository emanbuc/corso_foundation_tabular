"""Modulo 4 - L'addestramento: passo di training su batch di dataset interi.

Scheletro di partenza: il ciclo completo (ottimizzatore, scheduler, checkpoint)
si scrive in aula.
"""
import torch


def train_step(model, prior, opt, batch=32, n_rows=150, n_features=5):
    X, y = prior(batch, n_rows, n_features)
    cut = int(torch.randint(20, n_rows - 20, (1,)))      # contesto | test
    logits = model(X, y[:, :cut], n_train=cut)           # (batch, n_rows - cut, 2)
    loss = torch.nn.functional.cross_entropy(
        logits.reshape(-1, 2), y[:, cut:].reshape(-1))
    opt.zero_grad(); loss.backward()
    torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
    opt.step()
    return loss.item()
