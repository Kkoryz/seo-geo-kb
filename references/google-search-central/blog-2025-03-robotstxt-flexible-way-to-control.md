---
title: "Robots Refresher: robots.txt — a flexible way to control how machines explore your website | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2025/03/robotstxt-flexible-way-to-control
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2025-03-07
---

# Robots Refresher: robots.txt — a flexible way to control how machines explore your website | Google Search Central Blog | Google for Developers

Friday, March 7, 2025

A long-standing tool for website owners, robots.txt has been in active use for over 30 years and
is broadly supported by crawler operators (such as tools for site owners, services, and search
engines). In this edition of the [robots refresher series](/search/blog/2025/02/intro-robots-refresher),
we'll take a closer look at robots.txt as a flexible way to tell robots what you want them to do
(or not do) on your website.

## Getting started with robots.txt

The way these files work is simple: you make a text file called "robots.txt" and then upload it to your website—and if you're using a content management system (CMS), it's likely even easier. You can leave your robots.txt file empty (or not have one at all) if your whole site may be crawled, or you can add rules to manage crawling. For example, to tell all bots (also known as crawlers, robots, spiders) to stay out of your "add to cart" page, you could write this in your robots.txt file:

user-agent: * disallow: /cart

## More specific things you can do with robots.txt

robots.txt is the Swiss Army knife of expressing what you want different robots to do or
not do on your website: it can be just a few lines, or it can be complex with more elaborate
rules targeting very specific URL patterns. You can use a robots.txt file for solving technical
issues (such as [unnecessary paginated pages](/search/docs/specialty/ecommerce/pagination-and-incremental-page-loading#avoid-indexing-variations)),
or for editorial or personal reasons (such as just not wanting certain things crawled). For
example, you could:

This group tells both |
user-agent: examplebot user-agent: otherbot disallow: /search |
For example, you could tell |
user-agent: documentsbot disallow: *.pdf |
|
user-agent: documentsbot allow: /blog/ disallow: /blog/drafts/ |
This robots.txt file disallows the mentioned |
user-agent: * allow: / user-agent: aicorp-trainer-bot disallow: / allow: /$ |
You can start a line with |
# I don't want bots in my highschool photos user-agent: * disallow: /photos/highschool/ |

For even more, you can check out our [list of useful robots.txt rules](/search/docs/crawling-indexing/robots/create-robots-txt#useful-robots.txt-rules).

## Making changes to your robots.txt file (practically)

The [Robots Exclusion Protocol (REP)](https://datatracker.ietf.org/doc/rfc9309/) works
by putting together rules ("allow" or "disallow")
and specifying which robots these rules apply to. You don't need to learn programming or fiddle
with tools; you can just put these rules in a text file and upload it to your website.

For most websites, it's even simpler than that! If you're using a CMS, it usually has something already built in to help you change your robots.txt file. For example, some CMSes let you customize your robots.txt file using checkboxes or with a simple form, and many have plugins that help you set up and write rules for your robots.txt file. To check what's possible within your CMS, you can do a search for the name of your CMS +"edit robots.txt file".

Once you've got things set up, you can also test to make sure your file is set up how you
intended. There are many testing tools built by the web community to help with this, such as
[TametheBot's robots.txt testing tool](https://tamethebots.com/tools/robotstxt-checker)
and this [robots.txt parser](https://www.realrobotstxt.com/) that
are using the [open-source robots.txt parser library](https://github.com/google/robotstxt).

If you have any questions about robots.txt, you can find us on [LinkedIn](https://www.linkedin.com/showcase/googlesearchcentral/)
or chat with like-minded experts in [our community forums](https://support.google.com/webmasters/community).
