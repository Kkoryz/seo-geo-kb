---
title: "competencyRequired"
source_url: https://schema.org/competencyRequired
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# competencyRequired

# competencyRequired

A Schema.org Property

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/competencyRequired
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+competencyRequired)

Knowledge, skill, ability or personal attribute that must be demonstrated by a person or other entity in order to do something such as earn an Educational Occupational Credential or understand a LearningResource.

### Values expected to be one of these types


### Used on these types


#### Source

[https://github.com/schemaorg/schemaorg/issues/1779](https://github.com/schemaorg/schemaorg/issues/1779)

### Examples

[Example 1](#eg-0259)

Copied

Example notes or example HTML without markup.

<h1>HNC Facilities Management</h1> <p>Higher National qualifications provide practical skills and theoretical knowledge that meet the needs of employers. The HNC in Facilities Management (SCQF level 7) develops knowledge and skills of the modern Facilities Management industry including both ‘hard’ and ‘soft’ services, and is aimed at those in supervisory and management roles or aspiring managers within the wider realm of Facilities Services.</p> <h2>Mapping to National Occupational Standards</h2> <ul> <li>ASTFM401 Understand facilities management and its place in the organisation</li> <li>[etc]</li> </ul>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/EducationalOccupationalCredential"> <h1 itemprop="name">HNC Facilities Management</h1> <p itemprop="description">Higher National qualifications provide practical skills and theoretical knowledge that meet the needs of employers. The HNC in Facilities Management (SCQF level 7) develops knowledge and skills of the modern Facilities Management industry including both ‘hard’ and ‘soft’ services, and is aimed at those in supervisory and management roles or aspiring managers within the wider realm of Facilities Services.</p> <div itemprop="educationalLevel" itemscope itemtype="https://schema.org/DefinedTerm"> <meta itemprop="name" content="SCQF Level 7" /> <link itemprop="inDefinedTermSet" href="https://www.sqa.org.uk/sqa/71377.html" /> </div> <div itemprop="credentialCategory" itemscope itemtype="https://schema.org/DefinedTerm"> <meta itemprop="name" content="Higher National Certificate" /> <meta itemprop="termCode" content="HNC" /> </div> <h2>Mapping to National Occupational Standards</h2> <ul> <li itemprop="competencyRequired" itemscope itemtype="https://schema.org/DefinedTerm"> <span itemprop="termCode">ASTFM401</span> <span itemprop="name">Understand facilities management and its place in the organisation</span> <link itemprop="url" href="https://www.ukstandards.org.uk/PublishedNos/ASTFM401.pdf" /> <link itemprop="inDefinedTermSet" href="https://www.ukstandards.org.uk/" /> </li> <li>[etc]</li> </ul> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="EducationalOccupationalCredential"> <h1 property="name">HNC Facilities Management</h1> <p property="description">Higher National qualifications provide practical skills and theoretical knowledge that meet the needs of employers. The HNC in Facilities Management (SCQF level 7) develops knowledge and skills of the modern Facilities Management industry including both ‘hard’ and ‘soft’ services, and is aimed at those in supervisory and management roles or aspiring managers within the wider realm of Facilities Services.</p> <div property="educationalLevel" typeof="DefinedTerm"> <meta property="name" content="SCQF Level 7" /> <link property="inDefinedTermSet" href="https://www.sqa.org.uk/sqa/71377.html" /> </div> <div property="credentialCategory" typeof="DefinedTerm"> <meta property="name" content="Higher National Certificate" /> <meta property="termCode" content="HNC" /> </div> <h2>Mapping to National Occupational Standards</h2> <ul> <li property="competencyRequired" typeof="DefinedTerm"> <span property="termCode">ASTFM401</span> <span property="name">Understand facilities management and its place in the organisation</span> <link property="url" href="https://www.ukstandards.org.uk/PublishedNos/ASTFM401.pdf" /> <link property="inDefinedTermSet" href="https://www.ukstandards.org.uk/" /> </li> <li>[etc]</li> </ul> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "EducationalOccupationalCredential", "name" : "HNC Facilities Management", "description" : "Higher National qualifications provide practical skills and theoretical knowledge that meet the needs of employers. The HNC in Facilities Management (SCQF level 7) develops knowledge and skills of the modern Facilities Management industry including both ‘hard’ and ‘soft’ services, and is aimed at those in supervisory and management roles or aspiring managers within the wider realm of Facilities Services.", "educationalLevel" : { "@type": "DefinedTerm", "name": "SCQF Level 7", "inDefinedTermSet": "https://www.sqa.org.uk/sqa/71377.html" }, "credentialCategory" : { "@type": "DefinedTerm", "name": "Higher National Certificate", "termCode": "HNC" }, "competencyRequired" : { "@type": "DefinedTerm", "termCode": "ASTFM401", "name": "Understand facilities management and its place in the organisation", "url": "https://www.ukstandards.org.uk/PublishedNos/ASTFM401.pdf", "inDefinedTermSet": "https://www.ukstandards.org.uk/" } } </script>

Structured representation of the JSON-LD example.
