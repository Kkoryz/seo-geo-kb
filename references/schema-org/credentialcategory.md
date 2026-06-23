---
title: "credentialCategory"
source_url: https://schema.org/credentialCategory
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# credentialCategory

# credentialCategory

A Schema.org Property

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/credentialCategory
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+credentialCategory)

The category or type of credential being described, for example "degree”, “certificate”, “badge”, or more specific term.

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

[Example 2](#eg-0260)

Copied

Example notes or example HTML without markup.

<h1>Certified Safety Professional</h1> <p>Certified Safety Professionals (CSP) are persons who perform at least 50% of professional level safety duties, including making worksite assessments to determine risks, assessing potential hazards and controls, evaluating risks and hazard control measures, investigating incidents, maintaining and evaluating incident and loss records, and preparing emergency response plans.</p>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/EducationalOccupationalCredential"> <h1 itemprop="name">Certified Safety Professional</h1> <link itemprop="url" href="https://www.bcsp.org/CSP" /> <p itemprop="description">Certified Safety Professionals (CSP) are persons who perform at least 50% of professional level safety duties, including making worksite assessments to determine risks, assessing potential hazards and controls, evaluating risks and hazard control measures, investigating incidents, maintaining and evaluating incident and loss records, and preparing emergency response plans.</p> <div itemprop="credentialCategory" itemscope itemtype="https://schema.org/DefinedTerm"> <meta itemprop="name" content="Certification" /> <link itemprop="url" href="http://purl.org/ctdl/terms/Certification" /> <div itemprop="inDefinedTermSet" itemscope itemtype="https://schema.org/DefinedTermSet"> <meta itemprop="name" content="Credential Transparency Description Language"/> <link itemprop="url" content="http://purl.org/ctdl/terms/" /> </div> </div> <link itemprop="additionalType" href="http://purl.org/ctdl/terms/Certification"> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="EducationalOccupationalCredential"> <h1 property="name">Certified Safety Professional</h1> <link property="url" href="https://www.bcsp.org/CSP" /> <p property="description">Certified Safety Professionals (CSP) are persons who perform at least 50% of professional level safety duties, including making worksite assessments to determine risks, assessing potential hazards and controls, evaluating risks and hazard control measures, investigating incidents, maintaining and evaluating incident and loss records, and preparing emergency response plans.</p> <div property="credentialCategory" typeof="DefinedTerm" resource="http://purl.org/ctdl/terms/Certification"> <meta property="name" content="Certification" /> <div property="inDefinedTermSet" typeof="https://schema.org/DefinedTermSet" resource="http://purl.org/ctdl/terms/"> <meta property="name" content="Credential Transparency Description Language"/> </div> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": [ "EducationalOccupationalCredential" ], "name": "Certified Safety Professional", "url": "https://www.bcsp.org/CSP", "description": "Certified Safety Professionals (CSP) are persons who perform at least 50% of professional level safety duties, including making worksite assessments to determine risks, assessing potential hazards and controls, evaluating risks and hazard control measures, investigating incidents, maintaining and evaluating incident and loss records, and preparing emergency response plans.", "credentialCategory": { "@type": "DefinedTerm", "@id": "http://purl.org/ctdl/terms/Certification", "name": "Certification", "inDefinedTermSet": { "@type": "DefinedTermSet", "@id": "http://purl.org/ctdl/terms/", "name": "Credential Transparency Description Language" } } } </script>

Structured representation of the JSON-LD example.

[Example 3](#eg-0465)

Copied

Example notes or example HTML without markup.

Example of Job markup for experience standing in place of formal qualifications.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "JobPosting", "title": "Software Engineer", "educationRequirements": { "@type": "EducationalOccupationalCredential", "credentialCategory": "bachelor degree" }, "experienceRequirements": { "@type": "OccupationalExperienceRequirements", "monthsOfExperience": "60" }, "experienceInPlaceOfEducation": true } </script>

Structured representation of the JSON-LD example.
