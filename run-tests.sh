#!/bin/bash
set -euxo pipefail

git clone https://github.com/wikimedia/pywikibot $1/pywikibot-build --depth 1
mkdir -p $1/pywikibot-build/scripts/i18n
touch $1/pywikibot-build/scripts/i18n/__init__.py
for item in *; do
    if [[ -d "$item" ]]; then
        cp -rp "$item" $1/pywikibot-build/scripts/i18n;
    fi;
done

cd $1/pywikibot-build
python -m unittest -v tests/l10n_tests.py
