---
title: "provider"
source_url: https://schema.org/provider
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# provider

# provider

A Schema.org Property

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/provider
- Equivalent Property: unece:ServiceProvider
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+provider)

The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller.

### Values expected to be one of these types


### Used on these types


| Supersedes |
|---|
```
``` |

#### Source

[https://github.com/schemaorg/schemaorg/issues/2927](https://github.com/schemaorg/schemaorg/issues/2927)

[https://github.com/schemaorg/schemaorg/issues/2289](https://github.com/schemaorg/schemaorg/issues/2289)

### Examples

[Example 1](#eg-0337)

Copied

Example notes or example HTML without markup.

<body> <!-- A MOOC created by an Institution, offered through a MOOC platform, with named instructor --> <!-- Based on https://www.coursera.org/course/datascitoolbox --> <main> <h1>The Data Scientist's Toolbox</h1> <h2> Johns Hopkins University </h2> <h2>About this Course</h2> <div> <h2>Instructors</h2> <div> <a href="http://example.org/instructor/~315" > <p>Jeff Leek, PhD</p> <div>Associate Professor, Biostatistics</div> <div>Bloomberg School of Public Health </div> </a> </div> </div> </main> </body>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<body vocab="https://schema.org/"> <!-- A MOOC created by an Institution, offered through a MOOC platform, with named instructor --> <!-- Based on https://www.coursera.org/course/datascitoolbox --> <main typeof="Course"> <h1 property="name">The Data Scientist's Toolbox</h1> <h2 property="provider" typeof="EducationalOrganization"> <span property="name">Johns Hopkins University</span> </h2> <h2>About this Course</h2> <div rel="hasCourseInstance" typeof="CourseInstance"> <meta property="courseMode" content="MOOC" /> <meta property="courseMode" content="online" /> <span rel="offers" typeOf="Offer"> <meta property="price" content="0" /> <meta property="offeredBy" content="Coursera"> </span> <h2 >Instructors</h2> <div property="instructor" typeof="Person"> <a property="url" href="http://example.org/instructor/~315" > <p property="name">Jeff Leek, PhD</p> <div property="jobTitle" >Associate Professor, Biostatistics</div> <div property="worksFor" >Bloomberg School of Public Health </div> </a> </div> </div> </main> </body>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Course", "hasCourseInstance": { "@type": "CourseInstance", "courseMode": [ "MOOC", "online" ], "instructor": { "@type": "Person", "jobTitle": "Associate Professor, Biostatistics", "name": "Jeff Leek, PhD", "url": {"@id": "http://example.org/instructor/~315"}, "worksFor": "Bloomberg School of Public Health " }, "offers": { "@type": "Offer", "offeredBy": "Coursera", "price": "0" } }, "name": "The Data Scientist's Toolbox", "provider": { "@type": "EducationalOrganization", "name": "Johns Hopkins University" } } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0338)

Copied

Example notes or example HTML without markup.

<body> <!--A Bachellor's programme provided by a University, referencing the course code--> <!--based on http://search.ucas.com/course/summary/463149/physics --> <div> <h2>Physics</h2> <div> <a href="/provider/324/university-of-bristol"> <span>University of Bristol</span> </a> </div> <div> Course code: F300 </div> </div> </body>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<body vocab="https://schema.org/"> <!--A Bachellor's programme provided by a University, referencing the course code--> <!--based on http://search.ucas.com/course/summary/463149/physics --> <div typeof="Course"> <h2 property="name">Physics</h2> <div property="provider" typeOf="CollegeOrUniversity"> <a property="url" href="/provider/324/university-of-bristol"> <span property="name">University of Bristol</span> </a> </div> <div> Course code <span property="courseCode">F300</span> </div> </div> </body>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Course", "courseCode": "F300", "name": "Physics", "provider": { "@type": "CollegeOrUniversity", "name": "University of Bristol", "url": {"@id": "/provider/324/university-of-bristol"} } } </script>

Structured representation of the JSON-LD example.
