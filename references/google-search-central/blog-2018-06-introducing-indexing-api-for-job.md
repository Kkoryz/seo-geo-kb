---
title: "Introducing the Indexing API for job posting URLs | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2018/06/introducing-indexing-api-for-job
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2018-06-26
---

# Introducing the Indexing API for job posting URLs | Google Search Central Blog | Google for Developers

Tuesday, June 26, 2018

Last June we
[launched a job search experience](https://www.blog.google/products/search/connecting-more-americans-jobs/)
that has since connected tens of millions of job seekers around the world with relevant job
opportunities from third party providers across the web. Timely indexing of new job content is
critical because many jobs are filled relatively quickly. Removal of expired postings is important
because nothing's worse than finding a great job only to discover it's no longer accepting
applications.

Today we're releasing the [Indexing API](/search/apis/indexing-api) to address this
problem. This API allows any site owner to directly notify Google when job posting pages are added
or removed. This allows Google to schedule job postings for a fresh crawl, which can lead to
higher quality user traffic and job applicant satisfaction. Currently, the Indexing API can only
be used for job posting pages that include
[job posting structured data](/search/docs/appearance/structured-data/job-posting).

For websites with many short-lived pages like job postings, the Indexing API keeps job postings fresh in Search results because it allows updates to be pushed individually. This API can be integrated into your job posting flow, allowing high quality job postings to be searchable quickly after publication. In addition, you can check the last time Google received each kind of notification for a given URL.

Follow the [Quickstart](/search/apis/indexing-api/v3/quickstart) guide to see how the
Indexing API works. If you have any questions, ask us in the
[Webmaster Help Forum](https://support.google.com/webmasters/community). We look forward to hearing
from you!
