from udacity import get_file_content_as_string
import streamlit as st
import utils
import pandas as pd
import time


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

    # <div id = "uniqueDiv"></div>
    # <script>
    #     document.getElementById("#uniqueDiv").innerHTML = "Hello World!"
    # </script>

    main_panel = st.beta_container()
    sidebar = st.sidebar.beta_container()
    model_builder_button = st.sidebar.empty()

    sidebar.markdown('#### 1. Selects a dataset')
    dataset_selector = sidebar.selectbox('Select a dataset to proceed',
                                         ('Click here...', 'Diabetes.csv', 'Breast-Cancer.csv', 'Waveform.csv',
                                          'Image.csv', 'Segment.csv', 'Glass.csv', 'Heart.csv')
                                         )

    if dataset_selector == 'Click here...':
        main_panel.success('Awaiting for user to select a dataset...')
    else:
        # Sidebar - Specify parameter settings
        with sidebar.markdown('#### 2. Set Parameters'):
            split_size = sidebar.slider(
                'Data split ratio (% for Training Set)', 10, 90, 80, 5)
            seed_number = sidebar.slider(
                'Set the random seed number', 1, 100, 42, 1)

            model_builder_button.button('🔧 Build Models')

        dataset = utils.get_dataset(dataset_selector)
        print(dataset)
        with main_panel:
            progress_bar = main_panel.progress(0)
            df = pd.read_csv(dataset)

            percent_complete = 1

            for percent_complete in range(100):
                progress_bar.progress(percent_complete + 1)
            time.sleep(0.5)
            message = main_panel.success(
                f'Successfully loaded {dataset_selector}')

            time.sleep(1)
            progress_bar.empty()
            message.empty()

            main_panel.write(f'#### Dataset: {dataset_selector}\n')
            main_panel.write(df)


if __name__ == '__main__':
    main()
