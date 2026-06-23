---
title: "Taking feeds out of our web search results | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2007/12/taking-feeds-out-of-our-web-search
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2007-12-18
---

# Taking feeds out of our web search results | Google Search Central Blog | Google for Developers

Tuesday, December 18, 2007

As a webmaster, you may have been concerned about your RSS/Atom feeds crowding out their associated HTML pages in Google's search results. By serving feeds, we could cause a poor user experience:

- Feeds increase the likelihood that users see duplicate search results.
- Users clicking on a feed may miss valuable content available only in the HTML page.

To address these concerns, we prevent feeds from being returned in Google's search results, with
the exception of podcasts (feeds with multimedia enclosures). We continue to allow podcasts,
because we noticed a significant number of them are standalone documents (that is, no HTML page
has the same content) or they have more complete item descriptions than the associated HTML page.
However, if, as a webmaster, you'd like your podcasts to be excluded from Google's search results
(for example, if you have a vlog, its feed is probably a podcast), you can use
[Yahoo's spec for noindex feeds](https://publisher.yahoo.com/rss_guide/faq.php).
If you use [FeedBurner](https://www.feedburner.com/), making your
podcast `noindex`

is as simple as checking a box ("Noindex" under the "Publicize" tab).

As a user, you may ask yourself whether Google has a way to search for feeds. The answer is yes;
both [Google Reader](https://www.google.com/reader/) and
[iGoogle](https://www.google.com/ig) allow searching for feeds to
subscribe to.

We're aware that there are a few non-podcast feeds out there with no associated HTML pages, and
thus removing these feeds for now from the search results might be less than ideal. We remain open
to other feedback on how to improve the handling of feeds, and especially welcome your comments
and questions in the
[Crawling, Indexing and Ranking](https://groups.google.com/group/Google_Webmaster_Help-Indexing/topics)
subtopic of our Webmaster Help Group.
