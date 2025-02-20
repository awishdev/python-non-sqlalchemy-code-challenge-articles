class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if not hasattr(self, 'title'):
            if isinstance(title, str) and 5 <= len(title) <= 50:
                self._title = title
            else:
                raise Exception("Invalid title. Title should be a string between 5 and 50 characters inclusive")
        else:
            raise Exception("Title has already been set.")
        
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise Exception("Invalid author. Author should be an instance of Author class")
        
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            raise Exception("Invalid magazine. Magazine should be an instance of Magazine class")
        
class Author:
    all = []
    def __init__(self, name):
        self.name = name
        Author.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not hasattr(self, 'name'):
            if isinstance(name, str) and 0 <= len(name):
                self._name = name
            else:
                raise Exception("Invalid name. Name should be a string with at least one character")
        else:
            raise Exception("Name has already been set.")

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return [magazine for magazine in Magazine.all if magazine in [article.magazine for article in self.articles()]]

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        topics = list(set([article.magazine.category for article in self.articles()]))
        if topics: 
            return topics
        else:
            return None

class Magazine:
    all = []
    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            raise Exception("Invalid name. Name should be a string between 2 and 16 characters")

        
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if isinstance(category, str) and 0 < len(category):
            self._category = category
        else:
            raise Exception("Invalid category. Category should be a string with at least one character")

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return [author for author in Author.all if author in [article.author for article in self.articles()]]

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        if titles:
            return titles
        else:
            return None

    def contributing_authors(self):
        authors = [author for author in Author.all if author in [article.author for article in self.articles()]]
        contributing_authors = [author for author in authors if len([article for article in author.articles() if article.magazine == self]) >= 2]
        if contributing_authors:
            return contributing_authors
        else:
            return None
        
    @classmethod
    def top_publisher(cls):
        if Article.all:
            magazine_counts = {magazine: len([article for article in magazine.articles()]) for magazine in cls.all}
            if not magazine_counts:
                return None
            else:
                return max(magazine_counts, key=magazine_counts.get)
            #return max(magazine_counts, key=magazine_counts.get, default=None)
        
        else:
            return None