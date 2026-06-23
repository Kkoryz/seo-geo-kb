---
title: "BreadcrumbList"
source_url: https://schema.org/BreadcrumbList
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# BreadcrumbList

# BreadcrumbList

A Schema.org Type

- Canonical URL: https://schema.org/BreadcrumbList
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+BreadcrumbList)

A BreadcrumbList is an ItemList consisting of a chain of linked Web pages, typically described using at least their URL and their name, and typically ending with the current page.


The

The

[position](/position)property is used to reconstruct the order of the items in a BreadcrumbList. The convention is that a breadcrumb list has an[itemListOrder](/itemListOrder)of[ItemListOrderAscending](/ItemListOrderAscending)(lower values listed first), and that the first items in this list correspond to the "top" or beginning of the breadcrumb trail, e.g. with a site or section homepage. The specific values of 'position' are not assigned meaning for a BreadcrumbList, but they should be integers, e.g. beginning with '1' for the first item in the list.| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[aggregateElement](/aggregateElement)

[Thing](/Thing)```
```[itemListElement](/itemListElement)

[ListItem](/ListItem)or[Text](/Text)or[Thing](/Thing)Text values are best if the elements in the list are plain strings. Existing entities are best for a simple, unordered list of existing things in your data. ListItem is used with ordered lists when you want to provide additional context about the element in that list or when the same item might be in different places in different lists.

Note: The order of elements in your mark-up is not sufficient for indicating the order or elements. Use ListItem with a 'position' property in such cases.

```
```[itemListOrder](/itemListOrder)

[ItemListOrderType](/ItemListOrderType)or[Text](/Text)```
```[numberOfItems](/numberOfItems)

[Integer](/Integer)[Thing](/Thing)

```
```[additionalType](/additionalType)

[Text](/Text)or[URL](/URL)[style guide](https://schema.org/docs/styleguide.html).```
```[alternateName](/alternateName)

[Text](/Text)```
```[description](/description)

[Text](/Text)or[TextObject](/TextObject)```
```[disambiguatingDescription](/disambiguatingDescription)

[Text](/Text)```
```[identifier](/identifier)

[PropertyValue](/PropertyValue)or[Text](/Text)or[URL](/URL)[Thing](/Thing), such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links. See[background notes](/docs/datamodel.html#identifierBg)for more details.```
```[image](/image)

[ImageObject](/ImageObject)or[URL](/URL)[URL](/URL)or a fully described[ImageObject](/ImageObject).```
```[mainEntityOfPage](/mainEntityOfPage)

[CreativeWork](/CreativeWork)or[URL](/URL)[background notes](/docs/datamodel.html#mainEntityBackground)for details.Inverse property:

[mainEntity](/mainEntity)```
```[name](/name)

[Text](/Text)```
```[owner](/owner)

[Organization](/Organization)or[Person](/Person)Inverse property:

[owns](/owns)```
```[potentialAction](/potentialAction)

[Action](/Action)```
```[sameAs](/sameAs)

[URL](/URL)```
```[subjectOf](/subjectOf)

[CreativeWork](/CreativeWork)or[Event](/Event)Inverse property:

[about](/about)```
```[url](/url)

[URL](/URL)Instances of

[BreadcrumbList](/BreadcrumbList)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[WebPage](/WebPage)### Examples

[Example 1](#eg-0377)

Copied

Example notes or example HTML without markup.

<ol> <li> <a href="https://example.com/dresses">Dresses</a> </li> <li> <a href="https://example.com/dresses/real">Real Dresses</a> </li> </ol>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<ol itemscope itemtype="https://schema.org/BreadcrumbList"> <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem"> <a itemprop="item" href="https://example.com/dresses"> <span itemprop="name">Dresses</span></a> <meta itemprop="position" content="1" /> </li> <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem"> <a itemprop="item" href="https://example.com/dresses/real"> <span itemprop="name">Real Dresses</span></a> <meta itemprop="position" content="2" /> </li> </ol>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<ol vocab="https://schema.org/" typeof="BreadcrumbList"> <li property="itemListElement" typeof="ListItem"> <a property="item" typeof="WebPage" href="https://example.com/dresses"> <span property="name">Dresses</span></a> <meta property="position" content="1"> </li> <li property="itemListElement" typeof="ListItem"> <a property="item" typeof="WebPage" href="https://example.com/dresses/real"> <span property="name">Real Dresses</span></a> <meta property="position" content="2"> </li> </ol>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [ { "@type": "ListItem", "position": 1, "item": { "@id": "https://example.com/dresses", "name": "Dresses" } }, { "@type": "ListItem", "position": 2, "item": { "@id": "https://example.com/dresses/real", "name": "Real Dresses" } } ] } </script>

Structured representation of the JSON-LD example.
