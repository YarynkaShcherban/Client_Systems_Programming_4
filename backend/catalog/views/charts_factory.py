import plotly.graph_objects as go
import plotly.express as px
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool
from math import pi

TEMPLATE_STYLE = 'plotly_white'

LINE_CHART_LAYOUT_UPDATES = {
    'xaxis': {'gridcolor': '#e0e0e0', 'griddash': 'dash'},
    'yaxis': {'gridcolor': '#e0e0e0', 'griddash': 'dash'},
    'plot_bgcolor': 'white'
}

CUSTOM_COLORS_PIE = ['#22577a', '#38a3a5', '#57cc99', '#80ed99', '#c7f9cc']
EXPENSIVE_PUB_COLORS = ['#0d47a1', '#1565c0', '#1976d2', '#1e88e5', '#2196f3',
                        '#42a5f5', '#64b5f6', '#90caf9', '#bbdefb', '#e3f2fd']


def apply_bokeh_styles(fig):
    fig.xaxis.major_label_text_font_size = "11pt"
    fig.yaxis.major_label_text_font_size = "11pt"
    fig.xaxis.axis_label_text_font_size = "12pt"
    fig.yaxis.axis_label_text_font_size = "12pt"
    fig.xaxis.axis_label_text_font_style = "bold"
    fig.yaxis.axis_label_text_font_style = "bold"
    return fig

