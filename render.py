import sys
import os
import jinja2
import glob
import time

def render(tpl_path, context):
  path, filename = os.path.split(tpl_path)
  return jinja2.Environment(
      loader=jinja2.FileSystemLoader(path or './')
  ).get_template(filename).render(context)

def as_str(file):
  with open(file, 'r') as rdr:
    return rdr.read().replace('\n', '')

def numeric_date(localtime):
  return time.strftime('%Y-%m-%d', localtime)

def formal_date(localtime):
  return time.strftime('%B %d, %Y', localtime)

def localtime_of_file(file):
  return time.localtime(os.path.getmtime(file))

def get_articles(path):
  articles = []
  for article_dir in sorted([os.path.join(path, f) for f in os.listdir(path)]):
    article = {}
    for field in glob.glob(os.path.join(article_dir + "/*")):
      article[os.path.basename(field)] = as_str(field)
    article['date'] = numeric_date(localtime_of_file(article_dir))
    article['formatted-date'] = formal_date(localtime_of_file(article_dir))
    articles.append(article)
  return {"articles": articles}

template = sys.argv[1]
output = sys.argv[2]

f = open(output, 'w')
f.write(render(template, get_articles("articles/")))
f.close()