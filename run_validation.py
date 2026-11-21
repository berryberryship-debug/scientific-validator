import numpy as np
from validator.core import ScientificValidator
import validator.physics_checks as phys
import validator.data_checks as data

# 1. On instancie le validateur
validator = ScientificValidator("TemporalMode-QNet Quantum Routing")

# --- SIMULATION DE DONNÉES QUANTIQUES ---
# Une matrice densité valide (pure state |0><0|)
rho_valid = np.array([[1.0, 0.0], [0.0, 0.0]])
# Une matrice densité invalide (pas hermitienne)
rho_invalid = np.array([[1.0, 1.0], [0.0, 0.0]])
# Une porte quantique (Hadamard)
H_gate = (1/np.sqrt(2)) * np.array([[1, 1], [1, -1]])

# 2. On lance les tests
validator.run_test("Densité - Matrice Hermitienne", phys.is_hermitian, rho_valid)
validator.run_test("Densité - Fausse Matrice", phys.is_hermitian, rho_invalid) # Va échouer exprès
validator.run_test("Porte Hadamard - Unitarité", phys.is_unitary, H_gate)

# --- SIMULATION DE DONNÉES NEURO/PHYSIO ---
# Signal ECG avec quelques artefacts
signal_ecg = np.random.randn(1000)
signal_ecg[10:20] = np.nan # On injecte des NaNs

validator.run_test("Qualité Signal ECG", data.check_data_quality, signal_ecg, max_nan_ratio=0.001)
validator.run_test("Fréquence d'échantillonnage ECG", data.check_sampling_rate, signal_ecg, fs=250.0, expected_fs=256.0)

# 3. On génère le rapport JSON
validator.export_report("rapport_final.json")
