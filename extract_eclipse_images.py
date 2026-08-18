"""
Extract images from Eclipse Silhouette Series PDF
Saves images to the theme.solar-eclipse folder
"""

import fitz  # PyMuPDF
from pathlib import Path
import sys

def extract_images_from_pdf(pdf_path, output_dir):
    """Extract all images from PDF and save them"""
    
    # Open the PDF
    pdf_document = fitz.open(pdf_path)
    
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Image mapping based on PDF pages
    image_names = {
        1: "eclipse-base-plate-empty.png",  # Page 1 - cover with empty plate
        3: "eclipse-base-plate-empty-large.png",  # Page 3 - detailed view of empty plate
        4: [  # Page 4 - Banner Warrior comparison
            ("eclipse-banner-warrior-first-frame.png", 0),
            ("eclipse-banner-warrior-last-frame.png", 1)
        ],
        6: [  # Page 6 - Rearing Horseman comparison
            ("eclipse-rearing-horseman-first-frame.png", 0),
            ("eclipse-rearing-horseman-last-frame.png", 1)
        ],
        8: [  # Page 8 - Dragon Rider comparison
            ("eclipse-dragon-rider-first-frame.png", 0),
            ("eclipse-dragon-rider-last-frame.png", 1)
        ]
    }
    
    extracted_count = 0
    
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        page_index = page_num + 1  # 1-indexed for human readability
        
        # Get images from the page
        image_list = page.get_images()
        
        if page_index in image_names and image_list:
            mapping = image_names[page_index]
            
            if isinstance(mapping, str):
                # Single image on this page
                if image_list:
                    xref = image_list[0][0]
                    base_image = pdf_document.extract_image(xref)
                    image_bytes = base_image["image"]
                    
                    output_file = output_path / mapping
                    output_file.write_bytes(image_bytes)
                    print(f"✓ Extracted: {mapping}")
                    extracted_count += 1
            
            elif isinstance(mapping, list):
                # Multiple images on this page (comparison shots)
                for img_name, img_index in mapping:
                    if img_index < len(image_list):
                        xref = image_list[img_index][0]
                        base_image = pdf_document.extract_image(xref)
                        image_bytes = base_image["image"]
                        
                        output_file = output_path / img_name
                        output_file.write_bytes(image_bytes)
                        print(f"✓ Extracted: {img_name}")
                        extracted_count += 1
    
    pdf_document.close()
    print(f"\n✓ Total images extracted: {extracted_count}")
    return extracted_count

if __name__ == "__main__":
    # Default paths
    pdf_path = "Eclipse-Silhouette-Series.pdf"
    output_dir = r"PROMPTS\video\video.sequences\theme.solar-eclipse"
    
    # Allow command line arguments
    if len(sys.argv) > 1:
        pdf_path = sys.argv[1]
    if len(sys.argv) > 2:
        output_dir = sys.argv[2]
    
    print(f"PDF Path: {pdf_path}")
    print(f"Output Directory: {output_dir}\n")
    
    try:
        extract_images_from_pdf(pdf_path, output_dir)
    except FileNotFoundError:
        print(f"Error: PDF file not found at: {pdf_path}")
        print("\nUsage: python extract_eclipse_images.py <pdf_path> [output_dir]")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
