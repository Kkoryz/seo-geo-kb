---
title: "LocationFeatureSpecification"
source_url: https://schema.org/LocationFeatureSpecification
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# LocationFeatureSpecification

# LocationFeatureSpecification

A Schema.org Type

- Canonical URL: https://schema.org/LocationFeatureSpecification
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+LocationFeatureSpecification)

Specifies a location feature by providing a structured value representing a feature of an accommodation as a property-value pair of varying degrees of formality.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[hoursAvailable](/hoursAvailable)

[OpeningHoursSpecification](/OpeningHoursSpecification)```
```[validFrom](/validFrom)

[Date](/Date)or[DateTime](/DateTime)```
```[validThrough](/validThrough)

[Date](/Date)or[DateTime](/DateTime)[PropertyValue](/PropertyValue)

```
```[maxValue](/maxValue)

[Number](/Number)```
```[measurementMethod](/measurementMethod)

[DefinedTerm](/DefinedTerm)or[MeasurementMethodEnum](/MeasurementMethodEnum)or[Text](/Text)or[URL](/URL)[measurementTechnique](/measurementTechnique)that can be used for specifying specific methods, in particular via[MeasurementMethodEnum](/MeasurementMethodEnum).```
```[measurementTechnique](/measurementTechnique)

[DefinedTerm](/DefinedTerm)or[MeasurementMethodEnum](/MeasurementMethodEnum)or[Text](/Text)or[URL](/URL)[Observation](/Observation),[StatisticalVariable](/StatisticalVariable)or[Dataset](/Dataset)(or[DataDownload](/DataDownload),[DataCatalog](/DataCatalog)), corresponding to the method used for measuring the corresponding variable(s) (for datasets, described using[variableMeasured](/variableMeasured); for[Observation](/Observation), a[StatisticalVariable](/StatisticalVariable)). Often but not necessarily each[variableMeasured](/variableMeasured)will have an explicit representation as (or mapping to) an property such as those defined in Schema.org, or other RDF vocabularies and "knowledge graphs". In that case the subproperty of[variableMeasured](/variableMeasured)called[measuredProperty](/measuredProperty)is applicable.The

[measurementTechnique](/measurementTechnique)property helps when extra clarification is needed about how a[measuredProperty](/measuredProperty)was measured. This is oriented towards scientific and scholarly dataset publication but may have broader applicability; it is not intended as a full representation of measurement, but can often serve as a high level summary for dataset discovery.For example, if

[variableMeasured](/variableMeasured)is: molecule concentration,[measurementTechnique](/measurementTechnique)could be: "mass spectrometry" or "nmr spectroscopy" or "colorimetry" or "immunofluorescence". If the[variableMeasured](/variableMeasured)is "depression rating", the[measurementTechnique](/measurementTechnique)could be "Zung Scale" or "HAM-D" or "Beck Depression Inventory".If there are several

[variableMeasured](/variableMeasured)properties recorded for some given data object, use a[PropertyValue](/PropertyValue)for each[variableMeasured](/variableMeasured)and attach the corresponding[measurementTechnique](/measurementTechnique). The value can also be from an enumeration, organized as a[MeasurementMethodEnum](/MeasurementMethodEnum).```
```[minValue](/minValue)

[Number](/Number)```
```[propertyID](/propertyID)

[Text](/Text)or[URL](/URL)```
```[unitCode](/unitCode)

[Text](/Text)or[URL](/URL)```
```[unitText](/unitText)

[Text](/Text)[unitCode](unitCode).```
```[value](/value)

[Boolean](/Boolean)or[Number](/Number)or[StructuredValue](/StructuredValue)or[Text](/Text)[QuantitativeValue](/QuantitativeValue)(including[Observation](/Observation)) or property value node.- For
[QuantitativeValue](/QuantitativeValue)and[MonetaryAmount](/MonetaryAmount), the recommended type for values is 'Number'. - For
[PropertyValue](/PropertyValue), it can be 'Text', 'Number', 'Boolean', or 'StructuredValue'. - Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.
- Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.

```
```[valueReference](/valueReference)

[DefinedTerm](/DefinedTerm)or[Enumeration](/Enumeration)or[MeasurementTypeEnumeration](/MeasurementTypeEnumeration)or[PropertyValue](/PropertyValue)or[QualitativeValue](/QualitativeValue)or[QuantitativeValue](/QuantitativeValue)or[StructuredValue](/StructuredValue)or[Text](/Text)[Thing](/Thing)

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

[LocationFeatureSpecification](/LocationFeatureSpecification)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[Accommodation](/Accommodation)or[FloorPlan](/FloorPlan)or[LodgingBusiness](/LodgingBusiness)or[Place](/Place)### Acknowledgements

STI Accommodation Ontology

[http://ontologies.sti-innsbruck.at/acco/ns.html](http://ontologies.sti-innsbruck.at/acco/ns.html)for details. Many class and property definitions are inspired by or based on abstracts from Wikipedia, the free encyclopedia.

### Examples

[Example 1](#eg-0366)

Copied

Example notes or example HTML without markup.

This example is in microdata only.

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Hotel"> <h1><span itemprop="name">ACME Hotel Innsbruck</span></h1> <span itemprop="description">A beautifully located business hotel right in the heart of the alps. Watch the sun rise over the scenic Inn valley while enjoying your morning coffee.</span> Hotel Features: <ul> <li itemprop="amenityFeature" itemscope itemtype="https://schema.org/LocationFeatureSpecification"> <span itemprop="name">Sauna</span> <meta itemprop="value" content="True"> </li> <li itemprop="amenityFeature" itemscope itemtype="https://schema.org/LocationFeatureSpecification"> <span itemprop="name">Gym</span> <meta itemprop="value" content="True"> </li> </ul> </div>

[Example 2](#eg-0367)

Copied

Example notes or example HTML without markup.

This example is in microdata only.

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Hotel"> <h1><span itemprop="name">ACME Hotel Innsbruck</span></h1> <span itemprop="description">A beautifully located business hotel right in the heart of the alps. Watch the sun rise over the scenic Inn valley while enjoying your morning coffee.</span> Hotel Features: <ul> <li itemprop="amenityFeature" itemscope itemtype="https://schema.org/LocationFeatureSpecification"> <span itemprop="name">Sauna</span> <meta itemprop="value" content="True"> <div itemprop="hoursAvailable" itemscope itemtype="https://schema.org/OpeningHoursSpecification"> <link itemprop="dayOfWeek" href="http://purl.org/goodrelations/v1#Thursday" />(Open Thursdays <time itemprop="opens" content="16:00:00"> 4:00 PM</time> - <time itemprop="closes" content="21:00:00"> 9:00 PM</time>) </div> </li> </ul> </div>
