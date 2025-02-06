import datetime
import email.utils
import json
import subprocess
import shutil

from pathlib import Path
from operator import itemgetter
from os.path import basename
from urllib.parse import urlparse


def git(*args):
    argv = list(map(str, args))
    print(f"Running git {' '.join(argv)}")
    return str(subprocess.run(["git"] + list(map(str, argv)),
                          check=True, capture_output=True,
                          ).stdout, encoding='utf-8')


try:
    repos = Path("repos")
    repos.mkdir(exist_ok=True)

    urls = json.loads(Path('repourls.json').read_text())

    dates = {}
    score = {}
    for url in urls:

        dir = repos / basename(urlparse(url).path)
        author_date = b''

        if dir.exists():
            try:
                git("-C", dir, "pull")
                author_date = git("-C", dir, "show", "--pretty=format:'%aD'", "-s")
            except subprocess.CalledProcessError:
                print(f"Ignoring {url}")
        else:
            git("clone", "--depth=1", "--filter=blob:none",  url, dir)
            author_date = git("-C", dir, "show", "--pretty=format:'%aD'", "-s")

        dt = email.utils.parsedate_tz(author_date)

        points = 0
        try:
            wiring = git("-C", dir, "grep", "wiring.Signature")
            points += 1
            print(wiring)
            signature = git("-C", dir, "grep", "Signature")
            print(signature)
            points += 1
            io = git("-C", dir, "grep", "Direction")
            points += 1
        except subprocess.CalledProcessError:
            pass

        dates[dt] = (url, points)
        score[points] = (url, dt)

    ordered_keys = sorted(dates.keys(), reverse=True)
    print(f"latest repos: {itemgetter(*ordered_keys[:3])(dates)}")
    top_score = sorted(score.keys(), reverse=True)
    print(f"Top Amaranth score repos: {itemgetter(*top_score[:3])(score)}")

    full = [(dates[k], k) for k in ordered_keys]
    Path("latest.json").write_text(json.dumps(full))


except subprocess.CalledProcessError as e:
    print(f"Command:\n{e.cmd}\nfailed with exit code {e.returncode}:\n{str(e.output, encoding='utf-8')}")
