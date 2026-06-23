---
title: "DrugClass"
source_url: https://schema.org/DrugClass
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# DrugClass

# DrugClass

A Schema.org Type

- Canonical URL: https://schema.org/DrugClass
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+DrugClass)

A class of medical drugs, e.g., statins. Classes can represent general pharmacological class, common mechanisms of action, common physiological effects, etc.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[drug](/drug)

[Drug](/Drug)[MedicalEntity](/MedicalEntity)

```
```[code](/code)

[MedicalCode](/MedicalCode)```
```[funding](/funding)

[Grant](/Grant)[Grant](/Grant)that directly or indirectly provide funding or sponsorship for this item. See also[ownershipFundingInfo](/ownershipFundingInfo).Inverse property:

[fundedItem](/fundedItem)```
```[guideline](/guideline)

[MedicalGuideline](/MedicalGuideline)```
```[legalStatus](/legalStatus)

[DrugLegalStatus](/DrugLegalStatus)or[MedicalEnumeration](/MedicalEnumeration)or[Text](/Text)```
```[medicineSystem](/medicineSystem)

[MedicineSystem](/MedicineSystem)```
```[recognizingAuthority](/recognizingAuthority)

[Organization](/Organization)```
```[relevantSpecialty](/relevantSpecialty)

[MedicalSpecialty](/MedicalSpecialty)```
```[study](/study)

[MedicalStudy](/MedicalStudy)[Thing](/Thing)

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

[DrugClass](/DrugClass)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[Drug](/Drug)[possibleTreatment](/possibleTreatment)

[MedicalCondition](/MedicalCondition)or[MedicalSignOrSymptom](/MedicalSignOrSymptom)[secondaryPrevention](/secondaryPrevention)

[MedicalCondition](/MedicalCondition)### Examples

[Example 1](#eg-0225)

Copied

Example notes or example HTML without markup.

<h1>About High Blood Pressure (hypertension)</h1> <h2>Diagnosis</h2> High blood pressure is diagnosed by measuring ... ... <h2>Treatment</h2> There are many common treatments for high blood pressure, including beta-blocker drugs such as propanaolol (Innopran) and atenonlol (Tenormin) ...

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<body itemscope itemtype="https://schema.org/MedicalWebPage"> <link itemprop="audience" href="https://schema.org/Patient" /> <link itemprop="specialty" href="https://schema.org/Cardiovascular" /> <meta itemprop="lastReviewed" content="2011-09-14"/> <h1>About <span itemprop="about" itemscope itemtype="https://schema.org/MedicalCondition"> <span itemprop="name">High Blood Pressure</span> (<span itemprop="name">hypertension</span>)</span> </h1> ... <h2><span itemprop="mainContentOfPage">Diagnosis</span></h2> High blood pressure is diagnosed by measuring ... ... <h2><span itemprop="mainContentOfPage">Treatment</span></h2> There are many common treatments for high blood pressure, including <span itemscope itemtype="https://schema.org/DrugClass"> <span itemprop="name">beta-blocker</span> drugs such as <span itemprop="drug" itemscope itemtype="https://schema.org/Drug"> <span itemprop="nonProprietaryName">propanaolol</span> (<span itemprop="alternateName">Innopran</span>) </span> and <span itemprop="drug" itemscope itemtype="https://schema.org/Drug"> <span itemprop="nonProprietaryName">atenolol</span> (<span itemprop="alternateName">Tenormin</span>) </span> ... </span> </body>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<body vocab="https://schema.org/" typeof="MedicalWebPage"> <link property="audience" href="https://schema.org/Patient" /> <link property="specialty" href="https://schema.org/Cardiovascular" /> <meta property="lastReviewed" content="2011-09-14"/> <h1>About <span property="about" typeof="MedicalCondition"> <span property="name">High Blood Pressure</span> (<span property="name">hypertension</span>)</span> </h1> ... <h2><span property="mainContentOfPage">Diagnosis</span></h2> High blood pressure is diagnosed by measuring ... ... <h2><span property="mainContentOfPage">Treatment</span></h2> There are many common treatments for high blood pressure, including <span typeof="DrugClass"> <span property="name">beta-blocker</span> drugs such as <span property="drug" typeof="Drug"> <span property="nonProprietaryName">propanaolol</span> (<span property="alternateName">Innopran</span>) </span> and <span property="drug" typeof="Drug"> <span property="nonProprietaryName">atenolol</span> (<span property="alternateName">Tenormin</span>) </span> ... ... </span> </body>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "MedicalWebPage", "about": { "@type": "MedicalCondition", "name": [ "High Blood Pressure", "hypertension" ] }, "mainContentOfPage": [ "Diagnosis", "Treatment" ], "audience": "https://schema.org/Patient", "about": [ { "@type": "Drug", "nonProprietaryName": "propanaolol", "alternateName": "Innopran" }, { "@type": "Drug", "nonProprietaryName": "atenolol", "alternateName": "Tenormin" } ], "lastReviewed": "2011-09-14", "name": "beta-blocker", "specialty": "https://schema.org/Cardiovascular" } </script>

Structured representation of the JSON-LD example.
