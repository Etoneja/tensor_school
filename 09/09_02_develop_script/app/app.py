import logging
import os
import time
import typing

from mysql import connector


LOG = logging.getLogger(__name__)

DB_HOST = os.environ.get("DB_HOST")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_DATABASE = os.environ.get("DB_DATABASE")

SITE_PATH = "/usr/share/nginx/html/"
INDEX_PAGE = "index.html"

STEP_TIMEOUT = 60

select_random_article_query = """
select id, title, text
from articles
order by rand()
limit 1;
"""

ARTICLE_PAGE_HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<body>

<h1>{id}. {title}</h1>
<p>{text}</p>

</body>
</html>
"""


class Article(typing.NamedTuple):
    id: int
    title: str
    text: str


def get_random_article():
    with connector.connect(host=DB_HOST,
                           user=DB_USER,
                           password=DB_PASSWORD,
                           database=DB_DATABASE) as conn:

        with conn.cursor(dictionary=True) as cursor:
            cursor.execute(select_random_article_query)
            res = cursor.fetchone()

    return Article(**res)


def ensure_path(path):
    if not os.path.exists(path):
        os.makedirs(path)


def render_page(template, data):
    return template.format(**data)


def save_page(page, path):
    tmp_path = path + ".tmp"
    with open(tmp_path, 'w') as f:
        f.write(page)

    os.rename(tmp_path, path)


def create_index_page():
    article = get_random_article()
    article_data = {
        "id": article.id,
        "title": article.title,
        "text": article.text
    }
    page = render_page(ARTICLE_PAGE_HTML_TEMPLATE, article_data)
    path = os.path.join(SITE_PATH, INDEX_PAGE)
    save_page(page, path)

    LOG.info("Index page created")


def main():
    ensure_path(SITE_PATH)

    while True:
        create_index_page()
        time.sleep(STEP_TIMEOUT)


if __name__ == "__main__":
    main()
