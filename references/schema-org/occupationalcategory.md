---
title: "occupationalCategory"
source_url: https://schema.org/occupationalCategory
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# occupationalCategory

# occupationalCategory

A Schema.org Property

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/occupationalCategory
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+occupationalCategory)

A category describing the job, preferably using a term from a taxonomy such as


Note: for historical reasons, any textual label and formal code provided as a literal may be assumed to be from O*NET-SOC.

[BLS O*NET-SOC](http://www.onetcenter.org/taxonomy.html),[ISCO-08](https://www.ilo.org/public/english/bureau/stat/isco/isco08/)or similar, with the property repeated for each applicable value. Ideally the taxonomy should be identified, and both the textual label and formal code for the category should be provided.Note: for historical reasons, any textual label and formal code provided as a literal may be assumed to be from O*NET-SOC.

### Values expected to be one of these types


### Used on these types


#### Source

[https://github.com/schemaorg/schemaorg/issues/1698](https://github.com/schemaorg/schemaorg/issues/1698)

[https://github.com/schemaorg/schemaorg/issues/3420](https://github.com/schemaorg/schemaorg/issues/3420)

[https://github.com/schemaorg/schemaorg/issues/2460](https://github.com/schemaorg/schemaorg/issues/2460)

[https://github.com/schemaorg/schemaorg/issues/2289](https://github.com/schemaorg/schemaorg/issues/2289)

[https://github.com/schemaorg/schemaorg/issues/2192](https://github.com/schemaorg/schemaorg/issues/2192)

### Examples

[Example 1](#eg-0250)

Copied

Example notes or example HTML without markup.

See JSON example.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Person", "name": "Albert Einstein", "hasOccupation": [ { "@type": "Role", "hasOccupation": { "@type": "Occupation", "name": "Patent examiner", "occupationalCategory": "23-2099.00" }, "startDate": "1901", "endDate": "1906" }, { "@type": "Occupation", "name": "Professor of Physics", "educationRequirements": "PhD in Physics" } ] } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0251)

Copied

Example notes or example HTML without markup.

See JSON example.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "JobPosting", "name": "Mobile App Developer", "hiringOrganization": { "@type": "Organization", "name": "ACME Software" }, "relevantOccupation": { "@type": "Occupation", "name": "Software Developers, Applications", "occupationalCategory": { "@type": "CategoryCode", "inCodeSet": { "@type": "CategoryCodeSet", "name": "O*Net-SOC", "dateModified": "2019", "url": "https://www.onetonline.org/" }, "codeValue": "15-1132.00", "name": "Software Developers, Applications", "url": "https://www.onetonline.org/link/summary/15-1132.00" } } } </script>

Structured representation of the JSON-LD example.

[Example 3](#eg-0275)

Copied

Example notes or example HTML without markup.

<!-- occupationalCategory utilising CategoryCode --> <!-- JSONLD only example -->

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<!-- occupationalCategory utilising CategoryCode --> <script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Occupation", "occupationalCategory": { "@type": "CategoryCode", "inCodeSet": { "@type": "CategoryCodeSet", "name": "O*Net-SOC", "dateModified": "2019", "url": "https://www.onetonline.org/" }, "codeValue": "15-1211.00", "name": "Computer Systems Analysts", "url": "https://www.onetonline.org/link/summary/15-1121.00" } } </script>

Structured representation of the JSON-LD example.
