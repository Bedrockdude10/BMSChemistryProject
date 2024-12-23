# save_files.py
import os
import pandas as pd
from rdkit.Chem import Draw

def save_results_to_csv(results, output_path):
    """
    Saves the analysis results to a CSV file.
    """
    results_df = pd.DataFrame(results)
    results_df.to_csv(output_path, index=False)

def save_molecular_images(results, output_dir):
    """
    Saves molecular structure images for each valid result.
    """
    os.makedirs(output_dir, exist_ok=True)
    for idx, result in enumerate(results):
        if "Error" not in result and "Molecule" in result:
            mol = result["Molecule"]  # Use the precomputed molecule
            img_path = os.path.join(output_dir, f"structure_{idx}.png")
            Draw.MolToFile(mol, img_path)
