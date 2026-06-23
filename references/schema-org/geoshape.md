---
title: "GeoShape"
source_url: https://schema.org/GeoShape
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# GeoShape

# GeoShape

A Schema.org Type

- Canonical URL: https://schema.org/GeoShape
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+GeoShape)

The geographic shape of a place. A GeoShape can be described using several properties whose values are based on latitude/longitude pairs. Either whitespace or commas can be used to separate latitude and longitude; whitespace should be used when writing a list of several such points.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[address](/address)

[PostalAddress](/PostalAddress)or[Text](/Text)```
```[addressCountry](/addressCountry)

[Country](/Country)or[Text](/Text)[ISO 3166-1 alpha-2](http://en.wikipedia.org/wiki/ISO_3166-1)format, for example "US". For backward compatibility, a 3-letter[ISO 3166-1 alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3)country code such as "SGP" or a full country name such as "Singapore" can also be used.```
```[box](/box)

[Text](/Text)```
```[circle](/circle)

[Text](/Text)```
```[elevation](/elevation)

[Number](/Number)or[Text](/Text)[WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System)). Values may be of the form 'NUMBER UNIT_OF_MEASUREMENT' (e.g., '1,000 m', '3,200 ft') while numbers alone should be assumed to be a value in meters.```
```[line](/line)

[Text](/Text)```
```[polygon](/polygon)

[Text](/Text)```
```[postalCode](/postalCode)

[Text](/Text)[Thing](/Thing)

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

[GeoShape](/GeoShape)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[ContactPoint](/ContactPoint)or[DeliveryChargeSpecification](/DeliveryChargeSpecification)or[Demand](/Demand)or[FinancialIncentive](/FinancialIncentive)or[Offer](/Offer)or[Organization](/Organization)or[Service](/Service)[eligibleRegion](/eligibleRegion)

[ActionAccessSpecification](/ActionAccessSpecification)or[DeliveryChargeSpecification](/DeliveryChargeSpecification)or[Demand](/Demand)or[Offer](/Offer)See also

[ineligibleRegion](/ineligibleRegion).[geo](/geo)

[Place](/Place)[ineligibleRegion](/ineligibleRegion)

[ActionAccessSpecification](/ActionAccessSpecification)or[DeliveryChargeSpecification](/DeliveryChargeSpecification)or[Demand](/Demand)or[MediaObject](/MediaObject)or[Offer](/Offer)See also

[eligibleRegion](/eligibleRegion).[serviceArea](/serviceArea)

[ContactPoint](/ContactPoint)or[Organization](/Organization)or[Service](/Service)#### More specific Types

### Acknowledgements

IPTC rNews properties

[rnews.org](http://rnews.org).
