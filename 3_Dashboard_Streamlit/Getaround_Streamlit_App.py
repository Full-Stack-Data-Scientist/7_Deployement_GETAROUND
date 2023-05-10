# importing our depedencies
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp


st. set_page_config(layout='wide',
                    page_title='Getaround Dashboard',
                    page_icon='🚖',
                    )

st.title('Getaround Dashboard')


tab1, tab2 = st.tabs(['Fleet information and rental price per day', 'Delay analysis and threshold'])

with tab1:

    # --------------------------------------------------------------------------------
    st.subheader('📝 Fleet information and rental price per day')

    df_price = pd.read_pickle('price_analysis_df_clean.csv')

    st.write(df_price)
    st.divider()

    # --------------------------------------------------------------------------------
    st.subheader('Statistics')

    df_stats = df_price.describe().apply(lambda s: s.apply('{0:.2f}'.format))

    st.write(df_stats)
    st.divider()

    # --------------------------------------------------------------------------------
    st.subheader('📊 Features visualization')

    fig = None
    plot_displayed = False

    # I create a function I'll be able to call each time I need to plot a graph
    def histogram_plot(columns):
                
        global plot_displayed, fig

        # clear the existing figures
        if fig:
            fig.clear()
        
        num_cols = 4

        if len(columns) > 4:
            st.warning('⚠️ Please select up to 4 columns maximum ⚠️')

        if len(columns) > 1:

            fig = sp.make_subplots(rows=1, cols=num_cols, subplot_titles=columns, column_widths=[10, 10, 10, 10])

            # I create a for loop to go through each column
            for i, column in enumerate(columns):

                fig.add_trace(
                    go.Histogram(x=df_price[column], nbinsx=10), row=1, col=(i%num_cols)+1
                    )
                
                # I set the layout to have a nice figure to read      
                fig.update_xaxes(title_text=column.upper(), row=1, col=(i%num_cols)+1)
                fig.update_yaxes(title_text='Frequencies', row=1, col=(i%num_cols)+1)
                fig.update_layout(
                    height=750,
                    width=1350,
                    title=f'Representation of the column:',
                    title_font={"size": 20},
                    xaxis_tickfont_size=14,
                    yaxis_tickfont_size=14,
                )

            # Show the plot figures
            st.plotly_chart(fig)
            plot_displayed = True

        else:
            column = columns[0]

            fig = go.Figure(go.Histogram(x=df_price[column], nbinsx=10))

            # I set the layout to have a nice figure to read
            fig.update_layout(
                height=750,
                width=1350,
                title=f'Representation of the column: <b>{column.upper()}</b>',
                title_font={"size": 20},
                xaxis_tickfont_size=14,
                yaxis_tickfont_size=14,
                xaxis={'title': column.upper(), 'title_font': {'size': 16}},
                yaxis={'title': 'FREQUENCIES', 'title_font': {'size': 16}}
            )
            
            st.plotly_chart(fig)

            plot_displayed = True

    columns = ['model_key',
    'fuel',
    'paint_color',
    'car_type',
    'private_parking_available',
    'has_gps',
    'has_air_conditioning',
    'automatic_car',
    'has_getaround_connect',
    'has_speed_regulator',
    'winter_tires',]

    st.info('📣 Please select up to 4 columns you want to visualize')

    selected_columns = st.multiselect('',columns)

    if st.button('🟢 Click here to display the selected columns'):
        if len(selected_columns) > 0:
            histogram_plot(selected_columns)
        else:
            st.warning('⚠️ Please select at least one column to display ⚠️')

    if plot_displayed :
        if st.button('🔴 Click here to clear this chart'):
            fig = None

