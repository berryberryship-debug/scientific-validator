# Exemple de structure pour votre méta-outil
import numpy as np

class ScientificValidator:
    def __init__(self, program_name):
        self.program_name = program_name
        self.report = []

    def check_conservation(self, input_val, output_val, tolerance=1e-5):
        """Vérifie que la somme des entrées = somme des sorties (utile en physique/bio)"""
        if abs(input_val - output_val) < tolerance:
            self.report.append(f"[OK] Conservation validée pour {self.program_name}")
            return True
        else:
            self.report.append(f"[ERREUR] Perte de données détectée pour {self.program_name}")
            return False

    def check_nan_inf(self, data_array):
        """Vérifie qu'il n'y a pas de valeurs aberrantes (NaN/Infini) dans les résultats"""
        if np.isnan(data_array).any() or np.isinf(data_array).any():
            self.report.append("[ERREUR] Valeurs aberrantes (NaN/Inf) détectées.")
            return False
        self.report.append("[OK] Données propres.")
        return True

    def generate_report(self):
        print(f"--- RAPPORT DE VALIDATION : {self.program_name} ---")
        for line in self.report:
            print(line)
