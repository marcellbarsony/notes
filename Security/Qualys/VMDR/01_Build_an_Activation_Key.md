## Build an Activation Key

[[Qualys Video Library](https://www.iorad.com/player/1784494/Onboarding---Build-an-Activation-Key)]

1. Click to **Configure Agents for VMDR**.

2. Create an activation key for the agents.<br>
   Click **Manage Cloud Agent Keys**.<br>
   This opens the Cloud Agent application.

3. Navigate to **Activation Keys** tab.

4. Click **New Key**.

5. The title should start with an abbreviation (e.g AK: Labs) sye to naming convention.<br>
   It is also useful to tag anything with this key.

6. Click **Create** to create a tag.

7. Give the tag a **name** and use a naming convention (e.g. CA for all of the Cloud Agent tags).<br>
   Give the tag a **color** from the dropdown menu. (Not required)<br>
   Give the tag a **description**. (Not required)<br>
   Click **Continue**.

8. Use the option _No Dynamic Rule_ for the **Rule Engine**.<br>
   This is a static tag that will get assigned to all agent assets with this activation key.<br>
   Click **Continue**.

9. Review the tag information and click **Finish**.

10. The tag is created, and anything deployed using this key will get this tag.<br>
    That's important for building queries and dashboard widgets.

## Applications associated with Activation Key

- **Asset Inventory** is provisioned by default.
  The agent when deployed, will collect inventory data (e.g. Network info, Open Ports and Services, Software).

- **Vulnerability Management** - The agent will collect vulnerability data for the hosts where this agent is installed.

- **Secure Config Assessment** - The agent can gather configuration data points on the hosts.
  This will enable building policies on these hosts for compliance.

- **Patch Management** - Get patching information and discovered vulnerabilities.

- **Policy Compliance** -
