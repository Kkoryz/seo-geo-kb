---
title: "DefinedTerm"
source_url: https://schema.org/DefinedTerm
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# DefinedTerm

# DefinedTerm

A Schema.org Type

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/DefinedTerm
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+DefinedTerm)

A word, name, acronym, phrase, etc. with a formal definition. Often used in the context of category or subject classification, glossaries or dictionaries, product or creative work types, etc. Use the name property for the term being defined, use termCode if the term has an alpha-numeric code allocated, use description to provide the definition of the term. Use the about property to specify what the term is about.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[about](/about)

[Thing](/Thing)Inverse property:

[subjectOf](/subjectOf)```
```[inDefinedTermSet](/inDefinedTermSet)

[DefinedTermSet](/DefinedTermSet)or[URL](/URL)[DefinedTermSet](/DefinedTermSet)that contains this term.```
```[termCode](/termCode)

[Text](/Text)[DefinedTerm](/DefinedTerm)within a[DefinedTermSet](/DefinedTermSet).[Thing](/Thing)

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

[DefinedTerm](/DefinedTerm)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[CreativeWork](/CreativeWork)or[EducationEvent](/EducationEvent)or[LearningResource](/LearningResource)[biologicalRole](/biologicalRole)

[BioChemEntity](/BioChemEntity)[certificationIdentification](/certificationIdentification)

