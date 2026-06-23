---
title: "EducationalOccupationalProgram"
source_url: https://schema.org/EducationalOccupationalProgram
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# EducationalOccupationalProgram

# EducationalOccupationalProgram

A Schema.org Type

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/EducationalOccupationalProgram
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+EducationalOccupationalProgram)

A program offered by an institution which determines the learning progress to achieve an outcome, usually a credential like a degree or certificate. This would define a discrete set of opportunities (e.g., job, courses) that together constitute a program with a clear start, end, set of requirements, and transition to a new occupational opportunity (e.g., a job), or sometimes a higher educational opportunity (e.g., an advanced degree).

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[applicationDeadline](/applicationDeadline)

[Date](/Date)or[Text](/Text)```
```[applicationStartDate](/applicationStartDate)

[Date](/Date)```
```[dayOfWeek](/dayOfWeek)

[DayOfWeek](/DayOfWeek)```
```[educationalCredentialAwarded](/educationalCredentialAwarded)

[EducationalOccupationalCredential](/EducationalOccupationalCredential)or[Text](/Text)or[URL](/URL)```
```[educationalProgramMode](/educationalProgramMode)

[Text](/Text)or[URL](/URL)```
```[endDate](/endDate)

[Date](/Date)or[DateTime](/DateTime)[ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).```
```[financialAidEligible](/financialAidEligible)

[DefinedTerm](/DefinedTerm)or[Text](/Text)```
```[hasCourse](/hasCourse)

[Course](/Course)```
```[maximumEnrollment](/maximumEnrollment)

[Integer](/Integer)```
```[numberOfCredits](/numberOfCredits)

[Integer](/Integer)or[StructuredValue](/StructuredValue)```
```[occupationalCategory](/occupationalCategory)

[CategoryCode](/CategoryCode)or[Text](/Text)[BLS O*NET-SOC](http://www.onetcenter.org/taxonomy.html),[ISCO-08](https://www.ilo.org/public/english/bureau/stat/isco/isco08/)or similar, with the property repeated for each applicable value. Ideally the taxonomy should be identified, and both the textual label and formal code for the category should be provided.Note: for historical reasons, any textual label and formal code provided as a literal may be assumed to be from O*NET-SOC.

```
```[occupationalCredentialAwarded](/occupationalCredentialAwarded)

[EducationalOccupationalCredential](/EducationalOccupationalCredential)or[Text](/Text)or[URL](/URL)```
```[offers](/offers)

[Demand](/Demand)or[Offer](/Offer)[businessFunction](/businessFunction)to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can also be used to describe a[Demand](/Demand). While this property is listed as expected on a number of common types, it can be used in others. In that case, using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.Inverse property:

[itemOffered](/itemOffered)```
```[programPrerequisites](/programPrerequisites)

[AlignmentObject](/AlignmentObject)or[Course](/Course)or[EducationalOccupationalCredential](/EducationalOccupationalCredential)or[Text](/Text)```
```[programType](/programType)

[DefinedTerm](/DefinedTerm)or[Text](/Text)```
```[provider](/provider)

[Organization](/Organization)or[Person](/Person)[carrier](/carrier).```
```[salaryUponCompletion](/salaryUponCompletion)

[MonetaryAmountDistribution](/MonetaryAmountDistribution)```
```[startDate](/startDate)

[Date](/Date)or[DateTime](/DateTime)[ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).```
```[termDuration](/termDuration)

[Duration](/Duration)```
```[termsPerYear](/termsPerYear)

[Number](/Number)```
```[timeOfDay](/timeOfDay)

[Text](/Text)```
```[timeToComplete](/timeToComplete)

[Duration](/Duration)```
```[trainingSalary](/trainingSalary)

[MonetaryAmountDistribution](/MonetaryAmountDistribution)```
```[typicalCreditsPerTerm](/typicalCreditsPerTerm)

[Integer](/Integer)or[StructuredValue](/StructuredValue)[Thing](/Thing)

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

[URL](/URL)#### More specific Types

#### Source

[https://github.com/schemaorg/schemaorg/issues/2289](https://github.com/schemaorg/schemaorg/issues/2289)

### Examples

[Example 1](#eg-0278)

Copied

Example notes or example HTML without markup.

A 4 year educational program from a local university.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "EducationalOccupationalProgram", "name": "Undergraduate CS degree from ACME College", "url": "http://www.acme.edu/CS", "provider": { "@type": "CollegeOrUniversity", "name": "ACME Community College", "address": { "@type": "PostalAddress", "streetAddress": "123 Main Street", "addressLocality": "Boston", "addressRegion": "MA", "postalCode": "02134" } }, "timeToComplete": "P4Y", "educationalCredentialAwarded": { "@type": "EducationalOccupationalCredential", "credentialCategory": "Bachelor of Science in Computer Science" }, "programPrerequisites": { "@type": "EducationalOccupationalCredential", "credentialCategory": "High school diploma" }, "offers": [ { "@type": "Offer", "category": "Resident Tuition", "priceSpecification": { "@type": "PriceSpecification", "price": 16278, "priceCurrency": "USD" } }, { "@type": "Offer", "category": "International Tuition", "priceSpecification": { "@type": "PriceSpecification", "price": 37344, "priceCurrency": "USD" } }, { "@type": "Offer", "category": "Other Tuition", "priceSpecification": { "@type": "PriceSpecification", "price": 35599, "priceCurrency": "USD" } }, { "@type": "Offer", "category": "Room and Board", "priceSpecification": { "@type": "PriceSpecification", "price": 13588, "priceCurrency": "USD" } } ] } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0294)

Copied

Example notes or example HTML without markup.

A university program with a fixed application window and maximum enrollment.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "EducationalOccupationalProgram", "name": "ACME University Basketweaving Program", "applicationStartDate": "2019-09-01", "applicationDeadline": "2019-12-31", "educationalProgramMode": "full-time", "numberOfCredits": 32, "maximumEnrollment": 100, "termDuration": "P4M", "termsPerYear": 2, "typicalCreditsPerTerm": 4 } </script>

Structured representation of the JSON-LD example.
