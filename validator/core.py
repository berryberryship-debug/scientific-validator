import logging
import json
from dataclasses import dataclass, field
from typing import Callable, List, Any

# Configuration du logging (remplace les print)
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

@dataclass
class TestResult:
    name: str
    success: bool
    message: str
    details: dict = field(default_factory=dict)

class ScientificValidator:
    def __init__(self, project_name: str):
        self.project_name = project_name
        self.results: List[TestResult] = []
        logging.info(f"Initialisation du validateur pour : {project_name}")

    def run_test(self, test_name: str, test_func: Callable, *args, **kwargs) -> bool:
        """Exécute un test de manière sécurisée (gère les exceptions)."""
        try:
            success, msg, details = test_func(*args, **kwargs)
            self.results.append(TestResult(test_name, success, msg, details))
            if success:
                logging.info(f"✅ {test_name} : {msg}")
            else:
                logging.error(f"❌ {test_name} : {msg}")
            return success
        except Exception as e:
            error_msg = f"Exception lors de l'exécution : {str(e)}"
            self.results.append(TestResult(test_name, False, error_msg))
            logging.critical(f"🔥 {test_name} a crashé : {error_msg}")
            return False

    def export_report(self, filename="validation_report.json"):
        """Génère un rapport JSON exploitable par d'autres scripts."""
        report_data = {
            "project": self.project_name,
            "global_success": all(r.success for r in self.results),
            "total_tests": len(self.results),
            "failed_tests": sum(1 for r in self.results if not r.success),
            "results": [
                {"test": r.name, "success": r.success, "message": r.message, "details": r.details}
                for r in self.results
            ]
        }
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, indent=4, ensure_ascii=False)
        logging.info(f"📄 Rapport exporté avec succès vers {filename}")
