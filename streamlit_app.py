import streamlit as st
import tempfile
import os
import shutil
from pathlib import Path
import pandas as pd
from Python_genemapper_analysis import gene_mapper_analysis

# Set page config
st.set_page_config(
    page_title="Gene Mapper Analysis Tool",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and description
st.title("🧬 Gene Mapper Analysis Tool")
st.markdown("""
This application analyzes gene mapper data and creates formatted Excel output with conditional formatting.
Upload your input files and configure the analysis parameters to get started.
""")

# Sidebar for parameters
st.sidebar.header("Analysis Parameters")
X = st.sidebar.number_input("X value for EMX_MEY format", min_value=1, max_value=20, value=4)
Y = st.sidebar.number_input("Y value for EMX_MEY format", min_value=1, max_value=20, value=8)

# Display expected file names based on X and Y values
emx_mey_label = f"EM{X}_ME{Y}"
st.sidebar.markdown(f"**Expected file names:**")
st.sidebar.markdown(f"- `{emx_mey_label}_peaks_exported.xlsx`")
st.sidebar.markdown(f"- `Hyssop_sample_numbers_Genemapper.xlsx`")
st.sidebar.markdown(f"- `Size_ranges_{emx_mey_label}.xlsx` (optional)")

# Main content area
col1, col2 = st.columns(2)

with col1:
    st.header("📁 Input Files")
    
    # File upload for peaks exported file
    peaks_file = st.file_uploader(
        f"Upload {emx_mey_label}_peaks_exported.xlsx",
        type=['xlsx', 'xls'],
        help="The main peaks data exported from GeneMapper"
    )
    
    # File upload for sample order file
    sample_file = st.file_uploader(
        "Upload Hyssop_sample_numbers_Genemapper.xlsx",
        type=['xlsx', 'xls'],
        help="Sample order and naming information"
    )
    
    # Optional file upload for size ranges
    size_ranges_file = st.file_uploader(
        f"Upload Size_ranges_{emx_mey_label}.xlsx (Optional)",
        type=['xlsx', 'xls'],
        help="Size ranges configuration. If not provided, an empty template will be created."
    )

with col2:
    st.header("📊 Analysis Status")
    
    # Check if required files are uploaded
    if peaks_file and sample_file:
        st.success("✅ Required files uploaded successfully!")
        
        # Show file information
        st.markdown("**Uploaded Files:**")
        st.markdown(f"- Peaks file: {peaks_file.name} ({peaks_file.size} bytes)")
        st.markdown(f"- Sample file: {sample_file.name} ({sample_file.size} bytes)")
        if size_ranges_file:
            st.markdown(f"- Size ranges file: {size_ranges_file.name} ({size_ranges_file.size} bytes)")
        else:
            st.markdown("- Size ranges file: Will be created automatically")
    else:
        st.warning("⚠️ Please upload the required files to proceed.")
        missing_files = []
        if not peaks_file:
            missing_files.append(f"{emx_mey_label}_peaks_exported.xlsx")
        if not sample_file:
            missing_files.append("Hyssop_sample_numbers_Genemapper.xlsx")
        
        if missing_files:
            st.markdown("**Missing files:**")
            for file in missing_files:
                st.markdown(f"- {file}")

# Analysis button and processing
st.markdown("---")
st.header("🔬 Run Analysis")

if st.button("Run Gene Mapper Analysis", type="primary", disabled=not (peaks_file and sample_file)):
    if peaks_file and sample_file:
        try:
            # Create progress bar
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            # Create temporary directories
            with tempfile.TemporaryDirectory() as temp_dir:
                temp_path = Path(temp_dir)
                input_dir = temp_path / "input"
                config_dir = temp_path / "config"
                output_dir = temp_path / "output"
                
                # Create directories
                input_dir.mkdir()
                config_dir.mkdir()
                output_dir.mkdir()
                
                status_text.text("Setting up temporary directories...")
                progress_bar.progress(20)
                
                # Save uploaded files
                peaks_file_path = input_dir / f"{emx_mey_label}_peaks_exported.xlsx"
                sample_file_path = input_dir / "Hyssop_sample_numbers_Genemapper.xlsx"
                
                with open(peaks_file_path, "wb") as f:
                    f.write(peaks_file.getbuffer())
                
                with open(sample_file_path, "wb") as f:
                    f.write(sample_file.getbuffer())
                
                # Handle size ranges file
                if size_ranges_file:
                    size_ranges_path = input_dir / f"Size_ranges_{emx_mey_label}.xlsx"
                    with open(size_ranges_path, "wb") as f:
                        f.write(size_ranges_file.getbuffer())
                
                status_text.text("Files uploaded successfully...")
                progress_bar.progress(40)
                
                # Run the analysis
                status_text.text("Running gene mapper analysis...")
                progress_bar.progress(60)
                
                result_file = gene_mapper_analysis(
                    input_file_path=str(input_dir),
                    config_file_path=str(config_dir),
                    output_file_path=str(output_dir),
                    X=X,
                    Y=Y
                )
                
                progress_bar.progress(80)
                status_text.text("Analysis completed successfully!")
                
                # Store result file in session state for download
                if os.path.exists(result_file):
                    with open(result_file, "rb") as f:
                        st.session_state.result_file_data = f.read()
                    st.session_state.result_file_name = f"Sample_Size_Matrix_Colored_{emx_mey_label}.xlsx"
                    
                    progress_bar.progress(100)
                    status_text.text("Ready for download!")
                    
                    st.success("🎉 Analysis completed successfully!")
                    
                    # Display some basic information about the result
                    st.markdown("**Analysis Results:**")
                    st.markdown(f"- Output file: `{st.session_state.result_file_name}`")
                    st.markdown(f"- File size: {len(st.session_state.result_file_data)} bytes")
                    
                else:
                    st.error("❌ Analysis completed but output file not found.")
                    
        except Exception as e:
            st.error(f"❌ Error during analysis: {str(e)}")
            st.markdown("**Error Details:**")
            st.code(str(e))

# Download section
if hasattr(st.session_state, 'result_file_data') and st.session_state.result_file_data:
    st.markdown("---")
    st.header("📥 Download Results")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.download_button(
            label="📥 Download Analysis Results",
            data=st.session_state.result_file_data,
            file_name=st.session_state.result_file_name,
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            type="primary"
        )
        
        st.markdown("**File Details:**")
        st.markdown(f"- Filename: `{st.session_state.result_file_name}`")
        st.markdown(f"- Format: Excel (.xlsx)")
        st.markdown(f"- Size: {len(st.session_state.result_file_data):,} bytes")

# Footer with information
st.markdown("---")
st.markdown("### ℹ️ About This Tool")

with st.expander("How to use this tool"):
    st.markdown("""
    1. **Set Parameters**: Use the sidebar to set X and Y values for your EMX_MEY format
    2. **Upload Files**: Upload the required Excel files:
       - Peaks exported file from GeneMapper
       - Sample numbers file
       - Size ranges file (optional - will be created if not provided)
    3. **Run Analysis**: Click the "Run Gene Mapper Analysis" button
    4. **Download Results**: Once complete, download the formatted Excel output
    
    The tool will create a formatted Excel file with:
    - Color-coded classifications
    - Proper sample naming
    - Size range analysis
    - Conditional formatting for easy visualization
    """)

with st.expander("File Requirements"):
    st.markdown("""
    **Required Files:**
    - `EM{X}_ME{Y}_peaks_exported.xlsx`: Main peaks data from GeneMapper
    - `Hyssop_sample_numbers_Genemapper.xlsx`: Sample order and naming
    
    **Optional Files:**
    - `Size_ranges_EM{X}_ME{Y}.xlsx`: Size ranges configuration
    
    **Output:**
    - `Sample_Size_Matrix_Colored_EM{X}_ME{Y}.xlsx`: Formatted results with conditional formatting
    """)

with st.expander("Technical Details"):
    st.markdown("""
    **Classification Colors:**
    - 🔵 Light Blue: "c" classification
    - 🔴 Red: "a" classification
    - 🟢 Green: "b" classification
    - ⚫ Grey: "d" classification
    
    **Processing Steps:**
    1. File validation and upload
    2. Data cleaning and sample name mapping
    3. Height filtering (>160)
    4. Size range classification
    5. Matrix generation with conditional formatting
    6. Excel output with color coding
    """)
