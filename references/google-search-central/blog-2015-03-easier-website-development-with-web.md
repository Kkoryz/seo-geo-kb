---
title: "Easier website development with Web Components and JSON-LD | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2015/03/easier-website-development-with-web
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2015-03-09
---

# Easier website development with Web Components and JSON-LD | Google Search Central Blog | Google for Developers

Monday, March 09, 2015

[JSON-LD](https://www.w3.org/TR/json-ld/) is a JSON-based data format
that can be used to implement
[structured data](/search/docs/appearance/structured-data/intro-structured-data)
describing content on your site to Google and other search engines. For example, if you have a
list of events, cafes, people or more, you can include this data in your pages in a structured way
using the [schema.org](https://schema.org/) vocabulary embedded in
webpages as a JSON-LD snippet. The structured data helps Google understand your pages better and
highlight your content in search features, such
[events in the Knowledge Graph](/search/docs/appearance/structured-data/event)
and
[rich snippets](/search/docs/appearance/structured-data/search-gallery).

[Web Components](https://webcomponents.org/) are a nascent set of
technologies to define custom, reusable user interface widgets and their behavior. Any web
developer can build a Web Component. You start by defining a
[template](https://webcomponents.org/articles/introduction-to-template-element/)
for a distinct part of the user interface, which you
[import into the pages](https://webcomponents.org/articles/introduction-to-html-imports/)
on which you want to use the Web Component. A
[Custom Element](https://webcomponents.org/articles/introduction-to-custom-elements/)
is used to define the behavior of the Web Component. Because you're bundling the display and logic
for part of the user interface into the Web Component, you can share and reuse the bundle on other
pages and with other developers, thus simplifying web development.

JSON-LD and Web Components work really well together. The Custom Element functions as the
presentation layer and the JSON-LD functions as the data layer that the custom element and search
engines consume. This means you can build custom elements for any schema.org type, such as
[ Event](https://schema.org/Event) and

[.](https://schema.org/LocalBusiness)

`LocalBusiness`

Your architecture would then look like this. Your structured data is stored in your database, for example, the store locations in your chain. This data is embedded into your webpage as a JSON-LD snippet, which means it's available to be consumed by the Custom Element to display to a human visitor and for Googlebot to retrieve for Google indexing.

To learn more and get started with your own custom elements, please see:

-
Our latest article on
[HTML5 Rocks](https://updates.html5rocks.com/2015/03/creating-semantic-sites-with-web-components-and-jsonld)and[the accompanying code examples](https://github.com/PolymerLabs/structured-data-web-components). -
The
[JSON-LD website](https://json-ld.org/), and[the W3C spec](https://www.w3.org/TR/json-ld/) -
[Web Components wiki](https://www.w3.org/wiki/WebComponents/)and the Web Components community on[webcomponents.org](https://webcomponents.org/) [schema.org](https://schema.org)-
Google's
[structured data documentation](/search/docs/appearance/structured-data/intro-structured-data)
