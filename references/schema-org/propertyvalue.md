---
title: "PropertyValue"
source_url: https://schema.org/PropertyValue
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# PropertyValue

# PropertyValue

A Schema.org Type

- Canonical URL: https://schema.org/PropertyValue
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+PropertyValue)

A property-value pair, e.g. representing a feature of a product or place. Use the 'name' property for the name of the property. If there is an additional human-readable version of the value, put that into the 'description' property.


Always use specific schema.org properties when a) they exist and b) you can populate them. Using PropertyValue as a substitute will typically not trigger the same effect as using the original, specific property.

Always use specific schema.org properties when a) they exist and b) you can populate them. Using PropertyValue as a substitute will typically not trigger the same effect as using the original, specific property.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

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

[PropertyValue](/PropertyValue)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[MerchantReturnPolicy](/MerchantReturnPolicy)or[Offer](/Offer)or[Place](/Place)or[Product](/Product)or[QualitativeValue](/QualitativeValue)or[QuantitativeValue](/QuantitativeValue)Note: Publishers should be aware that applications designed to use specific schema.org properties (e.g. https://schema.org/width, https://schema.org/color, https://schema.org/gtin13, ...) will typically expect such data to be provided using those properties, rather than using the generic property/value mechanism.

[associatedDisease](/associatedDisease)

[BioChemEntity](/BioChemEntity)[exifData](/exifData)

[ImageObject](/ImageObject)[hasMolecularFunction](/hasMolecularFunction)

[BioChemEntity](/BioChemEntity)[hasRepresentation](/hasRepresentation)

[BioChemEntity](/BioChemEntity)[identifier](/identifier)

[Thing](/Thing)[Thing](/Thing), such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links. See[background notes](/docs/datamodel.html#identifierBg)for more details.[isInvolvedInBiologicalProcess](/isInvolvedInBiologicalProcess)

[BioChemEntity](/BioChemEntity)[isLocatedInSubcellularLocation](/isLocatedInSubcellularLocation)

[BioChemEntity](/BioChemEntity)[recipeIngredient](/recipeIngredient)

[Recipe](/Recipe)[taxonRank](/taxonRank)

[Taxon](/Taxon)[valueReference](/valueReference)

[PropertyValue](/PropertyValue)or[QualitativeValue](/QualitativeValue)or[QuantitativeValue](/QuantitativeValue)[variableMeasured](/variableMeasured)

[Dataset](/Dataset)or[Observation](/Observation)[StatisticalVariable](/StatisticalVariable).[variablesMeasured](/variablesMeasured)

[Dataset](/Dataset)[variablesMeasured](/variablesMeasured), the[variableMeasured](/variableMeasured)property can indicate (repeated as necessary) the variables that are measured in some dataset, either described as text or as pairs of identifier and description using PropertyValue.#### More specific Types

### Examples

[Example 1](#eg-0404)

Copied

Example notes or example HTML without markup.

<h2>Beach in Mexico</h2> <img src="mexico-beach.jpg" alt="" /> By Jane Doe Photographed in Puerto Vallarta, Mexico Date uploaded: Jan 25, 2008 I took this picture while on vacation last year. <!-- We assume the following EXIF meta-data is available, but currently not shown: Exposure Time: 1/659 sec. FNumber: f/4.0 MaxApertureValue: 2.00 Metering Mode: Pattern Flash: Flash did not fire. -->

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/ImageObject"> <h2 itemprop="name">Beach in Mexico</h2> <img src="mexico-beach.jpg" alt="" itemprop="contentUrl" /> By <span itemprop="author">Jane Doe</span> Photographed in <span itemprop="contentLocation">Puerto Vallarta, Mexico</span> Date uploaded: <meta itemprop="datePublished" content="2008-01-25">Jan 25, 2008 <span itemprop="description">I took this picture while on vacation last year.</span> <!-- Note: We do not split value strings in unit and value information, since this the raw EXIF data does not provide this granularity. If you are able to separate the unit, you can use the unitText property --> <div itemprop="exifData" itemscope itemtype="https://schema.org/PropertyValue"> <meta itemprop="name" content="Exposure Time"> <meta itemprop="value" content="1/659 sec."> </div> <div itemprop="exifData" itemscope itemtype="https://schema.org/PropertyValue"> <meta itemprop="name" content="FNumber"> <meta itemprop="value" content="f/4.0"> </div> <div itemprop="exifData" itemscope itemtype="https://schema.org/PropertyValue"> <meta itemprop="name" content="MaxApertureValue"> <meta itemprop="value" content="2.00"> </div> <div itemprop="exifData" itemscope itemtype="https://schema.org/PropertyValue"> <meta itemprop="name" content="Metering Mode"> <meta itemprop="value" content="Pattern"> </div> <div itemprop="exifData" itemscope itemtype="https://schema.org/PropertyValue"> <meta itemprop="name" content="Flash"> <meta itemprop="value" content="Flash did not fire."> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="ImageObject"> <h2 property="name">Beach in Mexico</h2> <img src="mexico-beach.jpg" alt="" property="contentUrl" /> By <span property="author">Jane Doe</span> Photographed in <span property="contentLocation">Puerto Vallarta, Mexico</span> Date uploaded: <meta property="datePublished" content="2008-01-25">Jan 25, 2008 <span property="description">I took this picture while on vacation last year.</span> <!-- Note: We do not split value strings in unit and value information, since this the raw EXIF data does not provide this granularity. If you are able to separate the unit, you can use the unitText property --> <div property="exifData" typeOf="PropertyValue"> <meta property="name" content="Exposure Time"> <meta property="value" content="1/659 sec."> </div> <div property="exifData" typeOf="PropertyValue"> <meta property="name" content="FNumber"> <meta property="value" content="f/4.0"> </div> <div property="exifData" typeOf="PropertyValue"> <meta property="name" content="MaxApertureValue"> <meta property="value" content="2.00"> </div> <div property="exifData" typeOf="PropertyValue"> <meta property="name" content="Metering Mode"> <meta property="value" content="Pattern"> </div> <div property="exifData" typeOf="PropertyValue"> <meta property="name" content="Flash"> <meta property="value" content="Flash did not fire."> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "ImageObject", "author": "Jane Doe", "contentLocation": "Puerto Vallarta, Mexico", "contentUrl": "mexico-beach.jpg", "datePublished": "2008-01-25", "description": "I took this picture while on vacation last year.", "name": "Beach in Mexico", "exifData": [ { "@type": "PropertyValue", "name": "Exposure Time", "value": "1/659 sec." }, { "@type": "PropertyValue", "name": "FNumber", "value": "f/4.0" }, { "@type": "PropertyValue", "name": "MaxApertureValue", "value": "2.00" }, { "@type": "PropertyValue", "name": "Metering Mode", "value": "Pattern" }, { "@type": "PropertyValue", "name": "Flash", "value": "Flash did not fire." } ] } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0405)

Copied

Example notes or example HTML without markup.

<!-- Product: Point Value, with unit as text --> <div> <img src="camera123.jpg" alt="" /> <span>Digital Camera 123</span> <div> <span>Approx. Weight</span> <span>450</span> <span>gram</span> </div> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<!-- Product: Point Value, with unit as text --> <div itemscope itemtype="https://schema.org/Product"> <img itemprop="image" src="camera123.jpg" alt="" /> <span itemprop="name">Digital Camera 123</span> <div itemprop="additionalProperty" itemscope itemtype="https://schema.org/PropertyValue"> <span itemprop="name">Approx. Weight</span> <span itemprop="value">450</span> <span itemprop="unitText">gram</span> </div> </div>

[Example 3](#eg-0406)

Copied

Example notes or example HTML without markup.

<!-- Product: Point Value, with unit as UN/CEFACT Common Code to be added to the template --> <div> <img src="camera123.jpg" alt="" /> <span>Digital Camera 123</span> <div> <span>Approx. Weight</span> <span>450</span>g </div> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<!-- Product: Point Value, with unit as UN/CEFACT Common Code --> <div itemscope itemtype="https://schema.org/Product"> <img itemprop="image" src="camera123.jpg" alt="" /> <span itemprop="name">Digital Camera 123</span> <div itemprop="additionalProperty" itemscope itemtype="https://schema.org/PropertyValue"> <span itemprop="name">Approx. Weight</span> <span itemprop="value">450</span> <meta itemprop="unitCode" content="GRM">g </div> </div>

[Example 4](#eg-0407)

Copied

Example notes or example HTML without markup.

<!-- Product: Range, with unit as UN/CEFACT Common Code to be added to the template --> <div> <img src="camera123.jpg" alt="" /> <span>Digital Camera 123</span> <div> <span>Operating Voltage</span> <span>100</span>- <span>250</span> volts </div> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<!-- Product: Range, with unit as UN/CEFACT Common Code --> <div itemscope itemtype="https://schema.org/Product"> <img itemprop="image" src="camera123.jpg" alt="" /> <span itemprop="name">Digital Camera 123</span> <div itemprop="additionalProperty" itemscope itemtype="https://schema.org/PropertyValue"> <span itemprop="name">Operating Voltage</span> <span itemprop="minValue">100</span>- <span itemprop="maxValue">250</span> <meta itemprop="unitCode" content="VLT">volts </div> </div>

[Example 5](#eg-0408)

Copied

Example notes or example HTML without markup.

<!-- Product: Open Interval, with unit as UN/CEFACT Common Code to be added to the template --> <div> <img src="camera123.jpg" alt="" /> <span>Digital Camera 123</span> <div> <span>Wifi range</span>: up to <span>30</span> ft. </div> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<!-- Product: Open Interval, with unit as UN/CEFACT Common Code --> <div itemscope itemtype="https://schema.org/Product"> <img itemprop="image" src="camera123.jpg" alt="" /> <span itemprop="name">Digital Camera 123</span> <div itemprop="additionalProperty" itemscope itemtype="https://schema.org/PropertyValue"> <span itemprop="name">Wifi range</span>: up to <span itemprop="maxValue">30</span> <!-- Note: The UN/CEFACT Common Code for foot is FOT --> <meta itemprop="unitCode" content="FOT">ft. </div> </div>

[Example 6](#eg-0409)

Copied

Example notes or example HTML without markup.

<!-- Product: Multiple Intervals --> <div> <img src="camera123.jpg" alt="" /> <span>Digital Camera 123</span> <div> <span>Operating voltage</span>: <span>9-12</span> or <span>100-250</span> volts </div> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<!-- Product: Multiple Intervals --> <div itemscope itemtype="https://schema.org/Product"> <img itemprop="image" src="camera123.jpg" alt="" /> <span itemprop="name">Digital Camera 123</span> <div itemprop="additionalProperty" itemscope itemtype="https://schema.org/PropertyValue"> <span itemprop="name">Operating voltage</span>: <span itemprop="value">9-12</span> or <span itemprop="value">100-250</span> <meta itemprop="unitCode" content="VLT">volts </div> </div>

[Example 7](#eg-0410)

Copied

Example notes or example HTML without markup.

<!-- Product: Range and Enumerated Values --> <div> <img src="camera123.jpg" alt="" /> <span>Digital Camera 123</span> <div> <span>ISO Sensitivity</span>: <span>100-6400</span>/ <span>12,800</span> (Hi-1) <span>ISO</span> </div> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<!-- Product: Range and Enumerated Values --> <div itemscope itemtype="https://schema.org/Product"> <img itemprop="image" src="camera123.jpg" alt="" /> <span itemprop="name">Digital Camera 123</span> <div itemprop="additionalProperty" itemscope itemtype="https://schema.org/PropertyValue"> <span itemprop="name">ISO Sensitivity</span>: <span itemprop="value">100-6400</span>/ <span itemprop="value">12,800</span> (Hi-1) <span itemprop="unitText">ISO</span> </div> </div>

[Example 8](#eg-0411)

Copied

Example notes or example HTML without markup.

<!-- Product: Boolean Value --> <div> <img src="camera123.jpg" alt="" /> <span>Digital Camera 123</span> <div> <span>USB interface</span>: Yes </div> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<!-- Product: Boolean Value --> <div itemscope itemtype="https://schema.org/Product"> <img itemprop="image" src="camera123.jpg" alt="" /> <span itemprop="name">Digital Camera 123</span> <div itemprop="additionalProperty" itemscope itemtype="https://schema.org/PropertyValue"> <span itemprop="name">USB interface</span>: <meta itemprop="value" content="True">Yes </div> </div>

[Example 9](#eg-0412)

Copied

Example notes or example HTML without markup.

<!-- Product: Qualitative Value --> <div> <img src="camera123.jpg" alt="" /> <span>Digital Camera 123</span> <div> <span>Interface</span>: <span>USB</span> </div> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<!-- Product: Qualitative Value --> <div itemscope itemtype="https://schema.org/Product"> <img itemprop="image" src="camera123.jpg" alt="" /> <span itemprop="name">Digital Camera 123</span> <div itemprop="additionalProperty" itemscope itemtype="https://schema.org/PropertyValue"> <span itemprop="name">Interface</span>: <span itemprop="value">USB</span> </div> </div>

[Example 10](#eg-0413)

Copied

Example notes or example HTML without markup.

<!-- Product: Qualitative Value (multiple) --> <div> <img src="camera123.jpg" alt="" /> <span>Digital Camera 123</span> <div> <span>Interfaces</span>: <span>USB</span>, <span>Ethernet</span> </div> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<!-- Product: Qualitative Value (multiple) --> <div itemscope itemtype="https://schema.org/Product"> <img itemprop="image" src="camera123.jpg" alt="" /> <span itemprop="name">Digital Camera 123</span> <div itemprop="additionalProperty" itemscope itemtype="https://schema.org/PropertyValue"> <span itemprop="name">Interfaces</span>: <span itemprop="value">USB</span>, <span itemprop="value">Ethernet</span> </div> </div>

[Example 11](#eg-0414)

Copied

Example notes or example HTML without markup.

<!-- Product: Property ID for clarifying the meaning of a property: URI from external vocabulary --> <!-- (see microdata example for comparison) --> <div> <img src="station_waggon123.jpg" alt="" /> <span>Station Waggon 123</span> <div> <span>Luggage Capacity (seats folded)</span>: <span>500</span> liter </div> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<!-- Product: Property ID for clarifying the meaning of a property: URI from external vocabulary --> <div itemscope itemtype="https://schema.org/Car"> <img itemprop="image" src="station_waggon123.jpg" alt="" /> <span itemprop="name">Station Waggon 123</span> <div itemprop="additionalProperty" itemscope itemtype="https://schema.org/PropertyValue"> <span itemprop="name">Luggage Capacity (seats folded)</span>: <span itemprop="value">500</span> <meta itemprop="unitCode" content="LTR">liter <link itemprop="propertyID" href="http://purl.org/vvo/ns#luggageCapacitySeatsFolded" /> </div> </div>

[Example 12](#eg-0415)

Copied

Example notes or example HTML without markup.

<!-- Product: Property ID for clarifying the meaning of a property: Code from eCl@ss Standard --> <!-- The Property code 02-AAM226 is for "USB interface present" in eCl@ss 8.1 (see microdata example for comparison) --> <div> <img src="camera123.jpg" alt="" /> <span>Digital Camera 123</span> <div> <span>USB Interface</span>:Yes </div> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<!-- Product: Property ID for clarifying the meaning of a property: Code from eCl@ss Standard --> <!-- The Property code 02-AAM226 is for "USB interface present" in eCl@ss 8.1 --> <div itemscope itemtype="https://schema.org/Product"> <img itemprop="image" src="camera123.jpg" alt="" /> <span itemprop="name">Digital Camera 123</span> <div itemprop="additionalProperty" itemscope itemtype="https://schema.org/PropertyValue"> <span itemprop="name">USB Interface</span>: <meta itemprop="value" content="True">Yes <meta itemprop="propertyID" content="eclass81:02-AAM226"> </div> </div>

[Example 13](#eg-0416)

Copied

Example notes or example HTML without markup.

<!-- Product: Value References --> <div> <img src="camera123.jpg" alt="" /> <span>Digital Camera 123</span> <div> <span>Operating Voltage</span> <span>100</span>- <span>250</span> volts at <div> <span>50</span> <span>Hz</span> </div> </div> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<!-- Product: Value References --> <div itemscope itemtype="https://schema.org/Product"> <img itemprop="image" src="camera123.jpg" alt="" /> <span itemprop="name">Digital Camera 123</span> <div itemprop="additionalProperty" itemscope itemtype="https://schema.org/PropertyValue"> <span itemprop="name">Operating Voltage</span> <span itemprop="minValue">100</span>- <span itemprop="maxValue">250</span> <meta itemprop="unitCode" content="VLT">volts at <div itemprop="valueReference" itemscope itemtype="https://schema.org/PropertyValue"> <span itemprop="value">50</span> <span itemprop="unitText">Hz</span> </div> </div> </div>

[Example 14](#eg-0417)

Copied

Example notes or example HTML without markup.

<!-- Product: Ratios --> <div> <img src="station_waggon123.jpg" alt="" /> <span>Station Waggon 123</span> <div> <span>Fuel consumption</span>: <span>5</span> <meta>liter</span> / <div> <span>100</span> <span>km</span> </div> </div> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<!-- Product: Ratios --> <div itemscope itemtype="https://schema.org/Car"> <img itemprop="image" src="station_waggon123.jpg" alt="" /> <span itemprop="name">Station Waggon 123</span> <div itemprop="additionalProperty" itemscope itemtype="https://schema.org/PropertyValue"> <span itemprop="name">Fuel consumption</span>: <span itemprop="value">5</span> <meta itemprop="unitCode" content="LTR">liter / <div itemprop="valueReference" itemscope itemtype="https://schema.org/PropertyValue"> <span itemprop="value">100</span> <span itemprop="unitText">km</span> </div> </div> </div>

[Example 15](#eg-0418)

Copied

Example notes or example HTML without markup.

<!-- Product: Grouping and Hierarchical Order of Properties --> <div> <img src="camera123.jpg" alt="" /> <span>Digital Camera 123</span> <div> <strong>Focus/Autofocus</strong> <div> <span>Picture Control</span> <span>Landscape</span> <span>Monochrome</span> <span>Portrait</span> </div> <div> <span>Single-point AF Mode</span>: Yes </div> </div> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<!-- Product: Grouping and Hierarchical Order of Properties --> <div itemscope itemtype="https://schema.org/Product"> <img itemprop="image" src="camera123.jpg" alt="" /> <span itemprop="name">Digital Camera 123</span> <div itemprop="additionalProperty" itemscope itemtype="https://schema.org/PropertyValue"> <strong itemprop="name">Focus/Autofocus</strong> <div itemprop="value" itemscope itemtype="https://schema.org/PropertyValue"> <span itemprop="name">Picture Control</span> <span itemprop="value">Landscape</span> <span itemprop="value">Monochrome</span> <span itemprop="value">Portrait</span> </div> <div itemprop="value" itemscope itemtype="https://schema.org/PropertyValue"> <span itemprop="name">Single-point AF Mode</span>: <meta itemprop="value" content="True">Yes </div> </div> </div>
