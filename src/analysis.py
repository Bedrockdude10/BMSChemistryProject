# analysis.py
from rdkit import Chem
from rdkit.Chem import Descriptors, Draw

def analyze_smiles(smiles: str) -> dict[str, float | str]:
    """
    Analyzes a single SMILES string and calculates molecular properties.
    Returns a dictionary of results or an error message if invalid.
    """
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return {"SMILES": smiles, "Error": "Invalid SMILES"}
    
    return {
        "SMILES": smiles,
        "Molecule": mol,  # Include the RDKit molecule object
        "Molecular Weight": Descriptors.MolWt(mol),
        "LogP": Descriptors.MolLogP(mol),
        "Rotatable Bonds": Descriptors.NumRotatableBonds(mol)
    }