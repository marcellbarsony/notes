# Rule-Based Alerts

In Qualys CSAM, alerts can be configured to notify users about asset health issues requiring their attention including _product lifecycle_, _software authorization_ or other items such as _open ports_ or _insufficient server storage_.

Alerts can be sent by numerous channels including: E-mail, Slack or PagerDuty.

## Responses

1. Click the **Responses** tab to create Rule-Based Alerts.

2. Before building an Alert Rule, click the **Actions** tab to define one or more Actions which determine the type of actions to be taken when an alert is triggered.

### Create New: Action

1. **Basic Information**<br>
   Give the Action a name and a description.

2. **Select Action**<br>
   Select **Send Email(Via Qualys)**.<br>
   Enter the Recipient e-mail address(es).<br>
   Enter the e-mail subject line.<br>
   Enter the alert message.

## Rule Manager

Rules specify the event that need to be monitored and the action need to be taken on the event.

### Create New: Rule

1. **Rule Information**<br>
   Enter a Rule Name and Description.<br>

2. **Rule Query**<br>
   Specify the query for the rule to identify the targeted activity or critical events.<br>
   Click the **Sampe Queries** link to select from predefined queries.<br>
   Click the **Test Query** button to check the query result.

3. **Action Settings**<br>
   Add the action to the rule in the **Actions** menu.<br>
   Select the previously created action to be populated.<br>

   Alert rules support the use of tokens which work as a placeholders or variables when the search completes.<br>
   Click **Insert Token** to view the list of available search tokens.<br>
   Only tokens that help in asset scoping or those that are directly related to the alert evaluation are supported for alert rule creation.
