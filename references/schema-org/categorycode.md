---
title: "CategoryCode"
source_url: https://schema.org/CategoryCode
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# CategoryCode

# CategoryCode

A Schema.org Type

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/CategoryCode
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+CategoryCode)

A Category Code.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[codeValue](/codeValue)

[Text](/Text)```
```[inCodeSet](/inCodeSet)

[CategoryCodeSet](/CategoryCodeSet)or[URL](/URL)[CategoryCodeSet](/CategoryCodeSet)that contains this category code.[DefinedTerm](/DefinedTerm)

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

[CategoryCode](/CategoryCode)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[ActionAccessSpecification](/ActionAccessSpecification)or[Guide](/Guide)or[Invoice](/Invoice)or[Offer](/Offer)or[PhysicalActivity](/PhysicalActivity)or[Product](/Product)or[Recommendation](/Recommendation)or[Service](/Service)or[SpecialAnnouncement](/SpecialAnnouncement)[hasCategoryCode](/hasCategoryCode)

[CategoryCodeSet](/CategoryCodeSet)[legislationType](/legislationType)

[Legislation](/Legislation)[occupationalCategory](/occupationalCategory)

[EducationalOccupationalProgram](/EducationalOccupationalProgram)or[JobPosting](/JobPosting)or[Occupation](/Occupation)or[Physician](/Physician)or[WorkBasedProgram](/WorkBasedProgram)[BLS O*NET-SOC](http://www.onetcenter.org/taxonomy.html),[ISCO-08](https://www.ilo.org/public/english/bureau/stat/isco/isco08/)or similar, with the property repeated for each applicable value. Ideally the taxonomy should be identified, and both the textual label and formal code for the category should be provided.Note: for historical reasons, any textual label and formal code provided as a literal may be assumed to be from O*NET-SOC.

#### More specific Types

#### Source

[https://github.com/schemaorg/schemaorg/issues/894](https://github.com/schemaorg/schemaorg/issues/894)

### Examples

[Example 1](#eg-0317)

Copied

Example notes or example HTML without markup.

<div> <h1 >Defined Values in The Mammal Classification List</h1> <ul> <li>Carnivore - A mammal that feeds on other animals</li> </ul> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/CategoryCodeSet" id="C1"> <h1>Defined Values in <span itemprop="name">The Mammal Classification List</span></h1> <ul> <li itemprop="hasCategoryCode" itemscope itemtype="https://schema.org/CategoryCode"> <span itemprop="name">Carnivore</span> - <span itemprop="description">A mammal that feeds on other animals</span> <link itemprop="inCodeSet" href="#C1"/> </li> </ul> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="CategoryCodeSet" id="C1"> <h1>Defined Values in <span property="name">The Mammal Classification List</span></h1> <ul> <li property="hasCategoryCode" typeof="CategoryCode"> <span property="name">Carnivore</span> - <span property="description">A mammal that feeds on other animals</span> <link property="inCodeSet" href="#C1"/> </li> </ul> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.{ "@context": "https://schema.org/", "@type": "CategoryCodeSet", "@id": "_C1", "name": "The Mammal Classification List", "hasCategoryCode": { "@type": "CategoryCode", "name": "Carnivore", "description": "A mammal that feeds on other animals", "inCodeSet": "_C1" } }

Structured representation of the JSON-LD example.

[Example 2](#eg-0318)

Copied

Example notes or example HTML without markup.

<div> <h1>ISO 639-2: Codes for the Representation of Names of Languages<h1> <h2>Listing of codes:</h2> <ul> <li>...</li> <li>cze</li> <li>...</li> </ul> </div> <div> <h2>Czech; tchèque; Tschechisch</h2> <h3>From: ISO 639-2: Codes for the Representation of Names of Languages</h3> English: Czech<br/> French: tchèque<br/> German: Tschechisch<br/> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/CategoryCodeSet" itemid="http://id.loc.gov/vocabulary/iso639-2"> <h1 itemprop="name">ISO 639-2: Codes for the Representation of Names of Languages</h1> <h2>Listing of codes:</h2> <ul> <li>...</li> <li><span itemprop="hasCategoryCode" itemid="http://id.loc.gov/vocabulary/iso639-2/cze">cze</span></li> <li>...</li> </ul> </div> <div itemscope itemtype="https://schema.org/CategoryCode" itemid="http://id.loc.gov/vocabulary/iso639-2/cze"> <meta itemprop="codeValue" content="cze"> <h2>Czech; tchèque; Tschechisch</h2> <link itemprop="inCodeSet" href="http://id.loc.gov/vocabulary/iso639-2"> <h3>From: ISO 639-2: Codes for the Representation of Names of Languages</h3> <span itemprop="name" xml:lang="en" content="Czech">English: Czech</span><br/> <span itemprop="name" xml:lang="fr" content="tchèque">French: tchèque</span><br/> <span itemprop="name" xml:lang="de" content="Tschechisch">German: Tschechisch</span><br/> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="CategoryCodeSet" resource="http://id.loc.gov/vocabulary/iso639-2"> <h1 property="name">ISO 639-2: Codes for the Representation of Names of Languages</h1> <h2>Listing of codes:</h2> <ul> <li>...</li> <li><span property="hasCategoryCode" resource="http://id.loc.gov/vocabulary/iso639-2/cze">cze</span></li> <li>...</li> </ul> </div> <div vocab="https://schema.org/" typeof="CategoryCode" resource="http://id.loc.gov/vocabulary/iso639-2/cze"> <meta property="codeValue" content="cze"> <h2>Czech; tchèque; Tschechisch</h2> <link property="inCodeSet" href="http://id.loc.gov/vocabulary/iso639-2"> <h3>From: ISO 639-2: Codes for the Representation of Names of Languages</h3> <span property="name" xml:lang="en" content="Czech">English: Czech</span><br/> <span property="name" xml:lang="fr" content="tchèque">French: tchèque</span><br/> <span property="name" xml:lang="de" content="Tschechisch">German: Tschechisch</span><br/> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.[ { "@context": "https://schema.org/" }, { "@type": "CategoryCodeSet", "@id": "http://id.loc.gov/vocabulary/iso639-2", "name": "ISO 639-2: Codes for the Representation of Names of Languages", "hasCategoryCode": "http://id.loc.gov/vocabulary/iso639-2/cze" }, { "@type": "CategoryCode", "@id": "http://id.loc.gov/vocabulary/iso639-2/cze", "codeValue": "cze", "name": { "en": "Czech", "fr": "tchèque", "de": "Tschechisch" }, "inCodeSet": "http://id.loc.gov/vocabulary/iso639-2" } ]

Structured representation of the JSON-LD example.
