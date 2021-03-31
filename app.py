import SessionState
import streamlit as st
import utils
import pandas as pd
import time
import models as models


def main():

    st.write(''' # Machine Learning: A comparison of classification algorithms
    
    ---  
    
    ''')
    instructions = st.markdown("""

        Jumpstart to find the best class of algorithm for your data:

        >   1. 👈 Select **Run the app** from the sidebar *(click on **>** if closed)* 
        2. Select a dataset to get started
        3. Click "📊 Visualize Dataset" to analyze the dataset
        4. Click ":rocket: Build Models" to start comparision among different models
        5. Select a model for hyperparameter tuning and click ":rocket: Tune Model"
        6. Find the best model & do your magic! :sparkles:
        
        ---
        """)
    st.sidebar.write('''
        ## Welcome!
        ''')
    app_mode = st.sidebar.selectbox(
        "Choose the app mode", ["Show instructions", "Run the app"])

    if app_mode == "Show instructions":
        st.sidebar.success('To continue select "Run the app".')
    elif app_mode == "Run the app":
        instructions.empty()
        run_the_app()


def run_the_app():

    sidebar = st.sidebar.beta_container()
    main_panel = st.empty()
    parameters_sidebar = st.sidebar.beta_container()
    model_builder_button = st.sidebar.empty()


    sidebar.markdown('#### 1. Selects a dataset')
    dataset_selector = sidebar.selectbox('Select a dataset to proceed',
                                         ('Click here...', 'Diabetes.csv', 'Breast-Cancer.csv', 'Waveform.csv',
                                          'Image.csv', 'Segment.csv', 'Glass.csv', 'Heart.csv')
                                         )
    flag = False
    if dataset_selector == 'Click here...':
        main_panel.info('Awaiting for user to select a dataset...')
    else:
        # Sidebar - Specify parameter settings

        flag = True
        v = sidebar.button(f'Visualize Dataset {dataset_selector}\n')
        with sidebar.markdown('#### 2. Set Parameters'):
            split_size = sidebar.slider(

        with parameters_sidebar.markdown('#### 2. Set Parameters'):
            split_size = parameters_sidebar.slider(

                'Data split ratio (% for Training Set)', 10, 90, 80, 5)
            seed_number = parameters_sidebar.slider(
                'Set the random seed number', 1, 100, 42, 1)


            build = sidebar.button('🔧 Build Models')
        st.write(f'#### Dataset: {dataset_selector}\n')

            dataset_selection_status = model_builder_button.button(
                '🔧 Build Models')


        dataset = utils.get_dataset(dataset_selector)

        print(dataset)

        with main_panel.beta_container():
            progress_bar = main_panel.progress(0)

        with main_panel:

            df = pd.read_csv(dataset)

            percent_complete = 1

            message = main_panel.empty()
            message.info(
                f'Fetching {dataset_selector}')
            progress_bar = main_panel.progress(0)

            for percent_complete in range(100):
                progress_bar.progress(percent_complete + 1)
                time.sleep(0.005)

            time.sleep(0.5)

            progress_bar.empty()
            message.success(
                f'Successfully loaded {dataset_selector}')

            time.sleep(1)

            message.empty()

            main_panel.write(df)


    if flag:
        if v:
            main_panel.empty()
            visualizer(df)
        elif build:
            build_model = st.beta_container()
            build_model.subheader('1. Performance for {}'.format(
                dataset.split('/')[-1]))
            classificationReports = models.driver(dataset, 0.2)
            counter = 1

            for model in classificationReports:
                build_model.write("**1.{}. {}**".format(str(counter), model))
                build_model.write(classificationReports[model])
                counter += 1


def visualizer(df):
    visualize = st.beta_container()
    with visualize:
        visualize.subheader('1. Dataset')
        visualize.markdown('1.1. Glimpse of dataset')
        visualize.write(df.head(10))

        # Using all column except for the last column as X

        X = df.iloc[:, :-1]
        Y = df.iloc[:, -1]  # Selecting the last column as Y

        visualize.markdown('1.2. Dataset dimension')
        cols = visualize.beta_columns(2)
        cols[0].write('X')
        cols[0].info('{} rows, {} attributes'.format(
            X.shape[0], X.shape[1]))
        cols[1].write('Y')
        cols[1].info('{} responses'.format(Y.shape[0]))

        visualize.markdown('1.3. Variable details:')
        visualize.write('X variables (first 20 are shown)')

        attributes = list(X.columns[:20])
        visualize.markdown('{}'.format(attributes))

        visualize.write('Y variable')
        visualize.markdown('{}'.format(Y.name))
            # Logic when button is clicked
            if dataset_selection_status:
                parameters_sidebar.empty()



if __name__ == '__main__':
    main()
