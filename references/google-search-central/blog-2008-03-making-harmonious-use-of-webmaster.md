---
title: "Making harmonious use of Webmaster Tools and Analytics | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2008/03/making-harmonious-use-of-webmaster
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2008-04-01
---

# Making harmonious use of Webmaster Tools and Analytics | Google Search Central Blog | Google for Developers

Tuesday, April 01, 2008

Occasionally in the
[discussion group](https://support.google.com/webmasters/community),
webmasters ask, "Should I be using Google Webmaster Tools or Google Analytics?" Our answer is:
use both! Here are three scenarios that really highlight the power of both tools.

## Make the most of your impressions

One of my favorite features of Webmaster Tools is that it will show you the Top 20 search queries
your site appeared for along with the Top 20 clicked queries. The data from the
[Top Search Queries](https://www.google.com/support/webmasters/bin/answer.py?answer=35252)
allows you to quickly pinpoint what searches your site appears for and which of those searches
are resulting in clicks. Let's look at last week's data for www.google.com/webmasters as an
example.

As you can see, Google Webmaster Central is receiving a great number of impressions for the query
"gadgets" but may not be fully capitalizing on these impressions with
user clicks. Click on "gadgets" to see how your site appears in our
search results. Does your title and snippet look appealing to users? As my colleague Michael
recently wrote, it might be time to do some
"[maintenance](/search/blog/2008/03/good-housekeeping)" on your website—it's a
great, low-to-no-cost way to catch the attention of your users. For example, we could
[work to improve our snippet](/search/blog/2007/09/improve-snippets-with-meta-description)
from:

To something more readable such as "Use gadgets to easily add cool, dynamic content to your site..." by adding a meta description to the URL.

And what are users doing when they visit your site? Are they browsing your content or bouncing
off your site quickly? To find out, Google Analytics will calculate your site's "bounce rate," or
the percentage of single-page visits (for example, someone just visiting your home page and then
leaving). This can be a helpful measure of the quality of your site's landing page and the traffic
your site receives. After all, once you've worked hard to get your users to visit your site, you
want to keep them there! Check out the Analytics blog for further information about
"[bounce rate](https://analytics.blogspot.com/2007/06/tip-evaluate-your-sources-and-your-site)."

## Perform smart geo-targeting

Let's imagine you have a .com that you want to target at a Japanese market. Webmaster Tools allows
you to
[set a geographic target](https://www.google.com/support/webmasters/bin/answer.py?answer=62399)
for your site, where you would probably pick Japan. But, doing so is not an immediate solution.
You can confirm the location of your visitors using the map overlay of Analytics, right up to the
city level. You can also discover what types of users are accessing your site—including
their browser and connection speed. If users cannot access your website due to an incompatible
browser or slower connection speeds, you may need to rethink your website's design. Doing so can
go a long way toward achieving the level of relevant traffic you would like.

## Control access to sensitive content

One day, you log into Analytics and look at your "Content by Title" data. You shockingly discover
that users are visiting your `/privatedata`

pages. Have no fear! Go into Webmaster
Tools and use the
[URL removal tool](https://www.google.com/support/webmasters/bin/answer.py?answer=61062)
to remove those pages from Google's search results. Modifying your robots.txt file will also block
Googlebot from crawling that section of your site in the future.

For more tips and tricks on Analytics, check out the
[Analytics Help Center](https://www.google.com/support/googleanalytics/).
If you have any more suggestions, you can post in our
[Webmaster Help Group](https://support.google.com/webmasters/community).
