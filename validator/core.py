from . import data_checks
from . import physics_checks

class ScientificValidator:
    def __init__(self, project_name):
        self.project_name = project_name
        self.report = []
        self.is_valid = True

    def log(self, success, message):
        """Enregistre le résultat d'un test."""
        if not success:
            self.is_valid = False
        self.report.append(message)

    def validate_data_integrity(self, data, name="Dataset"):
        success, msg = data_checks.check_nan_inf(data, name)
        self.log(success, msg)

    def validate_trace(self, matrix, expected=1.0, name="Density Matrix"):
        success, msg = physics_checks.check_trace(matrix, expected, name=name)
        self.log(success, msg)

    def validate_energy(self, energy_in, energy_out):
        success, msg = physics_checks.check_energy_conservation(energy_in, energy_out)
        self.log(success, msg)

    def generate_report(self):
        print(f"\n{'='*40}")
        print(f" RAPPORT DE VALIDATION : {self.project_name}")
        print(f"{'='*40}")
        for line in self.report:
            print(line)
        
        print(f"{'='*40}")
        if self.is_valid:
            print("✅ SUCCÈS : Toutes les vérifications sont passées.")
        else:
            print("❌ ÉCHEC : Des erreurs ont été détectées.")
        print(f"{'='*40}\n")
        
        return self.is_valid
