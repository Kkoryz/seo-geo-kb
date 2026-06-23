---
title: "JobPosting"
source_url: https://schema.org/JobPosting
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# JobPosting

# JobPosting

A Schema.org Type

- Canonical URL: https://schema.org/JobPosting
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+JobPosting)

A listing that describes a job opening in a certain organization.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[applicantLocationRequirements](/applicantLocationRequirements)

[AdministrativeArea](/AdministrativeArea)```
```[applicationContact](/applicationContact)

[ContactPoint](/ContactPoint)```
```[baseSalary](/baseSalary)

[MonetaryAmount](/MonetaryAmount)or[Number](/Number)or[PriceSpecification](/PriceSpecification)```
```[datePosted](/datePosted)

[Date](/Date)or[DateTime](/DateTime)```
```[directApply](/directApply)

[Boolean](/Boolean)[url](/url)that is associated with a[JobPosting](/JobPosting)enables direct application for the job, via the posting website. A job posting is considered to have directApply of[True](/True)if an application process for the specified job can be directly initiated via the url(s) given (noting that e.g. multiple internet domains might nevertheless be involved at an implementation level). A value of[False](/False)is appropriate if there is no clear path to applying directly online for the specified job, navigating directly from the JobPosting url(s) supplied.```
```[educationRequirements](/educationRequirements)

[EducationalOccupationalCredential](/EducationalOccupationalCredential)or[Text](/Text)```
```[eligibilityToWorkRequirement](/eligibilityToWorkRequirement)

[Text](/Text)```
```[employerOverview](/employerOverview)

[Text](/Text)```
```[employmentType](/employmentType)

[Text](/Text)```
```[employmentUnit](/employmentUnit)

[Organization](/Organization)```
```[estimatedSalary](/estimatedSalary)

[MonetaryAmount](/MonetaryAmount)or[MonetaryAmountDistribution](/MonetaryAmountDistribution)or[Number](/Number)```
```[experienceInPlaceOfEducation](/experienceInPlaceOfEducation)

[Boolean](/Boolean)[JobPosting](/JobPosting)will accept experience (as indicated by[OccupationalExperienceRequirements](/OccupationalExperienceRequirements)) in place of its formal educational qualifications (as indicated by[educationRequirements](/educationRequirements)). If true, indicates that satisfying one of these requirements is sufficient.```
```[experienceRequirements](/experienceRequirements)

[OccupationalExperienceRequirements](/OccupationalExperienceRequirements)or[Text](/Text)```
```[hiringOrganization](/hiringOrganization)

[Organization](/Organization)or[Person](/Person)```
```[incentiveCompensation](/incentiveCompensation)

[Text](/Text)[incentives](/incentives).```
```[industry](/industry)

[DefinedTerm](/DefinedTerm)or[Text](/Text)```
```[jobBenefits](/jobBenefits)

[Text](/Text)[benefits](/benefits).```
```[jobDuration](/jobDuration)

[Duration](/Duration)or[QuantitativeValue](/QuantitativeValue)```
```[jobImmediateStart](/jobImmediateStart)

[Boolean](/Boolean)```
```[jobLocation](/jobLocation)

[Place](/Place)```
```[jobLocationType](/jobLocationType)

[Text](/Text)```
```[jobStartDate](/jobStartDate)

[Date](/Date)or[Text](/Text)```
```[occupationalCategory](/occupationalCategory)

