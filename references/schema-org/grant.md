---
title: "Grant"
source_url: https://schema.org/Grant
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# Grant

# Grant

A Schema.org Type

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/Grant
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+Grant)

A grant, typically financial or otherwise quantifiable, of resources. Typically a


Grants support activities directed towards some agreed collective goals, often but not always organized as


The amount of a

[funder](/funder)sponsors some[MonetaryAmount](/MonetaryAmount)to an[Organization](/Organization)or[Person](/Person), sometimes not necessarily via a dedicated or long-lived[Project](/Project), resulting in one or more outputs, or[fundedItem](/fundedItem)s. For financial sponsorship, indicate the[funder](/funder)of a[MonetaryGrant](/MonetaryGrant). For non-financial support, indicate[sponsor](/sponsor)of[Grant](/Grant)s of resources (e.g. office space).Grants support activities directed towards some agreed collective goals, often but not always organized as

[Project](/Project)s. Long-lived projects are sometimes sponsored by a variety of grants over time, but it is also common for a project to be associated with a single grant.The amount of a

[Grant](/Grant)is represented using[amount](/amount)as a[MonetaryAmount](/MonetaryAmount).| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

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

[URL](/URL)Instances of

[Grant](/Grant)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[BioChemEntity](/BioChemEntity)or[CreativeWork](/CreativeWork)or[Event](/Event)or[MedicalEntity](/MedicalEntity)or[Organization](/Organization)or[Person](/Person)or[Product](/Product)[Grant](/Grant)that directly or indirectly provide funding or sponsorship for this item. See also[ownershipFundingInfo](/ownershipFundingInfo).#### More specific Types

#### Source

[https://schema.org/docs/collab/FundInfoCollab](https://schema.org/docs/collab/FundInfoCollab)

[https://github.com/schemaorg/schemaorg/issues/383](https://github.com/schemaorg/schemaorg/issues/383)

### Examples

[Example 1](#eg-0309)

Copied

Example notes or example HTML without markup.

Basic Grant example.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Dataset", "@id": "https://doi.org/10.5061/dryad.m53r1", "funding": { "@type": "Grant", "identifier": "1452510", "funder": { "@type": "Organization", "name": "National Science Foundation", "identifier": "https://doi.org/10.13039/100000001" } } } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0310)

Copied

Example notes or example HTML without markup.

Basic research output (dataset) example without detailed grant information.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Dataset", "@id": "https://doi.org/10.5061/dryad.m53r1", "funder": { "@type": "Organization", "name": "National Science Foundation", "identifier": "https://doi.org/10.13039/100000001" } } </script>

Structured representation of the JSON-LD example.

[Example 3](#eg-0312)

Copied

Example notes or example HTML without markup.

Showing funding of a researcher.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Person", "name": "Turner, Caroline B.", "givenName": "Caroline B.", "familyName": "Turner", "funding": { "@type": "Grant", "identifier": "1448821", "funder": { "@type": "Organization", "name": "National Science Foundation", "identifier": "https://doi.org/10.13039/100000001" } } } </script>

Structured representation of the JSON-LD example.

[Example 4](#eg-0469)

Copied

Example notes or example HTML without markup.

A scientific dataset.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Person", "name": "Turner, Caroline B.", "givenName": "Caroline B.", "familyName": "Turner", "funding": { "@type": "Grant", "identifier": "1448821", "funder": { "@type": "Organization", "name": "National Science Foundation", "identifier": "https://doi.org/10.13039/100000001" } } } </script>

Structured representation of the JSON-LD example.

[Example 5](#eg-0470)

Copied

Example notes or example HTML without markup.

EXample showing a research project that was funded by 3 grants.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "ResearchProject", "name": "U.S. GLOBEC Southern Ocean", "url": "https://www.bco-dmo.org/project/2039", "funding": [ { "@type": "MonetaryGrant", "name": "Foraging Ecology of Crabeater Seals (Lobodon Carcinophagus)", "alternateName": "ANT-9909933", "url": "https://www.bco-dmo.org/award/54719", "sameAs": "https://www.nsf.gov/awardsearch/showAward?AWD_ID=9909933", "funder": { "@id": "https://doi.org/10.13039/100000162", "@type": "FundingAgency", "name": "NSF Antarctic Sciences", "alternateName": "NSF ANT", "url": "https://www.bco-dmo.org/funding-source/369", "sameAs": "https://doi.org/10.13039/100000162", "parentOrganization": { "@type": "FundingAgency", "name": "National Science Foundation", "alternateName": "NSF", "sameAs": "https://doi.org/10.13039/100000001" } } }, { "@type": "MonetaryGrant", "name": "GLOBEC: Sea Ice Microbial Communities", "alternateName": "ANT-9910098", "url": "https://www.bco-dmo.org/award/54688", "sameAs": "https://www.nsf.gov/awardsearch/showAward?AWD_ID=9910098", "funder": {"@id": "https://doi.org/10.13039/100000162"} }, { "@type": "MonetaryGrant", "name": "unknown SOGLOBEC NSF ANT", "url": "https://www.bco-dmo.org/award/54617", "funder": {"@id": "https://doi.org/10.13039/100000162"} } ] } </script>

Structured representation of the JSON-LD example.

[Example 6](#eg-0471)

Copied

Example notes or example HTML without markup.

A scientific dataset.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Person", "name": "Turner, Caroline B.", "givenName": "Caroline B.", "familyName": "Turner", "funding": { "@type": "Grant", "identifier": "1448821", "funder": { "@type": "Organization", "name": "National Science Foundation", "identifier": "https://doi.org/10.13039/100000001" } } } </script>

Structured representation of the JSON-LD example.

[Example 7](#eg-0472)

Copied

Example notes or example HTML without markup.

EXample showing that a data repository was funded by the US National Science Foundation.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@id": "https://www.bco-dmo.org", "@type": "Organization", "name": "Biological and Chemical Oceanography Data Management Office", "alternateName": "BCO-DMO", "url": "https://www.bco-dmo.org", "funding": { "@type": "MonetaryGrant", "name": "BCO-DMO: Accelerating Scientific Discovery through Adaptive Data Management", "url": "https://www.nsf.gov/awardsearch/showAward?AWD_ID=1924618", "funder": { "@type": "FundingAgency", "name": "National Science Foundation", "alternateName": "NSF", "sameAs": "https://doi.org/10.13039/100000001" } } } </script>

Structured representation of the JSON-LD example.
