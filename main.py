import streamlit as st
from multipage import save, MultiPage, start_app, clear_cache
import pandas as pd
# from src.page.hranalytics import hranalytics
# from src.page.hranalyticsgraph import hranalyticsgraph
# from src.page.model import model
from PIL import Image
import os

def questions():
    return [
        'I found myself getting upset by quite trivial things.',
        'I was aware of dryness of my mouth.',
        'I couldn\'t seem to experience any positive feeling at all.',
        'I experienced breathing difficulty (eg, excessively rapid breathing, breathlessness in the absence of physical exertion).',
        'I just couldn\'t seem to get going.',
        'I tended to over-react to situations.',
        'I had a feeling of shakiness (eg, legs going to give way).',
        'I found it difficult to relax.',
       	'I found myself in situations that made me so anxious I was most relieved when they ended.',
       	'I felt that I had nothing to look forward to.',
       	'I found myself getting upset rather easily.',
       	'I felt that I was using a lot of nervous energy.',
       	'I felt sad and depressed.',
       	'I found myself getting impatient when I was delayed in any way (eg, elevators, traffic lights, being kept waiting).',
       	'I had a feeling of faintness.',
       	'I felt that I had lost interest in just about everything.',
       	'I felt I wasn&#39;t worth much as a person.',
       	'I felt that I was rather touchy.',
       	'I perspired noticeably (eg, hands sweaty) in the absence of high temperatures or physical exertion.',
       	'I felt scared without any good reason.',
       	'I felt that life wasn&#39;t worthwhile.',
       	'I found it hard to wind down.',
       	'I had difficulty in swallowing.',
       	'I couldn&#39;t seem to get any enjoyment out of the things I did.',
       	'I was aware of the action of my heart in the absence of physical exertion (eg, sense of heart rate increase, heart missing a beat).',
       	'I felt down-hearted and blue.',
       	'I found that I was very irritable.',
       	'I felt I was close to panic.',
       	'I found it hard to calm down after something upset me.',
       	'I feared that I would be &quot;thrown&quot; by some trivial but unfamiliar task.',
       	'I was unable to become enthusiastic about anything.',
       	'I found it difficult to tolerate interruptions to what I was doing.',
       	'I was in a state of nervous tension.',
       	'I felt I was pretty worthless.',
       	'I was intolerant of anything that kept me from getting on with what I was doing.',
       	'I felt terrified.',
    	'I could see nothing in the future to be hopeful about.',
       	'I felt that life was meaningless.',
       	'I found myself getting agitated.',
       	'I was worried about situations in which I might panic and make a fool of myself.',
       	'I experienced trembling (eg, in the hands).',
       	'I found it difficult to work up the initiative to do things.'
    ]

def main():
    st.set_page_config(page_title="Stress Analytics", page_icon="📊", layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': 'https://www.extremelycoolapp.com/help',
            'Report a bug': "https://www.extremelycoolapp.com/bug",
            'About': "# This is a header. This is an *extremely* cool app!"
        }
    )
    st.text("Hello World 2")

    start_app()

    logs = pd.read_csv("./res/logs.csv")
    st.dataframe(logs.tail(10))

    ##

    age = st.slider('How old are you?', 0, 130, 25)
    st.write("I'm ", age, 'years old')

    ##

    
    Q = []
    Q = questions()


    # A = []
    # A.append("Did not apply to me at all")
    # A.append("Applied to me to some degree, or some of the time")
    # A.append("Applied to me to a considerable degree, or a good part of the time")
    # A.append("Applied to me very much, or most of the time")

    A = {
        'Did not apply to me at all' : 1,
        'Applied to me to some degree, or some of the time' : 2,
        'Applied to me to a considerable degree, or a good part of the time': 3,
        'Applied to me very much, or most of the time' : 4
    }

    tmp = []

    for i in range(0, len(Q), 2):
        col1, col2 = st.columns(2)
        with col1:
            st.radio(f"{Q[i]}",(A))
        with col2:
            st.radio(f"{Q[i+1]}",(A))
        # genre = st.radio(f"{i}",(A))
        # genre = st.radio(f"{i}",('Did not apply to me at all', 'Applied to me to some degree, or some of the time', 'Applied to me to a considerable degree, or a good part of the time', 'Applied to me very much, or most of the time'))
        # tmp.append(A[genre])
    st.write(sum(tmp))
if __name__ == "__main__":
    main()