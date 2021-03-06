import joblib
import streamlit as st
import os
import pandas as pd
import io
import time
from PIL import Image
from multipage import save, MultiPage, start_app, clear_cache

def anxious_columns():
    return ['Q2A',
        'Q4A',
        'Q7A',
        'Q9A',
        'Q15A',
        'Q19A',
        'Q20A',
        'Q23A',
        'Q25A',
        'Q28A',
        'Q30A',
        'Q36A',
        'Q40A',
        'Q41A',
        'TIPI1',
        'TIPI2',
        'TIPI3',
        'TIPI4',
        'TIPI5',
        'TIPI6',
        'TIPI7',
        'TIPI8',
        'TIPI9',
        'TIPI10',
        'VCL1',
        'VCL2',
        'VCL3',
        'VCL4',
        'VCL5',
        'VCL6',
        'VCL7',
        'VCL8',
        'VCL9',
        'VCL10',
        'VCL11',
        'VCL12',
        'VCL13',
        'VCL14',
        'VCL15',
        'VCL16']

def stress_columns():
    return ['Q1A',
        'Q6A',
        'Q8A',
        'Q11A',
        'Q12A',
        'Q14A',
        'Q18A',
        'Q22A',
        'Q27A',
        'Q29A',
        'Q32A',
        'Q33A',
        'Q35A',
        'Q39A',
        'TIPI1',
        'TIPI2',
        'TIPI3',
        'TIPI4',
        'TIPI5',
        'TIPI6',
        'TIPI7',
        'TIPI8',
        'TIPI9',
        'TIPI10',
        'VCL1',
        'VCL2',
        'VCL3',
        'VCL4',
        'VCL5',
        'VCL6',
        'VCL7',
        'VCL8',
        'VCL9',
        'VCL10',
        'VCL11',
        'VCL12',
        'VCL13',
        'VCL14',
        'VCL15',
        'VCL16']

def depression_columns():
    return ['Q3A',
        'Q5A',
        'Q10A',
        'Q13A',
        'Q16A',
        'Q17A',
        'Q21A',
        'Q24A',
        'Q26A',
        'Q31A',
        'Q34A',
        'Q37A',
        'Q38A',
        'Q42A',
        'TIPI1',
        'TIPI2',
        'TIPI3',
        'TIPI4',
        'TIPI5',
        'TIPI6',
        'TIPI7',
        'TIPI8',
        'TIPI9',
        'TIPI10',
        'VCL1',
        'VCL2',
        'VCL3',
        'VCL4',
        'VCL5',
        'VCL6',
        'VCL7',
        'VCL8',
        'VCL9',
        'VCL10',
        'VCL11',
        'VCL12',
        'VCL13',
        'VCL14',
        'VCL15',
        'VCL16']

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
def check_category(i):
    DASS_keys = {'Depression': [3, 5, 10, 13, 16, 17, 21, 24, 26, 31, 34, 37, 38, 42],
            'Anxiety': [2, 4, 7, 9, 15, 19, 20, 23, 25, 28, 30, 36, 40, 41],
            'Stress': [1, 6, 8, 11, 12, 14, 18, 22, 27, 29, 32, 33, 35, 39]}
    if i+1 in DASS_keys["Depression"]:
        return "Depression"
    elif i+1 in DASS_keys["Anxiety"]:
        return "Anxiety"
    elif i+1 in DASS_keys["Stress"]:
        return "Stress"

def tipi():
    return [
        'Extraverted, enthusiastic',
        'Critical, quarrelsome.',
        'Dependable, self-disciplined.', 
        'Anxious, easily upset.',
        'Open to new experiences, complex.',
        'Reserved, quiet.',
        'Sympathetic, warm. ',
        'Disorganized, careless.',
        'Calm, emotionally stable.',
        'Conventional, uncreative.' 
    ]

def vcl():
    return[
        'boat',
        'incoherent',
        'pallid',
        'robot',
        'audible',
        'cuiovocal',
        'paucity',
        'epistemology',
        'florted',
        'decide',
        'pastiche',
        'verdid',
        'abysmal',
        'lucid',
        'betray',
        'funny'
    ]

