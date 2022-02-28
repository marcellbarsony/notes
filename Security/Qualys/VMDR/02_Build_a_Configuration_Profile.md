## Build a Configuration Profile

The **Configuration Profile** is what tells the agent how should they act.

1. Click **Configuration Profiles** tab.

2. Click **New Profile**.

## Configuration Profile Creation

1. **General Info**<br>
   Give the Configuration Profile a name.

2. **Blackout Windows**<br>
   Configure a Blackout Window to prevent the agent from communicating with the cloud platform at specific times of the day.

3. **Performance**<br>
   Change how often the agent check in to the Qualys Cloud platform, how often it checks the hosts, and how many system resources are used by the agent.

4. **Assign Hosts**<br>
   Add a tag to assign set of hosts that will get this set of configurations.

5. **Agent Scan Merge**<br>
   Activate **Enable Agent Scan Merge** to merge the data collected by the agent with data collected by a Qualys Scanner.

6. **VM Scan Interval**<br>
   Configure how often vulnerability data should be collected from the hosts.

7. **PC Scan Interval**<br>
   Configure how often agent should collect compliance data (if Policy Compliance is enabled).

8. **SCA Scan Interval**<br>
   Configure how often agent should collect data point for Secure Configuration Assessment.

9. **FIM**<br>

10. **EDR**<br>

11. **PM**<br>
    Enable Patch Management module for the profile if Patch Management is activated for the Activation Key.
