import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
import xlrd

# Load data
df2 = pd.read_csv('table/avg_pol.csv')
df2.index = pd.to_datetime(df2['created_at'])
df3 = pd.read_csv('table/common_words.csv')
words_df = df3.sort_values(by = 'count')
pos_df = pd.read_csv('table/pos_neg.csv')
number_sentiment_df = pd.read_csv('table/Percent_emotion.csv')
number_sentiment_df.index = pd.to_datetime(number_sentiment_df['created_at'])
senti_df = pd.read_csv('table/Number_emotion.csv')
mallet_pie_df = pd.read_excel('data/LDA_topics.xlsx')
df4 = pd.read_excel('data/Dominant_topic_polarity.xlsx')
df5 = pd.DataFrame(df4[['true_time','polarity','subjectivity']])
pol_mallet_df = df5.groupby('true_time').mean().sort_values(by = 'true_time')

#mallet_pie_df = df4.sort_values(by = 'Unnamed: 0')


##table for Average polarity and subjectivity per day
fig = go.Figure()
fig.add_trace(go.Scatter(x=df2.index, y=df2['polarity'],
                    name='Average Polarity',
                    mode='lines',
                    opacity=0.7,
                    textposition='bottom center'))
fig.add_trace(go.Scatter(x=df2.index, y=df2['subjectivity'],
                    mode='lines',
                    name='Average Subjectivity'))
fig.update_layout(
                template='plotly_dark',
                paper_bgcolor='rgba(0, 0, 0, 0)',
                plot_bgcolor='rgba(0, 0, 0, 0)',
                margin={'b': 15},
                hovermode='x',
                autosize=True,
                title={'text': 'Average Polarity and Sujectivity of tweets per day', 'font': {'color': 'white'}, 'x': 0.5},
                xaxis={'range': [df2.index.min(), df2.index.max()]},
                xaxis_title="Date",
                yaxis_title="Value",
)

##table for Sentiment density per day
fig_dense = go.Figure()
fig_dense.add_trace(go.Scatter(x=number_sentiment_df.index, y=number_sentiment_df['seg_sentiment'],
                    name='Average Polarity',
                    mode='lines',
                    opacity=0.7,
                    textposition='bottom center'))
fig_dense.update_layout(
                colorway=[ '#FF0056'],
                template='plotly_dark',
                paper_bgcolor='rgba(0, 0, 0, 0)',
                plot_bgcolor='rgba(0, 0, 0, 0)',
                margin={'t': 60},
                hovermode='x',
                height = 280,
                title={'text': 'Sentiment Density per Day', 'font': {'color': 'white'}, 'x': 0.5},
                #xaxis={'range': [df_sub.index.min(), df_sub.index.max()]},
                xaxis_title="Date",
                yaxis_title="Sentiment Density",
)

##Table for percentage change in density
fig_change = px.bar(number_sentiment_df, 
                    x='created_at',
                    y='difference',
                    color='difference',
                    #labels={'pop':'population of Canada'},
                    height=260,
                    width = 800
                    )
fig_change.update_layout(
                template='plotly_dark',
                paper_bgcolor='rgba(0, 0, 0, 0)',
                plot_bgcolor='rgba(0, 0, 0, 0)',
                margin={'t': 60,'l':100},
                hovermode='x',
                title={'text': 'Percentage change in Sentiment density', 'font': {'color': 'white'}, 'x': 0.5},
                #autosize=True,
                xaxis_title="Date",
                yaxis_title="Change",
)  

##Table for bar chart for total sentimnet 
x_bar = ['Anger', 'Fear','Analytical','Joy','Sadness']
y_bar = [senti_df['anger_output'].sum(), senti_df['fear_output'].sum(), senti_df['analytical_output'].sum(), senti_df['joy_output'].sum(), senti_df['sadness_output'].sum()]
fig_bar = go.Figure(data=[go.Bar(
            x=x_bar, y=y_bar,
            #colorway=["#5E0DAC", '#FF4F00', '#375CB1', '#FF7400', '#FFF400', '#FF0056'],
            text=y_bar,
            textposition='auto',
            marker =  {'color': ['#b50000','#037357', '#375CB1','#d4bc81','#a267cf', '#FF4F00','#FF0056','#5E0DAC',  ]}
        )])
