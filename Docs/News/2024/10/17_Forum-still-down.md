# KSP's Forum Preservation Project :: News :: 2024-1017

## Forum still down!

Forum still down. The Front Page appears to work fine, probably due caching, but if you click on any link to an internal page, you got the error page:

![Forum's Error Message](./content/17_Forum-still-down--image1.png#FullWidth)

Some few links (as `Guidelines`) works, probably due being a static page directly served by the HTTPD server.

There're some things that we know, however:

1. It's not a license issue, apparently. [Invision allows the Forum software to keep going when the license expires](https://invisioncommunity.com/forums/topic/463344-ex1146-cant-get-access-to-admin-panel/), you only lose access to support and updates.
	+ Unless this is not applicable to KSP by some unknown reason, off course.
1. Since I received a Daily Digest email yesterday, the Forum's database with the Topics and Posts should be alright, otherwise the service in charge for the Digests would not had been able to build that Digest.
1. And since the email was built and sent, it also means that the Profile's table is also working, otherwise the service would not had be able to find my email to send the digest neither.
1. Since we can be reasonably sure that the tables for the Topics, Posts and Profiles are working, the Forum's "soul" appears to be alive and sound. Whatever is happening, is screwing only the Front End.
	+ Perhaps someone revoked the FrontEnd user's rights to access the database
	+ It's really what I really hope it happened. Don't care why, as long it would be easily reversible once whatever triggered this action is overcomed.
	+ Perhaps some FrontEnd only table got corrupted (disk full?) and then only the queries from the FrontEnd gets an Exception, leading to the `EX1146` error.
	+ Way less than desirable, but it still can be fixed with little to no risk for the Forum's valuable content.

Some people tried to diagnose the problem from their couch. However, things are rarely that simple: I had found a forum stating that `EX1146` could be related to trying to access something you don't have a license for.

But then I remembered that 1146 is the MySQL error code for table or view not found, what corroborates their thesis.

And then I remembered too that 1146 is also raised when you don't have rights to access a table from another namespace.

So, unfortunately, things are not necessarily that simple. I think they would had already fixed the Forum if it would be...

I still think TTWO intents to reestablish Forum, otherwise they would had just shutdown the Front End if destroying it were their intention.


## References

* [Reddit comment](https://www.reddit.com/r/KerbalSpaceProgram/comments/1g5vl35/comment/lseh0la/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)
* [Reddit comment](https://www.reddit.com/r/KerbalSpaceProgram/comments/1g4j9rn/comment/lsej173/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)
* [Reddit comment](https://www.reddit.com/r/KerbalSpaceProgram/comments/1g4j9rn/comment/lsg39qa/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)
* [Reddit comment](https://www.reddit.com/r/KerbalSpaceProgram/comments/1g5trtu/comment/lsflj3b/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)
