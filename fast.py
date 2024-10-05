import os
import shutil
import colorama
from colorama import Fore
from threading import Thread
import sys
from random import choice



def printf(msg: str, color=Fore.WHITE):
    print(f"{color}{msg}", end="")


class Fast:
    def __init__(self):
        self.count = 0
        self.buffer_size = 1
        self.base_buffer_size = 1024

    def set_buffer_size(self, m):
        self.buffer_size = self.base_buffer_size * m

    def copy_file(self, src_file: str, dest_file: str):
        with open(src_file, "rb") as source, open(dest_file, "wb") as dest:
            while chunk := source.read(self.buffer_size):
                dest.write(chunk)
        self.count += 1
        printf(f"{self.count}. {src_file}\n", Fore.LIGHTGREEN_EX)
        

    def copy(self, src: str, dest: str):
        self.count = 0
        for dirpath, dirnames, filenames in os.walk(src):
            # Calculate the destination directory path
            dest_dirpath = dirpath.replace(src, dest, 1)
            if not os.path.exists(dest_dirpath):
                os.makedirs(dest_dirpath)

            # Copy each file in the directory
            for filename in filenames:
                # Full path to the source file
                src_file = os.path.join(dirpath, filename)
                # Full path to the destination file
                dest_file = os.path.join(dest_dirpath, filename)
                Thread(target=self.copy_file, args=(src_file, dest_file)).start()
                # Copy the file

    def delete(self, src: str):
        count = 0
        # Walk through the source directory
        for dirpath, dirnames, filenames in os.walk(src, topdown=False):
            # Copy each file in the directory
            for filename in filenames:
                # Full path to the source file
                src_file = os.path.join(dirpath, filename)
                os.remove(src_file,)
                count += 1
                printf(f"[{count}] ", Fore.LIGHTRED_EX)
            for dir in dirnames:
                dir_path = os.path.join(dirpath, dir)
                os.rmdir(dir_path)

        os.rmdir(src)

    def move(self, src: str, dest: str):
        for dirpath, dirnames, filenames in os.walk(src, topdown=False):
            # Calculate the destination directory path
            dest_dirpath = dirpath.replace(src, dest, 1)
            if not os.path.exists(dest_dirpath):
                os.makedirs(dest_dirpath)

            # Copy each file in the directory
            for filename in filenames:
                # Full path to the source file
                src_file = os.path.join(dirpath, filename)

                # Full path to the destination file
                dest_file = os.path.join(dest_dirpath, filename)

                # Copy the file
                Thread(target=self.copy_file, args=(src_file, dest_file)).start()
                # Use copy2 to preserve metaos.walk(src)
                os.remove(src_file)

            for dir in dirnames:
                dir_path = os.path.join(dirpath, dir)
                os.rmdir(dir_path)

        os.remove(src)

    def get_dir_info(self, src_dir):
        printf("Analizing...\n", Fore.LIGHTMAGENTA_EX)
        total_files = 0
        total_dirs = 0
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(src_dir):
            total_files += len(filenames)
            total_dirs += len(dirnames)
            for file in filenames:
                fp = os.path.join(dirpath, file)
                total_size += os.path.getsize(fp)

        printf(f"Directory : {src_dir}\n", Fore.LIGHTGREEN_EX)
        printf(
            f"Size : {total_size} Bytes | {round(total_size/1024, 2)} KB | {round(total_size/(1024 * 1024), 2)} MB | {round(total_size/(1024 * 1024 * 1024), 2)} GB\n",
            Fore.CYAN,
        )
        printf(f"Total files : {total_files}\n", Fore.WHITE)
        printf(f"Total Sub Directory : {total_dirs}\n", Fore.LIGHTYELLOW_EX)

    def copy_single_file(self, src, des):
        size = os.path.getsize(src)
        copied = 0
        with open(src, "rb") as source, open(des, "wb") as dest:
            while chunk := source.read(self.buffer_size):
                copied += len(chunk)
                dest.write(chunk)
                printf(f"{int((copied / size) * 100)}%\n", Fore.LIGHTGREEN_EX)

    def move_single_file(self, src, des):
        size = os.path.getsize(src)
        copied = 0
        with open(src, "rb") as source, open(des, "wb") as dest:
            while chunk := source.read(self.buffer_size):
                copied += len(chunk)
                dest.write(chunk)
                printf(f"{int((copied / size) * 100)}%\n", Fore.LIGHTGREEN_EX)
        os.remove(src)

    def get_file_info(self, src):
        total_size = os.path.getsize(src)

        printf(
            f"Size : {total_size} Bytes | {round(total_size/1024, 2)} KB | {round(total_size/(1024 * 1024), 2)} MB | {round(total_size/(1024 * 1024 * 1024), 2)} GB",
            Fore.LIGHTGREEN_EX,
        )
        printf(f"Last Modified : {os.path.getctime(src)}", Fore.CYAN)


