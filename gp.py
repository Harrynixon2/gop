import os
import time

def get_next_gopro_number(directory):
    # List all files in the directory
    files = os.listdir(directory)
    # Filter out files that start with GOPR and match the GOPR format
    gopro_files = [f for f in files if f.lower().startswith('gopr') and f.lower().endswith('.mp4')]
    
    # Extract the numbers from GOPRxxxx.mp4
    gopro_numbers = []
    for file in gopro_files:
        try:
            number = int(file[4:8])  # Extract the number after 'GOPR'
            gopro_numbers.append(number)
        except ValueError:
            continue

    # Return the next available number, which is the maximum number + 1
    return max(gopro_numbers, default=0) + 1

def rename_files(directory):
    # Get the next available GOPR number
    next_number = get_next_gopro_number(directory)
    
    # Monitor the directory for new files
    print("Monitoring the directory for new files. Press Ctrl+C to stop.")
    while True:
        # List all files in the directory
        files = os.listdir(directory)

        # Filter for MP4 files that don't start with 'GOPR'
        new_files = [f for f in files if f.lower().endswith('.mp4') and not f.lower().startswith('gopr')]
        
        for file in new_files:
            # Build the full file path
            file_path = os.path.join(directory, file)
            
            # Create the new file name
            new_file_name = f"GOPR{next_number:04d}.mp4"
            new_file_path = os.path.join(directory, new_file_name)
            
            # Rename the file
            try:
                os.rename(file_path, new_file_path)
                print(f"Renamed file: {file} -> {new_file_name}")
                next_number += 1  # Increment the GOPR number
            except Exception as e:
                print(f"Error renaming file: {file} -> {new_file_name}. Error: {e}")
        
        # Wait for a short period before checking again (to avoid too frequent checks)
        time.sleep(1)

# Specify the directory where the MP4 files are located
directory = r"C:\Users\harry\Videos\Screen Recordings\MP4"
rename_files(directory)
