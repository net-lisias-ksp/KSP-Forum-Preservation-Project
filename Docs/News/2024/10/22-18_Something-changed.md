# KSP's Forum Preservation Project :: News :: 2024-1022T18:14z

## Something Changed

Forun's Front Page was shut down.

![Forum Front Page](./content/22-18_Something-changed--image1.png#FullWidth)

Sniffing into the HTTP Response, I got:

```
HTTP/1.1 500 Internal Server Error
date: Tue, 22 Oct 2024 18:15:41 GMT
content-type: text/html; charset=UTF-8
cf-ray: 8d6b795ffd1b4ecb-GRU
cf-cache-status: DYNAMIC
cache-control: no-cache, no-store, must-revalidate, max-age=0, s-maxage=0
expires: 0
cf-apo-via: origin,host
x-powered-by: PHP/8.1.19
vary: Accept-Encoding
server: cloudflare
X-Firefox-Spdy: h2

<!DOCTYPE html>
<html lang="en">
<head>
<title>Error</title>
<style type="text/css">
			body {
				background: #f9f9f9;
				margin: 0;
				padding: 30px 20px;
				font-family: "Helvetica Neue", helvetica, arial, sans-serif;
			}

			#error {
				max-width: 800px;
				background: #fff;
				margin: 0 auto;
			}

			h1 {
				background: #151515;
				color: #fff;
				font-size: 22px;
				font-weight: 500;
				padding: 10px;
			}

				h1 span {
					color: #7a7a7a;
					font-size: 14px;
					font-weight: normal;
				}

			#content {
				padding: 20px;
				line-height: 1.6;
			}

			#reload_button {
				background: #151515;
				color: #fff;
				border: 0;
				line-height: 34px;
				padding: 0 15px;
				font-family: "Helvetica Neue", helvetica, arial, sans-serif;
				font-size: 14px;
				border-radius: 3px;
			}
		</style>
</head>
<body>
<div id="error">
<h1>An error occurred <span>(500 Error)</span></h1>
<div id="content">
We're sorry, but a temporary technical error has occurred which means we cannot display this site right now.
<br><br>
You can try again by clicking the button below, or try again later.
<br><br>
<button onclick="window.location.reload();" id="reload_button">Try again</button>
</div>
</div>
</body>
</html>
```

So they are still using CloudFlare, besides the Front Page being down.

This **suggests** that someone is finally working on Forum.

Granted, it may also the final blow on Forum's demise - but, why bother keeping CloudFlare so?

Let's wait and see.
