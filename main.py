# main.py
import argparse
import pandas as pd
from src.analysis import analyze_smiles
from src.save_files import save_results_to_csv, save_molecular_images

def analyze_compounds(input_file, output_dir):
    # Load dataset
    data = pd.read_csv(input_file)
    smiles_list = data['SMILES']
    results = [analyze_smiles(smiles) for smiles in smiles_list]

    # Save results
    save_results_to_csv(results, f"{output_dir}/analysis_results.csv")
    save_molecular_images(results, f"{output_dir}/images")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze chemical compounds.")
    parser.add_argument("input_file", help="Path to the input CSV file with SMILES.")
    parser.add_argument("output_dir", help="Directory to save analysis results.")
    args = parser.parse_args()

    analyze_compounds(args.input_file, args.output_dir)
