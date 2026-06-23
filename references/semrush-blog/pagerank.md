---
title: "Google PageRank in 2025: What Google Search Leak Reveals"
source_url: https://www.semrush.com/blog/pagerank/
category: semrush-blog
section: "Semrush blog — SEO/GEO methodology"
date: 2020-06-17
---

# Google PageRank in 2025: What Google Search Leak Reveals

PageRank is one of Google’s oldest algorithms. Larry Page and Sergey Brin developed it in 1996 during a college research project. PageRank remains important today and plays a key role in SEO.

In this article, learn how PageRank works and how to use that knowledge to improve SEO results.

Let’s start with the basics.

## What Is PageRank?

PageRank is a Google algorithm that measures webpage importance based on the quality and quantity of incoming links. PageRank treats these links as votes. Pages with more high-quality links are considered more important in ranking search results.

PageRank was designed to:

**Identify valuable content**: It determines which pages are most useful and relevant based on links from reputable sites**Reward sites that have natural, high-quality backlinks**: Pages earning links from trusted, authoritative sources rank higher**Discourage link manipulation**: By valuing link quality, PageRank makes it harder to artificially boost rankings**Organize web content by relevance and authority**: It creates a hierarchy that helps Google see which pages are most authoritative on specific topics

Previously, Google assigned a public PageRank score (PR0 to PR10) to every webpage. SEOs could see those scores via the Google Toolbar.

PageRank used a logarithmic scale, possibly with a base of five. Each increase represents a multiple increase in importance.

For example, a PR4 page could be 25 times more important than a PR2 page. Google retired the toolbar in 2016 because SEOs became too focused on the metric. However, the PageRank algorithm remains important.

## How Does PageRank Work?

PageRank works by measuring webpage importance based on incoming links—and the credibility of the source providing those links. This ranking authority transfer is sometimes called “link juice” by SEOs.

When Google’s founders created the algorithm, they treated links as signals of trust and authority. Not all votes are equal. A link from a page with higher authority is stronger than a link from a lower-authority page. Also, a page linking to many different sites can dilute its link authority.

## History of Google PageRank

