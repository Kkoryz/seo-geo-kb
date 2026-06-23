---
title: "ListItem"
source_url: https://schema.org/ListItem
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# ListItem

# ListItem

A Schema.org Type

- Canonical URL: https://schema.org/ListItem
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+ListItem)

An list item, e.g. a step in a checklist or how-to description.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[item](/item)

[Thing](/Thing)```
```[nextItem](/nextItem)

[ListItem](/ListItem)```
```[position](/position)

[Integer](/Integer)or[Text](/Text)```
```[previousItem](/previousItem)

[ListItem](/ListItem)[Thing](/Thing)

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

[ListItem](/ListItem)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[ItemList](/ItemList)Text values are best if the elements in the list are plain strings. Existing entities are best for a simple, unordered list of existing things in your data. ListItem is used with ordered lists when you want to provide additional context about the element in that list or when the same item might be in different places in different lists.

Note: The order of elements in your mark-up is not sufficient for indicating the order or elements. Use ListItem with a 'position' property in such cases.

[negativeNotes](/negativeNotes)

[Product](/Product)or[Review](/Review)[positiveNotes](/positiveNotes)). For symmetryIn the case of a

[Review](/Review), the property describes the[itemReviewed](/itemReviewed)from the perspective of the review; in the case of a[Product](/Product), the product itself is being described. Since product descriptions tend to emphasise positive claims, it may be relatively unusual to find[negativeNotes](/negativeNotes)used in this way. Nevertheless for the sake of symmetry,[negativeNotes](/negativeNotes)can be used on[Product](/Product).The property values can be expressed either as unstructured text (repeated as necessary), or if ordered, as a list (in which case the most negative is at the beginning of the list).

[nextItem](/nextItem)

[ListItem](/ListItem)[positiveNotes](/positiveNotes)

[Product](/Product)or[Review](/Review)[negativeNotes](/negativeNotes)) pro/con lists for reviews.In the case of a

[Review](/Review), the property describes the[itemReviewed](/itemReviewed)from the perspective of the review; in the case of a[Product](/Product), the product itself is being described.The property values can be expressed either as unstructured text (repeated as necessary), or if ordered, as a list (in which case the most positive is at the beginning of the list).

[previousItem](/previousItem)

[ListItem](/ListItem)#### More specific Types

### Examples

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
