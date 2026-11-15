"""Modulo 2 - Il prior: generatori di dataset sintetici di classificazione.

Interfaccia comune: sample(batch, n_rows, n_features) -> X, y
Scheletro di partenza: contiene solo P2 (MLP casuale). P1 e P3 si scrivono in aula.
"""
import torch


def sample_mlp_prior(batch, n_rows, n_features, device="cuda"):
    X = torch.randn(batch, n_rows, n_features, device=device)
    hidden = int(torch.randint(4, 33, (1,)))
    act = [torch.tanh, torch.relu, torch.sin][int(torch.randint(0, 3, (1,)))]
    W1 = torch.randn(batch, n_features, hidden, device=device)
    W2 = torch.randn(batch, hidden, 1, device=device)
    z = act(X @ W1) @ W2                       # (batch, n_rows, 1)
    z = z + 0.1 * torch.randn_like(z)          # rumore sulle etichette
    y = (z > z.median(dim=1, keepdim=True).values).long().squeeze(-1)
    return X, y
