from goose3 import Goose
from goose3.text import StopWordsChinese


g = Goose({'stopwords_class': StopWordsChinese})# 对语言进行初始化
article = g.extract(url='https://www.zhihu.com/question/356322653/answer/911210165')
# #property bucket
# print(article.additional_data)

# #作者
# print(article.authors)

# #在元数据可以找到的文章的规范链接
# print(article.canonical_link)

# #文本信息
# print(article.cleaned_text)

# #处理lxml文档
# print(article.doc)
# #[<Element div at 0x1faacbb8f98>, <Element span at 0x1faacbcd638>, <Element span at 0x1faacbcd408>, <Element span at 0x1faacbcd368>, <Element article at 0x1faacbcdc28>]

# #文章解析域
# print(article.domain)
# #zhuanlan.zhihu.com

# #提取解析url
# print(article.final_url)
# #https://zhuanlan.zhihu.com/p/34949081

# # 提取文章所有可用数据总和
# print(article.infos)
# #{'meta': {'description': '来源：微信订阅号 芯媒体（ID：icwant2018 ）原创2020年的大事件来了！.....

# #最终网址的MD5(MD5信息摘要算法)
# print(article.link_hash)
# #a1edb811c6a24ba2d7483ce08896e1ca.1578057021.0945435

# #文章中的url链表列表
# print(article.links)
# #[]

# #HTML源中的元描述字段内容
# print(article.meta_description)
# #源：微信订阅号 芯媒体（ID：icwant2018 ）原创2020年的大事件来了！ 美帝经济将在2020年左右出现严重危机！这绝对不是危言耸听。 美帝经济要遭受到严重打击的前提： 1. 美元的世界霸权体系崩溃 2. 美帝的军事打…

# #HTML源中的编码/字符集字段内容
# print(article.meta_favicon)
# #https://static.zhihu.com/heifetz/assets/apple-touch-icon-152.67c7b278.png

# #HTML源中meta-keywords字段的内容
# print(article.meta_keywords)
# #贸易战,中美贸易战,关税，川普，贸易战

# #HTML源中meta-lang字段的内容
# print(article.meta_lang)
# #zh

# # 返回视频对象,个人觉得效果并不好
# print(article.movies)

# #所有打开的图形标签数据
# print(article.opengraph)
# #{'description': '2019马上要过去啦，迎接2020年，好像每年都会做一个年终总结。一直很喜欢论语的一句话：吾日三省吾身，为…'}

# #基于元标记提取的文章发表日期
# print(article.publish_date)
# #None

# #原始的未清除和修改的xml文档
# print(article.raw_doc)
# #<Element html at 0x23741bfb6d8>

# #表示为字符串的HTML
# print(article.raw_html)
# # <!doctype html><html lang="zh" .....

# # 所有架构标签数据
# print(article.schema)
# #None

# #文章根标签列表
# print(article.tags)
# #['人生规划', '2020年', '年终总结', '2019']

# #从HTML源提取的标题
# print(article.title)
# #2020年马上到来了，如何总结你的2019？ - 知乎

#....差不多就这样了，剩下的我不想写了









