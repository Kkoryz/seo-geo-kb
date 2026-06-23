---
title: "Minor cleaning up in the Search Console API | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2019/08/minor-cleaning-up-in-search-console-api
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2019-08-26
---

# Minor cleaning up in the Search Console API | Google Search Central Blog | Google for Developers

With the move to the
new Search Console,
we've decided to clean up some parts of the Search Console API as well. In the
Search Analytics API,
going forward we'll no longer support these Android app search appearance types:

Is Install

Is App Universal

Is Opened

Since these appearance types are no longer used in the UI, they haven't been populated with data
recently. Going forward, we won't be showing these types at all through the API.

Additionally, for the
Sitemaps API,
we're no longer populating data on indexing status of submitted sitemap files in the "Indexed"
field.

We're still committed to the Search Console API. In particular, we're working on updating the
Search Console API to the new Search Console. We don't have any specific timeframes to share at
the moment, but stay tuned to find out more!

Posted by Ziv Hodak, Search Console product manager

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],[],[],["The Search Console API will discontinue support for Android app search appearance types: Is Install, Is App Universal, and Is Opened, as they are no longer used in the UI. The Sitemaps API will also stop populating the \"Indexed\" field for submitted sitemap files. These changes reflect a cleanup alongside the move to the new Search Console, with ongoing work to update the API. There are currently no timeframes provided for the changes.\n"]]
