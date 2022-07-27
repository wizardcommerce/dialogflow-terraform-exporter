def get_bot_definition(name):
    header_data = """
resource "google_dialogflow_cx_agent" "{}" LBRAC
  display_name = "dialogflowcx-{}"
  location = "global"
  default_language_code = "en"
  supported_language_codes = ["fr","de","es"]
  time_zone = "America/New_York"
  description = "Example description."
  avatar_uri = ""
  enable_stackdriver_logging = true
  enable_spell_correction    = true
    speech_to_text_settings LBRAC
        enable_speech_adaptation = true
    RBRAC
RBRAC
    """

    return header_data.format(name,name).replace('LBRAC', '{').replace('RBRAC', '}')