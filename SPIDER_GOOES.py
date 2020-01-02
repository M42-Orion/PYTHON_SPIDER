from goose3 import Goose
from goose3.text import StopWordsChinese


g = Goose({'stopwords_class': StopWordsChinese})# 对语言进行初始化
article = g.extract(url='https://www.jianshu.com/p/aec34e87c97f')

print(article.additional_data)
print(article.authors)
print(article.canonical_link)
print(article.cleaned_text)
print (article.cleaned_text)