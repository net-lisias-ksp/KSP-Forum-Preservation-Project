# KSP's Forum Preservation Project :: Scrapping Reports

Reports aiming to measure the impact of the scrapping on Forum's servers, in an attempt to minimise them.


## `report_http5`

Between 2023-05-01T23:27:27 and xxxxx this project was naively (or stupidly) ignoring the `HTTP 429 Too Many Requests` responses from Forum, and so kept scrapping until the bitter when Forum gets screwed by overloading, event flagged by `HTTP 5xx` messages.

As from xxxxx, the scrapping tool is now recognising and temporarily pausing operations when receiving a `HTTP 429` and, so, it's now rarely receiving any `HTTP 5XX` responses (be it because they ceased happening, be it because Forum is not being hit in order get such responses).

So this report can't be used anymore as a Forum's health meter and it's now relevant only for historical reference.

This report consolidates the `WARC` file contents before being sanitised.


## `build_connect_log`

This report aims to monitor the Forum's perceivable health by reporting on a timeline how many hits per minute we are being able to score, as well the response time.

Given the self imposed constrains while scrapping, this can't be used to check Forum's **performance** neither **effective load**, so the usefulness is limited.

But it can help to infer what would be the best time windows for scrapping the Forum, minimizing impacts.

This report consolidates the `pywb` logs.


## `site_complaints`

With the deprecation of the `report_http5`, due the implementation of the `http 429` guards, a new (and probably more accurate) report is now issued by monitoring the log entries for when the site "complains" about something (using the tool's new lingo).

I high concentration of `429` complains strongly suggests Forum is starting to struggle, while `5xx` ones definitively marks the points in which Forum broke (being it our fault or not) before we could withdrawn our scrapings.

This report consolidates the "spider" tool's logs.
