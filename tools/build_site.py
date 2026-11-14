"""Build both documentation projects before replacing the generated website."""

import argparse
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', default='site', help='site or a path under output/ or tmp/')
    args = parser.parse_args()
    destination = (ROOT / args.output).resolve()
    relative = destination.relative_to(ROOT)
    if not relative.parts or relative.parts[0] not in {'site', 'output', 'tmp'}:
        parser.error('Output must be site or a directory under output/ or tmp/.')
    if relative.parts[0] == 'site' and len(relative.parts) != 1:
        parser.error('Use site itself, not a subdirectory of an existing site.')
    if relative.parts[0] in {'output', 'tmp'} and len(relative.parts) < 2:
        parser.error('Choose a dedicated directory below output/ or tmp/.')
    if destination.exists() and (
        not (destination / 'index.html').is_file()
        or not (destination / '.nojekyll').is_file()
        or (destination / '.git').exists()
    ):
        parser.error('Existing output must be a generated site with index.html and .nojekyll.')

    domain = (ROOT / 'CNAME').read_text(encoding='ascii').strip()
    if not re.fullmatch(r'[a-z0-9](?:[a-z0-9.-]*[a-z0-9])?', domain):
        raise ValueError('CNAME must contain one domain name.')

    temp_root = ROOT / 'tmp'
    temp_root.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='hpr-build-', dir=temp_root) as temp_name:
        temporary = Path(temp_name).resolve()
        if temporary.parent != temp_root.resolve():
            raise ValueError('Build directory escaped the project temporary directory.')
        stage = temporary / 'site'
        for solver in ('hprlp', 'hprqp'):
            subprocess.run([
                sys.executable, '-m', 'sphinx', '-W', '--keep-going', '-E', '-a',
                '-b', 'html', '-d', str(temporary / 'doctrees' / solver),
                str(ROOT / 'docs' / solver), str(stage / solver),
            ], cwd=ROOT, check=True)
        shutil.copytree(ROOT / 'landing', stage, dirs_exist_ok=True)
        shutil.copytree(ROOT / 'assets', stage / 'assets')
        (stage / '.nojekyll').touch()
        (stage / 'CNAME').write_text(domain + '\n', encoding='ascii')

        destination.parent.mkdir(parents=True, exist_ok=True)
        previous = temporary / 'previous-site'
        if destination.exists():
            os.replace(destination, previous)
        try:
            os.replace(stage, destination)
        except OSError:
            if previous.exists():
                os.replace(previous, destination)
            raise
    print(f'Built both documentation projects successfully: {destination}')


if __name__ == '__main__':
    main()
