import gpt_invader as ggr

def get_conversation(topic):
    ggr.init_open()
    rw_perspective = ggr.get_gpt_response(topic)
    challenger_perspective = ggr.get_gpt_response(rw_perspective, mode='disagree')
    neutral_perspective = ggr.get_gpt_response(rw_perspective, mode='neutral')
    print('- - - - - - - - -')
    print("Right-wing perspective:", rw_perspective)
    print('- - - - - - - - -')
    print("Left-wing perspective:", challenger_perspective)
    print('- - - - - - - - -')
    print("Neutral perspective:", neutral_perspective)