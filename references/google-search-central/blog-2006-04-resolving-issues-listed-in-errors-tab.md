---
title: "Resolving issues listed in the Errors tab | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2006/04/resolving-issues-listed-in-errors-tab
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2006-04-11
---

# Resolving issues listed in the Errors tab | Google Search Central Blog | Google for Developers

Under the Errors tab, I see a URL listed with a
404 error.
That page doesn't exist on my site and I don't link to it. Why does this show up?
The Errors tab lists both errors we encountered following links in your Sitemap and
errors we had following links during our regular discovery crawl. If we tried to follow the link
from the Sitemap, the URL lists "Sitemap" beside it. If it doesn't list "Sitemap", then we tried
to follow that link from a web page (either on your site or another site). You might double-check
your site and make sure that none of the internal links are pointing to that URL. If they aren't,
then this URL is probably linked from an external page.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],[],[],["The \"Errors\" tab in a webmaster tool displays URLs with 404 errors, either from links in a Sitemap or during regular web crawling. If \"Sitemap\" is listed, the error originated from a Sitemap link. Otherwise, the link was found on a web page, potentially external. Users should check their internal links for incorrect URLs. If no internal links are found, then the problematic link is likely coming from an external source.\n"]]
