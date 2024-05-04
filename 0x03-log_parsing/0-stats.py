#!/usr/bin/python3
"""
Write a script that reads stdin line by line
and computes metrics:
"""
import sys
import re


def show_status_log(fileSize, statusOccurence):
    """Prints the status log"""
    print('File size: {}'.format(fileSize))
    for k, v in statusOccurence.items():
        if v > 0:
            print('{}: {}'.format(k, v))


if __name__ == "__main__":
    """
    Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
    <status code> <file size>
    (if the format is not this one, the line must be skipped)
    After every 10 lines and/or a keyboard interruption (CTRL + C),
    print these statistics from the beginning:
    Total file size: File size: <total size>
    where <total size> is the sum of all previous <file size>
    (see input format above)
    Number of lines by status code:
    possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
    if a status code doesn’t appear or is not an integer,
    don’t print anything for this status code
    format: <status code>: <number>
    status codes should be printed in ascending order
    """
    fileSize = 0
    numLines = 0
    statusOccurence = {
        200: 0, 301: 0, 400: 0,
        401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    try:
        for line in sys.stdin:
            numLines += 1
            IPpattern = '[0-9]{2,3}\.[0-9]{2,3}\.[0-9]{2,3}\.[0-9]{2,3}'
            DatePattern = '\[[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{6}\]'
            UrlPattern = '"GET /[a-z]+/[0-9]+ HTTP/[0-9]\.[0-9]" [0-9]{3} [0-9]+'
            pattern = '{} - {} {}'.format(IPpattern, DatePattern, UrlPattern)
            p = re.search(pattern, line)
            if p is None:
                continue
            wordList = line.split()
            fileSize += int(wordList[8])
            statusOccurence[int(wordList[7])] += 1
            if numLines == 10:
                show_status_log(fileSize, statusOccurence)
                numLines = 0
    except KeyboardInterrupt:
        show_status_log(fileSize, statusOccurence)
