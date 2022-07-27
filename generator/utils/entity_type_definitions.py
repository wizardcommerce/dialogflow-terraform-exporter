import json
import glob

def get_all_entity_types(folder,agent_name):
    files = folder + '/*.json'
    files = glob.glob(files.replace('//', '/'))
    return [get_entity(file,agent_name) for file in files]

def get_entity(file, agent_name):
    f = open(file)
    data = json.load(f)
    data['agent_name'] = agent_name
    f.close()
    text = get_entity_header(data)+get_entity_values(data)+get_fuzzy_matching_value(data)+'\nRBRAC\n'
    return text.replace('LBRAC', '{').replace('RBRAC', '}')

def synonym_list_string(synonyms):
    return str(synonyms).replace("'",'"')

def get_fuzzy_matching_value(entity):
    fuzzy_matching_string = """
  enable_fuzzy_extraction = {allowFuzzyExtraction}
    """
    return str(fuzzy_matching_string).format(**entity)

def get_entity_values(entity):
    value_string = """
  entities LBRAC
    value = "{value}"
    synonyms = {synonym_list}
  RBRAC"""
    entries = [{'value': val['value'], 'synonym_list': synonym_list_string(val['synonyms'])} for val in entity['entries']]
    entries = [str(value_string).format(**entry) for entry in entries]
    return '\n'.join(entries)

def get_entity_header(entity):
    header = """
resource "google_dialogflow_cx_entity_type" "{name}" LBRAC
  parent       = google_dialogflow_cx_agent.{agent_name}.id
  display_name = "{name}"
  kind         = "KIND_MAP" 
  """
    return header.format(**entity)

