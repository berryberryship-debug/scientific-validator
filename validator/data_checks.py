import numpy as np

def is_hermitian(matrix: np.ndarray, tolerance=1e-8) -> tuple[bool, str, dict]:
    """Vérifie si une matrice est hermitienne (M = M†). Fondamental en mécanique quantique."""
    if not np.allclose(matrix, matrix.conj().T, atol=tolerance):
        return False, "La matrice n'est pas hermitienne.", {"norm_diff": float(np.linalg.norm(matrix - matrix.conj().T))}
    return True, "Matrice hermitienne validée.", {}

def is_unitary(matrix: np.ndarray, tolerance=1e-8) -> tuple[bool, str, dict]:
    """Vérifie si une matrice est unitaire (U U† = I). Fondamental pour les portes quantiques."""
    identity = np.eye(matrix.shape[0])
    product = np.dot(matrix, matrix.conj().T)
    if not np.allclose(product, identity, atol=tolerance):
        return False, "La matrice n'est pas unitaire.", {"max_deviation": float(np.max(np.abs(product - identity)))}
    return True, "Matrice unitaire validée (U U† = I).", {}
