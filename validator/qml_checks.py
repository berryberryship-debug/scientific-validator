import numpy as np

def get_ry_gate(theta):
    """Génère une porte de rotation quantique Ry paramétrée par un angle theta."""
    cos = np.cos(theta / 2)
    sin = np.sin(theta / 2)
    return np.array([[cos, -sin], [sin, cos]])

def check_gate_unitarity(theta, tolerance=1e-8):
    """Vérifie que la porte générée est bien unitaire (U U† = I)."""
    gate = get_ry_gate(theta)
    identity = np.eye(2)
    product = np.dot(gate, gate.conj().T)
    
    if np.allclose(product, identity, atol=tolerance):
        return True, f"Porte Ry({theta:.2f}) est unitaire. Physique respectée."
    return False, f"Porte Ry({theta:.2f}) a échoué le test d'unitarité."
