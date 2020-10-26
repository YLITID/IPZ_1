import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import time



app = dash.Dash(__name__,)

colors = {
    'background': '#111111',
    'text': '#009a00'
}

app.layout = html.Div([
    html.Div(
        className="banner",
        children = [html.H2("WorkspaceC.alpha 0.1",
                        style={
                        'color': colors['text'],
                        }),
                    html.Img(src='/assets/stock_icon.png')]),
    html.Div(
        children=html.Div([
            html.H5('Log in'),

        ])),
    html.Div(["Input: ",
              dcc.Input(id='my-input', value='initial value', type='text')]),
    html.Div(["Write: ",
              html.Button(id='time-button', children='Gettime')]),
    html.Br(),
    html.Div(id='my-output'),

])

@app.callback(
    Output(component_id='my-output', component_property='children'),
    [Input(component_id='time-button', component_property='n_clicks')]
)
def update_output_div(input_value):
    return 'Now is: {}'.format(time.asctime())


if __name__ == '__main__':
    app.run_server(debug=True)
