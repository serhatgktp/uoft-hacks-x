import gpt_invader as ggr

def get_conversation(topic):
    ggr.init_open()
    rw_perspective = ggr.get_gpt_response(topic)
    challenger_perspective = ggr.get_gpt_response(rw_perspective, mode='disagree')
    neutral_perspective = ggr.get_gpt_response(topic, mode='neutral')
    
    return rw_perspective, challenger_perspective, neutral_perspective
