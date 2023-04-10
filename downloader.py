# Laboratory 1
# Run:
# 'python downloader.py <URL for dowloading>'


import sys
import time
from urllib import request
from urllib import parse

link = ''
# urls:
# 'https://www.vssut.ac.in/lecture_notes/lecture1423726199.pdf'
# 'https://personal.utdallas.edu/~chung/Fujitsu/UML_2.0/Rumbaugh--UML_2.0_Reference_CD.pdf'


def reporthook(counter, block_size, total_size):
    global t_init
    global t_visualization

    if counter == 0:
        t_init = time.time()
        t_visualization = 0
        sys.stdout.write(f"Progress: 0% || 0/{total_size} bytes, 0 secs \n")
        return
    duration = time.time() - t_init
    progress_size = int(counter * block_size)
    percent = min(int(counter * block_size * 100 / total_size), 100)

    if int(t_visualization) != int(duration):
        sys.stdout.write(
            f"Progress: {percent}% || {progress_size}/{total_size} bytes, {round(duration)} secs \n")
        t_visualization = duration

    if progress_size >= total_size:
        sys.stdout.write(
            f"Progress: {percent}% || {total_size}/{total_size} bytes, {round(duration, 2)} secs\nFile {link} is successful downloaded!\n")


def main(argv):
    url = argv[1]
    unq_url = parse.unquote(url)
    path = parse.urlparse(unq_url).path

    global link
    link = path.rstrip("/").split("/")[-1]

    # dowloading method from the url
    request.urlretrieve(url, link, reporthook)


if __name__ == '__main__':
    main(sys.argv)
