# lib/classes/many_to_many.py

class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = title
        Article.all.append(self)
        magazine.articles.append(self)
        author.articles.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise ValueError("Title must be a string.")
        if not 5 <= len(value) <= 50:
            raise ValueError("Title must be between 5 and 50 characters long.")
        self._title = value

class Author:
    def __init__(self, name):
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    @property
    def articles(self):
        return self._articles

   
    def add_article(self, magazine, title):
        if magazine not in self.magazines:
            self.magazines.append(magazine)
        article = Article(self, magazine, title)
        self.articles.append(article)
        return article
    

    def topic_areas(self):
        return list(set(article.magazine.category for article in self._articles))

class Magazine:
    """Magazine class"""

    def __init__(self, name, category):
        if not category:
            raise ValueError("Magazine category cannot be empty.")
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    @property
    def articles(self):
        return self._articles

    def add_article(self, article):
        if article not in self._articles:
            self._articles.append(article)
            article.magazine = self

    def remove_article(self, article):
        if article in self._articles:
            self._articles.remove(article)
            article.magazine = None

    def article_titles(self):
        return [article.title for article in self._articles]

    def contributors(self):
        return list(set(article.author for article in self._articles if article.author))

    def contributing_authors(self):
        author_counts = {}
        for article in self._articles:
            author = article.author
            if author:
                author_counts[author] = author_counts.get(author, 0) + 1
        return [author for author, count in author_counts.items() if count > 2]

    @classmethod
    def top_publisher(cls):
        if not cls._articles:
            return None
        return max(cls._articles, key=lambda mag: len(mag.articles))

    def topic_areas(self):
        return list(set(article.category for article in self._articles))
