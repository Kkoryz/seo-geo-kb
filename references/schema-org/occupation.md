---
title: "Occupation"
source_url: https://schema.org/Occupation
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# Occupation

# Occupation

A Schema.org Type

- Canonical URL: https://schema.org/Occupation
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+Occupation)

A profession, may involve prolonged training and/or a formal qualification.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[educationRequirements](/educationRequirements)

[EducationalOccupationalCredential](/EducationalOccupationalCredential)or[Text](/Text)```
```[estimatedSalary](/estimatedSalary)

[MonetaryAmount](/MonetaryAmount)or[MonetaryAmountDistribution](/MonetaryAmountDistribution)or[Number](/Number)```
```[experienceRequirements](/experienceRequirements)

[OccupationalExperienceRequirements](/OccupationalExperienceRequirements)or[Text](/Text)```
```[occupationLocation](/occupationLocation)

[AdministrativeArea](/AdministrativeArea)```
```[occupationalCategory](/occupationalCategory)

[CategoryCode](/CategoryCode)or[Text](/Text)[BLS O*NET-SOC](http://www.onetcenter.org/taxonomy.html),[ISCO-08](https://www.ilo.org/public/english/bureau/stat/isco/isco08/)or similar, with the property repeated for each applicable value. Ideally the taxonomy should be identified, and both the textual label and formal code for the category should be provided.Note: for historical reasons, any textual label and formal code provided as a literal may be assumed to be from O*NET-SOC.

```
```[qualifications](/qualifications)

[Credential](/Credential)or[Text](/Text)```
```[responsibilities](/responsibilities)

[Text](/Text)```
```[skills](/skills)

[DefinedTerm](/DefinedTerm)or[Text](/Text)[Thing](/Thing)

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

[Occupation](/Occupation)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[Person](/Person)[relevantOccupation](/relevantOccupation)

[JobPosting](/JobPosting)#### Source

[https://github.com/schemaorg/schemaorg/issues/1698](https://github.com/schemaorg/schemaorg/issues/1698)

### Examples

[Example 1](#eg-0249)

Copied

Example notes or example HTML without markup.

See JSON example.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Person", "name": "Peter Venkman", "hasOccupation": { "@type": "Occupation", "name": "Parapsychologist", "educationRequirements": "PhD in parapsychology" } } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0250)

Copied

Example notes or example HTML without markup.

See JSON example.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Person", "name": "Albert Einstein", "hasOccupation": [ { "@type": "Role", "hasOccupation": { "@type": "Occupation", "name": "Patent examiner", "occupationalCategory": "23-2099.00" }, "startDate": "1901", "endDate": "1906" }, { "@type": "Occupation", "name": "Professor of Physics", "educationRequirements": "PhD in Physics" } ] } </script>

Structured representation of the JSON-LD example.

[Example 3](#eg-0251)

Copied

Example notes or example HTML without markup.

See JSON example.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "JobPosting", "name": "Mobile App Developer", "hiringOrganization": { "@type": "Organization", "name": "ACME Software" }, "relevantOccupation": { "@type": "Occupation", "name": "Software Developers, Applications", "occupationalCategory": { "@type": "CategoryCode", "inCodeSet": { "@type": "CategoryCodeSet", "name": "O*Net-SOC", "dateModified": "2019", "url": "https://www.onetonline.org/" }, "codeValue": "15-1132.00", "name": "Software Developers, Applications", "url": "https://www.onetonline.org/link/summary/15-1132.00" } } } </script>

Structured representation of the JSON-LD example.

[Example 4](#eg-0252)

Copied

Example notes or example HTML without markup.

See JSON example.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Occupation", "name": "Nurse Practioner", "educationRequirements": "Graduate degree in nursing", "occupationalCategory": "29-1171.00", "occupationLocation": { "@type": "Country", "name": "USA", "sameAs": "https://www.wikidata.org/wiki/Q30" }, "qualifications": "Registered nurse licensure in state where practicing", "responsibilities": "Diagnose and treat acute, episodic, or chronic illness, independently or as part of a healthcare team.", "skills": ["Active listening", "Critical thinking", "Social awareness"], "estimatedSalary": { "@type": "MonetaryAmountDistribution", "duration": "1Y", "currency": "USD", "percentile10": 72000, "percentile25": 86000, "median": 109000, "percentile75": 120000, "percentile90": 140000 } } </script>

Structured representation of the JSON-LD example.

[Example 5](#eg-0261)

Copied

Example notes or example HTML without markup.

<h1>Occupation: Research Scientist</h1> <h2>educationRequirements"</h2> <p>PhD or equivalent<p>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Occupation"> <h1>Occupation: <span itemprop="name"> Research Scientist</span></h1> <h2>qualifications</h2> <p itemprop="educationRequirements" itemscope itemtype="https://schema.org/EducationalOccupationalCredential"> <span itemprop="educationalLevel">PhD or equivalent</span> </p> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="https://schema.org/Occupation"> <h1>Occupation: <span property="name"> Research Scientist</span></h1> <h2>qualifications</h2> <p property="educationRequirements" typeof="https://schema.org/EducationalOccupationalCredential"> <span property="educationalLevel">PhD or equivalent</span> </p> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Occupation", "name": "Research Scientist", "qualifications": { "@type": "EducationalOccupationalCredential", "educationalLevel": "PhD or equivalent" } } </script>

Structured representation of the JSON-LD example.

[Example 6](#eg-0275)

Copied

Example notes or example HTML without markup.

<!-- occupationalCategory utilising CategoryCode --> <!-- JSONLD only example -->

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<!-- occupationalCategory utilising CategoryCode --> <script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Occupation", "occupationalCategory": { "@type": "CategoryCode", "inCodeSet": { "@type": "CategoryCodeSet", "name": "O*Net-SOC", "dateModified": "2019", "url": "https://www.onetonline.org/" }, "codeValue": "15-1211.00", "name": "Computer Systems Analysts", "url": "https://www.onetonline.org/link/summary/15-1121.00" } } </script>

Structured representation of the JSON-LD example.
