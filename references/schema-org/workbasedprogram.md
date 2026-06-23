---
title: "WorkBasedProgram"
source_url: https://schema.org/WorkBasedProgram
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# WorkBasedProgram

# WorkBasedProgram

A Schema.org Type

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/WorkBasedProgram
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+WorkBasedProgram)

A program with both an educational and employment component. Typically based at a workplace and structured around work-based learning, with the aim of instilling competencies related to an occupation. WorkBasedProgram is used to distinguish programs such as apprenticeships from school, college or other classroom based educational programs.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[occupationalCategory](/occupationalCategory)

[CategoryCode](/CategoryCode)or[Text](/Text)[BLS O*NET-SOC](http://www.onetcenter.org/taxonomy.html),[ISCO-08](https://www.ilo.org/public/english/bureau/stat/isco/isco08/)or similar, with the property repeated for each applicable value. Ideally the taxonomy should be identified, and both the textual label and formal code for the category should be provided.Note: for historical reasons, any textual label and formal code provided as a literal may be assumed to be from O*NET-SOC.

```
```[trainingSalary](/trainingSalary)

[MonetaryAmountDistribution](/MonetaryAmountDistribution)[EducationalOccupationalProgram](/EducationalOccupationalProgram)

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

[URL](/URL)#### Source

[https://github.com/schemaorg/schemaorg/issues/2289](https://github.com/schemaorg/schemaorg/issues/2289)

### Examples

[Example 1](#eg-0279)

Copied

Example notes or example HTML without markup.

a wage-based training program like a union apprenticeship in the United States.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "WorkBasedProgram", "name": "IBEW Apprenticeship", "provider": { "@type": "WorkersUnion", "name": "International Brotherhood of Electrical Workers" }, "occupationalCategory": "47-2111.00", "occupationalCredentialAwarded": { "@type": "EducationalOccupationalCredential", "credentialCategory": "Electrical workers license" }, "salaryUponCompletion": { "@type": "MonetaryAmountDistribution", "currency": "USD", "duration": "P1Y", "median": 41500.00 }, "trainingSalary": { "@type": "MonetaryAmountDistribution", "currency": "USD", "duration": "PT1H", "median": "16.00" } } </script>

Structured representation of the JSON-LD example.
