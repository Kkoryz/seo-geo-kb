---
title: "educationRequirements"
source_url: https://schema.org/educationRequirements
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# educationRequirements

# educationRequirements

A Schema.org Property

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/educationRequirements
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+educationRequirements)

Educational background needed for the position or Occupation.

### Values expected to be one of these types


### Used on these types


#### Source

[https://github.com/schemaorg/schemaorg/issues/1698](https://github.com/schemaorg/schemaorg/issues/1698)

[https://github.com/schemaorg/schemaorg/issues/1779](https://github.com/schemaorg/schemaorg/issues/1779)

### Examples

[Example 1](#eg-0261)

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

[Example 2](#eg-0465)

Copied

Example notes or example HTML without markup.

Example of Job markup for experience standing in place of formal qualifications.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "JobPosting", "title": "Software Engineer", "educationRequirements": { "@type": "EducationalOccupationalCredential", "credentialCategory": "bachelor degree" }, "experienceRequirements": { "@type": "OccupationalExperienceRequirements", "monthsOfExperience": "60" }, "experienceInPlaceOfEducation": true } </script>

Structured representation of the JSON-LD example.
