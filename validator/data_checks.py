import numpy as np

def check_nan_inf(data, name="data"):
    """
    Vérifie la présence de valeurs aberrantes (NaN ou Infini).
    Retourne (bool, str) : (True si valide, message).
    """
    if not isinstance(data, np.ndarray):
        data = np.array(data)
        
    if np.isnan(data).any():
        return False, f"[ERREUR] {name} contient des valeurs NaN."
    if np.isinf(data).any():
        return False, f"[ERREUR] {name} contient des valeurs infinies (Inf)."
    
    return True, f"[OK] {name} ne contient pas de NaN/Inf."

def check_shape(data, expected_shape, name="data"):
    """
    Vérifie que la dimension des données est celle attendue.
    """
    if data.shape == expected_shape:
        return True, f"[OK] {name} a la bonne dimension {expected_shape}."
    else:
        return False, f"[ERREUR] {name} a la dimension {data.shape}, attendu : {expected_shape}."
