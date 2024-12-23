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

def rename_and_move_files(source_directory, destination_directory):
    # Ensure the destination folder exists
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)
    
    # Get the next available GOPR number
    next_number = get_next_gopro_number(destination_directory)
    
    # Monitor the directory for new files
    print(f"Monitoring the directory for new files. Press Ctrl+C to stop.")
    print(f"Renamed files will be moved to: {destination_directory}")
    
    while True:
        # List all files in the source directory
        files = os.listdir(source_directory)

        # Filter for MP4 files that don't start with 'GOPR'
        new_files = [f for f in files if f.lower().endswith('.mp4') and not f.lower().startswith('gopr')]
        
        for file in new_files:
            # Build the full file path
            source_path = os.path.join(source_directory, file)
            
            # Create the new file name
            new_file_name = f"GOPR{next_number:04d}.mp4"
            destination_path = os.path.join(destination_directory, new_file_name)
            
            # Rename and move the file
            try:
                os.rename(source_path, destination_path)
                print(f"Renamed and moved file: {file} -> {new_file_name}")
                next_number += 1  # Increment the GOPR number
            except Exception as e:
                print(f"Error renaming and moving file: {file} -> {new_file_name}. Error: {e}")
        
        # Wait for a short period before checking again (to avoid too frequent checks)
        time.sleep(1)

# Specify the source and destination directories
source_directory = r"C:\Users\harry\Videos\Screen Recordings\MP4"
destination_directory = r"C:\Users\harry\Videos\Screen Recordings\Renamed"

rename_and_move_files(source_directory, destination_directory)
