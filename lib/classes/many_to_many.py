class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = title
        Article.all.append(self)
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if self.title is None and isinstance(title, str) and (5 < len(title) < 50):
            self._title = title

        
class Author:
    all = []
    def __init__(self, name):
        self._name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if self.name is None and isinstance(name, str) and (len(name) > 0):
            self._name = name

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        articles = self.articles()
        if articles == []:
            return None
        else:
            return list(set([article.magazine.category for article in self.articles()]))
            
        


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
        if isinstance(name, str) and (2 <= len(name) <= 16):
            self._name = name

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if isinstance(category, str) and (len(category) > 0):
            self._category = category

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set([article.author for article in self.articles()]))

    def article_titles(self):
        articles = self.articles()
        if not articles:
            return None
        else:
            return [article.title for article in self.articles()]

    def contributing_authors(self):
        articles = self.articles()
        if len(articles) > 2:
            return [article.author for article in self.articles()]