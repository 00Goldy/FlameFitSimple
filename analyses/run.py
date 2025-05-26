import os
import subprocess

# Set base directory
base_dir = "/home/goldy/Documents/Stage_M1/FlameFitSimple/analyses"
os.chdir(base_dir)

# === Step 1: Générer le fichier de likelihood
print("Génération du fichier de likelihood...")
subprocess.run([
    "python3", "create_simple_template_likelihood.py",
    "-c", "wimp_sensitivity/likelihood_configs/SI_60t_210ty.ini",
    "-t", "wimp_sensitivity/PDFs/pdfs_mig_SI_60t_0.3-2.0Gev_4fold.pkl",
    "-o", "SI_60t_210ty_mig_0.3-2.0Gev_5toys_25_new_mu_3fold"
], check=True)

# === Step 2: Lancer l’inférence directement
print("Lancement de l inférence (run_routine)...")
subprocess.run([
    "python3", "run_routine.py",
    "-l", "likelihoods/SI_60t_210ty_mig_0.3-2.0Gev_5toys_25_new_mu_3fold.pkl",
    "-m", "create_simple_template_likelihood",
    "-c", "wimp_sensitivity/inference_configs/SI_WIMP.ini",
    "-o", "outputs/SI_60t_210ty_mig_0.3-2.0Gev_5toys_25_new_mu_3fold"
], check=True)

# === Step 3: Stitch final
print("Stitch des résultats...")
subprocess.run([
    "python3", "stitch.py",
    "-d", "outputs/SI_60t_210ty_mig_0.3-2.0Gev_5toys_25_new_mu_3fold"
], check=True)
