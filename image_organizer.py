import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import shutil
import io
import win32clipboard
from datetime import datetime

class ImageOrganizer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Image Organizer")
        self.root.geometry("600x400")
        
        # Create main frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
        
        # Directory selection
        self.dir_frame = tk.Frame(self.main_frame)
        self.dir_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(self.dir_frame, text="Output Directory:").pack(side=tk.LEFT)
        self.dir_entry = tk.Entry(self.dir_frame, width=40)
        self.dir_entry.pack(side=tk.LEFT, padx=5)
        self.dir_entry.insert(0, os.path.join(os.getcwd(), "organized_images"))
        
        tk.Button(self.dir_frame, text="Browse", command=self.browse_directory).pack(side=tk.LEFT)
        
        # Image name entry
        self.name_frame = tk.Frame(self.main_frame)
        self.name_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(self.name_frame, text="Image Name:").pack(side=tk.LEFT)
        self.name_entry = tk.Entry(self.name_frame, width=40)
        self.name_entry.pack(side=tk.LEFT, padx=5)
        
        # Buttons frame
        self.button_frame = tk.Frame(self.main_frame)
        self.button_frame.pack(fill=tk.X, pady=10)
        
        # Select Images button
        self.select_button = tk.Button(self.button_frame, text="Select Images", command=self.select_images)
        self.select_button.pack(side=tk.LEFT, padx=5)
        
        # Paste button
        self.paste_button = tk.Button(self.button_frame, text="Paste Image", command=self.paste_image)
        self.paste_button.pack(side=tk.LEFT, padx=5)
        
        # Status area
        self.status_frame = tk.Frame(self.main_frame, bg="lightgray", height=200)
        self.status_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.status_label = tk.Label(self.status_frame, 
                                   text="Click 'Select Images' to choose files or 'Paste Image' to paste from clipboard",
                                   bg="lightgray",
                                   wraplength=550)
        self.status_label.pack(expand=True)
        
        # Status message
        self.message_label = tk.Label(self.main_frame, text="")
        self.message_label.pack(pady=10)
        
        # Counter for pasted images
        self.paste_counter = 0
        
    def browse_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.dir_entry.delete(0, tk.END)
            self.dir_entry.insert(0, directory)
    
    def select_images(self):
        files = filedialog.askopenfilenames(
            title="Select Images",
            filetypes=[
                ("Image files", "*.png *.jpg *.jpeg *.bmp *.gif"),
                ("All files", "*.*")
            ]
        )
        
        if files:
            self.process_files(files)
    
    def process_files(self, files):
        # Get output directory and base name
        output_dir = self.dir_entry.get()
        base_name = self.name_entry.get()
        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Process each file
        for i, file_path in enumerate(files):
            if file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                # Generate new filename
                if base_name:
                    new_name = f"{base_name}_{i+1}{os.path.splitext(file_path)[1]}"
                else:
                    new_name = os.path.basename(file_path)
                
                # Copy file to new location
                try:
                    shutil.copy2(file_path, os.path.join(output_dir, new_name))
                    self.message_label.config(text=f"Saved: {new_name}")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to save {file_path}: {str(e)}")
            else:
                messagebox.showwarning("Warning", f"Skipped non-image file: {file_path}")
    
    def paste_image(self):
        try:
            # Get clipboard data
            win32clipboard.OpenClipboard()
            
            # Try different clipboard formats
            if win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_DIB):
                # Get the clipboard data
                data = win32clipboard.GetClipboardData(win32clipboard.CF_DIB)
                win32clipboard.CloseClipboard()
                
                # Convert DIB to image
                try:
                    # Get image dimensions from DIB header
                    width = data[1]
                    height = data[2]
                    bits_per_pixel = data[3]
                    
                    # Create image from raw data
                    if bits_per_pixel == 24:
                        image = Image.frombytes('RGB', (width, height), data[0])
                    elif bits_per_pixel == 32:
                        image = Image.frombytes('RGBA', (width, height), data[0])
                    else:
                        raise ValueError(f"Unsupported bits per pixel: {bits_per_pixel}")
                        
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to process clipboard image: {str(e)}")
                    return
                    
            elif win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_BITMAP):
                # Get bitmap handle
                hbitmap = win32clipboard.GetClipboardData(win32clipboard.CF_BITMAP)
                win32clipboard.CloseClipboard()
                
                # Convert bitmap to image
                try:
                    image = Image.frombytes('RGB', (hbitmap.width, hbitmap.height), hbitmap.bits)
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to process bitmap: {str(e)}")
                    return
                    
            else:
                win32clipboard.CloseClipboard()
                messagebox.showwarning("Warning", "No image data found in clipboard")
                return
            
            # Get output directory and base name
            output_dir = self.dir_entry.get()
            base_name = self.name_entry.get()
            
            # Create output directory if it doesn't exist
            os.makedirs(output_dir, exist_ok=True)
            
            # Generate filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            if base_name:
                new_name = f"{base_name}_{timestamp}.png"
            else:
                new_name = f"pasted_image_{timestamp}.png"
            
            # Save image
            image.save(os.path.join(output_dir, new_name))
            self.message_label.config(text=f"Saved: {new_name}")
            self.paste_counter += 1
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to paste image: {str(e)}")
        finally:
            try:
                win32clipboard.CloseClipboard()
            except:
                pass
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = ImageOrganizer()
    app.run() 