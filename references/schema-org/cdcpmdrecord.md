---
title: "CDCPMDRecord"
source_url: https://schema.org/CDCPMDRecord
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# CDCPMDRecord

# CDCPMDRecord

A Schema.org Type

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/CDCPMDRecord
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+CDCPMDRecord)

A CDCPMDRecord is a data structure representing a record in a CDC tabular data format
used for hospital data reporting. See

[documentation](/docs/cdc-covid.html)for details, and the linked CDC materials for authoritative definitions used as the source here.| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[cvdCollectionDate](/cvdCollectionDate)

[DateTime](/DateTime)or[Text](/Text)```
```[cvdFacilityCounty](/cvdFacilityCounty)

[Text](/Text)[cvdFacilityId](/cvdFacilityId)to identify the facility. To provide other details,[healthcareReportingData](/healthcareReportingData)can be used on a[Hospital](/Hospital)entry.```
```[cvdFacilityId](/cvdFacilityId)

[Text](/Text)[cvdFacilityCounty](/cvdFacilityCounty)to indicate the county. To provide other details,[healthcareReportingData](/healthcareReportingData)can be used on a[Hospital](/Hospital)entry.```
```[cvdNumBeds](/cvdNumBeds)

[Number](/Number)```
```[cvdNumBedsOcc](/cvdNumBedsOcc)

[Number](/Number)```
```[cvdNumC19Died](/cvdNumC19Died)

[Number](/Number)```
```[cvdNumC19HOPats](/cvdNumC19HOPats)

[Number](/Number)```
```[cvdNumC19HospPats](/cvdNumC19HospPats)

[Number](/Number)```
```[cvdNumC19MechVentPats](/cvdNumC19MechVentPats)

[Number](/Number)```
```[cvdNumC19OFMechVentPats](/cvdNumC19OFMechVentPats)

[Number](/Number)```
```[cvdNumC19OverflowPats](/cvdNumC19OverflowPats)

[Number](/Number)```
```[cvdNumICUBeds](/cvdNumICUBeds)

[Number](/Number)```
```[cvdNumICUBedsOcc](/cvdNumICUBedsOcc)

[Number](/Number)```
```[cvdNumTotBeds](/cvdNumTotBeds)

[Number](/Number)```
```[cvdNumVent](/cvdNumVent)

[Number](/Number)```
```[cvdNumVentUse](/cvdNumVentUse)

[Number](/Number)```
```[datePosted](/datePosted)

[Date](/Date)or[DateTime](/DateTime)[Thing](/Thing)

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

[CDCPMDRecord](/CDCPMDRecord)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[Hospital](/Hospital)[CDCPMDRecord](/CDCPMDRecord)or as some kind of[Dataset](/Dataset).#### Source

[https://github.com/schemaorg/schemaorg/issues/2521](https://github.com/schemaorg/schemaorg/issues/2521)
