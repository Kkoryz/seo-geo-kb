---
title: "Bye Bye Preferred Domain setting | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2019/06/bye-bye-preferred-domain-setting
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2019-06-18
---

# Bye Bye Preferred Domain setting | Google Search Central Blog | Google for Developers

As we progress with
the migration
to the new Search Console experience, we will be saying farewell to one of our settings: preferred
domain.

It's common for a website to have the same content on multiple URLs. For example, it might have
the same content on https://example.com/ as on
https://www.example.com/index.html. To make things easier, when our
systems recognize that, we'll pick one URL as the "canonical" for Search. You can still tell us
your preference in multiple ways if there's something specific you want us to pick (see
paragraph below). But if you don't have a preference, we'll choose the best option we find. Note
that with the deprecation we will no longer use any existing Search Console preferred domain
configuration.

You can find detailed explanations on how to tell us your preference in the
Consolidate duplicate URLs
help center article. Here are some of the options available to you:

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],[],[],["The \"preferred domain\" setting in the Search Console is being removed. Websites with duplicate content on multiple URLs will have one URL chosen as the \"canonical\" for search. Users can still indicate their preferred URL using `rel=\"canonical\"` link tags or HTTP headers, sitemaps, or `301` redirects. If no preference is indicated, the system will automatically select the best option. The change means any current preferred domain configurations will be ignored. Feedback can be submitted through Twitter or the forum.\n"]]
