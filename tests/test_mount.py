#!/usr/bin/env python3

import sys, os, tempfile
from pathlib import Path

from testsupport import run, run_project_executable, subtest
from fuse_helpers import run_background, fuse_unmount, fuse_mount, gen_mnt_path, fuse_check_mnt

def main() -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        temp_path = Path(tmpdir)
        mnt_path  = fuse_mount(temp_path, "memfs_mnt")

        with subtest("Check mount"):
            fuse_check_mnt(tmpdir, mnt_path)
        fuse_unmount(mnt_path)
        sys.exit(0)

if __name__ == "__main__":
    main()
