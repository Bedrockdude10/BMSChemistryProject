
# Molecular Analysis Tool

## **Overview**
This project is a Python and Shell-based molecular analysis tool designed to process chemical compounds from a dataset, analyze molecular properties, and generate visualizations of molecular structures. The tool demonstrates the integration of Python scripting for cheminformatics and Shell scripting for workflow automation, aligning with research needs in the chemistry field.

---

## **Features**
### **Python Capabilities**
- **Molecular Property Analysis**:
  - Molecular weight
  - LogP (octanol-water partition coefficient)
  - Number of rotatable bonds
- **Molecular Visualizations**:
  - Individual molecule images (PNG format)
  - Batch molecular image collages

### **Shell Script Automation**
- Automates the workflow of running the Python script, managing input and output files.
- Validates input files and creates necessary output directories.
- Integrates seamlessly with the Python script for batch processing.

---

## **Usage Instructions**

### **Prerequisites**
- Python 3.7+
- RDKit library
- pandas library

Install dependencies with:
```bash
pip install rdkit pandas
```

### **Setup**
1. Clone the repository:

2. Make the Shell script executable:
   ```bash
   chmod +x run_analysis.sh
   ```

### **Running the Tool**
#### **1. Command-Line Script**
Execute the Shell script with:
```bash
./run_analysis.sh input_file.csv output_directory/
```
- **Input:** A CSV file containing SMILES strings of chemical compounds.
- **Output:**
  - A CSV file with calculated molecular properties.
  - Molecular structure images saved in the specified directory.

#### **2. Python Script**
To run the analysis directly with Python:
```bash
python main_script.py input_file.csv output_directory/
```

---

## **Example Workflow**

### **Input File Format**
- Input is a CSV file with a `SMILES` column:
  ```csv
  SMILES
  CCO
  CC(=O)O
  c1ccccc1
  ```

### **Generated Outputs**
1. **CSV File:**
   - Contains molecular properties for each compound:
     ```csv
     SMILES, Molecular Weight, LogP, Rotatable Bonds, TPSA, Drug-Like
     CCO, 46.07, -0.22, 0, 20.23, True
     ```

2. **Molecular Images:**
   - Individual PNG files for each compound.

---

## **Technical Details**

### **Code Structure**
- `analyze.py`: Contains molecular property analysis logic.
- `save_files.py`: Handles saving results (CSV and images).
- `run_analysis.sh`: Automates the workflow.

## **Future Enhancements**
- Support for additional input formats (e.g., SDF, TXT).
- Integration with cheminformatics APIs.
- Web-based interface for molecule submission and analysis.
- Incorporating Additional Molecular Descriptors:

- Topological Polar Surface Area (TPSA): Reflects the molecule's potential to interact with biological membranes, influencing bioavailability.
 - Hydrogen Bond Donors and Acceptors: Important for drug-receptor interactions.
- Lipinski's Rule of Five Compliance: A quick assessment of a molecule's drug-likeness based on molecular properties.
 - Ring Count or Aromaticity: Relevant for identifying structural motifs in drug design or chemical analysis.

---

## **Acknowledgments**
This project leverages the following libraries:
- [RDKit](https://www.rdkit.org/): A toolkit for cheminformatics and molecular modeling.
- [pandas](https://pandas.pydata.org/): Data manipulation and analysis.

---

## **Contact**
For questions or suggestions, feel free to reach out:
- **Email:** dannyrollo4@gmail.com
- **GitHub:** [Bedrockdude10](https://github.com/Bedrockdude10)
