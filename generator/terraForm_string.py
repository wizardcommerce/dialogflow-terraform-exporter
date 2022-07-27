from utils.bot_definition_yaml import get_bot_definition
from utils.intent_definitions_json import get_all_intents,get_intent
from utils.entity_type_definitions import get_all_entity_types,get_entity
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--bot_name', dest='bot_name', type=str, required=True)
    parser.add_argument('--intents', dest='intents', type=str, required=True)
    parser.add_argument('--entities', dest='entities', type=str, required=True)
    parser.add_argument('--destination', dest='dest', type=str, required=True)

    args = parser.parse_args()

    # Get bot definition
    bot = get_bot_definition(args.bot_name)

    # Get intent definition(s)
    if '.json' in args.intents:
        intents = get_intent(args.intents, args.bot_name)
    else:
        intents = '\n'.join(get_all_intents(args.intents, args.bot_name))


    # Get entity definition(s)
    if '.json' in args.entities:
        entities = get_entity(args.entities, args.bot_name)
    else:
        entities = '\n'.join(get_all_entity_types(args.entities, args.bot_name))

    text = '\n'.join([bot,intents,entities])


    output = '{}/{}-main.tf'.format(args.dest, args.bot_name)
    f = open(output, 'w')
    f.write(text)
    f.close()



