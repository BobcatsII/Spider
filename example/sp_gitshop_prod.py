#-*- coding:utf-8 -*-

import os
import time
import requests
from lxml import etree


today = time.strftime("%Y_%m_%d")
count_time  = time.strftime("%Y/%m/%d %H:%M:%S")

url = "https://github.myshopify.com/collections/all-products"
headers = {
    "Host": "github.myshopify.com",
    "Referer": "https://github.myshopify.com/cart",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"
}

req = requests.get(url, headers=headers)
tree = etree.HTML(req.text)
prod_lst = tree.xpath('//div[@class="collection__products"]/div[@class="product-thumbnail"]')
sold_out = tree.xpath('//div[@class="collection__products"]/div[@class="product-thumbnail sold-out"]')
discount = tree.xpath('//div[@class="collection__products"]/div[@class="product-thumbnail on-sale"]')


if not os.path.exists('d:\\GithubShop\\{0}\\'.format(today)):
    os.makedirs('d:\\GithubShop\\{0}\\'.format(today))

with open('d:\\GithubShop\\{0}\\{0}_normal.txt'.format(today), 'a') as f:
    f.write("统计时间点：{0}\n".format(count_time))
    f.write("正常商品列表：\n")
for prod in prod_lst:
    prod_price = prod.xpath('./a/div/span')[0].text.strip()
    if prod_price == "":
        prod_name  = prod.xpath('./a/h3')[0].text.strip()
        prod_price = prod.xpath('./a/div[@class="product-thumbnail__price"]/span[@class="product-thumbnail__price__cost"]/span[contains(@class,"product-thumbnail__price__from")]')[0].text.strip()
        prod_img   = prod.xpath('./a/img/@src')[0]
        with open('d:\\GithubShop\\{0}\\{0}_normal.txt'.format(today), 'a') as f:
            f.write("商品名称：{0} || 商品最低价格：{1} || 商品图片展示：{2}\n".format(prod_name, prod_price, prod_img))
    else:
        prod_name = prod.xpath('./a/h3')[0].text.strip()
        prod_img = prod.xpath('./a/img/@src')[0]
        with open('d:\\GithubShop\\{0}\\{0}_normal.txt'.format(today), 'a') as f:
            f.write("商品名称：{0} || 商品价格：{1} || 商品图片展示：{2}\n".format(prod_name, prod_price, prod_img))


with open('d:\\GithubShop\\{0}\\{0}_discount.txt'.format(today), 'a') as f:
    f.write("统计时刻：{0}\n".format(count_time))
    f.write("折扣商品列表：\n")
for dis in discount:
    dis_name = dis.xpath('./a/h3')[0].text.strip()
    regular_price = dis.xpath('./a/div/span/s')[0].text.strip()
    dis_price = dis.xpath('./a/div/span/span[2]')[0].text.strip()
    dis_img = dis.xpath("./a/img/@src")[0]
    with open('d:\\GithubShop\\{0}\\{0}_discount.txt'.format(today), 'a') as f:
        f.write("商品名称：{0} || 商品原价：{1} || 商品折扣价：{2} || 商品展示链接：{3}\n".format(dis_name,regular_price,dis_price,dis_img))


with open('d:\\GithubShop\\{0}\\{0}_soldout.txt'.format(today), 'a') as f:
    f.write("统计时刻：{0}\n".format(count_time))
    f.write("售罄商品列表：\n")
for sold in sold_out:
    sold_price = sold.xpath('./a/div[@class="product-thumbnail__price"]/span')[0].text.strip()
    if sold_price == "":
        sold_name   = sold.xpath('./a/h3')[0].text.strip()
        sold_status = sold.xpath('./a/div/span')[0].text.strip()
        sold_img = sold.xpath('./a/img/@src')[0]
        sold_price = sold.xpath('./a/div[@class="product-thumbnail__price"]/span[@class="product-thumbnail__price__cost"]/span[contains(@class,"product-thumbnail__price__from")]')[0].text.strip()
        with open('d:\\GithubShop\\{0}\\{0}_soldout.txt'.format(today), 'a') as f:
            f.write("商品名称：{0} || 商品价格：{1} || 商品状态：{2} || 商品展示链接：{3}\n".format(sold_name, sold_price, sold_status, sold_img))
    else:
        sold_name = sold.xpath('./a/h3')[0].text.strip()
        sold_img    = sold.xpath('./a/img/@src')[0]
        sold_status = sold.xpath('./a/div/span')[0].text.strip()
        with open('d:\\GithubShop\\{0}\\{0}_soldout.txt'.format(today), 'a') as f:
            f.write("商品名称：{0} || 商品价格：{1} || 商品状态：{2} || 商品展示链接：{3}\n".format(sold_name, sold_price, sold_status, sold_img))
            
            
            
            
