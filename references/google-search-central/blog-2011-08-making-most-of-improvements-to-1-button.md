---
title: "Making the most of improvements to the +1 button | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2011/08/making-most-of-improvements-to-1-button
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2011-08-24
---

# Making the most of improvements to the +1 button | Google Search Central Blog | Google for Developers

Wednesday, August 24, 2011

For the past few months,
[you might have used +1 buttons](https://googleblog.blogspot.com/2011/06/1-button-for-websites-recommend-content)
to help visitors recommend your content on Google Search and on their Google Profiles. We've
just announced
[a few changes](https://googleblog.blogspot.com/2011/08/doing-more-with-1-button-more-than-4)
that make +1 even more useful.

First, the +1 button now lets visitors share links to your pages on Google+. If someone wants to start a conversation about your content, it's easy for them to do so. Second, you can use +Snippets to customize the name, image and description that appear when your content is shared. Finally, new inline annotations help increase engagement after users see a friend's recommendation right on your page.

Here are a couple of tips to help you take full advantage of these improvements:

## +Snippets

The +1 button opens up your site to a valuable new source of traffic with sharing on Google+. +Snippets let you put your best face forward by customizing exactly what appears when your content is shared.

For example, if you're running a movie review site, you might want visitors to share posts containing the title, movie poster, and a brief synopsis:

You
[may already be using](https://googleblog.blogspot.com/2011/06/introducing-schemaorg-search-engines)
this markup to build rich annotations for your pages on Google Search. If not, marking up your
pages is simple. Just add the correct
[schema.org](https://schema.org/) attributes to the data already
present on your pages. You'll set a name, image, and description in your code:

<bodyitemscope itemtype="https://schema.org/Article"> <h1itemprop="name">This is the article name</h1> <imgitemprop="image"src="thumbnail.jpg" /> <pitemprop="description">This is the description of the article.</p> </body>

For more details on alternate markup types, please see our
[technical documentation](https://code.google.com/apis/+1button/#plus-snippet).

## Inline annotations

Now, when a person visits a page that someone they know has +1'd, they can see a name and face reminding them to pay special attention to your content. Here's how it looks:

To add inline annotations, you need to update your +1 button code. Visit the
[configuration tool](https://www.google.com/webmasters/+1/button/),
select 'inline' from the 'Annotation' menu, and grab a new snippet of code.

Both sharing from +1 and inline annotations are rolling out fully over the next few days. To test
these improvements right now, join our
[Platform Preview group](https://www.google.com/+/learnmore/platform-preview/).