# --------------------------------------------------------------------------------
with tab2:
    st.subheader('📊 Rentals information')

    df_delay = pd.read_pickle('delay_analysis_df_clean.csv')

    st.write(df_delay)
    st.divider()


    # --------------------------------------------------------------------------------
    st.subheader('Statistics')

    df_stats_2 = df_delay.describe().apply(lambda s: s.apply('{0:.2f}'.format))

    st.write(df_stats_2)
    st.divider()


    # --------------------------------------------------------------------------------
    st.subheader('📊 Features visualization')

    df_delay_0 = pd.read_excel('get_around_delay_analysis.xlsx')
    
    fig_1 = px.histogram(df_delay_0, 
                         x='state', 
                         color='checkin_type', 
                         title = 'Rental States',)
    st.plotly_chart(fig_1)

    col1, col2 = st.columns(2)
    with col1:  
        fig_2 = px.histogram(df_delay, 
                    x='delay_at_checkin',
                    color='checkin_type',
                    title = 'Number of Delay at the <b>Checkin</b> phase')
        st.plotly_chart(fig_2)

    with col2:  
        fig_3 = px.histogram(df_delay, 
                x='delay_at_checkout',
                color='checkin_type',
                title = 'Number of Delay at the <b>Checkout</b> phase')
        st.plotly_chart(fig_3)

# --------------------------------------------------------------------------------
    st.subheader('📊 Threshold impact analysis')

    df_threshold = pd.read_pickle('threshold_analysis_df_clean.csv')

    fig_4 = px.line (df_threshold,
            x = 'threshold',
            y = 'nb_of_rentals_impacted_by_threshold',
            color = 'checkin_type', 
            text = 'nb_of_rentals_impacted_by_threshold',
            )

    fig_4.update_traces(textposition = 'bottom right')

    fig_4.update_layout(
        height=700,
        width=1350,
        title = '<b>Overall impact of thresholds on rentals</b>',
        title_font={'size': 20}, 
        xaxis={'title': 'Threshold in minutes', 'title_font': {'size': 16}},
        yaxis={'title': 'Number of rentals impacted', 'title_font': {'size': 16}},
    )
    st.plotly_chart(fig_4)

    # -------------------------

    df_cancelation = pd.read_pickle('cancelation_threshold_analysis_df_clean.csv')

    fig_5 = px.line (df_cancelation,
            x = 'threshold',
            y = 'nb_of_rentals_impacted_by_threshold',
            color = 'checkin_type', 
            text = 'nb_of_rentals_impacted_by_threshold',
            )

    fig_5.update_traces(textposition = 'bottom right')

    fig_5.update_layout(
        height=700,
        width=1350,
        title = '<b>Canceled rentals avoided by thresholds</b>',
        title_font={'size': 20}, 
        xaxis={'title': 'Threshold in minutes', 'title_font': {'size': 16}},
        yaxis={'title': 'Number of rentals impacted', 'title_font': {'size': 16}},
    )
    st.plotly_chart(fig_5)

    # -------------------------

    df_late_checkout = pd.read_pickle('late_checkout_threshold_analysis_df_clean.csv')

    fig_6 = px.line (df_late_checkout,
            x = 'threshold',
            y = 'nb_of_rentals_impacted_by_threshold',
            color = 'checkin_type', 
            text = 'nb_of_rentals_impacted_by_threshold',
            )

    fig_6.update_traces(textposition = 'bottom right')

    fig_6.update_layout(
        height=700,
        width=1350,
        title = '<b>Rentals not impacted by the previous rental delay during the checkout depending on the thresholds</b>',
        title_font={'size': 20}, 
        xaxis={'title': 'Threshold in minutes', 'title_font': {'size': 16}},
        yaxis={'title': 'Number of rentals impacted', 'title_font': {'size': 16}},
    )
    st.plotly_chart(fig_6)

    # -------------------------

    df_revenue = pd.read_pickle('revenue_threshold_impact_df_clean.csv')

    fig_7 = px.line (df_revenue,
        x = 'threshold',
        y = 'owner_revenue_affected_by_threshold',
        color = 'checkin_type', 
        text = 'owner_revenue_affected_by_threshold',
        )

    fig_7.update_traces(textposition = 'bottom right')

    fig_7.update_layout(
        height=700,
        width=1350,
        title = "<b>Share of owner's revenue affected by threshold</b>",
        title_font={'size': 20}, 
        xaxis={'title': 'Threshold in minutes', 'title_font': {'size': 16}},
        yaxis={'title': 'Proportion of revenue impacted', 'title_font': {'size': 16}},
    )
    st.plotly_chart(fig_7)