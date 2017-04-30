#/bin/bash
python render.py index.template index.html
git add -A
git commit -m "blog update"
git push origin master
