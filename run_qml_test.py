import numpy as np
from validator.core import ScientificValidator
import validator.qml_checks as qml

def main():
    # On initialise le validateur pour le projet QLSTM
    validator = ScientificValidator("QLSTM - Quantum Gate Validation")
    
    print("\n--- Test des portes de rotation quantique ---")
    
    # On teste plusieurs angles (comme le ferait un réseau de neurones qui apprend)
    angles_to_test = [np.pi, np.pi/2, 0.5, 2.0, -1.5]
    
    for theta in angles_to_test:
        # On utilise la méthode run_test du validateur
        validator.run_test(f"Unité de la porte Ry({theta:.2f})", qml.check_gate_unitarity, theta)

    # On génère le rapport
    validator.export_report("rapport_qml.json")

if __name__ == "__main__":
    main()
