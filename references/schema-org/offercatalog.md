---
title: "OfferCatalog"
source_url: https://schema.org/OfferCatalog
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# OfferCatalog

# OfferCatalog

A Schema.org Type

- Canonical URL: https://schema.org/OfferCatalog
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+OfferCatalog)

An OfferCatalog is an ItemList that contains related Offers and/or further OfferCatalogs that are offeredBy the same provider.

| Property | Expected Type | Description |
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

[OfferCatalog](/OfferCatalog)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[Organization](/Organization)or[Person](/Person)or[Service](/Service)### Examples

[Example 1](#eg-0396)

Copied

Example notes or example HTML without markup.

ACME Home Cleaning offers a variety of services in Massachusetts, including: <ul> <li>House cleaning</li> <ul> <li>Apartment light cleaning</li> <li>House light cleaning up to 2 bedrooms</li> <li>House light cleaning 3+ bedrooms</li> </ul> <li>One-time services</li> <ul> <li>Window washing</li> <li>Carpet deep cleaning</li> <li>Move in/out cleaning</li> </ul> </ul>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Service"> <meta itemprop="serviceType" content="Home cleaning" /> <span itemprop="provider" itemscope itemtype="https://schema.org/LocalBusiness"> <span itemprop="name">ACME Home Cleaning</span> </span> offers a variety of services in <span itemprop="areaServed" itemscope itemtype="https://schema.org/State"> <span itemprop="name">Massachusetts</span>, including </span> <ul itemprop="hasOfferCatalog" itemscope itemtype="https://schema.org/OfferCatalog"> <li itemprop="itemListElement" itemscope itemtype="https://schema.org/OfferCatalog"> <span itemprop="name">House cleaning</span> <ul itemprop="itemListElement" itemscope itemtype="https://schema.org/OfferCatalog"> <li itemprop="itemListElement" itemscope itemtype="https://schema.org/Offer"> <div itemprop="itemOffered" itemscope itemtype="https://schema.org/Service"> <span itemprop="name">Apartment light cleaning</span> </div> </li> <li itemprop="itemListElement" itemscope itemtype="https://schema.org/Offer"> <div itemprop="itemOffered" itemscope itemtype="https://schema.org/Service"> <span itemprop="name">House light cleaning up to 2 bedrooms</span> </div> </li> <li itemprop="itemListElement" itemscope itemtype="https://schema.org/Offer"> <div itemprop="itemOffered" itemscope itemtype="https://schema.org/Service"> <span itemprop="name">House light cleaning 3+ bedrooms</span> </div> </li> </ul> <li itemprop="itemListElement" itemscope itemtype="https://schema.org/OfferCatalog"> <span itemprop="name">One-time services</span> <ul itemprop="itemListElement" itemscope itemtype="https://schema.org/OfferCatalog"> <li itemprop="itemListElement" itemscope itemtype="https://schema.org/Offer"> <div itemprop="itemOffered" itemscope itemtype="https://schema.org/Service"> <span itemprop="name">Window washing</span> </div> </li> <li itemprop="itemListElement" itemscope itemtype="https://schema.org/Offer"> <div itemprop="itemOffered" itemscope itemtype="https://schema.org/Service"> <span itemprop="name">Carpet deep cleaning</span> </div> </li> <li itemprop="itemListElement" itemscope itemtype="https://schema.org/Offer"> <div itemprop="itemOffered" itemscope itemtype="https://schema.org/Service"> <span itemprop="name">Move in/out cleaning</span> </div> </li> </ul> </li> </ul> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Service"> <meta property="serviceType" content="Home cleaning" /> <span property="provider" typeof="LocalBusiness"> <span property="name">ACME Home Cleaning</span> </span> offers a variety of services in <span property="areaServed" typeof="State"> <span property="name">Massachusetts</span>, including </span> <ul property="hasOfferCatalog" typeof="OfferCatalog"> <li property="itemListElement" typeof="OfferCatalog"> <span property="name">House cleaning</span> <ul property="itemListElement" typeof="OfferCatalog"> <li property="itemListElement" typeof="Offer"> <div property="itemOffered" typeof="Service"> <span property="name">Apartment light cleaning</span> </div> </li> <li property="itemListElement" typeof="Offer"> <div property="itemOffered" typeof="Service"> <span property="name">House light cleaning up to 2 bedrooms</span> </div> </li> <li property="itemListElement" typeof="Offer"> <div property="itemOffered" typeof="Service"> <span property="name">House light cleaning 3+ bedrooms</span> </div> </li> </ul> <li property="itemListElement" typeof="OfferCatalog"> <span property="name">One-time services</span> <ul property="itemListElement" typeof="OfferCatalog"> <li property="itemListElement" typeof="Offer"> <div property="itemOffered" typeof="Service"> <span property="name">Window washing</span> </div> </li> <li property="itemListElement" typeof="Offer"> <div property="itemOffered" typeof="Service"> <span property="name">Carpet deep cleaning</span> </div> </li> <li property="itemListElement" typeof="Offer"> <div property="itemOffered" typeof="Service"> <span property="name">Move in/out cleaning</span> </div> </li> </ul> </li> </ul> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Service", "serviceType": "Weekly home cleaning", "provider": { "@type": "LocalBusiness", "name": "ACME Home Cleaning" }, "areaServed": { "@type": "State", "name": "Massachusetts" }, "hasOfferCatalog": { "@type": "OfferCatalog", "name": "Cleaning services", "itemListElement": [ { "@type": "OfferCatalog", "name": "House Cleaning", "itemListElement": [ { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Apartment light cleaning" } }, { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "House light cleaning up to 2 bedrooms" } }, { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "House light cleaning 3+ bedrooms" } } ] }, { "@type": "OfferCatalog", "name": "One-time services", "itemListElement": [ { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Window washing" } }, { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Carpet cleaning" } }, { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Move in/out cleaning" } } ] } ] } } </script>

Structured representation of the JSON-LD example.
