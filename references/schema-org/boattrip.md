---
title: "BoatTrip"
source_url: https://schema.org/BoatTrip
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# BoatTrip

# BoatTrip

A Schema.org Type

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/BoatTrip
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+BoatTrip)

A trip on a commercial ferry line.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[arrivalBoatTerminal](/arrivalBoatTerminal)

[BoatTerminal](/BoatTerminal)```
```[departureBoatTerminal](/departureBoatTerminal)

[BoatTerminal](/BoatTerminal)[Trip](/Trip)

```
```[arrivalTime](/arrivalTime)

[DateTime](/DateTime)or[Time](/Time)```
```[departureTime](/departureTime)

[DateTime](/DateTime)or[Time](/Time)```
```[itinerary](/itinerary)

[ItemList](/ItemList)or[Place](/Place)[Place](/Place)) that make up a trip. For a trip where destination order is important use[ItemList](/ItemList)to specify that order (see examples).```
```[offers](/offers)

[Demand](/Demand)or[Offer](/Offer)[businessFunction](/businessFunction)to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can also be used to describe a[Demand](/Demand). While this property is listed as expected on a number of common types, it can be used in others. In that case, using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.Inverse property:

[itemOffered](/itemOffered)```
```[partOfTrip](/partOfTrip)

[Trip](/Trip)[Trip](/Trip)is a subTrip of another Trip. For example Day 1, Day 2, etc. of a multi-day trip.Inverse property:

[subTrip](/subTrip)```
```[provider](/provider)

[Organization](/Organization)or[Person](/Person)[carrier](/carrier).```
```[subTrip](/subTrip)

[Trip](/Trip)[Trip](/Trip)that is a subTrip of this Trip. For example Day 1, Day 2, etc. of a multi-day trip.Inverse property:

[partOfTrip](/partOfTrip)```
```[tripOrigin](/tripOrigin)

[Place](/Place)[Thing](/Thing)

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

[URL](/URL)#### Source

[https://github.com/schemaorg/schemaorg/issues/1755](https://github.com/schemaorg/schemaorg/issues/1755)
