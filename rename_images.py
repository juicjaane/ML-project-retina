import os

# Mapping of old filenames to new filenames
name_mapping = {
    'adaptive-threshold-approach1.png': 'adaptive_threshold.png',
    'non local means filtering approach 1.png': 'non_local_means.png',
    'unsharp-clahe-HE-comaprisiion appraoch 1.png': 'enhancement_comparison.png',
    'lapplaican in appraoch1.png': 'laplacian_detection.png',
    'matched_filtering_example-not_on_dataset.png': 'matched_filtering.png',
    'laplacian.png': 'laplacian_filter.png',
    'exp.png': 'exp_transform.png',
    'log.png': 'log_transform.png',
    'usharp_masking.png': 'unsharp_masking.png',
    'gamme_correction.png': 'gamma_correction.png',
    'CLAHE.png': 'clahe.png',
    'adaptive_HE.png': 'adaptive_he.png',
    'histogram_ewualisation.png': 'histogram_eq.png',
    'red-blue-green.png': 'rgb_channels.png',
    'original_fundus.png': 'original.png'
}

def rename_files():
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    images_dir = os.path.join(current_dir, 'Images')
    
    # Check if Images directory exists
    if not os.path.exists(images_dir):
        print("Error: Images directory not found!")
        return
    
    # Rename files
    for old_name, new_name in name_mapping.items():
        old_path = os.path.join(images_dir, old_name)
        new_path = os.path.join(images_dir, new_name)
        
        if os.path.exists(old_path):
            try:
                os.rename(old_path, new_path)
                print(f"Renamed: {old_name} → {new_name}")
            except Exception as e:
                print(f"Error renaming {old_name}: {str(e)}")
        else:
            print(f"Warning: File not found: {old_name}")

if __name__ == "__main__":
    rename_files() 