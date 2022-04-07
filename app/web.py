import re
import time
import urllib.request

import bs4


class Web:
    def __init__(self):
        pass

    def tag_visible(self, element):
        """Helper method for filtering visible elements.

        :param element:
        :return:
        """
        if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
            return False
        if isinstance(element, bs4.element.Comment):
            return False
        return True

    def scrape(self, url, keyword):
        """Method measures page loading time and counts occurrences of the keyword.

        :param url:
        :param keyword:
        :return:
        """
        start_time = time.time()
        html = urllib.request.urlopen(url).read()
        elapsed_time = time.time() - start_time

        soup = bs4.BeautifulSoup(html, 'html.parser')
        texts = soup.findAll(text=True)
        visible_texts = filter(self.tag_visible, texts)

        hits = 0
        for content in visible_texts:
            # removing all whitespace characters
            regex = re.compile(r'\s+')

            # pattern matching for keyword
            for word in regex.split(content):
                pattern = re.compile(r'\b{0}\b'.format(keyword))
                try:
                    match = re.findall(pattern, word)
                    hits += len(match)
                    print(word)
                except AttributeError:
                    pass

        return [url, keyword, start_time, elapsed_time, hits]
