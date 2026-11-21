# Universal Scientific Validator

> **A modular Python framework for rigorous validation of scientific software across multiple disciplines.**
> *Un framework Python modulaire pour la validation rigoureuse de logiciels scientifiques multidisciplinaires.*

## 📖 Overview / Vue d'ensemble

Scientific software often suffers from silent failures: a simulation runs without crashing, but the physical invariants are violated, or data analysis pipelines output hidden artifacts. 

This framework provides a universal "Test Harness" to validate programs across completely different fields: **Quantum Physics, Biology, and Neuroscience**. It was born from the need to rigorously verify simulations developed during my research, such as the *TemporalMode-QNet* project.

*Ce framework est né du besoin de vérifier rigoureusement des programmes issus de domaines variés. Il s'inspire des tests de non-régression et des vérifications d'invariants physiques.*

## 🛠️ Core Features / Fonctionnalités Clés

*   **Quantum Physics (`physics_checks.py`)** : Validates density matrices (Hermiticity), unitary gates (\(U U^\dagger = I\)), and energy conservation.
*   **Data Science & Neuro (`data_checks.py`)** : Detects `NaN`/`Inf` artifacts, validates sampling rates, and checks data quality ratios.
*   **Quantum Machine Learning (`qml_checks.py`)** : Validates parameterized quantum circuits (e.g., \(R_y\) gates) for QLSTM architectures.
*   **Transparent Reporting** : Generates clear, human-readable JSON validation reports.

## 🚀 Quick Start / Démarrage Rapide

Ensure you have `numpy` installed, then run the validation scripts:

```bash
# Clone the repository
git clone https://github.com/berryberryship-debug/[ton-nom-de-depot].git
cd [ton-nom-de-depot]

# Run the physics & data validation suite
python run_validation.py

# Run the Quantum Machine Learning (QML) validation suite
python run_qml_test.py
