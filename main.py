import os
import shutil


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile("entry.txt", os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()


# The entry text is finished before this program ever runs: it lives in
# entry.txt, written by hand, and this script writes none of it. All it
# does is carry that finished file, byte for byte, into the folder the
# grader names through MAKEFUN_OUTPUT_DIR, making the folder first when
# it is not there yet, so the judged text reads exactly as written.
