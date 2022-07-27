# [CB-62] Migration from DF ES to CX

### 1. Task and JIRA Description
Our objective is to create a migration plan and automated tools for constructing a bot in DialogFlox CX.

Let each story here be a step in the ES to CX migration plan detailed here: (https://docs.google.com/document/d/1hsSYyt3xOE7USXzWxvuKlr3aMpn-TOivTFdEpJtMoAs/edit?usp=sharing)

https://wizardcommerce.atlassian.net/browse/CBOT-62

### 2. Log

##### 07/18/2022
- Decided to create project that takes in inputs and outputs HCL2 file for TerraForm to set up a DF CX bot.
- created generator module with
  - `./utils`
    - `./bot_deinition_yaml.py` takes a .yaml and returns the bot definitions header block for a new DF CX bot
    - `./intent_definitions_json.py` takes a folder containing intent.json files and returns relevant information to create a DF CX intent block.
  - `./terraForm_string.py` takes a `bot.yaml` file and a `folder-containing/intent.json` files and returns an HCL2 string formatted for TerraForm and creating a DF CX bot from scratch

#### 07/19/2022
- Built out `get_intent_header()`
- Built out `get_intent()` and `get_intents()`

#### 07/20/2022
- Built out `get_bot_header()`
- ToDo:
  - Script that takes as input bot name and folder of intent definitions and outputs an HCL2 string with all intents and bot header filled.
  - Test that the HCL2 script executes building a bot in TerraForm
  - Save script in a .tf file
  - Annotate functions in order to allow for AGILE-based swapping them out and replacement with new business needs.

#### 07/27/2022
- Finished `entity_type_definitions.py` generator.
- Finished script to generate complete bot.tf file
- github repo started (https://github.com/zrosen-wizard/DF-ES-to-CX-TerraForm/)
  - project pushed to github
