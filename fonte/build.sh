#!/bin/sh
# LITE=1 ./build.sh gera a versão de gráfico simples (mesmo código, sem arte embutida).
# build completo: index-v17.bak.html -> index.html (publicar) e site/index.html (teste, com gancho __d)
set -e
mkdir -p site
python3 idle_merge.py
python3 edgefade.py >/dev/null
python3 patch18.py >/dev/null
python3 patch19.py >/dev/null
python3 patch20.py
python3 patch21.py
python3 patch22.py
python3 patch23.py
python3 patch24.py
python3 patch25.py
python3 patch26.py
python3 patch27.py
python3 patch28.py
python3 patch29.py
python3 patch30.py
python3 patch31.py
python3 patch32.py
rm -f game18.js game19.js
echo "__d em index.html: $(grep -c __d index.html || true)"
