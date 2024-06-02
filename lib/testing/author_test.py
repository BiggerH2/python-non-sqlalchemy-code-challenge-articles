import pytest
from classes.many_to_many import Author, Magazine, Article


class TestAuthor:
    """Tests for Author class"""

    def test_has_name(self):
        """Author is initialized with a name"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")

        assert author_1.name == "Carry Bradshaw"
        assert author_2.name == "Nathaniel Hawthorne"

    def test_name_is_immutable_string(self):
        """Author name is of type str and cannot change"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")

        assert isinstance(author_1.name, str)
        assert isinstance(author_2.name, str)

        with pytest.raises(AttributeError):
            author_1.name = "ActuallyTopher"

        with pytest.raises(AttributeError):
            author_2.name = 2

    def test_name_len(self):
        """Author name is longer than 0 characters"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")

        assert len(author_1.name) > 0
        assert len(author_2.name) > 0

    def test_has_many_articles(self):
        """Author has many articles"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author_1, magazine, "How to wear a tutu with style")
        article_2 = Article(author_1, magazine, "Dating life in NYC")
        article_3 = Article(author_2, magazine, "How to be single and happy")

        assert len(author_1.articles) == 2
        assert len(author_2.articles) == 1
        assert article_1 in author_1.articles
        assert article_2 in author_1.articles
        assert article_3 in author_2.articles

    def test_articles_of_type_articles(self):
        """Author articles are of type Article"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine = Magazine("Vogue", "Fashion")
        Article(author_1, magazine, "How to wear a tutu with style")
        Article(author_2, magazine, "Dating life in NYC")

        assert all(isinstance(article, Article) for article in author_1.articles)
        assert all(isinstance(article, Article) for article in author_2.articles)

    def test_topic_areas(self):
        """Returns a list of topic areas for all articles by author"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        author_1.add_article(magazine_1, "How to wear a tutu with style")
        author_1.add_article(magazine_2, "Carrara Marble is so 2020")
        author_2.add_article(magazine_2, "2023 Eccentric Design Trends")

        assert len(author_1.topic_areas()) == 2
        assert set(author_1.topic_areas()) == {"Fashion", "Architecture"}
        assert author_2.topic_areas() == ["Architecture"]

    def test_has_many_magazines(self):
        """Author has many magazines"""
        author_1 = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        article_1 = Article(author_1, magazine_1, "How to wear a tutu with style")
        article_2 = Article(author_1, magazine_2, "2023 Eccentric Design Trends")
        article_3 = Article(author_1, magazine_2, "Carrara Marble is so 2020")

        assert len(set([article.magazine for article in author_1.articles])) == len(author_1.articles)
        assert len(author_1.articles) == 3

    def test_add_article(self):
        """Creates and returns a new article given a magazine and title"""
        author_1 = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        article_1 = author_1.add_article(magazine_1, "How to wear a tutu with style")
        article_2 = author_1.add_article(magazine_2, "2023 Eccentric Design Trends")
        article_3 = author_1.add_article(magazine_2, "Carrara Marble is so 2020")

        assert isinstance(article_1, Article)
        assert len(author_1.articles) == 3
        assert len(magazine_1.articles) == 1
        assert len(magazine_2.articles) == 2
        assert article_1 in magazine_1.articles
        assert article_2 in magazine_2.articles
        assert article_3 in magazine_2.articles
