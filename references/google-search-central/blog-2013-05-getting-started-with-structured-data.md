---
title: "Getting started with structured data | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2013/05/getting-started-with-structured-data
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2013-05-30
---

# Getting started with structured data | Google Search Central Blog | Google for Developers

Thursday, May 30, 2013

If Google understands your website's content in a structured way, we can present that content more
accurately and more attractively to Google users. For example, our algorithms can enhance your
search results with
"[rich snippets](/search/docs/appearance/structured-data/intro-structured-data)"
when we understand that your page is a structured product listing, event, recipe, review, or
similar. We can also feature your data in
[Knowledge Graph](https://www.google.com/insidesearch/features/search/knowledge)
panels or in
[Google Now](https://www.google.com/landing/now/)
cards, helping to spread the word about your content.

Today we're excited to announce two features that make it simpler than ever before to participate in structured data features. The first is an expansion of Data Highlighter to seven new types of structured data. The second is a brand new tool, the Structured Data Markup Helper.

## Support for Products, Businesses, Reviews and more in Data Highlighter

[Data Highlighter](https://support.google.com/webmasters/bin/answer.py?answer=2692911)
launched in
[December 2012](/search/blog/2012/12/introducing-data-highlighter-for-event) as a
point-and-click tool for teaching Google the pattern of structured data about
[events](https://schema.org/Event) on your website—without even
having to edit your site's HTML. Now, you can also use Data Highlighter to teach us about many
other kinds of structured data on your site:
[products](https://schema.org/Product),
[local businesses](https://schema.org/LocalBusiness),
[articles](https://schema.org/Article),
[software applications](https://schema.org/SoftwareApplication),
[movies](https://schema.org/Movie),
[restaurants](https://schema.org/Restaurant), and
[TV episodes](https://schema.org/TVEpisode).

To get started, visit
[Webmaster Tools](https://search.google.com/search-console), select
your site, click the "Optimization" link in the left sidebar, and click "Data Highlighter". You'll
be prompted to enter the URL of a typically structured page on your site (for example, a product
or event's detail page) and "tag" its key fields with your mouse.

The tagging process takes about 5 minutes for a single page, or about 15 minutes for a pattern of consistently formatted pages. At the end of the process, you'll have the chance to verify Google's understanding of your structured data and, if it's correct, "publish" it to Google. Then, as your site is recrawled over time, your site will become eligible for enhanced displays of information like prices, reviews, and ratings right in the Google search results.

## New Structured Data Markup Helper tool

While Data Highlighter is a great way to quickly teach Google about your site's structured data
without having to edit your HTML, it's ultimately preferable to embed structured data markup
directly into your web pages, so your structured content is available to everyone. To assist web
authors with that task, we're happy to announce a new tool: the
[Structured Data Markup Helper](https://www.google.com/webmasters/markup-helper/).

Like in Data Highlighter, you start by submitting a web page (URL or HTML source) and using your mouse to "tag" the key properties of the relevant data type. When you're done, the Structured Data Markup Helper generates sample HTML code with microdata markup included. This code can be downloaded and used as a guide as you implement structured data on your website.

The Structured Data Markup Helper supports a subset of data types, including all the types
supported by Data Highlighter as well as several types used for
[embedding structured data in Gmail](/gmail/schemas/embedding-schemas-in-emails).
Consult schema.org for complete schema documentation.

We hope these two tools make it easier for all websites to participate in Google's growing suite
of structured data features! As always, please post in our
[forums](https://support.google.com/webmasters/threads?hl=en&thread_filter=(category:structured_data))
if you have any questions or feedback.
