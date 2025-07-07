# Gene Mapper Analysis Tool

This Python script analyzes gene mapper data and creates formatted Excel output with conditional formatting.

## Overview

The script has been refactored to provide a reusable function `gene_mapper_analysis()` that can be imported and used from other Python files, while maintaining the ability to run as a standalone script.

## Function Signature

```python
def gene_mapper_analysis(input_file_path, config_file_path, output_file_path, X=4, Y=8):
    """
    Analyze gene mapper data and create a formatted Excel output with conditional formatting.
    
    Args:
        input_file_path (str): Path to the input files directory
        config_file_path (str): Path to the config files directory  
        output_file_path (str): Path to the output files directory
        X (int): X value for EMX_MEY format (default: 4)
        Y (int): Y value for EMX_MEY format (default: 8)
    
    Returns:
        str: Path to the created output file
    """
```

## Required Input Files

The function expects the following files in the `input_file_path` directory:

1. `EM{X}_ME{Y}_peaks_exported.xlsx` - The main peaks data exported from GeneMapper
2. `Hyssop_sample_numbers_Genemapper.xlsx` - Sample order and naming information
3. `Size_ranges_EM{X}_ME{Y}.xlsx` - Size ranges configuration (created automatically if not present)

## Usage Examples

### As a standalone script

```bash
python Python_genemapper_analysis.py
```

The script will use the default paths and parameters defined in the `if __name__ == "__main__":` block.

### As an imported function

```python
from Python_genemapper_analysis import gene_mapper_analysis

# Define your paths
input_path = r"C:/path/to/input/files"
config_path = r"C:/path/to/config/files"
output_path = r"C:/path/to/output/files"

# Run the analysis
result_file = gene_mapper_analysis(
    input_file_path=input_path,
    config_file_path=config_path,
    output_file_path=output_path,
    X=4,
    Y=8
)

print(f"Analysis complete. Output saved to: {result_file}")
```

## Output

The function generates:

1. `Exported_table_changed_sample_names_EM{X}_ME{Y}.xlsx` - Intermediate file with renamed samples
2. `Sample_Size_Matrix_Colored_EM{X}_ME{Y}.xlsx` - Final formatted output with conditional formatting

The final Excel file includes:
- Color-coded cells based on classification:
  - Light blue: "c" classification
  - Red: "a" classification  
  - Green: "b" classification
  - Grey: "d" classification
- Empty columns every 5 data columns for better readability
- Size ranges and EMX_MEY labels

## Dependencies

- pandas
- numpy
- openpyxl
- os (built-in)

## Error Handling

The function will raise exceptions if:
- Required input files are missing
- File paths are invalid
- Data formatting issues occur

Make sure to wrap function calls in try-except blocks when using programmatically.

## Streamlit Web Application

A user-friendly web interface is available for the Gene Mapper Analysis tool. The Streamlit app provides:

- **File Upload Interface**: Easy drag-and-drop file uploading
- **Parameter Configuration**: Interactive controls for X and Y values
- **Real-time Validation**: Immediate feedback on file uploads
- **Progress Tracking**: Visual progress bar during analysis
- **Download Results**: One-click download of the formatted Excel output

### Running the Streamlit App

#### Option 1: Using the run script (Recommended)
```bash
python run_app.py
```

#### Option 2: Direct streamlit command
```bash
# First install requirements
pip install -r requirements.txt

# Run the app
streamlit run streamlit_app.py
```

### Streamlit App Features

1. **Interactive Parameter Setting**: Use sidebar controls to set X and Y values
2. **File Upload**: 
   - Required: Peaks exported file and sample numbers file
   - Optional: Size ranges file (auto-generated if not provided)
3. **Real-time Validation**: Immediate feedback on file compatibility
4. **Progress Tracking**: Visual progress bar during analysis
5. **Download Results**: Direct download of the formatted Excel output
6. **Help Documentation**: Built-in help sections explaining usage

### Web Interface Benefits

- **No Command Line Required**: User-friendly graphical interface
- **File Validation**: Automatic checking of file formats and names
- **Error Handling**: Clear error messages and troubleshooting guidance
- **Cross-platform**: Works on Windows, Mac, and Linux
- **No Installation Hassles**: All processing happens locally

The Streamlit app makes the gene mapper analysis accessible to users who prefer a graphical interface over command-line tools.
