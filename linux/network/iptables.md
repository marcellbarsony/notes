# iptables

**iptables** is a command line utility for configuring
Linux kernel firewall implemented within the [Netfilter]() project.
The term **iptables** is also commonly used
to refer to this kernel-level firewall.

## Installation

The stock Arch Linux kernel is compiled with _iptables_ support.
The _iptables_ package is an indirect dependency of the _base meta package_.

## Basic concepts

__iptables__ is used to inspect, modify, forward, redirect,
and/or drop IP packets. The code for filtering IP packets
is already built into the kernel and is organized into a collection of tables,
each with a specific purpose.
