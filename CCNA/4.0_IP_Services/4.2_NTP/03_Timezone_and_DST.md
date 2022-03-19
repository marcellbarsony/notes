# Configure Timezone and Daylight Saving Time (DST)

It is recommended to set the correct timezone and adjust the DST setting before configuring a router as an NTP client. The syntax of the command used to set the timezone is:

```
R1(config)clock timezone NAME HOURS [MINUTES]
```

The name of the timezone can be anything you like.
After the name parameter, you need to specify the difference in hours (and optionally minutes) from Coordinated Universal Time (UTC).
For example, to specify the Atlantic Standard Time, which is 4 hours behind UTC, we would use the following command:

```
R1(config)#clock timezone AST -4
```

The syntax of the command used to adjust for DST is:

```
R1(config)clock summer-time NAME recurring [week day month hh:mm week day month hh:mm [offset]]
```

Again, the name parameter can be anything you like.
The recurring keyword instructs the router to update the clock each year.
If you press enter after the recurring keyword, the router will use the U.S. DST rules for the annual time changes in April and October.
You can also manually set the date and time for DST according to your location.
For example, to specify the DST that starts on the last Sunday of March and ends on the last Sunday of October, we would use the following command:

```
R1(config)clock summer-time DST recurring last Sunday March 2:00 last Sunday October 2:00
```
