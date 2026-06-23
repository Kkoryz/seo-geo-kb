---
title: "An update on the site: operator | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2006/06/update-on-site-operator
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2006-06-02
---

# An update on the site: operator | Google Search Central Blog | Google for Developers

We've fixed the
issue with site: queries
for domains with punctuation in them. We are still working on site: operator queries for domains
that include a trailing slash at the end (such as site:www.example.com/), so you may
get better results for now by omitting the trailing slash in your queries. The
Index Stats page
of Google Sitemaps no longer uses the trailing slash for its queries, so you should see correct
results when using this page.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],[],[],["The core update addresses issues with `site:` queries for domains. A fix was implemented for domains containing punctuation. However, domains with trailing slashes in `site:` queries still pose a problem. Users are advised to omit the trailing slash for improved results. The Index Stats page in Google Sitemaps has been updated to exclude the trailing slash in queries, ensuring more accurate results.\n"]]
