---
title: "An update to referral source URLs for Google Images | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2018/07/an-update-to-referral-source-urls-for
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2018-07-17
---

# An update to referral source URLs for Google Images | Google Search Central Blog | Google for Developers

Tuesday, July 17, 2018

Every day, hundreds of millions of people use
[Google Images](https://images.google.com/) to visually discover and
explore content on the web. Whether it be finding ideas for your next baking project, or visual
instructions on how to fix a flat tire, exploring image results can sometimes be much more
helpful than exploring text.

## Updating the referral source

For webmasters, it hasn't always been easy to understand the role Google Images plays in driving
site traffic. To address this, we will roll out a new
[referrer URL](https://en.wikipedia.org/wiki/HTTP_referer) specific to
Google Images over the next few months. The referrer URL is part of the HTTP header, and indicates
the last page the user was on and clicked to visit the destination webpage.

If you create software to track or analyze website traffic, we want you to be prepared for this change. Make sure that you are ingesting the new referer URL, and attribute the traffic to Google Images. The new referer URL is:

https://images.google.com

If you use [Google Analytics](https://analytics.google.com/) to track
site data, the new referral URL will be automatically ingested and traffic will be attributed to
Google Images appropriately. Just to be clear, this change will not affect
[Search Console](https://search.google.com/search-console). Webmasters
will continue to receive an aggregate list of top search queries that drive traffic to their site.

## How this affects country-specific queries

The new referer URL has the same
[country code top level domain](https://en.wikipedia.org/wiki/Country_code_top-level_domain)
(ccTLD) as the URL used for searching on Google Images. In practice, this means that most visitors
worldwide come from images.google.com. That's because last year,
[we made a change](https://www.blog.google/products/search/making-search-results-more-local-and-relevant/)
so that google.com became the default choice for searchers worldwide. However, some users may
still choose to go directly to a country specific service, such as google.co.uk for the UK. For
this use case, the referer uses that country TLD (for example, `images.google.co.uk`

).

We hope this change will foster a healthy visual content ecosystem. If you're interested in
learning how to optimize your pages for Google Images, please refer to the
[Google Image Publishing Guidelines](/search/docs/appearance/google-images).
If you have questions, feedback or suggestions, please let us know through the
[Webmaster Tools Help Forum](https://groups.google.com/a/googleproductforums.com/forum/#!categories/webmasters).
