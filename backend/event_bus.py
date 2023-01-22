import gpt_invader as ggr
# from gpt-invader import get_gpt_disagreement as ggd

MAX_TOPIC_LEN = 60

if __name__ == '__main__':
    topic = input('What would you like to talk about?\n> ')
    while len(topic) > MAX_TOPIC_LEN:
        topic = input('What would you like to talk about?\n> ')
    
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