"""
Example usage of the gene_mapper_analysis function.

This demonstrates how to import and use the refactored function from another Python file.
"""

from Python_genemapper_analysis import gene_mapper_analysis

# Example 1: Using the function with custom paths and parameters
def run_analysis_custom():
    # Define your custom paths
    input_path = r"C:/Users/bilya/Desktop/bibicode/R_course/GeneMapper_analysis/Input files"
    config_path = r"C:/Users/bilya/Desktop/bibicode/R_course/GeneMapper_analysis/Config files"
    output_path = r"C:/Users/bilya/Desktop/bibicode/R_course/GeneMapper_analysis/Output files"
    
    # Run analysis with custom X and Y values
    try:
        result_file = gene_mapper_analysis(
            input_file_path=input_path,
            config_file_path=config_path,
            output_file_path=output_path,
            X=4,
            Y=8
        )
        print(f"Analysis completed successfully!")
        print(f"Output file: {result_file}")
        return result_file
    except Exception as e:
        print(f"Error running analysis: {e}")
        return None

# Example 2: Using the function with different EMX_MEY values
def run_analysis_different_params():
    # Define your custom paths
    input_path = r"C:/Users/bilya/Desktop/bibicode/R_course/GeneMapper_analysis/Input files"
    config_path = r"C:/Users/bilya/Desktop/bibicode/R_course/GeneMapper_analysis/Config files"
    output_path = r"C:/Users/bilya/Desktop/bibicode/R_course/GeneMapper_analysis/Output files"
    
    # Run analysis with different X and Y values
    try:
        result_file = gene_mapper_analysis(
            input_file_path=input_path,
            config_file_path=config_path,
            output_file_path=output_path,
            X=3,  # Different X value
            Y=5   # Different Y value
        )
        print(f"Analysis with EM3_ME5 completed successfully!")
        print(f"Output file: {result_file}")
        return result_file
    except Exception as e:
        print(f"Error running analysis: {e}")
        return None

if __name__ == "__main__":
    print("Running gene mapper analysis examples...")
    
    # Run the first example
    print("\n--- Example 1: Standard analysis ---")
    run_analysis_custom()
    
    # Run the second example (uncomment if you have the corresponding input files)
    # print("\n--- Example 2: Different parameters ---")
    # run_analysis_different_params()
