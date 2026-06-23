---
title: "Using RSS/Atom feeds to discover new URLs | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2009/10/using-rssatom-feeds-to-discover-new
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2009-10-30
---

# Using RSS/Atom feeds to discover new URLs | Google Search Central Blog | Google for Developers

Google uses numerous sources to find new webpages, from links we find on the web to
submitted URLs. We aim to
discover new pages quickly so that users can find new content in Google search results soon after
they go live. We recently launched a feature that uses RSS and Atom feeds for the discovery of
new webpages.

RSS/Atom feeds have been very popular in recent years as a mechanism for content publication.
They allow readers to check for new content from publishers. Using feeds for discovery allows us
to get these new pages into our index more quickly than traditional crawling methods. We may use
many potential sources to access updates from feeds including Reader, notification services, or
direct crawls of feeds. Going forward, we might also explore mechanisms such as
PubSubHubbub
to identify updated items.

In order for us to use your RSS/Atom feeds for discovery, it's important that crawling these files
is not disallowed by your robots.txt.
To find out if Googlebot can crawl your feeds and find your pages as fast as possible, test your
feed URLs with the
robots.txt tester in Google Webmaster Tools.

Written by Raymond Lo, Guhan Viswanathan, and Dave Weissman, Crawl and Indexing Team

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],[],[],["Google uses various sources, including submitted URLs, to find new webpages. A new feature utilizes RSS and Atom feeds to expedite the discovery and indexing of fresh content. Feeds are accessed through methods like direct crawls or notification services. Ensuring that feed crawling isn't blocked by `robots.txt` is crucial for fast indexing. Webmasters can test feed URLs via the `robots.txt` tester tool to confirm accessibility. PubSubHubbub is a future technology they may also explore to identify updated items.\n"]]
