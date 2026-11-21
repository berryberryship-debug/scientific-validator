import numpy as np

def check_trace(matrix, expected_trace=1.0, tolerance=1e-5, name="density_matrix"):
    """
    Vérifie que la trace d'une matrice (ex: matrice densité) est égale à la valeur attendue.
    Très utile en physique quantique.
    """
    trace = np.trace(matrix)
    if np.isclose(trace, expected_trace, atol=tolerance):
        return True, f"[OK] Trace de {name} validée (Trace = {trace:.4f})."
    else:
        return False, f"[ERREUR] Trace de {name} invalide (Trace = {trace:.4f}, attendu = {expected_trace})."

def check_energy_conservation(energy_in, energy_out, tolerance=1e-3):
    """
    Vérifie la conservation de l'énergie (utile pour les simulations de systèmes ouverts).
    """
    if np.isclose(energy_in, energy_out, atol=tolerance):
        return True, f"[OK] Énergie conservée ({energy_in} -> {energy_out})."
    else:
        return False, f"[ERREUR] Perte d'énergie détectée (In: {energy_in}, Out: {energy_out})."
