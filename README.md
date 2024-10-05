
# Fast File Management Utility

`Fast` is a lightweight Python-based file management tool designed to perform fast copying, moving, and deleting of files and directories, as well as provide detailed file and directory information. It utilizes multi-threading to improve performance when working with large numbers of files.

## Features
- **Copy/Move files and directories**: Recursively copy or move directories and files from one location to another.
- **Delete files and directories**: Remove files and directories with ease.
- **Directory and file information**: Get detailed information such as size, number of files, and last modified date.
- **Single file operations**: Copy, move, or delete individual files.
- **Buffer size control**: Set the buffer size for optimized file transfer.

## Installation
You need to have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).
## Download the Executable

You can download the executable file for **Fast** here:

[Download Fast.exe](https://github.com/your-username/your-repo-name/raw/main/your-exe-file.exe)
To install the required dependencies:
```bash
pip install colorama
```

## Usage
To run the utility, use the command:

```bash
python fast.py <mode> <src> <dest> [buffer_size]
```

### Modes
- `copy`: Copy all files and directories from source to destination.
- `move`: Move all files and directories from source to destination.
- `delete` or `remove`: Delete all files and directories in the source path.
- `copyfile`: Copy a single file from source to destination.
- `movefile`: Move a single file from source to destination.
- `deletefile`: Delete a single file.
- `dirinfo`: Get detailed information about a directory (size, number of files, etc.).
- `fileinfo`: Get detailed information about a single file (size, last modified, etc.).

### Optional Arguments:
- `buffer_size`: Set the buffer size for file copying/moving (default is 1024 bytes).

### Examples
1. **Copy a directory**:
   ```bash
   python fast.py copy /path/to/source /path/to/destination
   ```

2. **Move a single file**:
   ```bash
   python fast.py movefile /path/to/file.txt /path/to/destination
   ```

3. **Delete a directory**:
   ```bash
   python fast.py delete /path/to/directory
   ```

4. **Get information about a directory**:
   ```bash
   python fast.py dirinfo /path/to/directory
   ```

### Multi-threading
This tool uses multi-threading to parallelize file operations for faster performance, especially when copying or moving large directories.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
