
# Fast File Management Utility

**Fast** is a powerful, lightweight file management tool that allows users to efficiently copy, move, and delete files and directories. It also provides detailed information about files and directories, and supports multi-threading to speed up operations.

## Download the Executable

For users who do not want to run the script manually, a pre-built executable is available for download:

[Download Fast.exe](https://github.com/your-username/your-repo-name/raw/main/fast.exe)

## Features
- **Fast file operations**: Copy, move, or delete multiple files and directories efficiently.
- **Single file operations**: Handle individual file operations such as copy, move, or delete.
- **Directory analysis**: Get detailed information such as size, number of files, and last modified time.
- **Customizable buffer size**: Optimize file transfer speeds by adjusting the buffer size.
- **Multi-threading support**: Perform file operations in parallel for better performance.

## How to Use

1. **Download** the `Fast.exe` file from the link above.
2. Open a command prompt (CMD) or PowerShell.
3. Navigate to the directory where `Fast.exe` is located.
4. Run `Fast.exe` with the following syntax:

```bash
fast <mode> <src> <dest> [buffer_size]
```

### Modes:
- `copy`: Recursively copy files and directories from the source to the destination.
- `move`: Move files and directories from the source to the destination.
- `delete`: Delete all files and directories in the specified source path.
- `copyfile`: Copy a single file from source to destination.
- `movefile`: Move a single file from source to destination.
- `deletefile`: Delete a single file.
- `dirinfo`: Get detailed information about a directory (size, number of files, etc.).
- `fileinfo`: Get detailed information about a file (size, last modified, etc.).

### Examples

1. **Copy a directory**:
   ```bash
   fast copy C:/source_directory D:/destination_directory
   ```

2. **Move a file**:
   ```bash
   fast movefile C:/source/file.txt D:/destination/
   ```

3. **Delete a directory**:
   ```bash
   fast delete C:/directory_to_delete
   ```

4. **Get directory info**:
   ```bash
   fast dirinfo C:/directory_to_analyze
   ```

### Custom Buffer Size
You can adjust the buffer size to optimize performance (in bytes). By default, it uses 1024 bytes.

For example, to use a 2048-byte buffer size for copying a directory:
```bash
fast copy C:/source_directory D:/destination_directory 2048
```

## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/your-username/your-repo-name/raw/main/LICENSE) file for details.
