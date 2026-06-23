---
title: "Troubleshooting hreflang annotations in Webmaster Tools | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2014/07/troubleshooting-hreflang-annotations-in
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2014-07-14
---

# Troubleshooting hreflang annotations in Webmaster Tools | Google Search Central Blog | Google for Developers

Monday, July 14, 2014

If you are targeting users in more than one country, chances are you already heard about
[ rel-alternate-hreflang](/search/docs/specialty/international/localized-versions).
If you haven't, in short, this annotation enables Google and other search engines to serve the
correct language or regional version of pages to searchers, which can lead to increased user
satisfaction.

Making sure the deployed annotations are usable by search engines can be rather difficult,
especially on sites with many pages, and site owners all around the world haven't been shy
telling us about this. Today we're releasing a feature that should make debugging
`rel-alternate-hreflang`

annotations much easier.

The Language Targeting section in the
[International Targeting](https://www.google.com/webmasters/tools/i18n)
feature enables you to identify two of the most common issues with `hreflang`

annotations:

-
Missing return links: annotations must be confirmed from the pages they are pointing to. If page A links to page B, page B must link back to page A, otherwise the annotations may not be interpreted correctly.

For each error of this kind we report where and when we detected them, as well as where the return link is expected to be.

-
Incorrect

`hreflang`

values: The value of the`hreflang`

attribute must either be a language code in[ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)format such as`es`

, or a combination of language and country code such as`es-AR`

, where the country code is in[ISO 3166-1 Alpha 2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)format.In case our indexing systems detect language or country codes that are not in these formats, we provide example URLs to help you fix them.


Additionally, we've moved the
[geographic targeting](https://support.google.com/webmasters/answer/62399)
setting to this part of Webmaster Tools, so that you can find all information relevant to
international and multilingual targeting in the same place.

We hope you'll find this new feature useful and that it helps you to identify issues with the
`rel-hreflang-implementation`

on your site. If you have comments or questions about the
feature, please post in our
[Webmaster Help Forum](https://support.google.com/webmasters/go/community).