def create_main_stats_plotly(df):
    if df is None or df.empty: return None
    fig = go.Figure()
    traces = [
        ('Середнє', 'avg_price', '#219ebc'),
        ('Медіана', 'median_price', '#fb8500'),
        ('Мінімум', 'min_price', '#2a9d8f'),
        ('Максимум', 'max_price', '#e63946')
    ]
    
    for name, col, color in traces:
        fig.add_trace(go.Bar(name=name, x=df['genre'], y=df[col], marker_color=color))
    fig.update_layout(
        xaxis_title='Жанр', yaxis_title='Ціна (грн)', barmode='group',
        template=TEMPLATE_STYLE, xaxis_tickangle=20, hovermode='x unified',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    return fig

def create_genres_count_plotly(df):
    if df is None or df.empty: return None
    df_sorted = df.sort_values('num_books', ascending=False)
    fig = px.bar(df_sorted, x='name', y='num_books', 
                 labels={'name': 'Жанр', 'num_books': 'Кількість книг'},
                 template=TEMPLATE_STYLE)
    fig.update_traces(marker_color='#8ECAE6')
    return fig

def create_genres_price_plotly(df):
    if df is None or df.empty: return None
    df_sorted = df.sort_values('avg_price', ascending=False)
    fig = px.line(df_sorted, x='name', y='avg_price',
                  labels={'name': 'Жанр', 'avg_price': 'Середня ціна, грн'},
                  template=TEMPLATE_STYLE, markers=True)
    fig.update_layout(LINE_CHART_LAYOUT_UPDATES)
    return fig

def create_authors_price_plotly(df):
    if df is None or df.empty: return None
    df_sorted = df.sort_values('avg_price', ascending=False)
    fig = px.line(df_sorted, x='full_name', y='avg_price',
                  labels={'full_name': 'Автор', 'avg_price': 'Середня ціна, грн'},
                  template=TEMPLATE_STYLE, markers=True)
    fig.update_layout(LINE_CHART_LAYOUT_UPDATES)
    fig.update_traces(line_color='#f4a259')
    fig.update_layout(xaxis={'tickangle': 45})
    return fig

def create_top_authors_pie_plotly(df):
    if df is None or df.empty: return None
    fig = px.pie(df, values='num_books', names='full_name', hole=0.3,
                 template=TEMPLATE_STYLE,
                 color_discrete_sequence=CUSTOM_COLORS_PIE[:len(df)])
    return fig

def create_publishers_price_plotly(df):
    if df is None or df.empty: return None
    df_sorted = df.sort_values('avg_price', ascending=False)
    fig = px.line(df_sorted, x='name', y='avg_price',
                  labels={'name': 'Видавництво', 'avg_price': 'Середня ціна, грн'},
                  template=TEMPLATE_STYLE, markers=True)
    fig.update_layout(LINE_CHART_LAYOUT_UPDATES)
    fig.update_traces(line_color='#2a9d8f')
    fig.update_layout(xaxis={'tickangle': 20})
    return fig

def create_expensive_publishers_pie_plotly(df):
    if df is None or df.empty: return None
    fig = px.pie(df, names='name', values='avg_price',
                 title="Дорогі видавництва (розподіл за ціною)",
                 template=TEMPLATE_STYLE,
                 color_discrete_sequence=EXPENSIVE_PUB_COLORS[:len(df)],
                 hole=0.3)
    return fig

def create_store_sales_plotly(df):
    if df is None or df.empty: return None
    df_sorted = df.sort_values('total_sales', ascending=False)
    fig = px.bar(df_sorted, x='name', y='total_sales',
                 labels={'name': 'Магазин', 'total_sales': 'Сума продажів, грн'},
                 template=TEMPLATE_STYLE, color='total_sales',
                 color_continuous_scale=px.colors.sequential.Viridis)
    return fig

def create_store_count_plotly(df):
    if df is None or df.empty: return None
    df_sorted = df.sort_values('total_purchases', ascending=False)
    fig = px.line(df_sorted, x='name', y='total_purchases',
                  labels={'name': 'Магазин', 'total_purchases': 'Кількість продажів'},
                  template=TEMPLATE_STYLE, markers=True)
    fig.update_layout(LINE_CHART_LAYOUT_UPDATES)
    fig.update_traces(line_color='#bc4b51')
    return fig

def create_genres_count_bokeh(df):
    if df is None or df.empty: return None
    df_sorted = df.sort_values('num_books', ascending=False)
    p = figure(x_axis_label="Жанр", y_axis_label="Кількість книг",
               x_range=df_sorted['name'].tolist(), height=400,
               sizing_mode="stretch_width", output_backend="svg")
    p.vbar(x='name', top='num_books', width=0.7, source=ColumnDataSource(df_sorted), fill_color="#8ECAE6")
    p.add_tools(HoverTool(tooltips=[("Жанр", "@name"), ("Кількість", "@num_books")]))
    return apply_bokeh_styles(p)

def create_genres_price_bokeh(df):
    if df is None or df.empty: return None
    df_sorted = df.sort_values('avg_price', ascending=False)
    p = figure(x_axis_label="Жанр", y_axis_label="Середня ціна, грн",
               x_range=df_sorted['name'].tolist(), height=400,
               sizing_mode="stretch_width", output_backend="svg")
    p.line(x='name', y='avg_price', source=ColumnDataSource(df_sorted), line_width=3, color="#219ebc")
    p.add_tools(HoverTool(tooltips=[("Жанр", "@name"), ("Ціна", "@avg_price")]))
    return apply_bokeh_styles(p)

def create_authors_price_bokeh(df):
    if df is None or df.empty: return None
    df_sorted = df.sort_values('avg_price', ascending=False)
    p = figure(x_axis_label="Автор", y_axis_label="Середня ціна, грн",
               x_range=df_sorted['full_name'].tolist(), height=400,
               sizing_mode="stretch_width", output_backend="svg")
    p.vbar(x='full_name', top='avg_price', width=0.7, source=ColumnDataSource(df_sorted), color="#f4a259")
    p.xaxis.major_label_orientation = pi/4
    p.add_tools(HoverTool(tooltips=[("Автор", "@full_name"), ("Ціна", "@avg_price")]))
    return apply_bokeh_styles(p)

def create_top_authors_bokeh(df):
    if df is None or df.empty: return None
    p = figure(x_axis_label="Автор", y_axis_label="Кількість книг",
               x_range=df['full_name'].tolist(), height=400,
               sizing_mode="stretch_width", output_backend="svg")
    p.vbar(x='full_name', top='num_books', source=ColumnDataSource(df), width=0.7, color='#57cc99')
    p.xaxis.major_label_orientation = pi/4
    p.add_tools(HoverTool(tooltips=[("Автор", "@full_name"), ("Книг", "@num_books")]))
    return apply_bokeh_styles(p)

def create_pub_price_bokeh(df):
    if df is None or df.empty: return None
    df_sorted = df.sort_values('avg_price', ascending=False)
    p = figure(x_axis_label="Видавництво", y_axis_label="Середня ціна, грн",
               x_range=df_sorted['name'].tolist(), height=400,
               sizing_mode="stretch_width", output_backend="svg")
    p.line(x='name', y='avg_price', source=ColumnDataSource(df_sorted), line_width=3, color='#2a9d8f')
    p.xaxis.major_label_orientation = pi/4
    p.add_tools(HoverTool(tooltips=[("Видавництво", "@name"), ("Ціна", "@avg_price")]))
    return apply_bokeh_styles(p)

def create_expensive_pub_bokeh(df):
    if df is None or df.empty: return None
    p = figure(x_axis_label="Видавництво", y_axis_label="Середня ціна, грн",
               x_range=df['name'].tolist(), height=400,
               sizing_mode="stretch_width", output_backend="svg")
    p.vbar(x='name', top='avg_price', source=ColumnDataSource(df), width=0.7, color='#1565c0')
    p.xaxis.major_label_orientation = pi/4
    p.add_tools(HoverTool(tooltips=[("Видавництво", "@name"), ("Ціна", "@avg_price")]))
    return apply_bokeh_styles(p)

def create_store_sales_bokeh(df):
    if df is None or df.empty: return None
    df_sorted = df.sort_values('total_sales', ascending=False)
    p = figure(x_axis_label="Магазин", y_axis_label="Сума продажів, грн",
               x_range=df_sorted['name'].tolist(), height=400,
               sizing_mode="stretch_width", output_backend="svg")
    p.vbar(x='name', top='total_sales', source=ColumnDataSource(df_sorted), width=0.7, color="#8ecae6")
    p.add_tools(HoverTool(tooltips=[("Магазин", "@name"), ("Сума", "@total_sales")]))
    return apply_bokeh_styles(p)

def create_store_count_bokeh(df):
    if df is None or df.empty: return None
    df_sorted = df.sort_values('total_purchases', ascending=False)
    p = figure(x_axis_label="Магазин", y_axis_label="Кількість продажів",
               x_range=df_sorted['name'].tolist(), height=400,
               sizing_mode="stretch_width", output_backend="svg")
    p.line(x='name', y='total_purchases', source=ColumnDataSource(df_sorted), line_width=3, color='#bc4b51')
    p.add_tools(HoverTool(tooltips=[("Магазин", "@name"), ("Кількість", "@total_purchases")]))
    return apply_bokeh_styles(p)

def create_benchmark_line_chart(df, title, color='#2196f3', x_col='threads', y_col='total_time'):
    if df is None or df.empty: return None
    
    fig = px.line(
        df, x=x_col, y=y_col, 
        title=title,
        markers=True, 
        template='plotly_white'
    )
    fig.update_traces(line_color=color)
    return fig