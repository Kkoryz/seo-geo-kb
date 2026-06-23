---
title: "URL Structure Best Practices for Google Search | Google Search Central | Documentation | Google for Developers"
source_url: https://developers.google.com/search/docs/crawling-indexing/url-structure
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2025-12-10
---

# URL Structure Best Practices for Google Search | Google Search Central | Documentation | Google for Developers

# URL structure best practices for Google Search

To make sure Google Search can crawl your site effectively, use a crawlable URL structure that meets the following requirements. If your URLs don't meet the following criteria, Google Search will likely crawl your site inefficiently — including but not limited to extremely high crawl rates, or not at all.

## Requirements for a crawlable URL structure | |||||||
|---|---|---|---|---|---|---|---|
## Follow
|
Google Search supports URLs as defined by
|
||||||
## Don't use URL fragments to change content |
Don't use https://example.com/#/potatoes
If you're using JavaScript to change content, |
||||||
## Use a common encoding for URL parameters |
When specifying URL parameters, use the following common encoding: an equal sign
(
|

## Make it easy to understand your URL structure

To help Google Search (and your users) better understand your site, we recommend creating a simple URL structure, applying the following best practices when possible.

| Best practices | |||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|
## Use descriptive URLs |
When possible, use readable words rather than long ID numbers in your URLs.
|
||||||||||
## Use your audience's language |
Use words in your audience's language in the URL (and, if applicable, transliterated words). For example, if your audience is searching in German, use German words in the URL: https://example.com/ Or if your audience is searching in Japanese, use Japanese words in the URL: https://example.com/ |
||||||||||
## Use percent encoding as necessary |
When
|
||||||||||
## Use hyphens to separate words |
We recommend separating words in your URLs, when possible. Specifically, we recommend using
hyphens (
|
||||||||||
## Use as few parameters as you can |
Whenever possible, shorten URLs by trimming unnecessary parameters (meaning, parameters that don't change the content). | ||||||||||
## Be aware that URLs are case sensitive |
Like any other HTTP client following IETF STD 66, Google Search's URL handling is case
sensitive (for example, Google treats both `/APPLE` and `/apple` as
distinct URLs with their own content). If upper and lower case text in a URL is treated
the same by your web server, convert all text to the same case so it's easier for Google
to determine that URLs reference the same page.
|
||||||||||
## For multi-regional sites |
If your site is multi-regional, consider using a URL structure that makes it easy to
geotarget your site. For more examples of how you can structure your URLs, refer to
Recommended (using a country-specific domain): https://example.de Recommended (using a country-specific subdirectory with gTLD): https://example.com/de/ |

## Avoid common issues related to URLs

Overly complex URLs, especially those containing multiple parameters, can cause problems for crawlers by creating unnecessarily high numbers of URLs that point to identical or similar content on your site. As a result, Googlebot may consume much more bandwidth than necessary, or Google Search may be unable to completely index all the content on your site.

Unnecessarily high numbers of URLs can be caused by a number of issues. These include:

| Common issues | |
|---|---|
## Additive filtering of a set of items |
Many sites provide different views of the same set of items or search results, often allowing the user to filter this set using defined criteria (for example: show me hotels on the beach). When filters can be combined in an additive manner (for example: hotels on the beach and with a fitness center), the number of URLs (views of data) in the sites explodes. Creating a large number of slightly different lists of hotels is redundant, as Googlebot only needs to see a small number of lists from which it can reach the page for each hotel. For example: - Hotel properties at "value rates":
https://example.com/hotel-search-results.jsp?Ne=292&N=461 - Hotel properties at "value rates" on the beach:
https://example.com/hotel-search-results.jsp?Ne=292&N=461+4294967240 - Hotel properties at "value rates" on the beach and with a fitness center:
https://example.com/hotel-search-results.jsp?Ne=292&N=461+4294967240+4294967270
|
## Irrelevant parameters |
Irrelevant parameters in the URL can cause a large number of URLs, such as: - Referral parameters:
https://example.com/search/noheaders?click=6EE2BF1AF6A3D705D5561B7C3564D9C2&clickPage=OPD+Product+Page&cat=79 https://example.com/discuss/showthread.php?referrerid=249406&threadid=535913 https://example.com/products/products.asp?N=200063&Ne=500955&ref=foo%2Cbar&Cn=Accessories - Shopping sorting parameters:
https://example.com/results?search_type=search_videos&search_query=tpb&search_sort=relevance&search_category=25 - Session IDs:
https://example.com/search/noheaders?sessionid=6EE2BF1AF6A3D705D5561B7C3564D9C2
Consider using a |
## Calendar issues |
A dynamically generated calendar might generate links to future and previous dates with no restrictions on start or end dates. For example: https://example.com/calendar.php?d=13&m=8&y=2011
If your site has an infinite calendar, add a |
## Broken relative links |
Placing a
`<a href="../../category/stuff">...</a>` on `https://example.com/category/community/070413/html/FAQ.htm`
may lead to bogus URLs such as `https://example.com/category/community/category/stuff` .
To fix, use root-relative URLs in your links (instead of parent-relative).
|

## Fixing crawling-related URL structure problems

If you notice that Google Search is crawling these problematic URLs, we recommend the following:

- Consider using a
[robots.txt file](/search/docs/crawling-indexing/robots/intro)to block Googlebot's access to[problematic URLs](#common-issues). Typically, consider blocking dynamic URLs, such as URLs that generate search results, or URLs that can create infinite spaces, such as calendars, and ordering and filtering functions. - If your site has faceted navigation, learn how to
[manage crawling of those faceted navigation URLs](/search/docs/crawling-indexing/crawling-managing-faceted-navigation#prevent-crawling-of-faceted-navigation-urls).
