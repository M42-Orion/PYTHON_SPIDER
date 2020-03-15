import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq


'''
模拟浏览器pyppeteer,pyquery选择器，京东爬虫
'''
async def jingdong():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto("https://www.jd.com")

    input = await page.querySelector('#key')
    await input.type('手机')
    await page.keyboard.press('Enter')

    await page.waitForSelector('ul.gl-warp.clearfix>li')
    #list = await page.querySelectorAll('ul.gl-warp.clearfix>li')
    list = await page.JJeval('ul.gl-warp.clearfix>li', '(nodes => nodes.map(n => n.innerText))')#使用puppeteer中的方法提取相应的文字内容

    for i in list:
        print(i)
    await browser.close()
    return list
list = asyncio.get_event_loop().run_until_complete(jingdong())