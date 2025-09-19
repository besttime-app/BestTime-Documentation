import os
from pathlib import Path

def combine_markdown_files(source_dir: str, output_file: str) -> None:
    """
    Combine all markdown files from source directory into a single output file.
    
    Args:
        source_dir (str): Path to the directory containing markdown files
        output_file (str): Path where the combined markdown file will be saved
    """
    # Convert to Path object for better path handling
    source_path = Path(source_dir)
    
    # Ensure source directory exists
    if not source_path.exists():
        raise FileNotFoundError(f"Source directory {source_dir} does not exist")
    
    # Find all .md files in the source directory
    md_files = sorted(source_path.glob("*.md"))
    
    if not md_files:
        print(f"No markdown files found in {source_dir}")
        return
    
    # Combine content from all files
    combined_content = []
    for md_file in md_files:
        print(f"Processing: {md_file.name}")
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                # Add a separator between files
                combined_content.append(f"\n\n<!-- Content from {md_file.name} -->\n\n")
                combined_content.append(content)
        except Exception as e:
            print(f"Error reading {md_file.name}: {str(e)}")
    
    # Write combined content to output file
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("".join(combined_content))
        print(f"\nSuccessfully created combined markdown file: {output_file}")
    except Exception as e:
        print(f"Error writing to output file: {str(e)}")

if __name__ == "__main__":
    # Define source and output paths
    source_directory = "source/includes"
    output_filename = "combined_documentation.md"
    
    try:
        combine_markdown_files(source_directory, output_filename)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
