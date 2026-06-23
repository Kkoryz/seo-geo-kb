---
title: "educationalCredentialAwarded"
source_url: https://schema.org/educationalCredentialAwarded
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# educationalCredentialAwarded

# educationalCredentialAwarded

A Schema.org Property

- Canonical URL: https://schema.org/educationalCredentialAwarded
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+educationalCredentialAwarded)

A description of the qualification, award, certificate, diploma or other educational credential awarded as a consequence of successful completion of this course or program.

### Values expected to be one of these types


### Used on these types


#### Source

[https://github.com/schemaorg/schemaorg/issues/2289](https://github.com/schemaorg/schemaorg/issues/2289)

### Examples

[Example 1](#eg-0335)

Copied

Example notes or example HTML without markup.

<body> <!-- A college course leading to an HNC in Accounting --> <!-- based on http://www.fife.ac.uk/student/courses/course/HCACC --> <h1>Course Details</h1> <h2>HNC Accounting</h2> </body>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<body vocab="https://schema.org/" typeof="Course"> <!-- A college course leading to an HNC in Accounting --> <!-- based on http://www.fife.ac.uk/student/courses/course/HCACC --> <h1>Course Details</h1> <h2 property="name">HNC Accounting</h2> <meta property="educationalCredentialAwarded" content="Higher National Certificate in Accounting" /> </body>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Course", "educationalCredentialAwarded": "Higher National Certificate in Accounting", "name": "HNC Accounting" } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0336)

Copied

Example notes or example HTML without markup.

<!-- Certificate for a distance learning course --> <!--Based on http://www.train4publishing.co.uk/courses/distance-learning/basic-proofreading --> <body> <div> <h1>Basic Proofreading</h1> <h2>What is Included?</h2> <h3>Certificate</h3> <p>A completion certificate from PQB showing whether you have achieved a pass, merit or distinction in your work.</p> </div> </body>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<!-- Certificate for a distance learning course --> <!--Based on http://www.train4publishing.co.uk/courses/distance-learning/basic-proofreading --> <body vocab="https://schema.org/"> <div typeof="Course"> <h1 property="name">Basic Proofreading</h1> <h2>What is Included?</h2> <h3>Certificate</h3> <p>A <span property= "educationalCredentialAwarded">completion certificate from PQB</span> showing whether you have achieved a pass, merit or distinction in your work.</p> </div> </body>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Course", "educationalCredentialAwarded": "completion certificate from \r\n PQB", "name": "Basic Proofreading" } </script>

Structured representation of the JSON-LD example.
