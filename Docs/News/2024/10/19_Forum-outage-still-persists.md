# KSP's Forum Preservation Project :: News :: 2024-1019

## Forum outage still persists!

I think we need some background.

`1146` is a MySQL error code meaning "table or view not found" - but that, in reality, means that your user could not open the table or view by any reason - like the table getting corrupted or your user lacking permissions to access that table.

[https://10web.io/blog/mysql-error-1146/](https://10web.io/blog/mysql-error-1146/)

The most common cause for Invision borking on a `EX1146` is the table `ibf_core_log` getting corrupted, not rarely by the disk where it is getting full.

But it also happens when you install something that you don't have a license to use. Or when you install something badly. Or when you deinstall something wrongly.

Or when someone messes up the MySQL's `GRANT` table, like removing an user from it.

Since I had received a Digest email from Forum about one day after the sinister event, we can conclude without a doubt that:

* The underling database management system is healthy
* The Forum's soul (tables with Topics, Posts, Profiles, etc) are intact.
* Forum services other than the FrontEnd are working fine.

So, no. Forum is not really dead. It's being self DoS'ed by something on the database - perhaps a disk full, perhaps some mess up on a support table on the database.

Given the current *status quo*, I think the most probably cause for the time they are taking to fix the problem should be one of that follows:

* There's no one left on whatever is caring for the Forum infrastructure on TTWO that knows how to handle Invision
* There's no on there **willing** to touch this thing
* There're something else **way bigger** happening, and KSP Forum was only one of the victims, and these poor bastards are buried in deep shit trying to fix the mess, and KSP Forum will come back after they clean thigns up.

I want to stress out that we are seeing some pretty nasty events happening the last few weeke - Internet Archive being hacked and defaced just for starters. My confidenciality agreement don't allow me to tell what else is happening on the industry, but I can tell what's already publicly disclosed: this is a **very very bad** time to be a [Fortinet customer](https://www.cybersecuritydive.com/news/critical-cve-fortinet-exploited/729736/) - CrowdStrike is not alone.


## References

* [Reddit comment](https://www.reddit.com/r/KerbalSpaceProgram/comments/1g70ajs/comment/lso0p36/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)
