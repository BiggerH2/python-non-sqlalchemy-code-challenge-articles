import pytest
from classes.many_to_many import Article
from classes.many_to_many import Magazine
from classes.many_to_many import Author


class TestMagazine:
    """Tests for Magazine class"""

    def test_has_name(self):
        """Magazine is initialized with a name"""
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")

        assert magazine_1.name == "Vogue"
        assert magazine_2.name == "AD"

    def test_name_is_immutable_string(self):
        """Magazine name is of type str and cannot change"""
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")

        assert isinstance(magazine_1.name, str)
        assert isinstance(magazine_2.name, str)

        with pytest.raises(AttributeError):
            magazine_1.name = "New Yorker"

    
    def test_name_len(self):
        """Magazine name is between 2 and 16 characters, inclusive"""
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
    
        assert 2 <= len(magazine_1.name) <= 16
        assert 2 <= len(magazine_2.name) <= 16
    def test_has_category(self):
        """Magazine is initialized with a category"""
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")

        assert magazine_1.category == "Fashion"
        assert magazine_2.category == "Architecture"

    def test_category_is_immutable_string(self):
        """Magazine category is of type str and cannot change"""
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")

        assert isinstance(magazine_1.category, str)
        assert isinstance(magazine_2.category, str)

        with pytest.raises(AttributeError):
            magazine_1.category = "Life Style"

    def test_category_len(self):
        """Magazine category has length greater than 0"""
        magazine_1 = Magazine("Vogue", "Fashion")

        assert magazine_1.category != ""
        def test_has_many_articles(self):
            """Magazine has many articles"""
            author = Author("Carry Bradshaw")
            magazine_1 = Magazine("Vogue", "Fashion")
            magazine_2 = Magazine("AD", "Architecture")
            article_1 = Article(author, magazine_1, "How to wear a tutu with style")
            article_2 = Article(author, magazine_1, "Dating life in NYC")
            article_3 = Article(author, magazine_2, "A new article title")  # Fixed code

    def test_has_many_contributors(self):
        """Magazine has many contributors"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine_1 = Magazine("Vogue", "Fashion")
        Article(author_1, magazine_1, "How to wear a tutu with style")
        Article(author_2, magazine_1, "Dating life in NYC")

        assert len(magazine_1.contributors) == 2
        assert author_1 in magazine_1.contributors
        assert author_2 in magazine_1.contributors