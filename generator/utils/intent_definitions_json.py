import json
import glob

# create a dictionary from each .json file for an intent
def get_intent(file,agent_name):
    f = open(file)
    data = json.load(f)
    data['agent_name'] = agent_name
    f.close()
    text = '\n'.join([get_intent_header(data), get_training_phrases(data), get_entities(data)]) + '\nRBRAC'
    return text.replace('LBRAC', '{').replace('RBRAC', '}')

# given a folder containing a series of .json files for intents,
#  yields dictionaries for each
def get_all_intents(folder,agent_name):
    files = folder + '/*.json'
    files = glob.glob(files.replace('//', '/'))
    return [get_intent(file,agent_name) for file in files]

def get_entities(intent):
    entity_string = """
  parameters LBRAC
    id          = "{name}"
    entity_type = "projects/-/locations/-/agents/-/entityTypes/{datatype}"
  RBRAC
    """
    entity_list = []
    for response in intent['responses']:
        if 'parameters' in response.keys():
            entity_list += [{'name': param['name'], 'datatype': param['dataType'].replace('@', '')} for param in response['parameters']]
    data = [str(entity_string).format(**entity) for entity in entity_list]
    return ''.join(data)

def get_training_phrases(intent):
    top_of_case ="""    training_phrases LBRAC\n"""
    training_phrase = """
      parts LBRAC
        text = "{text}"
      RBRAC
    """

    lifespan = """
      repeat_count = 2
    RBRAC  
    """
    data = ''
    for utterance_set in intent['userSays']:
        training_phrase_set = [entry for entry in utterance_set['data'] if entry['userDefined']==False]
        data += ''.join([
            str(training_phrase).format(**entry) for entry in training_phrase_set
        ])
    return str(top_of_case+data+lifespan)#.replace('LBRAC', '{').replace('RBRAC', '}')

def get_intent_header(intent):
    header = """
resource "google_dialogflow_cx_intent" "{name}" LBRAC
  parent       = google_dialogflow_cx_agent.{agent_name}.id
  display_name = "{name}"
  priority     = 1
  description  = "{condition} {id}"  
    """.format(**intent)

    return header