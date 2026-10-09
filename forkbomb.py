import os
import sys
import subprocess

MAX_DEPTH = 1000

def replicate(depth):
    if depth >= MAX_DEPTH:
        print(f"[{depth}] стоп — досягнуто ліміту")
        return

    print(f"[{depth}] копія запущена, pid={os.getpid()}")

    for _ in range(2):
        subprocess.Popen(
            [sys.executable, __file__, str(depth + 1)],
            creationflags=subprocess.CREATE_NEW_CONSOLE if os.name == "nt" else 0
        )

if __name__ == "__main__":
    d = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    replicate(d)