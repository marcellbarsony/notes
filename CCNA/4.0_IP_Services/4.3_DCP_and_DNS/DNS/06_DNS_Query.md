# What are the types of DNS queries?

What are the types of DNS queries?
In a typical DNS lookup three types of queries occur. By using a combination of these queries, an optimized process for DNS resolution can result in a reduction of distance traveled. In an ideal situation cached record data will be available, allowing a DNS name server to return a non-recursive query.

[[Cloudflare](https://www.cloudflare.com/learning/dns/what-is-dns/)]

## 3 types of DNS queries

- **Recursive query** - In a recursive query, a DNS client requires that a DNS server (typically a DNS recursive resolver) will respond to the client with either the requested resource record or an error message if the resolver can't find the record.

- **Iterative query** - in this situation the DNS client will allow a DNS server to return the best answer it can.
  If the queried DNS server does not have a match for the query name, it will return a referral to a DNS server authoritative for a lower level of the domain namespace.
  The DNS client will then make a query to the referral address.
  This process continues with additional DNS servers down the query chain until either an error or timeout occurs.

- **Non-recursive query** - typically this will occur when a DNS resolver client queries a DNS server for a record that it has access to either because it's authoritative for the record or the record exists inside of its cache.
  Typically, a DNS server will cache DNS records to prevent additional bandwidth consumption and load on upstream servers.
