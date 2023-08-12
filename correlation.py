import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    st.title("Data Analysis with Streamlit")

    # File Upload
    st.sidebar.title("Upload Data")
    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=["csv"])

    if uploaded_file is not None:
        st.sidebar.subheader("Data Preview")
        df = pd.read_csv(uploaded_file)
        st.sidebar.write(df.head())

        # Data Exploration and Visualization
        if not df.empty:
            st.sidebar.subheader("Data Exploration")
            selected_columns = st.sidebar.multiselect("Select columns to show", df.columns)
            if selected_columns:
                st.write(df[selected_columns])

            st.sidebar.subheader("Data Visualization")
            plot_type = st.sidebar.selectbox("Select plot type", ["Histogram", "Box Plot", "Correlation Heatmap"])

            if plot_type == "Histogram":
                st.subheader("Histogram")
                selected_column = st.selectbox("Select a column", df.columns)
                plt.hist(df[selected_column], bins=20, edgecolor="k")
                st.pyplot()

            elif plot_type == "Box Plot":
                st.subheader("Box Plot")
                selected_column = st.selectbox("Select a column", df.columns)
                if df[selected_column].dtype in [float, int]:
                    sns.boxplot(data=df, y=selected_column)
                    st.pyplot(plt.gcf())
                else:
                    st.write("Selected column is not numeric. Please choose a numeric column for the box plot.")

            elif plot_type == "Correlation Heatmap":
                st.subheader("Correlation Heatmap")
                numeric_df = df.select_dtypes(include=['float64', 'int64'])  # Select numeric columns only
                corr_matrix = numeric_df.corr(method='spearman')
                plt.figure(figsize=(10, 8))
                sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", linewidths=.5)
                st.pyplot(plt.gcf())

if __name__ == "__main__":
    main()
