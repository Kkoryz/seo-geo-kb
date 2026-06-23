---
title: "Holiday source code maintenance: Website clinic for non-profits | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2010/12/holiday-source-code-housekeeping
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2010-12-21
---

# Holiday source code maintenance: Website clinic for non-profits | Google Search Central Blog | Google for Developers

Tuesday, December 21, 2010

*
Cross-posted on the
Google Grants Blog
*

As the holiday season comes around, we all have a bit of maintenance to do. This is precisely why
we wanted to focus the second post in our
[site clinic series](/search/blog/2010/12/helping-holiday-hand-website-clinic-for)
on cleaning up your source code. Throughout our analysis of submitted non-profit websites, we
noticed some confusion about what HTML markup, or tags, to use where, and what content to place
within them, both of which could have significant impact on users and how your website looks on
the search results page.

## Before you deck the halls, deck out your `<title>`

elements

**Out of all the submitted non-profit websites, 27% were misusing their**

`<title>`

elements, which are critical in letting both Google and users know what's important to your
website. Typically, a search engine will display ~60 characters from your title element; this
is valuable real estate, so you should use it! Before getting into the actual code, let's first
take a look at how a great title element from one of our submitted sites,
[Sharp](https://www.sharp.com/index.cfm), will appear in the search results page:
Ideally, a great `<title>`

element will include the name of the organization,
along with a descriptive tag line. Let's take a look at some submitted examples:

| Organization | `<title>` source code |
User Friendliness | Tag Behavior |
|
|

`<title>Top San Diego Doctors and Hospitals - Sharp HealthCare</title>`

[Interieur](https://www.interieur.be/)`<title>Interieur 2010 - 15-24 October Kortrijk, Belgium</title>`

[VAMS International](https://www.vamsinternational.org/)`<title>Visual Arts and Music for Society | VAMS International</title>`

If you don't specify a `<title>`

tag, then Google will try to create a title for
you. You can probably do better than our best guess, so go for it: take control of your
`<title>`

tag! It's a simple fix that can make a huge difference. Using specific
`<title>`

tags for your deeper URLs is also important, and we'll address that in
our next site clinic post.

## Keep an eye on your description `meta`

tags

[Description meta tags](/search/blog/2007/09/improve-snippets-with-meta-description)
weren't being utilized to their full potential in 54% of submitted sites. These tags are often
used to populate the two-line snippet provided to users in the search results page. With a
solid snippet, you can get your potential readers excited and ready to learn more about your
organization. Let's take another look at a good example from among the submitted sites,

[Tales of Aussie Rescue](https://www.aussierescueil.com/):

If description `meta`

tags are absent or not relevant, a snippet will be chosen from the page's
content automatically. If you're lucky and have a good snippet auto-selected, keep in mind
that search engines vary in the way that they select snippets, so it's better to keep things
consistent and relevant by writing a solid description `meta`

tag.

## Keep your `<h>`

elements in their place

Another quick fix is to assure your website makes proper use of heading
tags. In our non-profit study, nearly 19% of submitted sites had room for improvement with
heading elements. The most common problem in heading tags was the tendency to initiate
headers with an `<h2>`

or `<h3>`

tag while not including an
`<h1>`

tag, presumably for aesthetic reasons.

Headings give you the opportunity to tell both Google and users what's important to you and
your website. The lower the number on your heading tag, the more important the text, in the
eyes of Google and your users. Take advantage of that `<h1>`

tag! If you don't
like how an `<h1>`

tag is rendered visually, you can always alter its appearance
in your CSS.

## Use alt text for images

Everyone is always proud to display their family photos come holiday season, but don't forget to tell us what they're all about. Over 37% of analyzed sites were not making appropriate use of the image alt attribute. If used properly, this attribute can:

- Help Google understand what your image is
- Allow users on text-only browsers, with accessibility problems, or on limited devices to understand your images

Keep in mind, rich and descriptive alt text is the key here. Let's take another look at some of our submitted sites and their alt attribute usage:

| Organization | Source Code | User Friendliness | Tag Behavior |
|
|

`<img alt="Sponsor a Puppy logo" src="..." />`

[Philanthropedia](https://www.myphilanthropedia.org/)`<img alt="Logo" height="..." />`

[Coastal Community Foundation](https://www.coastalcommunityfoundation.org/)`<img src="..." />`

## A little window shopping for your New Year's resolution

Google has some great resources to further address best practices in your source code. For
starters, you can use our
[HTML Suggestion Tool](https://www.google.com/support/webmasters/bin/answer.py?answer=80407)
in Webmaster Tools. Also, it's always a good practice to make your site
[accessible](https://www.google.com/accessibility/) to all viewers.