[CategoryCode](/CategoryCode)or[Text](/Text)[BLS O*NET-SOC](http://www.onetcenter.org/taxonomy.html),[ISCO-08](https://www.ilo.org/public/english/bureau/stat/isco/isco08/)or similar, with the property repeated for each applicable value. Ideally the taxonomy should be identified, and both the textual label and formal code for the category should be provided.Note: for historical reasons, any textual label and formal code provided as a literal may be assumed to be from O*NET-SOC.

```
```[physicalRequirement](/physicalRequirement)

[DefinedTerm](/DefinedTerm)or[Text](/Text)or[URL](/URL)```
```[qualifications](/qualifications)

[Credential](/Credential)or[Text](/Text)```
```[relevantOccupation](/relevantOccupation)

[Occupation](/Occupation)```
```[responsibilities](/responsibilities)

[Text](/Text)```
```[salaryCurrency](/salaryCurrency)

[Text](/Text)[ISO 4217](http://en.wikipedia.org/wiki/ISO_4217)) used for the main salary information in this job posting or for this employee.```
```[securityClearanceRequirement](/securityClearanceRequirement)

[Text](/Text)or[URL](/URL)```
```[sensoryRequirement](/sensoryRequirement)

[DefinedTerm](/DefinedTerm)or[Text](/Text)or[URL](/URL)```
```[skills](/skills)

[DefinedTerm](/DefinedTerm)or[Text](/Text)```
```[specialCommitments](/specialCommitments)

[Text](/Text)```
```[title](/title)

[Text](/Text)```
```[totalJobOpenings](/totalJobOpenings)

[Integer](/Integer)```
```[validThrough](/validThrough)

[Date](/Date)or[DateTime](/DateTime)```
```[workHours](/workHours)

[Text](/Text)[Thing](/Thing)

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

[URL](/URL)### Examples

[Example 1](#eg-0028)

Copied

Example notes or example HTML without markup.

<div> <h2>Software Engineer</h2> <p><strong>Location:</strong> Kirkland WA</p> <p><strong>Industry:</strong> Computer Software <br><strong>Occupational Category:</strong> 15-1132.00 Software Developers, Application <br><strong>Hours:</strong> Full-time, 40 hours per week <br><strong>Salary:</strong> USD 100000 </p> <p> <strong>Description:</strong> ABC Company Inc. seeks a full-time mid-level software engineer to develop in-house tools. </p> <p><strong>Responsibilities:</strong></p> <ul> <li>Design and write specifications for tools for in-house customers</li> <li>Build tools according to specifications</li> </ul> <p><strong>Educational requirements:</strong></p> <ul> <li>Bachelor's Degree in Computer Science, Information Systems or related fields of study.</li> </ul> <p><strong>Experience requirements:</strong></p> <ul> <li>Minumum 3 years experience as a software engineer</li> </ul> <p><strong>Desired Skills:</strong></p> <ul> <li>Web application development using Java/J2EE</li> <li>Web application development using Python or familiarity with dynamic programming languages</li> </ul> <p><strong>Qualifications:</strong></p> <ul> <li>Ability to work in a team environment with members of varying skill levels.</li> <li>Highly motivated.</li> <li>Learns quickly.</li> </ul> <p><strong>Benefits:</strong></p> <ul><li>ABC Corp provides top-tier employee compensation benefits and a relaxed, team-oriented work environment, including: Medical, Life, Dental</li> </ul> <p><strong>Incentives:</strong></p> <ul><li>Performance-based annual bonus plan, project-completion bonuses</li> </ul> <p>If interested in this position, please email us your resume, along with salary requirements and a cover letter to Jobs@abc.123.</p> <p>Date Posted: 2011-10-31</p> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/JobPosting"> <meta itemprop="specialCommitments" content="VeteranCommit" /> <h2 itemprop="title">Software Engineer</h2> <span> <p><strong>Location:</strong> <span itemprop="jobLocation" itemscope itemtype="https://schema.org/Place"><span itemprop="address" itemscope itemtype="https://schema.org/PostalAddress"> <span itemprop="addressLocality">Kirkland</span> <span itemprop="addressRegion">WA</span></span></span></p> </span> <p><strong>Industry:</strong> <span itemprop="industry">Computer Software</span> <br><strong>Occupational Category:</strong> <span itemprop="occupationalCategory">15-1132.00 Software Developers, Application</span> <br><strong>Hours:</strong> <span itemprop="employmentType">Full-time</span>, <span itemprop="workHours">40 hours per week</span> <br><strong>Salary:</strong> <span itemprop="salaryCurrency">USD</span> <span itemprop="baseSalary">100000</span> </p> <p itemprop="description"> <strong>Description:</strong> <span itemprop="hiringOrganization" itemscope itemtype="https://schema.org/Organization"><span itemprop="name">ABC Company Inc.</span> seeks a full-time mid-level software engineer to develop in-house tools.</span> </p> <p><strong>Responsibilities:</strong></p> <ul itemprop="responsibilities"> <li>Design and write specifications for tools for in-house customers</li> <li>Build tools according to specifications</li> </ul> <p><strong>Educational requirements:</strong></p> <ul itemprop="educationRequirements"> <li>Bachelor's Degree in Computer Science, Information Systems or related fields of study.</li> </ul> <p><strong>Experience requirements:</strong></p> <ul itemprop="experienceRequirements"> <li>Minumum 3 years experience as a software engineer</li> </ul> <p><strong>Desired Skills:</strong></p> <ul itemprop="skills"> <li>Web application development using Java/J2EE</li> <li>Web application development using Python or familiarity with dynamic programming languages</li> </ul> <p><strong>Qualifications:</strong></p> <ul itemprop="qualifications"> <li>Ability to work in a team environment with members of varying skill levels.</li> <li>Highly motivated.</li> <li>Learns quickly.</li> </ul> <p><strong>Benefits:</strong></p> <ul><li>ABC Corp provides top-tier employee compensation benefits and a relaxed, team-oriented work environment, including:<span itemprop="jobBenefits"> Medical, Life, Dental</span></li> </ul> <p><strong>Incentives:</strong></p> <ul><li><span itemprop="incentiveCompensation">Performance-based annual bonus plan, project-completion bonuses</span></li> </ul> <p>If interested in this position, please email us your resume, along with salary requirements and a cover letter to Jobs@abc.123.</p> <p>Date Posted: <span itemprop="datePosted">2011-10-31</span></p> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="JobPosting"> <meta property="specialCommitments" content="VeteranCommit" /> <h2 property="title">Software Engineer</h2> <span> <p><strong>Location:</strong> <span property="jobLocation" typeof="Place"><span property="address" typeof="PostalAddress"> <span property="addressLocality">Kirkland</span> <span property="addressRegion">WA</span></span></span></p> </span> <p><strong>Industry:</strong> <span property="industry">Computer Software</span> <br><strong>Occupational Category:</strong> <span property="occupationalCategory">15-1132.00 Software Developers, Application</span> <br><strong>Hours:</strong> <span property="employmentType">Full-time</span>, <span property="workHours">40 hours per week</span> <br><strong>Salary:</strong> <span property="salaryCurrency">USD</span> <span property="baseSalary">100000</span> </p> <p property="description"> <strong>Description:</strong> <span property="hiringOrganization" typeof="Organization"><span property="name">ABC Company Inc.</span> seeks a full-time mid-level software engineer to develop in-house tools.</span> </p> <p><strong>Responsibilities:</strong></p> <ul property="responsibilities"> <li>Design and write specifications for tools for in-house customers</li> <li>Build tools according to specifications</li> </ul> <p><strong>Educational requirements:</strong></p> <ul property="educationRequirements"> <li>Bachelor's Degree in Computer Science, Information Systems or related fields of study.</li> </ul> <p><strong>Experience requirements:</strong></p> <ul property="experienceRequirements"> <li>Minumum 3 years experience as a software engineer</li> </ul> <p><strong>Desired Skills:</strong></p> <ul property="skills"> <li>Web application development using Java/J2EE</li> <li>Web application development using Python or familiarity with dynamic programming languages</li> </ul> <p><strong>Qualifications:</strong></p> <ul property="qualifications"> <li>Ability to work in a team environment with members of varying skill levels.</li> <li>Highly motivated.</li> <li>Learns quickly.</li> </ul> <p><strong>Benefits:</strong></p> <ul><li>ABC Corp provides top-tier employee compensation benefits and a relaxed, team-oriented work environment, including:<span property="jobBenefits"> Medical, Life, Dental</span></li> </ul> <p><strong>Incentives:</strong></p> <ul><li><span property="incentiveCompensation">Performance-based annual bonus plan, project-completion bonuses</span></li> </ul> <p>If interested in this position, please email us your resume, along with salary requirements and a cover letter to Jobs@abc.123.</p> <p>Date Posted: <span property="datePosted">2011-10-31</span></p> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "JobPosting", "baseSalary": "100000", "jobBenefits": "Medical, Life, Dental", "datePosted": "2011-10-31", "description": "Description: ABC Company Inc. seeks a full-time mid-level software engineer to develop in-house tools.", "educationRequirements": "Bachelor's Degree in Computer Science, Information Systems or related fields of study.", "employmentType": "Full-time", "experienceRequirements": "Minumum 3 years experience as a software engineer", "incentiveCompensation": "Performance-based annual bonus plan, project-completion bonuses", "industry": "Computer Software", "jobLocation": { "@type": "Place", "address": { "@type": "PostalAddress", "addressLocality": "Kirkland", "addressRegion": "WA" } }, "occupationalCategory": "15-1132.00 Software Developers, Application", "qualifications": "Ability to work in a team environment with members of varying skill levels. Highly motivated. Learns quickly.", "responsibilities": "Design and write specifications for tools for in-house customers Build tools according to specifications", "salaryCurrency": "USD", "skills": "Web application development using Java/J2EE Web application development using Python or familiarity with dynamic programming languages", "specialCommitments": "VeteranCommit", "title": "Software Engineer", "workHours": "40 hours per week" } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0251)

Copied

Example notes or example HTML without markup.

See JSON example.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "JobPosting", "name": "Mobile App Developer", "hiringOrganization": { "@type": "Organization", "name": "ACME Software" }, "relevantOccupation": { "@type": "Occupation", "name": "Software Developers, Applications", "occupationalCategory": { "@type": "CategoryCode", "inCodeSet": { "@type": "CategoryCodeSet", "name": "O*Net-SOC", "dateModified": "2019", "url": "https://www.onetonline.org/" }, "codeValue": "15-1132.00", "name": "Software Developers, Applications", "url": "https://www.onetonline.org/link/summary/15-1132.00" } } } </script>

Structured representation of the JSON-LD example.

[Example 3](#eg-0268)

Copied

Example notes or example HTML without markup.

A job where one must be in the United States to apply.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "JobPosting", "name": "Telecommute from anywhere in USA!", "applicantLocationRequirements": { "@type": "Country", "sameAs": "https://www.wikidata.org/wiki/Q30", "name": "USA" } } </script>

Structured representation of the JSON-LD example.

[Example 4](#eg-0280)

Copied

Example notes or example HTML without markup.

JobPosting for a position that requires applicants to have a bachelor of science in computer science from a program accredited by ABET.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "JobPosting", "title": "Systems Research Engineer", "qualifications": { "@type": "EducationalOccupationalCredential", "credentialCategory": "Bachelor of Science", "about": "Computer Science", "recognizedBy": { "@type": "Organization", "name": "ABET", "url": "https://www.abet.org/" } } } </script>

Structured representation of the JSON-LD example.

[Example 5](#eg-0465)

Copied

Example notes or example HTML without markup.

Example of Job markup for experience standing in place of formal qualifications.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "JobPosting", "title": "Software Engineer", "educationRequirements": { "@type": "EducationalOccupationalCredential", "credentialCategory": "bachelor degree" }, "experienceRequirements": { "@type": "OccupationalExperienceRequirements", "monthsOfExperience": "60" }, "experienceInPlaceOfEducation": true } </script>

Structured representation of the JSON-LD example.
