---
title: "courseCode"
source_url: https://schema.org/courseCode
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# courseCode

# courseCode

A Schema.org Property

- Canonical URL: https://schema.org/courseCode
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+courseCode)

### Values expected to be one of these types


### Used on these types


### Examples

[Example 1](#eg-0338)

Copied

Example notes or example HTML without markup.

<body> <!--A Bachellor's programme provided by a University, referencing the course code--> <!--based on http://search.ucas.com/course/summary/463149/physics --> <div> <h2>Physics</h2> <div> <a href="/provider/324/university-of-bristol"> <span>University of Bristol</span> </a> </div> <div> Course code: F300 </div> </div> </body>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<body vocab="https://schema.org/"> <!--A Bachellor's programme provided by a University, referencing the course code--> <!--based on http://search.ucas.com/course/summary/463149/physics --> <div typeof="Course"> <h2 property="name">Physics</h2> <div property="provider" typeOf="CollegeOrUniversity"> <a property="url" href="/provider/324/university-of-bristol"> <span property="name">University of Bristol</span> </a> </div> <div> Course code <span property="courseCode">F300</span> </div> </div> </body>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Course", "courseCode": "F300", "name": "Physics", "provider": { "@type": "CollegeOrUniversity", "name": "University of Bristol", "url": {"@id": "/provider/324/university-of-bristol"} } } </script>

Structured representation of the JSON-LD example.
