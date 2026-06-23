---
title: "We've fixed an issue with verification files that included leading zeros | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2006/03/weve-fixed-issue-with-verification
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2006-03-03
---

# We've fixed an issue with verification files that included leading zeros | Google Search Central Blog | Google for Developers

We've fixed an issue with verification files that included leading zeros

March 03, 2006

Thank you to our
Google Group
members for finding a bug in the
verification
file logic, which stripped out leading zeros when we accessed the verification file. We've fixed
this. This should have only affected site owners with verification files that had the pattern
google0<unique_string>.html. If your verification file has this pattern and you've
had trouble verifying, please request verification again.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],[],[],["A bug was found and fixed in the Google verification file logic. The bug affected files with leading zeros in their names, specifically those following the pattern `google0\u003cunique_string\u003e.html`. This issue caused verification problems for site owners using such files. Site owners who experienced verification difficulties due to this bug are advised to request verification again, now that the problem has been resolved.\n"]]
