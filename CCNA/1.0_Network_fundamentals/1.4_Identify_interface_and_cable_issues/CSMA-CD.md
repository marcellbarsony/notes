## CSMA/CD

**CSMA/CD (Carrier Sense Multiple Access with Collision Detection)** helps hosts to decide when to send packets on a shared network segment and how to detect collisions if the occur.

> **NOTE**
>
> Since switches are now commonly used instead of hubs, CSMA/CD is not really used anymore. Each port on a switch usually operate in a **full duplex mode** and there are **no packet collisions in a full duplex mode**.

[[Study CCNA - CSMA/CD](https://study-ccna.com/csma-cd/)]

## Example

In the example, we have a hub network.
**Host A** is trying to to communicate with **Host B**.
**Host A** "senses the wire and decides to send packets.
In the same time, **host C** sends its packets to **host D** and the collision occurs.
The sending hosts (**A** and **C**) detect the collision and resend the packet after a random period of time.

<img src="https://www.dropbox.com/s/mk9ioq4dkz3zzmm/csma_cd.jpg?dl=1" alt="csma_cd" class="inline" />
