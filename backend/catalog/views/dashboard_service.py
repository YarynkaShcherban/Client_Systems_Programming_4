from plotly.offline import plot
from bokeh.embed import components
from .data_dashboard import *
from .charts_factory import *


def get_dashboard_figures():
    df_main = get_main_stats_df()
    df_genres = get_genres_stats_df()
    df_authors = get_authors_stats_df()
    df_top_authors = get_top_authors_df()
    df_publishers = get_publishers_stats_df()
    df_expensive_pub = get_expensive_publishers_df()
    df_stores = get_store_stats_df()

    def to_div(fig):
        return plot(fig, output_type='div') if fig else "<p>Немає даних</p>"

    plotly_figs = {
        'fig_main_stats': to_div(create_main_stats_plotly(df_main)),
        'fig_genres_count': to_div(create_genres_count_plotly(df_genres)),
        'fig_genres_price': to_div(create_genres_price_plotly(df_genres)),
        'fig_authors_price': to_div(create_authors_price_plotly(df_authors)),
        'fig_top_authors': to_div(create_top_authors_pie_plotly(df_top_authors)),
        'fig_publishers_price': to_div(create_publishers_price_plotly(df_publishers)),
        'fig_expensive_pub': to_div(create_expensive_publishers_pie_plotly(df_expensive_pub)),
        'fig_store_sales': to_div(create_store_sales_plotly(df_stores)),
        'fig_store_count': to_div(create_store_count_plotly(df_stores)),
    }

    def get_bokeh_comp(fig):
        if fig:
            return components(fig)
        return "", "<p>Немає даних</p>"

    b_script_1, b_div_1 = get_bokeh_comp(create_genres_count_bokeh(df_genres))
    b_script_2, b_div_2 = get_bokeh_comp(create_genres_price_bokeh(df_genres))
    b_script_3, b_div_3 = get_bokeh_comp(create_authors_price_bokeh(df_authors))
    b_script_4, b_div_4 = get_bokeh_comp(create_top_authors_bokeh(df_top_authors))
    b_script_5, b_div_5 = get_bokeh_comp(create_pub_price_bokeh(df_publishers))
    b_script_6, b_div_6 = get_bokeh_comp(create_expensive_pub_bokeh(df_expensive_pub))
    b_script_7, b_div_7 = get_bokeh_comp(create_store_sales_bokeh(df_stores))
    b_script_8, b_div_8 = get_bokeh_comp(create_store_count_bokeh(df_stores))

    result = {
        **plotly_figs, 
        
        "bokeh_genres_count_script": b_script_1,
        "bokeh_genres_count_div": b_div_1,
        
        "bokeh_genres_price_script": b_script_2,
        "bokeh_genres_price_div": b_div_2,
        
        "bokeh_authors_price_script": b_script_3,
        "bokeh_authors_price_div": b_div_3,
        
        "bokeh_top_authors_script": b_script_4,
        "bokeh_top_authors_div": b_div_4,
        
        "bokeh_publishers_price_script": b_script_5,
        "bokeh_publishers_price_div": b_div_5,
        
        "bokeh_expensive_pub_script": b_script_6,
        "bokeh_expensive_pub_div": b_div_6,
        
        "bokeh_store_sales_script": b_script_7,
        "bokeh_store_sales_div": b_div_7,
        
        "bokeh_store_count_script": b_script_8,
        "bokeh_store_count_div": b_div_8,
    }

    return result