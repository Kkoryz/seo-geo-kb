---
title: "instructor"
source_url: https://schema.org/instructor
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# instructor

# instructor

A Schema.org Property

- Canonical URL: https://schema.org/instructor
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+instructor)

A person assigned to instruct or provide instructional assistance for the

[CourseInstance](/CourseInstance).### Values expected to be one of these types


### Used on these types


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