def survey(prev_vars):
    if prev_vars != None:
        start_index = prev_vars
    else:
        start_index = 1 
    # st.header("Coba Tes Apakah Kamu Stres atau Depresi atau Gerogi!")
    st.header("Lets find out your Depression, Stress, and Anxiety level!")



    Q = questions()
    Q2 = tipi()
    VCL = vcl()
    anx_columns = anxious_columns()
    dep_columns = depression_columns()
    str_columns = stress_columns()

    A = {
        'Did not apply to me at all' : 0,
        'Applied to me to some degree, or some of the time' : 1,
        'Applied to me to a considerable degree, or a good part of the time': 2,
        'Applied to me very much, or most of the time' : 3
    }

    tmp_depression = []
    tmp_anxiety = []
    tmp_stress = []
    A2 = {
        "Disagree strongly" : 1,
        "Disagree moderately" : 2,
        "Disagree a litte" : 3,
        "Neither agree or disagree" : 4,
        "Agree a litte" : 5,
        "Agree moderately" : 6,
        "Agree strongly" : 7
    }

    A3 = {
        "Yes" : 1,
        "No" : 0
    }

    tmp = []


    with st.container():
        with st.expander("Section 1 Questions"):
            for i in range(0, len(Q), 2):
                col1, col2 = st.columns(2)
                with col1:
                    answer_col_1 = st.radio(f"{Q[i]}",(A))
                    category = check_category(i)
                    if category == "Depression":
                        tmp_depression.append(A[answer_col_1])
                    if category == "Anxiety":
                        tmp_anxiety.append(A[answer_col_1])
                    if category == "Stress":
                        tmp_stress.append(A[answer_col_1])
                with col2:
                    answer_col_2 = st.radio(f"{Q[i+1]}",(A))
                    category = check_category(i+1)
                    if category == "Depression":
                        tmp_depression.append(A[answer_col_2])
                    if category == "Anxiety":
                        tmp_anxiety.append(A[answer_col_2])
                    if category == "Stress":
                        tmp_stress.append(A[answer_col_2])
    
        # genre = st.radio(f"{i}",(A))
        # genre = st.radio(f"{i}",('Did not apply to me at all', 'Applied to me to some degree, or some of the time', 'Applied to me to a considerable degree, or a good part of the time', 'Applied to me very much, or most of the time'))
        # tmp.append(A[genre])
    # if st.button("Go!"):
    #     st.write(f" Score Anxiety ??? {sum(tmp_anxiety)}")
    #     st.write(f" Score Stress ??? {sum(tmp_stress)}")
    #     st.write(f" Score Depression ??? {sum(tmp_depression)}")
    
    tipi2 = []

    with st.container():
        with st.expander("Section 2 Questions"):
            for i in range(0, len(Q2), 2):
                col1, col2 = st.columns(2)
                with col1:
                    a = st.radio(f"{Q2[i]}",(A2))

                    tipi2.append(A2[a])
                with col2:
                    b = st.radio(f"{Q2[i+1]}",(A2))
                    tipi2.append(A2[b])

    # if st.button("Tipi Scores!"):
    #     st.write(f" TIPI Scores ??? {sum(tipi2)}")
    
    
    vcl2 = []
    flip = [5, 8, 11]

    with st.container():
        with st.expander("Section 3 Questions"):
            st.caption("Do you understand these words?")
            for i in range(0, len(VCL), 4):
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    a = st.radio(f"{VCL[i]}",(A3))
                    if (i in flip):
                        if (a == "Yes"):
                            vcl2.append(0)
                        else:
                            vcl2.append(1)
                    else:
                        if (a == "No"):
                            vcl2.append(0)
                        else:
                            vcl2.append(1)
                with col2:
                    b = st.radio(f"{VCL[i+1]}",(A3))
                    if (i+1 in flip):
                        if (b == "Yes"):
                            vcl2.append(0)
                        else:
                            vcl2.append(1)
                    else:
                        if (b == "No"):
                            vcl2.append(0)
                        else:
                            vcl2.append(1)
                with col3:
                    c = st.radio(f"{VCL[i+2]}",(A3))
                    if (i+2 in flip):
                        if (c == "Yes"):
                            vcl2.append(0)
                        else:
                            vcl2.append(1)
                    else:
                        if (c == "No"):
                            vcl2.append(0)
                        else:
                            vcl2.append(1)
                with col4:
                    d = st.radio(f"{VCL[i+3]}",(A3))
                    if (i+3 in flip):
                        if (d == "Yes"):
                            vcl2.append(0)
                        else:
                            vcl2.append(1)
                    else:
                        if (d == "No"):
                            vcl2.append(0)
                        else:
                            vcl2.append(1)
    # if st.button("VCL Scores!"):
    #     st.write(f" VCL Scores ??? {sum(vcl2)}")
    if st.button("Predict"):
        model_anxious = joblib.load("./res/model_anxious.pkl")
        model_depression = joblib.load("./res/model_depression.pkl")
        model_stress = joblib.load("./res/model_stress.pkl")

        result_anxious = model_anxious.predict(pd.DataFrame({y : x for (x,y) in zip(tmp_anxiety + tipi2 + vcl2, anx_columns)}, index=[0]))
        result_depression = model_depression.predict(pd.DataFrame({y : x for (x,y) in zip(tmp_depression + tipi2 + vcl2, dep_columns)}, index=[0]))
        result_stress = model_stress.predict(pd.DataFrame({y : x for (x,y) in zip(tmp_stress + tipi2 + vcl2, str_columns)}, index=[0]))

        st.write(f"Anxiety level    ??? {result_anxious[0]}")
        st.write(f"Depression level ??? {result_depression[0]}")
        st.write(f"Stress level     ??? {result_stress[0]}")
    st.header
    # st.text("How we did our training and parameters")
    save([start_index], "placeholder1", ["App2", "App3"])