fig_bar.update_layout(
                #colorway=["#5E0DAC", '#FF4F00', '#375CB1', '#FF7400', '#FFF400', '#FF0056'],
                template='plotly_dark',
                paper_bgcolor='rgba(0, 0, 0, 0)',
                plot_bgcolor='rgba(0, 0, 0, 0)',
                margin={'b': 15},
                hovermode='x',
                autosize=True,
                title={'text': 'Overall Recorded Sentiments', 'font': {'color': 'white'}, 'x': 0.5},
                #xaxis={'range': [df_sub.index.min(), df_sub.index.max()]},
                xaxis_title="Emotions",
                yaxis_title="Count",
)

##Table for common words
fig_words = px.bar(words_df, x="count", y="words", orientation='h')
fig_words.update_layout(
                #colorway=['crimson'],
                #color='crimson',
                template='plotly_dark',
                paper_bgcolor='rgba(0, 0, 0, 0)',
                plot_bgcolor='rgba(0, 0, 0, 0)',
                margin={'t': 75},
                hovermode='x',
                height = 550,
                #autosize=True,
                title={'text': 'Most Used Common Words', 'font': {'color': 'white'}, 'x': 0.5},
                #xaxis={'range': [df_sub.index.min(), df_sub.index.max()]},
                xaxis_title="Count",
                yaxis_title="Words",
)

##Table for pie chart of pos neg neutral
labels_pie = ['Positive','Neutral','Negative']
values_pie = [pos_df['Positive'].sum(),pos_df['Neutral'].sum(),pos_df['Negative'].sum()]
fig_pie = go.Figure(data=[go.Pie(labels=labels_pie, values=values_pie)])
fig_pie.update_layout(
                colorway=["#5E0DAC", '#FF4F00', '#375CB1', '#FF7400', '#FFF400', '#FF0056'],
                template='plotly_dark',
                paper_bgcolor='rgba(0, 0, 0, 0)',
                plot_bgcolor='rgba(0, 0, 0, 0)',
                margin={'t': 50},
                hovermode='x',
                height = 300,
                #autosize=True,
                title={'text': 'Polarity Distribution observed', 'font': {'color': 'white'}, 'x': 0.5},
                #xaxis={'range': [df_sub.index.min(), df_sub.index.max()]},
)

##Average for polarity and subjectivity of news articles / mallet
fig_pol = go.Figure()
fig_pol.add_trace(go.Scatter(x=pol_mallet_df.index, y=pol_mallet_df['polarity'],
                    mode='lines',
                    name='Average Polarity',
                    opacity=0.7,
                    textposition='bottom center'))
fig_pol.add_trace(go.Scatter(x=pol_mallet_df.index, y=pol_mallet_df['subjectivity'],
                    mode='lines',
                    name='Average Subjectivity'))
fig_pol.update_layout(
                #colorway=["#5E0DAC", '#FF4F00', '#375CB1', '#FF7400', '#FFF400', '#FF0056'],
                template='plotly_dark',
                paper_bgcolor='rgba(0, 0, 0, 0)',
                plot_bgcolor='rgba(0, 0, 0, 0)',
                margin={'b': 15},
                hovermode='x',
                height = 500,
                width = 850,
                #autosize=True,
                title={'text': 'Polarity and Subjectivity of News Articles', 'font': {'color': 'white'}, 'x': 0.5},
                xaxis={'range': [pol_mallet_df.index.min(), pol_mallet_df.index.max()]},
                xaxis_title="Date",
                yaxis_title="Value Recorded",
)   

##Table for pie chart of occurance of topics
fig_mallet_pie = px.pie(mallet_pie_df, values='Num_Documents', names='topic',hole = 0.3, color_discrete_sequence=px.colors.sequential.RdBu)
fig_mallet_pie.update_layout(
                template='plotly_dark',
                paper_bgcolor='rgba(0, 0, 0, 0)',
                plot_bgcolor='rgba(0, 0, 0, 0)',
                margin={'t':50},
                hovermode='x',
                title={'text': 'Occurance of Topics', 'font': {'color': 'white'}, 'x': 0.5},
                height = 300
                #autosize=True,
)  

#Initialize the app
app = dash.Dash(__name__)
app.config.suppress_callback_exceptions = True


def get_options(list_stocks):
    dict_list = []
    for i in list_stocks:
        dict_list.append({'label': i, 'value': i})
    return dict_list


