import pytsk3
import os

def scan_deleted_files(drive_letter):
    """
    Scans the specified drive for deleted files.
    """
    print(f"Scanning {drive_letter} for deleted files...")

    try:
        img = pytsk3.Img_Info(f"\\\\.\\{drive_letter}")  # Open raw disk access
        fs = pytsk3.FS_Info(img)

        deleted_files = []
        for directory in fs.open_dir(path="/"):
            for entry in directory:
                if entry and entry.info.meta and not entry.info.meta.flags & pytsk3.TSK_FS_META_FLAG_ALLOC:
                    file_name = entry.info.name.name.decode()
                    deleted_files.append(file_name)
                    print(f"Deleted file found: {file_name}")

        if not deleted_files:
            print("No deleted files found.")
        else:
            print(f"Total deleted files found: {len(deleted_files)}")

        return deleted_files

    except Exception as e:
        print(f"Error scanning drive: {e}")
        return []

if __name__ == "__main__":
    scan_deleted_files("C:")  # Adjust to the correct drive
