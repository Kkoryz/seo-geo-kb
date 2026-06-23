---
title: "Index Coverage Data Improvements | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2021/01/index-coverage-data-improvements
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2021-01-11
---

# Index Coverage Data Improvements | Google Search Central Blog | Google for Developers

Monday, January 11, 2021

Helping people understand how Google crawls and indexes their sites has been one of the main objectives of Search Console since its
[early days](/search/blog/2005/11/more-stats). When we launched the
[new Search Console](/search/blog/2018/01/introducing-new-search-console), we also introduced the
[Index Coverage report](https://support.google.com/webmasters/answer/7440203), which shows the indexing state of URLs
that Google has visited, or tried to visit, in your property.

Based on the feedback we got from the community, today we are rolling out significant improvements to this report so you’re better informed on issues that might prevent Google from crawling and indexing your pages. The change is focused on providing a more accurate state to existing issues, which should help you solve them more easily. The list of changes include:

- Removal of the generic "crawl anomaly" issue type - all crawls errors should now be mapped to an issue with a finer resolution.
- Pages that were submitted but blocked by robots.txt and got indexed are now reported as "indexed but blocked" (warning) instead of "submitted but blocked" (error)
- Addition of a new issue: "
[indexed without content](https://support.google.com/webmasters/answer/7440203#indexed_no_content)" (warning) `Soft 404`

reporting is now more accurate

The changes above are now reflected in the index coverage report so you may see new types of issues or changes in counts of issues. We hope that
this change will help you better understand how [we crawl and index](https://www.google.com/search/howsearchworks/crawling-indexing/) your site.

Please share your feedback about the report through the [Search Central Help Community](https://support.google.com/webmasters/community)
or via [Twitter](https://twitter.com/googlesearchc).
