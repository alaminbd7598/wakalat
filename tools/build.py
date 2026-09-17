#!/usr/bin/env python3
"""Generate the static site (HTML pages, sitemap, robots) into the repository root.

Usage:  python3 tools/build.py
"""
import os, sys, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wsite import pages_home, pages_services, pages_info
from wsite.layout import SITE

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def main():
    pages = {}
    pages.update(pages_home.build())
    pages.update(pages_services.build())
    pages.update(pages_info.build())
    for name, html in pages.items():
        with open(os.path.join(ROOT, name), 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'wrote {name} ({len(html)//1024} KB)')
    today = datetime.date.today().isoformat()
    urls = [n for n in pages if n != '404.html']
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(
        f"  <url><loc>{SITE['url']}/{'' if u == 'index.html' else u}</loc><lastmod>{today}</lastmod><priority>{'1.0' if u == 'index.html' else '0.8'}</priority></url>\n" for u in urls) + '</urlset>\n'
    open(os.path.join(ROOT, 'sitemap.xml'), 'w').write(sm)
    open(os.path.join(ROOT, 'robots.txt'), 'w').write(f"User-agent: *\nAllow: /\nSitemap: {SITE['url']}/sitemap.xml\n")
    print('wrote sitemap.xml, robots.txt')

if __name__ == '__main__':
    main()