[Certification](/Certification)[gs1:certificationIdentification](https://www.gs1.org/voc/certificationIdentification).[chemicalRole](/chemicalRole)

[ChemicalSubstance](/ChemicalSubstance)or[MolecularEntity](/MolecularEntity)[competencyRequired](/competencyRequired)

[EducationalOccupationalCredential](/EducationalOccupationalCredential)or[LearningResource](/LearningResource)[creativeWorkStatus](/creativeWorkStatus)

[CreativeWork](/CreativeWork)[credentialCategory](/credentialCategory)

[Credential](/Credential)[educationalLevel](/educationalLevel)

[CreativeWork](/CreativeWork)or[EducationEvent](/EducationEvent)or[EducationalOccupationalCredential](/EducationalOccupationalCredential)or[LearningResource](/LearningResource)[educationalUse](/educationalUse)

[CreativeWork](/CreativeWork)or[LearningResource](/LearningResource)[errorCode](/errorCode)

[Error](/Error)[expressedIn](/expressedIn)

[Gene](/Gene)[financialAidEligible](/financialAidEligible)

[Course](/Course)or[EducationalOccupationalProgram](/EducationalOccupationalProgram)[genre](/genre)

[BroadcastChannel](/BroadcastChannel)or[CreativeWork](/CreativeWork)or[MusicGroup](/MusicGroup)[hasDefinedTerm](/hasDefinedTerm)

[DefinedTermSet](/DefinedTermSet)or[Taxon](/Taxon)[hasMolecularFunction](/hasMolecularFunction)

[BioChemEntity](/BioChemEntity)[incentivizedItem](/incentivizedItem)

[FinancialIncentive](/FinancialIncentive)DefinedTermSets are used for product and service categories such as the United Nations Standard Products and Services Code:

```
{
"@type": "DefinedTerm",
"inDefinedTermSet": "https://www.unspsc.org/",
"termCode": "261315XX",
"name": "Photovoltaic module"
}
```


For a specific product or service, use the Product type:```
{
"@type": "Product",
"name": "Kenmore White 17" Microwave",
}
```


For multiple different incentivized items, use multiple [DefinedTerm](/DefinedTerm)or[Product](/Product).[industry](/industry)

[JobPosting](/JobPosting)[isInvolvedInBiologicalProcess](/isInvolvedInBiologicalProcess)

[BioChemEntity](/BioChemEntity)[isLocatedInSubcellularLocation](/isLocatedInSubcellularLocation)

[BioChemEntity](/BioChemEntity)[jobTitle](/jobTitle)

[Person](/Person)[keywords](/keywords)

[CreativeWork](/CreativeWork)or[Event](/Event)or[Organization](/Organization)or[Place](/Place)or[Product](/Product)[learningResourceType](/learningResourceType)

[CreativeWork](/CreativeWork)or[LearningResource](/LearningResource)[measurementMethod](/measurementMethod)

[DataCatalog](/DataCatalog)or[DataDownload](/DataDownload)or[Dataset](/Dataset)or[Observation](/Observation)or[PropertyValue](/PropertyValue)or[StatisticalVariable](/StatisticalVariable)[measurementTechnique](/measurementTechnique)that can be used for specifying specific methods, in particular via[MeasurementMethodEnum](/MeasurementMethodEnum).[measurementTechnique](/measurementTechnique)

[DataCatalog](/DataCatalog)or[DataDownload](/DataDownload)or[Dataset](/Dataset)or[Observation](/Observation)or[PropertyValue](/PropertyValue)or[StatisticalVariable](/StatisticalVariable)[Observation](/Observation),[StatisticalVariable](/StatisticalVariable)or[Dataset](/Dataset)(or[DataDownload](/DataDownload),[DataCatalog](/DataCatalog)), corresponding to the method used for measuring the corresponding variable(s) (for datasets, described using[variableMeasured](/variableMeasured); for[Observation](/Observation), a[StatisticalVariable](/StatisticalVariable)). Often but not necessarily each[variableMeasured](/variableMeasured)will have an explicit representation as (or mapping to) an property such as those defined in Schema.org, or other RDF vocabularies and "knowledge graphs". In that case the subproperty of[variableMeasured](/variableMeasured)called[measuredProperty](/measuredProperty)is applicable.The

[measurementTechnique](/measurementTechnique)property helps when extra clarification is needed about how a[measuredProperty](/measuredProperty)was measured. This is oriented towards scientific and scholarly dataset publication but may have broader applicability; it is not intended as a full representation of measurement, but can often serve as a high level summary for dataset discovery.For example, if

[variableMeasured](/variableMeasured)is: molecule concentration,[measurementTechnique](/measurementTechnique)could be: "mass spectrometry" or "nmr spectroscopy" or "colorimetry" or "immunofluorescence". If the[variableMeasured](/variableMeasured)is "depression rating", the[measurementTechnique](/measurementTechnique)could be "Zung Scale" or "HAM-D" or "Beck Depression Inventory".If there are several

[variableMeasured](/variableMeasured)properties recorded for some given data object, use a[PropertyValue](/PropertyValue)for each[variableMeasured](/variableMeasured)and attach the corresponding[measurementTechnique](/measurementTechnique). The value can also be from an enumeration, organized as a[MeasurementMethodEnum](/MeasurementMethodEnum).[pattern](/pattern)

[CreativeWork](/CreativeWork)or[Product](/Product)[physicalRequirement](/physicalRequirement)

[JobPosting](/JobPosting)[potentialUse](/potentialUse)

[ChemicalSubstance](/ChemicalSubstance)or[MolecularEntity](/MolecularEntity)[programType](/programType)

[EducationalOccupationalProgram](/EducationalOccupationalProgram)[pronouns](/pronouns)

[Person](/Person)In English, formulations such as "they/them", "she/her", and "he/him" are commonly used online and can also be used here. We do not intend to enumerate all possible micro-syntaxes in all languages. More structured and well-defined external values for pronouns can be referenced using the

[StructuredValue](/StructuredValue)or[DefinedTerm](/DefinedTerm)values.[sensoryRequirement](/sensoryRequirement)

[JobPosting](/JobPosting)[size](/size)

[CreativeWork](/CreativeWork)or[Product](/Product)[SizeSpecification](/SizeSpecification); in other cases, the[width](/width),[height](/height),[depth](/depth)and[weight](/weight)properties may be more applicable.[skills](/skills)

[JobPosting](/JobPosting)or[Occupation](/Occupation)or[Organization](/Organization)or[Person](/Person)[taxonomicRange](/taxonomicRange)

[BioChemEntity](/BioChemEntity)[teaches](/teaches)

[CreativeWork](/CreativeWork)or[EducationEvent](/EducationEvent)or[LearningResource](/LearningResource)[valueReference](/valueReference)

[PropertyValue](/PropertyValue)or[QualitativeValue](/QualitativeValue)or[QuantitativeValue](/QuantitativeValue)[variesBy](/variesBy)

[ProductGroup](/ProductGroup)[ProductGroup](/ProductGroup)vary, e.g. their size, color etc. Schema.org properties can be referenced by their short name e.g. "color"; terms defined elsewhere can be referenced with their URIs.#### More specific Types

#### Source

[https://github.com/schemaorg/schemaorg/issues/894](https://github.com/schemaorg/schemaorg/issues/894)

### Examples

[Example 1](#eg-0287)

Copied

Example notes or example HTML without markup.

Systems Research Engineer at a Software Publishers (NAICS code 511210)

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "JobPosting", "title": "Systems Research Engineer", "industry": { "@type": "DefinedTerm", "termCode": "511210", "name": "Software Publishers", "url": "https://www.naics.com/naics-code-description/?code=511210", "inDefinedTermSet": "NAICS (North American Industry Classification System)" } } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0314)

Copied

Example notes or example HTML without markup.

<div> <h1>Library of Congress Resource Type: <b>Manuscript</b></h1> Code: <b>Man</b> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/DefinedTerm"> <h1>Library of Congress Resource Type: <b><span itemprop="name">Manuscript</span></b></h1> Code: <b><span itemprop="termCode">Man</span></b> <link itemprop="inDefinedTermSet" href="http://id.loc.gov/vocabulary/resourceTypes"/> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="DefinedTerm"> <h1>Library of Congress Resource Type: <b><span property="name">Manuscript</span></b></h1> Code: <b><span property="termCode">Man</span></b> <link property="inDefinedTermSet" href="http://id.loc.gov/vocabulary/resourceTypes"/> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.{ "@context": "https://schema.org/", "@type": "DefinedTerm", "termCode": "Man", "inDefinedTermSet": "http://id.loc.gov/vocabulary/resourceTypes" }

Structured representation of the JSON-LD example.

[Example 3](#eg-0315)

Copied

Example notes or example HTML without markup.

<div> <div> <h1><a href="http://openjurist.org/dictionary/Ballentine">Ballentine's Law Dictionary</a></h1> </div> <div> <h2>Dictionary term</h2> Name: calendar year<br/> Description: The period from January 1st to December 31st, inclusive, of any year.<br/> In Dictionary: Ballentine's Law Dictionary </div> <div> <h2>Dictionary term</h2> Name: schema<br/> Description: A representation of a plan or theory in the form of an outline or model.<br/> In Dictionary: Ballentine's Law Dictionary </div> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div> <div itemscope itemtype="https://schema.org/DefinedTermSet"> <link itemprop="additionalType" href="https://schema.org/Book"> <h1><a itemprop="url" href="http://openjurist.org/dictionary/Ballentine"><span itemprop="name">Ballentine's Law Dictionary</span></a></h1> </div> <div itemscope itemtype="https://schema.org/DefinedTerm"> <h2>Dictionary term</h2> <link itemprop="url" href="http://openjurist.org/dictionary/Ballentine/term/calendar-year"/> Name: <span itemprop="name">calendar year</span><br/> Description: <span itemprop="description">The period from January 1st to December 31st, inclusive, of any year.</span><br/> In Dictionary: Ballentine's Law Dictionary <link itemprop="inDefinedTermSet" href="http://openjurist.org/dictionary/Ballentine"> </div> <div itemscope itemtype="https://schema.org/DefinedTerm"> <h2>Dictionary term</h2> <link itemprop="url" href="http://openjurist.org/dictionary/Ballentine/term/schema"/> Name: <span itemprop="name">schema</span><br/> Description: <span itemprop="description">A representation of a plan or theory in the form of an outline or model.</span><br/> In Dictionary: Ballentine's Law Dictionary <link itemprop="inDefinedTermSet" href="http://openjurist.org/dictionary/Ballentine"> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/"> <div typeof="DefinedTermSet Book"> <h1><a property="url" href="http://openjurist.org/dictionary/Ballentine"><span property="name">Ballentine's Law Dictionary</span></a></h1> </div> <div typeof="DefinedTerm"> <h2>Dictionary term</h2> <link property="url" href="http://openjurist.org/dictionary/Ballentine/term/calendar-year"/> Name: <span property="name">calendar year</span><br/> Description: <span property="description">The period from January 1st to December 31st, inclusive, of any year.</span><br/> In Dictionary: Ballentine's Law Dictionary <link property="inDefinedTermSet" href="http://openjurist.org/dictionary/Ballentine"> </div> <div typeof="DefinedTerm"> <h2>Dictionary term</h2> <link propery="url" href="http://openjurist.org/dictionary/Ballentine/term/schema"/> Name: <span property="name">schema</span><br/> Description: <span property="description">A representation of a plan or theory in the form of an outline or model.</span><br/> In Dictionary: Ballentine's Law Dictionary <link property="inDefinedTermSet" href="http://openjurist.org/dictionary/Ballentine"> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.[ { "@context": "https://schema.org/" }, { "@type": ["DefinedTermSet","Book"], "@id": "http://openjurist.org/dictionary/Ballentine", "name": "Ballentine's Law Dictionary" }, { "@type": "DefinedTerm", "@id": "http://openjurist.org/dictionary/Ballentine/term/calendar-year", "name": "calendar year", "description": "The period from January 1st to December 31st, inclusive, of any year.", "inDefinedTermSet": "http://openjurist.org/dictionary/Ballentine" }, { "@type": "DefinedTerm", "@id": "http://openjurist.org/dictionary/Ballentine/term/schema", "name": "schema", "description": "A representation of a plan or theory in the form of an outline or model.", "inDefinedTermSet": "http://openjurist.org/dictionary/Ballentine" } ]

Structured representation of the JSON-LD example.

[Example 4](#eg-0316)

Copied

Example notes or example HTML without markup.

<div> <h1>Occupation Term defined by <a href="http://onetonline.org">O*Net Online</a></h1> <h2>51-6042.00 - Shoe Machine Operators and Tenders</h2> Operate or tend a variety of machines to join, decorate, reinforce, or finish shoes and shoe parts. </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/DefinedTerm"> <h1>Occupation Term defined by <a itemprop="inDefinedTermSet" href="http://onetonline.org">O*Net Online</a></h1> <h2><span itemprop="termCode">51-6042.00</span> - <span itemprop="name">Shoe Machine Operators and Tenders</span></h2> <span itemprop="description">Operate or tend a variety of machines to join, decorate, reinforce, or finish shoes and shoe parts.</span> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="DefinedTerm"> <h1>Occupation Term defined by <a property="inDefinedTermSet" href="http://onetonline.org">O*Net Online</a></h1> <h2><span property="termCode">51-6042.00</span> - <span property="name">Shoe Machine Operators and Tenders</span></h2> <span property="description">Operate or tend a variety of machines to join, decorate, reinforce, or finish shoes and shoe parts.</span> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.{ "@context": "https://schema.org/", "@type": "DefinedTerm", "name": "Shoe Machine Operators and Tenders", "termCode": "51-6042.00", "description": "Operate or tend a variety of machines to join, decorate, reinforce, or finish shoes and shoe parts.", "inDefinedTermSet": "http://onetonline.org" }

Structured representation of the JSON-LD example.
