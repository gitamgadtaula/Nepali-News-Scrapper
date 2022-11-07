from newspaper import Article
# import nltk
# nltk.download('punkt')
url = 'https://www.onlinekhabar.com/2022/11/1214182'
article = Article(url, language='hi')
article.download()
# article.html
article.parse()
article.nlp()
data = {
    "TITLE": article.title,
    "keywords": article.keywords,
    "summary": article.summary,
    "TEXT": article.text,
    "img_url": article.top_image,
}
print(data)
# print(article.keywords)