def help_menu():
    printf("Usage:\n", Fore.LIGHTGREEN_EX)
    printf(
        "  fast <mode> <src> <dest> [buffer_size]\n\n",
        Fore.LIGHTCYAN_EX,
    )

    printf("Modes:\n", Fore.LIGHTGREEN_EX)
    printf(
        "  copy          - Copy all files and directories from source to destination.\n",
        Fore.WHITE,
    )
    printf(
        "  move          - Move all files and directories from source to destination.\n",
        Fore.WHITE,
    )
    printf(
        "  delete/remove  - Delete all files and directories in the source path.\n",
        Fore.WHITE,
    )
    printf(
        "  copyfile      - Copy a single file from source to destination.\n", Fore.WHITE
    )
    printf(
        "  movefile      - Move a single file from source to destination.\n", Fore.WHITE
    )
    printf("  deletefile    - Delete a single file.\n", Fore.WHITE)
    printf(
        "  dirinfo       - Get detailed information about a directory (size, number of files, etc.).\n",
        Fore.WHITE,
    )
    printf(
        "  fileinfo      - Get detailed information about a single file (size, last modified, etc.).\n",
        Fore.WHITE,
    )

    printf("\nOptional Arguments:\n", Fore.LIGHTGREEN_EX)
    printf(
        "  buffer_size   - Set the buffer size for file copying/moving (default is 1024 bytes).\n",
        Fore.WHITE,
    )

    printf("\nExamples:\n", Fore.LIGHTGREEN_EX)
    printf(
        "  fast copy /path/to/source /path/to/destination\n", Fore.CYAN
    )
    printf(
        "  fast movefile /path/to/file.txt /path/to/destination\n",
        Fore.CYAN,
    )
    printf("  fast delete /path/to/directory\n", Fore.CYAN)
    printf("  fast dirinfo /path/to/directory\n", Fore.CYAN)
    printf("  fast fileinfo /path/to/file.txt\n", Fore.CYAN)


def main():
    colorama.init()
    fast = Fast()

    if len(sys.argv) == 1:
        help_menu()
        return
    modes = [
        "copy",
        "move",
        "remove",
        "delete",
        "copyfile",
        "movefile",
        "deletefile",
        "removefile",
        "dirinfo",
        "fileinfo",
    ]

    mode = sys.argv[1]

    if not mode in modes:
        printf("Command Not Found", Fore.MAGENTA)
        return

    src = None
    des = None
    bs = 1024

    if mode == "copy" or mode == "move":
        src = sys.argv[2]
        if not os.path.exists(src):
            printf("Source path not found !", Fore.RED)
            return

        des = sys.argv[3]
        
        if len(sys.argv) == 5:
            if not (sys.argv[4].isnumeric()):
                printf("Buffer size is not Int !", Fore.RED)
                return
            else:
                bs = int(sys.argv[4])

        fast.set_buffer_size(bs)
        if mode == "copy":
            fast.copy(src, des)
        if mode == "move":
            fast.move(src, des)

    elif mode == "delete" or mode == "remove":
        src = sys.argv[2]
        if not os.path.exists(src):
            printf("Source path not found !", Fore.RED)
            return
        fast.delete(src)

    elif mode == "copyfile" or mode == "movefile":
        src = sys.argv[2]
        if not os.path.exists(src):
            printf("Source path not found !", Fore.RED)
            return

        des = sys.argv[3]
       

        if len(sys.argv) == 5:
            if not (sys.argv[4].isnumeric()):
                printf("Buffer size is not Int !", Fore.RED)
                return
            else:
                bs = int(sys.argv[4])

        fast.set_buffer_size(bs)
        if mode == "movefile":
            fast.move_single_file(src, des)
        else:
            fast.copy_single_file(src, des)

    elif mode == "deletefile" or mode == "removefile":
        os.remove(src)

    elif mode == "dirinfo":
        src = sys.argv[2]
        if not os.path.exists(src):
            printf("Source path not found !", Fore.RED)
            return
        fast.get_dir_info(src)

    elif mode == "fileinfo":
        src = sys.argv[2]
        if not os.path.exists(src):
            printf("Source path not found !", Fore.RED)
            return
        fast.get_file_info(src)

    else:
        printf("Invalid Arguments", Fore.RED)
    

if __name__ == "__main__":
    main()