app.layout = html.Div( 
    children = [
        html.Div(
            children=[
                html.Div(className = 'row heading',
                children = [
                    html.H1('VISUALISATION DASHBOARD',
                    style ={'font-family': 'Courier New','font-size' : '31px','color':'#FFFFFF','margin-bottom' : '0px'}),
                    html.H5('SENTIMENT ANALYSIS OF COVID 19 TWEETS',
                    style ={'font-family': 'Courier New','color':'#FFFFFF','padding-top':'0px','margin-top':'0px'})
                ])
            ]
        ),

        html.Div(
        children=[
            html.Div(className='row',
                    children=[
                        html.Div(className='four columns div-user-controls',
                                children=[
                                    html.H2('Classification of tweets into different emotions'),
                                    html.P('Visualisation Dashboard built using Plotly Dash'),
                                    html.P('Pick one or more emotions from the dropdown below.'),
                                    html.Div(
                                        className='div-for-dropdown',
                                        children=[
                                            dcc.Dropdown(id='Sentiment_5selector', options=[{'label' : 'Anger', 'value': 'anger_output'},
                                                                                            {'label':'Analytical','value':'analytical_output'},
                                                                                            {'label':'Fear','value':'fear_output'},
                                                                                            {'label':'Joy','value':'joy_output'} ,
                                                                                            {'label':'Sadness','value':'sadness_output'}   ],
                                                        multi=True, value=['anger_output','analytical_output'],
                                                        style={'backgroundColor': '#1E1E1E'}, #colour '#1E1E1E'
                                                        className='Sentiment_5selector'
                                                        ),
                                        ],
                                        style={'color': '#1E1E1E'})
                                    ]
                                ),
                        html.Div(className='eight_half columns div-for-charts bg-grey',
                                children=[
                                    dcc.Graph(id='number_sentiment', config={'displayModeBar': False}, animate=True)
                                ])
                            ]
                        )
                    ]
        ),
        
        html.Div( className = 'row',
            children = [
                html.Div(className = 'eight_half columns',
                    children = [
                        html.Div( className = 'div-for-charts_small_2 bg-grey',
                            children = [
                                dcc.Graph(id = 'Sentiment_density',
                                config={'displayModeBar': False},
                                animate =True,
                                figure = fig_dense
                                )
                            ]
                        ),
                        html.Div( className = 'div-for-charts_small_2 bg-grey',
                            children = [
                                dcc.Graph(id = 'Sentiment_density_Change',
                                config={'displayModeBar': False},
                                animate =True,
                                figure = fig_change
                                )
                            ]
                        )
                    ]
                ),
                html.Div(className = 'four columns div-for-charts bg-grey',
                    children = [
                        dcc.Graph(id = 'Sentiment_Bar',
                                config={'displayModeBar': False},
                                animate =True,
                                figure = fig_bar
                                )
                    ]
                )
            ]
        ),

        html.Div(
            children=[
                html.Div(className = 'row',
                children = [
                    
                ])
            ]
        ),


        html.Div(
            children=[
                html.Div(className = 'row',
                children = [
                    html.Div(className='eight_half columns div-for-charts bg-grey',
                        children=[
                            dcc.Graph(id='polarity', 
                                    config={'displayModeBar': False}, 
                                    animate=True,
                                    figure= fig
                                )]
                            ),
                    html.Div(className='four columns div-for-charts bg-grey',
                    children = [
                        dcc.Graph(id = 'common_words',
                                config={'displayModeBar': False},
                                animate =True,
                                figure = fig_words
                        )
                    ])
                ])
            ]
        ),

        html.Div(className = 'row',
        children = [
            html.Div(className = 'four columns',
            children = [
                 html.Div(className = 'div-user-controls-small ',
                    children=[
                                    html.H2('POSITIVE, NEGATIVE AND NEUTRAL SENTIMENTS'),
                                    html.P('Pick one or more sentiment from the dropdown below.'),
                                    html.Div(
                                        className='div-for-dropdown',
                                        children=[
                                            dcc.Dropdown(id='Sentimentselector', options=[{'label' : 'Positive', 'value': 'Positive'},
                                                                                            {'label':'Neutral','value':'Neutral'},
                                                                                            {'label':'Negative','value':'Negative'}  ],
                                                        multi=True, value=['Positive','Negative'],
                                                        style={'backgroundColor': '#1E1E1E'}, #colour '#1E1E1E'
                                                        className='Sentimentselector'
                                                        ),
                                        ],
                                        style={'color': '#1E1E1E'})
                                    ]
                 ),             
                html.Div(className = 'div-for-charts_small bg-grey',
                children = [
                    dcc.Graph(id = 'pie_graph',
                        config={'displayModeBar': False},
                        animate =True,
                        figure = fig_pie
                    )],
                    
                ),
            ]),

            html.Div(className = 'eight_half columns div-for-charts bg-grey',
            children = [
                dcc.Graph(id = 'pos_neg_graph',
                        config={'displayModeBar': False},
                        animate =True,
                        #figure = fig_posneg 
                )
            ]),
        ]),
        

        html.Div(
            children=[
                html.Div(className = 'row',
                children = [
                    
                ])
            ]
        ), 

        html.Div(className = 'row',
            children = [
                html.Div(className = 'eight_half columns div-for-charts bg-grey',
                    children = [
                        dcc.Graph(id = 'Graph_mallet_pol',
                        config={'displayModeBar': False},
                        animate =True,
                        figure = fig_pol
                )
            ]
                ),
                html.Div(className = 'four columns',
                    children = [
                        html.Div( className = 'div-for-charts_small bg-grey',
                            children = [
                                dcc.Graph(id = 'Graph_mallet_pie',
                                        config={'displayModeBar': False},
                                        animate =True,
                                        figure = fig_mallet_pie
                                )
                            ]
                        ),
                        html.Div( className = 'div-for-charts_small bg-grey',
                            children =[
                                    dcc.Markdown('''
                                                #### Topics and their Keywords
                                                |  **USA: hotspot** includes *trump, president, state * etc.
                                                |  **Vaccine** includes *vaccine,virus, drug* etc. 
                                                |  **Healthcare** includes *health, hospital, ventilator* etc.
                                                |  **Life during covid** includes * life, public, country, men,* etc.
                                                |  **Lockdown** includes *police, government, lockdown,* etc
                                                |  **Effect on Economy** includes *company, market, demand, stock,* etc.
                                                |  **Travel Restriction** includes *country, china,travel, restriction*etc.
                                                
                                                ''')
                                ]
                            
                        ),
                    ] 
                ),
            ]
        )
        
    ])

