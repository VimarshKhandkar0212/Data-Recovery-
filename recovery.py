import pytsk3
import os

def recover_deleted_file(drive_letter, file_name, output_folder):
    """
    Recovers a deleted file from the specified drive.
    """
    print(f"Attempting to recover {file_name} from {drive_letter}...")

    try:
        img = pytsk3.Img_Info(f"\\\\.\\{drive_letter}")  # Open disk for raw access
        fs = pytsk3.FS_Info(img)

        for directory in fs.open_dir(path="/"):
            for entry in directory:
                if entry and entry.info.meta and not entry.info.meta.flags & pytsk3.TSK_FS_META_FLAG_ALLOC:
                    if entry.info.name.name.decode() == file_name:
                        output_path = os.path.join(output_folder, file_name)
                        with open(output_path, "wb") as out_file:
                            file_obj = entry.open()
                            out_file.write(file_obj.read_random(0, entry.info.meta.size))
                        
                        print(f"File successfully recovered: {output_path}")
                        return

        print("File not found in deleted records.")

    except Exception as e:
        print(f"Error during recovery: {e}")

if __name__ == "__main__":
    recover_deleted_file("C:", "deleted_image.jpg", "C:/RecoveredFiles")