**April 1, 1998**: Larry Page and Sergey Brin publish “[The Anatomy of a Large-Scale Hypertextual Web Search Engine](http://infolab.stanford.edu/~backrub/google.html)”**September 1, 1998**:[First PageRank patent](https://patents.google.com/patent/US6285999B1/en)is filed**September 4, 1998**: Google is incorporated**December 11, 2000**: Google launches the[Google Toolbar](http://googlepress.blogspot.com/2000/12/google-launches-google-toolbar.html)**June 17, 2004**: Google files the[“reasonable surfer” patent](https://patents.google.com/patent/US7716225B1/en)**October 12, 2006**: Google files its[“seed sets” patent](https://patents.google.com/patent/US9165040B1/en)**March 8, 2016**: Google announces the retirement of Google Toolbar**March 27, 2024**: Leaked Google search API documents reveal PageRank is still used internally

### PageRank Is Born

Larry Page and Sergey Brin developed PageRank based on ranking web information by link popularity. They filed the [first PageRank patent](https://patents.google.com/patent/US6285999B1/en) in September 1998. It became Google’s original method to calculate a webpage’s importance.

Their paper noted that “the citation (link) graph of the web is an important resource that has largely gone unused in existing web search engines.” This concept made Google unique.

### The Introduction of the Google Toolbar

Google launched the Google Toolbar in 2000. It showed each page’s PageRank score. SEOs began chasing high PageRank links. This led to widespread link manipulation, with paid and unnatural links.

### An Updated PageRank Patent

The original PageRank patent expired in 2018. Around that time, a [former Google employee said](https://news.ycombinator.com/item?id=20440079) the original algorithm hadn’t been used since 2006.

But a [2006 patent](https://patents.google.com/patent/US9165040B1/en) about “seed sites in the trusted seed sets” seemed to replace it. These high-quality “seed” sites provide good connectivity to other sites, such as The New York Times.

The new patent assigns a ranking score based on how far a page is from these seed sites. The patent does not explicitly say it is an updated version of PageRank. However, the SEO community believes it acts as a PageRank modifier based on distance from trusted sites.

### Google Retires the Toolbar

Google stopped updating PageRank scores in December 2013 and retired the toolbar in 2016. Without a public score, SEOs had less insight into a webpage’s authority. This made it harder to manipulate PageRank.

### Google’s Internal Document Leak Referencing PageRank

In March 2024, leaked internal Google API documents showed multiple PageRank versions still in use. While the exact functions are unknown, the evidence shows that Google continues to consider link importance. These versions include:

**RawPageRank:**Likely the basic calculation of a page’s importance based on links**PageRank2:**An updated version (differences not specified)**PageRank_NS (nearest seed):**Possibly helps identify content relationships and low-quality pages**FirstCoveragePageRank:**A PageRank value when Google first discovers a page

A website’s homepage PageRank can boost the authority of all its internal pages. Even though public scores are gone, PageRank principles continue to guide how Google evaluates websites.

## Factors That Influenced PageRank

Not all links are equal. Several factors have influenced PageRank historically. These factors also matter for SEO today.

### Anchor Text

[Anchor text](https://www.semrush.com/blog/anchor-text/) is the clickable text of a link.

In early Google algorithms, anchor text strongly influenced rankings. SEOs raced to get as many exact-match anchor text links as possible from high-PageRank pages.

Today, Google views anchor text manipulation as link spam and can penalize it. To see the anchor texts linking to your domain, use Semrush’s [Backlinks](https://www.semrush.com/analytics/backlinks/).

Open the tool, enter your domain, and click “**Analyze**.”

Go to the “**Anchors**” tab.

You’ll see the list of anchor texts sorted by popularity. Anchor text used in the most backlinks is at the top.

In many cases, varied anchor text is best. Avoid manipulative link building.

### The Likelihood of a Link Being Clicked

Links that are more likely to be clicked carry more PageRank weight.

The original PageRank algorithm gave equal weight to all links. Later, the [“reasonable surfer” patent](https://patents.google.com/patent/US7716225B1/en) introduced the concept that not all links are equally likely to be clicked. Links in prominent areas of a page carry more weight than links in footers or banner ads.

### Internal Links

[Internal links](https://www.semrush.com/blog/internal-links/) connect pages on your own site.

They help PageRank flow from one page to another. This flow can raise the authority of [orphaned pages](https://www.semrush.com/blog/orphan-pages/) (pages with no inbound internal links).

### Nofollow Links

[Nofollow links](https://www.semrush.com/blog/nofollow-links/) contain the rel=”nofollow” attribute. They look like this:

`<a href="https://website.com/" rel="nofollow">Click this link</a>`

Originally, these didn’t pass PageRank. SEOs used nofollow to control PageRank flow, a practice called “PageRank sculpting.” [Google’s Matt Cutts stated](https://www.mattcutts.com/blog/pagerank-sculpting/) in 2009 that PageRank sculpting doesn’t work because the presence of nofollow links still dilutes authority.

Later, [Google changed nofollow](https://developers.google.com/search/blog/2019/09/evolving-nofollow-new-ways-to-identify) to a “hint.” Sometimes, Google may pass PageRank through these links.

Learn more about [nofollow, sponsored, and UGC links](https://www.semrush.com/blog/dofollow-link/).

## Why PageRank Still Matters

Multiple sources confirm that PageRank remains relevant. In 2017, Google’s Gary Illyes [confirmed on X](https://twitter.com/methode/status/829755916895535104) (formerly Twitter) that the algorithm still uses PageRank.

The 2024 leak further proves this, showing multiple modern PageRank versions.

PageRank helps Google:

- Assess webpage authority and relevance
- Evaluate link value
- Understand how information flows through a site’s structure

Knowing how PageRank works can help you improve visibility by creating link-worthy content and using strategic internal linking.

## Does a Replacement PageRank Metric Exist?

Google does not offer a public PageRank metric. Semrush’s [Authority Score](https://www.semrush.com/blog/semrush-authority-score-explained/) is an alternative. It runs from 0 to 100 and reflects:

**Link power**: Quantity and quality of backlinks**Organic traffic**: Estimated monthly average**Spam factors**: Indicators of a spammy or natural link profile

Authority Score is not a direct substitute for PageRank, but it can show site quality and potential ranking power.

Using Semrush’s [Backlink Audit](https://www.semrush.com/backlink_audit/), you can monitor your Authority Score and backlink profile:

Open the tool, enter your domain, and click "**Start Backlink Audit**."

Once setup is complete, the “Overview” tab shows your Authority Score and its trend.

Use the “**Audit**” report to review the backlinks you’ve received.

Compare your score to competitors with Semrush’s [Backlinks](https://www.semrush.com/analytics/backlinks/).

Just enter a competitor’s domain and click “**Analyze**.”

Add up to four competitors to compare their Authority Scores and access other helpful metrics.

### Start Improving Your PageRank

Improving internal links and earning high-quality backlinks are strong ways to improve your PageRank. Potential [link building strategies](https://www.semrush.com/blog/link-building-strategies/) include:

**Outreach**: Share your content with relevant publishers**Broken link building**: Find broken backlinks and offer your content as a replacement**Guest blogging**: Write high-quality posts for reputable sites (be aware that not all sites let you link back to your own website and many that do use nofollow attributes)

To streamline your link building, try Semrush’s [Link Building Tool](https://www.semrush.com/link_building/). It analyzes your competitors to find link opportunities and helps manage outreach.
