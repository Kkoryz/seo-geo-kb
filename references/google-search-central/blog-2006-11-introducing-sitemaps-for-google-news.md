---
title: "Introducing Sitemaps for Google News | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2006/11/introducing-sitemaps-for-google-news
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2006-11-20
---

# Introducing Sitemaps for Google News | Google Search Central Blog | Google for Developers

Monday, November 20, 2006

Good news for webmasters of English-language news sites: If your site is currently included in
[Google News](https://news.google.com/), you can now create News
Sitemaps that tell us exactly which articles to crawl for inclusion in Google News. In addition,
you can access crawl errors, which tell you if there were any problems crawling the articles in
your News Sitemaps, or, for that matter, any articles on your site that Google News reaches
through its normal crawl.

Freshness is important for news, so we recrawl all News Sitemaps frequently. The
[News Sitemaps XML definition](/search/docs/crawling-indexing/sitemaps/news-sitemap)
lets you specify a publication date and time for each article to help us process fresh articles in
timely fashion. You can also specify keywords for each article to inform the placement of the
articles into sections on Google News.

If your English-language news site is currently included in Google News, the news features are automatically enabled in Webmaster Tools; just add the site to your account. Here's how the new summary page will look:

The presence of the **News crawl** link on the left indicates that the news features are
enabled. A few things to note:

-
You will only have the news features enabled if your site is currently included in Google News.
If it's not, you can
[request inclusion](https://www.google.com/support/news_pub/bin/answer.py?answer=40787). -
In most cases, you should
[add the site](https://support.google.com/webmasters/answer/34592)for the**hostname**under which you publish your articles. For example, if you publish your articles at URLs such as`https://www.example.com/business/article123.html`

, you should add the site`https://www.example.com/`

. Exception: If your site is within a hosting site, you should add the site for your**home page**, for example,`https://members.tripod.com/mynewssite/`

. If you publish articles under multiple hostnames, you should add a site for each of them. -
You must
[verify your site](https://support.google.com/webmasters/answer/34592)to enable the news features.

We'll be working to make the news features available to publishers in more languages as soon as possible.
