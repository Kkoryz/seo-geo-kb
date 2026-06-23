---
title: "Speaking the language of robots | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2008/03/speaking-language-of-robots
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2008-03-27
---

# Speaking the language of robots | Google Search Central Blog | Google for Developers

Thursday, March 27, 2008

We all know
[how friendly Googlebot is](/search/blog/2008/03/first-date-with-googlebot-headers-and).
And like all benevolent robots, Googlebot listens to us and respects our wishes about parts of
our site that we don't want crawled. We can just give Googlebot a robots.txt file explaining what
we want, and it'll happily comply. But what if you're intimidated by the idea of communicating
directly with Googlebot? After all, not all of us are fluent in the language of
[robots.txt](/search/docs/crawling-indexing/overview-google-crawlers). This is why
we're pleased to introduce you to your personal robot translator: the Robots.txt Generator in
[Webmaster Tools](https://search.google.com/search-console).
It's designed to give you an easy and interactive way to build a robots.txt file. It can be as
simple as entering the files and directories you don't want crawled by any robots.

Or, if you need to, you can create fine-grained rules for specific robots and areas of your site.

Once you're finished with the generator, you can test the effects of your new robots.txt file with
our
[robots.txt analysis tool](https://www.google.com/webmasters/tools/robots-testing-tool).
When you're done, just save the generated file to the top level (root) directory of your site,
and you're good to go. There are a couple of important things to keep in mind about robots.txt
files:

-
**Not every search engine will support every extension to robots.txt files**

The Robots.txt Generator creates files that Googlebot will understand, and most other major robots will understand them too. But it's possible that some robots won't understand all of the robots.txt features that the generator uses. -
**Robots.txt is simply a request**

Although it's highly unlikely from a major search engine, there are some unscrupulous robots that may ignore the contents of robots.txt and crawl blocked areas anyway. If you have sensitive content that you need to protect completely, you should put it behind password protection rather than relying on robots.txt.

We hope this new tool helps you communicate your wishes to Googlebot and other robots that visit
your site. If you want to learn more about robots.txt files, check out
[our Help Center](/search/docs/crawling-indexing/robots/intro). And if you'd like to discuss
robots.txt and robots with other webmasters, visit our
[Google Webmaster Help Group](https://support.google.com/webmasters/community).
