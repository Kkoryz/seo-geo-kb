---
title: "MonetaryGrant"
source_url: https://schema.org/MonetaryGrant
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# MonetaryGrant

# MonetaryGrant

A Schema.org Type

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/MonetaryGrant
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+MonetaryGrant)

A monetary grant.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[amount](/amount)

[MonetaryAmount](/MonetaryAmount)or[Number](/Number)```
```[funder](/funder)

[Organization](/Organization)or[Person](/Person)[Grant](/Grant)

```
```[fundedItem](/fundedItem)

[BioChemEntity](/BioChemEntity)or[CreativeWork](/CreativeWork)or[Event](/Event)or[MedicalEntity](/MedicalEntity)or[Organization](/Organization)or[Person](/Person)or[Product](/Product)[Grant](/Grant). See also[ownershipFundingInfo](/ownershipFundingInfo).Inverse property:

[funding](/funding)```
```[funder](/funder)

[Organization](/Organization)or[Person](/Person)```
```[sponsor](/sponsor)

[Organization](/Organization)or[Person](/Person)[Thing](/Thing)

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

[https://schema.org/docs/collab/FundInfoCollab](https://schema.org/docs/collab/FundInfoCollab)

[https://github.com/schemaorg/schemaorg/issues/383](https://github.com/schemaorg/schemaorg/issues/383)

### Examples

[Example 1](#eg-0311)

Copied

Example notes or example HTML without markup.

Showning a dataset as output of NSF funding, Page for grant:

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "MonetaryGrant", "identifier": "1448821", "url": "https://www.nsf.gov/awardsearch/showAward?AWD_ID=1448821&HistoricalAwards=false", "name": "Making Data Count: Developing a Data Metrics Pilot", "funder": { "@type": "Organization", "name": "National Science Foundation", "identifier": "https://doi.org/10.13039/100000001" }, "fundedItem": { "@type": ["Article", "Event"], "identifier": "https://doi.org/10.1038/sdata.2015.39", "name": "Making data count", "startDate": "2014-09-01", "endDate": "2016-02-29" } } </script>

Structured representation of the JSON-LD example.
