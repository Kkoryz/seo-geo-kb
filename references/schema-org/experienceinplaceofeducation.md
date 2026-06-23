---
title: "experienceInPlaceOfEducation"
source_url: https://schema.org/experienceInPlaceOfEducation
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# experienceInPlaceOfEducation

# experienceInPlaceOfEducation

A Schema.org Property

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/experienceInPlaceOfEducation
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+experienceInPlaceOfEducation)

Indicates whether a

[JobPosting](/JobPosting)will accept experience (as indicated by[OccupationalExperienceRequirements](/OccupationalExperienceRequirements)) in place of its formal educational qualifications (as indicated by[educationRequirements](/educationRequirements)). If true, indicates that satisfying one of these requirements is sufficient.### Values expected to be one of these types


### Used on these types


#### Source

[https://github.com/schemaorg/schemaorg/issues/2681](https://github.com/schemaorg/schemaorg/issues/2681)

### Examples

[Example 1](#eg-0465)

Copied

Example notes or example HTML without markup.

Example of Job markup for experience standing in place of formal qualifications.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "JobPosting", "title": "Software Engineer", "educationRequirements": { "@type": "EducationalOccupationalCredential", "credentialCategory": "bachelor degree" }, "experienceRequirements": { "@type": "OccupationalExperienceRequirements", "monthsOfExperience": "60" }, "experienceInPlaceOfEducation": true } </script>

Structured representation of the JSON-LD example.
