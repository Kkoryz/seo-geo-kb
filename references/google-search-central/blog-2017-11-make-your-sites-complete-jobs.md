---
title: "Make your site's complete jobs information accessible to job seekers | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2017/11/make-your-sites-complete-jobs
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2017-11-15
---

# Make your site's complete jobs information accessible to job seekers | Google Search Central Blog | Google for Developers

Wednesday, November 15, 2017

In June, we
[announced a new experience](https://www.blog.google/products/search/connecting-more-americans-jobs/)
that put the convenience of Search into the hands of job seekers. Today, we are taking the next
step in improving the job search experience on Google by adding a feature that shows estimated
salary information from the web alongside job postings, as well as adding new UI features for
users.

Salary information has been one of the most requested additions from job seekers. This helps people evaluate whether a job is a good fit, and is an opportunity for sites with estimated salary information to:

-
**Increase brand awareness**: Estimated salary information shows a representative logo from the estimated salary provider. -
**Get more referral traffic**: Users can click through directly to salary estimate pages when salary information surfaces in job search results.

If your site provides salary estimates, you can take advantage of these changes in the following ways:

## Specify actual salary information

Actual salary refers to the base salary information that is provided by the employer. If your site
publishes job listings, you can add
[ JobPosting structured data](/search/docs/appearance/structured-data/job-posting)
and populate the

`baseSalary`

property to be eligible for inclusion in job search
results.
This salary information will be made available in both the list and the detail views.

## Provide estimated salary information

In cases where employers don't provide actual salary, job seekers may see estimated salaries
sourced from multiple partners for the same or similar occupation. If your site provides salary
estimate information, you can add
[Occupation structured data](/search/docs/appearance/structured-data/estimated-salary)
to be eligible for inclusion in job search results.

## Include exact location information

We've heard from users that having accurate, street-level location information helps them to focus
on opportunities that work best for them. Sites that publish job listings can do this by using the
jobLocation property in
[JobPosting structured data](/search/docs/appearance/structured-data/job-posting#JobPosting-definition).

## Validate your structured data

To double-check the structured data on your pages, we'll be updating the
[Structured Data Testing Tool](/search/docs/advanced/structured-data)
and the
[Search Console reports](https://support.google.com/webmasters/answer/6381755)
in the near future. In the meantime, you can
[monitor the performance of your job postings in Search Analytics](https://support.google.com/webmasters/answer/7042828).
Stay tuned!

Since launching this summer, we've seen over 60% growth in number of companies with jobs showing
on Google and connected tens of millions of people to new job opportunities. We are excited to
help users find jobs with salaries that meet their needs, and to route them to your site for more
information. We invite sites that provide salary estimates to mark up their salary pages using the
[Occupation structured data](/search/docs/appearance/structured-data/estimated-salary).
Should you have any questions regarding the use of structured data on your site, drop by our
[webmaster help forums](https://support.google.com/webmasters/go/community).
