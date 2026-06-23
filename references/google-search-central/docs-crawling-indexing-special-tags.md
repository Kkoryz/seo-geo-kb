---
title: "Meta Tags and Attributes that Google Supports | Google Search Central | Documentation | Google for Developers"
source_url: https://developers.google.com/search/docs/crawling-indexing/special-tags
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2025-12-10
---

# Meta Tags and Attributes that Google Supports | Google Search Central | Documentation | Google for Developers

`meta`

tags and attributes that Google supports

This page explains what `meta`

tags are, which `meta`

tags and HTML
attributes Google supports to control indexing, and other important points to note when
implementing `meta`

tags on your site.

`meta`

tags

`meta`

tags are HTML tags used to provide additional information about a page to
search engines and other clients. Clients process the `meta`

tags and ignore those they don't
support. `meta`

tags are added to the `<head>`

section of
your HTML page and generally look like this:

<!DOCTYPE html> <html> <head><meta charset="utf-8"><meta name="description" content="Author: A.N. Author, Illustrator: P. Picture, Category: Books, Price: £9.24, Length: 784 pages"><meta name="google-site-verification" content="+nxGUDJ4QpAZ5l9Bsjdi102tLVC21AIh5d1Nl23908vVuFHs34="><title>Example Books - high-quality used books for children</title><meta name="robots" content="noindex,nofollow"></head> </html>

Google supports the following `meta`

tags:

List of `meta` tags that Google supports | |
|---|---|
## description |
<meta name="description" content="A description of the page">
|
## robots and googlebot |
<meta name="robots" content="..., ..."> <meta name="googlebot" content="..., ...">
These The In the case of conflicting The default values are You can also specify this information in the header of your pages using the
|
## notranslate |
<meta name="googlebot" content="notranslate">
When Google recognizes that the contents of a page aren't in the language that the
user likely wants to read, Google may provide a |
## nopagereadaloud |
<meta name="google" content="nopagereadaloud"> Prevents various |
## google-site-verification |
<meta name="google-site-verification" content="...">
You can use this tag on the top-level page of your site to |
## Content-Type and charset |
<meta http-equiv="Content-Type" content="...; charset=..."> <meta charset="...">
These tags define the page's content type and character set respectively. Make sure that you
surround the value of the |
## refresh |
<meta http-equiv="refresh" content="...;url=...">
This tag, commonly called meta-refresh, sends the user to a new URL after a certain
amount of time, and is sometimes used as a simple form of redirection. However, it is
|
## viewport |
<meta name="viewport" content="...">
This tag tells the browser how to render a page on a mobile device. Presence of this tag
indicates to Google that the page is mobile friendly.
|
## rating |
<meta name="rating" content="adult"> <meta name="rating" content="RTA-5042-1996-1400-1577-RTA">
Labels a page as containing sexually-explicit adult content, to signal that it be filtered by SafeSearch
results. |


## HTML tag attributes

[HTML tag attributes](https://developer.mozilla.org/docs/Web/HTML/Attributes)
are additional values of HTML tags that configure the parent tag. For example, the
`href`

attribute of the `<a>`

tag configures the resource the anchor
tag points to: `<a `

.
**href="https://example.com/"**...>

Google Search supports a limited number of HTML attributes for indexing purposes. Attributes
like `src`

and `href`

are used for discovering resources such as images
and URLs. Google also supports various
[ rel attributes](/search/docs/crawling-indexing/qualify-outbound-links)
that allow site owners to qualify outbound links.

The
[ data-nosnippet attribute](/search/docs/crawling-indexing/robots-meta-tag#data-nosnippet-attr)
of

`div`

, `span`

, and `section`

tags allow you to exclude
parts of an HTML page from snippets.
## Other points to note

-
Google can read both HTML and XHTML-style
`meta`

tags, regardless of the code used on the page. -
To ensure machine readability, the
`head`

section must be[valid HTML](/search/docs/crawling-indexing/valid-page-metadata)and in case of attributes, all parent tags closed accordingly. -
With the exception of
`google-site-verification`

, letter case is generally not important in`meta`

tags. -
You can use other
`meta`

tags if they are important to your site, but Google will ignore`meta`

tags that it doesn't support. -
If you're considering using JavaScript to inject or change
`meta`

tags, proceed with caution. We recommend that you avoid using JavaScript to inject or change`meta`

tags whenever possible, and if you must use it,[test your implementations](/search/docs/crawling-indexing/javascript/fix-search-javascript)thoroughly. -
To check the
`meta`

tags and attributes on your pages, use the[URL Inspection Tool](https://support.google.com/webmasters/answer/9012289).

## Unsupported tags and attributes

The following tags and attributes aren't supported by Google Search and are ignored. We're including them here because they're either very common in HTML or we used to support them.

| Unsupported tags and attributes | |
|---|---|
| meta-keyword tag |
`<meta name="keywords" content="...">`
The meta-keyword tag is not used by Google Search, and it has no effect on indexing and
ranking at all. |
HTML tag `lang` attributes |
Google Search detects the language of a page
based on the textual content of the page. It doesn't rely on code annotations such as the
`lang` . |
`next` and `prev` `rel` attribute values
|
<link rel="next" href="..."> <link rel="prev" href="...">
Google no longer uses these HTML |
## nositelinkssearchbox |
<meta name="google" content="nositelinkssearchbox">
The |
