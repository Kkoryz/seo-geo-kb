---
title: "Expanding markup support for Organization details, including Logo structured data | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2023/11/introducing-organization-markup
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2023-11-29
---

# Expanding markup support for Organization details, including Logo structured data | Google Search Central Blog | Google for Developers

Wednesday, November 29, 2023

[Since 2013](/search/blog/2013/05/using-schemaorg-markup-for-organization), Google has
supported logo structured data, which recognizes two

fields: [Organization](https://schema.org/Organization)`logo`

and `url`

. Today we're expanding our support for
organizational information by extracting additional administrative data such as name, address,
contact information, and various business identifiers. You can continue to provide the `logo`

and `url`

fields to specify which image we use as your logo in Google search results.
With this update, Google can make use of this markup in knowledge panels and other visual elements
(such as [attribution](/search/docs/appearance/visual-elements-gallery#attribution)),
which helps users more easily find your organization's details on Google Search.

As part of this expanded support for organizational data, we're merging the logo documentation
into the new [organization](/search/docs/appearance/structured-data/organization)
documentation. The existing logo report in Search Console and
validations in the Rich Results Test are now replaced with more extensive organization
validations in the Rich Results Test.

If you've already added the `logo`

and `url`

fields via organization markup,
there's nothing you need to do and Google still understands your logo markup. We do encourage you
to add the new fields if applicable for your organization.

When you provide additional organization details, your markup can be eligible to be shown on
knowledge panels, such as the [recently announced merchant knowledge panel](https://blog.google/products/shopping/google-merchant-new-features-holiday/).

## Adding support for `Organization`

to the Rich Results Test

You can test your organization structured data using the
[Rich Results Test](https://search.google.com/test/rich-results) by submitting the URL
of a page or a code snippet. Using the tool, you can confirm whether or not your markup is valid
instantly.

If your site is a local business, we recommend you also follow the existing
[local business](/search/docs/appearance/structured-data/local-business) markup
guidelines in addition to the new [organization](/search/docs/appearance/structured-data/organization) markup.
If your site is only an online business, we recommend using the [ OnlineBusiness](https://schema.org/OnlineBusiness)
subtype of

`Organization`

.
We hope these additions make it easier for you to add organization structured data describing your
business or organization, and enable it to be shown on Google knowledge panels. If you have any
questions or concerns, please reach out to us via the
[Google Search Central Community](https://support.google.com/webmasters/threads?thread_filter=(category%3Astructured_data)).
