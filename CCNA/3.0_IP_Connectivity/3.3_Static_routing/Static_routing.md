# Static Routing

**Static Routing** is a routing method that occurs when a router uses a manually-configure routing entry, rather than information from dynamic routing traffic.<br>
**Static Routes** are fixed and do not change is the network is changed or reconfigured.
Both dynamic and static routing are usually used on a router to maximize routing efficiency and to provide backups in case dynamic routing information fails to be exchanged.

[[Wikipedia - Static routing](https://en.wikipedia.org/wiki/Static_routing)]<br>
[[Cisco - Configuring Static Routing](9https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus3000/sw/unicast/503_u1_2/nexus3000_unicast_config_gd_503_u1_2/l3_route.html)<br>
[[Stydy CCNA - Connected, static & dynamic routes](https://study-ccna.com/connected-static-dynamic-routes/)]<br>

## Uses

Static routing may have the following uses:

- **Static routing** can be used to define an exit point (default route) from a router when no other routes are available or necessary.
- **Static routing** can be used for small networks that require only one or two routes.
  This is often more efficient since a link is not being wasted by exchanging dynamic routing information.
- **Static routing** is often used as a complement to dynamic routing to provide a failsafe backup if a dynamic route is unavailable.
- **Static routing** is often used to help transfer routing information from one routing protocol to another (routing redistribution).

## Advantages & Disadvantages

### Advantages

Static routing, if used without dynamic routing, has the following advantages:

- **Low resource requirements**: Static routing causes very little load on the CPU of the router, and produces no traffic to other routers.
- **Full control**: Static routing leaves the network administrator with full control over the routing behavior.
- **Easy to configure**: Static Routing is easy to configure on small networks.

### Disadvantages

Static routing can have some potential disadvantages:

- **Human error**: Configuring static routes manually can lead to human error.
  Administrators can configure incorrect routing paths by mistake.
- **Fault tolerance**: Static routing is not fault tolerant.
  If there is a change in the network or a failure occurs between two statically defined devices, traffic will not be re-routed.
- **Administrative distance**: Static routes typically take precedence over routes configured with a dynamic routing protocol.
  Static routes may prevent routing protocols from working as intended, unless the administrative distance is modified.
- **Administrative overhead**: Static routes must be configured on each router in the network(s).
  Dynamic routing on the other hand automatically propagates routing changes, reducing the need for manual reconfiguration.