##Callback for five emotions line graph
@app.callback(
    Output('number_sentiment','figure'),
    [Input('Sentiment_5selector','value')]
)

def update_graph_sentiment_5(selected_dropdown_value):
    dff = number_sentiment_df

    sentiment = px.line(
        data_frame=dff,
        x = dff.index,
        y = selected_dropdown_value

    )

    sentiment.update_layout(
                #colorway=["#5E0DAC", '#FF4F00', '#375CB1', '#FF7400', '#FFF400', '#FF0056'],
                template='plotly_dark',
                paper_bgcolor='rgba(0, 0, 0, 0)',
                plot_bgcolor='rgba(0, 0, 0, 0)',
                margin={'b': 15},
                hovermode='x',
                autosize=True,
                  title={'text': 'Sentiment level Recorded w.r.t Date', 'font': {'color': 'white'}, 'x': 0.5},
                #xaxis={'range': [df_sub.index.min(), df_sub.index.max()]},
                xaxis_title="Date",
                yaxis_title="Sentiment level(%)",
    )
    

    return (sentiment)


##Callback for positive/negative/neutral line graph
@app.callback(
    Output('pos_neg_graph','figure'),
    [Input('Sentimentselector','value')]
)

def update_graph_sentiment(selected_dropdown_value):
    dff = pos_df
    dff.index = pd.to_datetime(dff['created_at'])
    sentiment = px.line(
        data_frame=dff,
        x = dff.index,
        y = selected_dropdown_value

    )

    sentiment.update_layout(
                colorway=["#5E0DAC", '#FF4F00', '#375CB1', '#FF7400', '#FFF400', '#FF0056'],
                template='plotly_dark',
                paper_bgcolor='rgba(0, 0, 0, 0)',
                plot_bgcolor='rgba(0, 0, 0, 0)',
                margin={'b': 15},
                hovermode='x',
                autosize=True,
                title={'text': 'Number of Tweets', 'font': {'color': 'white'}, 'x': 0.5},
                xaxis_title="Date",
                yaxis_title="Count",
    )
    

    return (sentiment)


if __name__ == '__main__':
    app.run_server(debug=True)
