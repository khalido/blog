---
title: "Shopify"
description: "notes for setting up a shopify site"
date: 2022-01-12
draft: True
tags:
- web
---

## What is shopify anyways?

This is a good overview: [How Shopify Outfoxed Amazon to Become the Everywhere Store](https://www.bloomberg.com/news/features/2021-12-23/shopify-amazon-retail-rivalry-heats-up-with-covid-sparked-online-shopping-booma?sref=dJuchiL5) and lots of [discussion over at the Shopify reddit](https://www.reddit.com/r/shopify/).

## Useful Apps

I am sticking with mostly free apps or paid ones with a useful free tier.

[Shopify Inbox](https://shopifyinbox.com) for adding messages to the website.

Shopify Reviews

Shopify has a [local delivery app](https://apps.shopify.com/local-delivery) which helps to build delivery lists, but there is no way to print out labels.

[Order Printer](https://apps.shopify.com/order-printer) by Shopify, allows you to add a templates for each order, so I used the following on to print shipping labels. 

```html
<strong>
<span style="font-size:25px">{{ shop_name }} AU</span><br/>
<span style="font-size:34px">Local Delivery</span>
<br><br>
</strong>
<span style="font-size:18px">Order #{{ order_number }} on {{ created_at | date: "%Y-%m-%d %H:%M" }}.</span>
<br/><br/><br/>

<strong><span style="text-transform:uppercase;font-size:26px">{{ shipping_address.name }}</strong></span><br/>
<span style="text-transform:uppercase;font-size:20px">{{ shipping_address.company }}<br/>
{{ shipping_address.street }}<br/>
{{ shipping_address.city }}, {{ shipping_address.province_code }} {{shipping_address.zip }}<br/>
{{ shipping_address.phone }}</span>
```