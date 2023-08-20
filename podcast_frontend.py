import streamlit as st
import modal
import json
import os

def main():
    st.title("Newsletter Dashboard")

    # Set the font and font size for the variable names and comments
    st.set_option('font', 'Roboto')
    st.set_option('font_size', 12)

    # Use colors to highlight the different parts of the code
    st.color_code(comments='light_blue', code='dark_blue')

    # Use images and icons to represent the different steps of the process
    image_magnifying_glass = st.image('https://iconfinder.com/icons/2408457/search_magnifier_magnifying_glass_loupe_icon')
    image_check_mark = st.image('https://iconfinder.com/icons/2518105/check_tick_ok_success_icon')

    available_podcast_info = create_dict_from_json_files('.')

    # Left section - Input fields
    st.sidebar.header("Podcast RSS Feeds")

    # Dropdown box
    st.sidebar.subheader("Available Podcasts Feeds")
    selected_podcast = st.sidebar.selectbox(
        "Select Podcast",
        options=available_podcast_info.keys(),
        icon=image_magnifying_glass
    )

    if selected_podcast:

        podcast_info = available_podcast_info[selected_podcast]

        # Right section - Newsletter content
        st.header("Newsletter Content")

        # Display the podcast title
        st.subheader("Episode Title")
        st.write(podcast_info['podcast_details']['episode_title'], unsafe_allow_html=True)

        # Display the podcast summary and the cover image in a side-by-side layout
        col1, col2 = st.columns([7, 3])

        with col1:
            # Display the podcast episode summary
            st.subheader("Podcast Episode Summary")
            st.write(podcast_info['podcast_summary'], unsafe_allow_html=True)

        with col2:
            st.image(podcast_info['podcast_details']['episode_image'], caption="Podcast Cover", width=300, use_column_width=True, icon=image_magnifying_glass)

        # Display the podcast guest and their details in a side-by-side layout
        col3, col4 = st.columns([3, 7])

        with col3:
            st.subheader("Podcast Guest")
            st.write(podcast_info['podcast_guest']['name'], unsafe_allow_html=True)
        with col4:
            st.subheader("Podcast Guest Details")
            st.write(podcast_info["podcast_guest"]['org'], unsafe_allow_html=True)

        # Display the five key moments
        st.subheader("Key Moments")
        key_moments = podcast_info['podcast_highlights']
        for moment in key_moments.split('\n'):
            st.markdown(
                f"<p style='margin-bottom: 5px;'>{moment}</p>", unsafe_allow_html=True)

    # User Input box
    st.sidebar.subheader("Add and Process New Podcast Feed")
    url = st.sidebar.text_input("Link to RSS Feed", icon=image_magnifying_glass)

    process_button = st.sidebar.button("Process Podcast Feed", icon=image_check_mark)
    st.sidebar.markdown("**Note**: Podcast processing can take upto 5 mins, please be patient.")

    if process_button:

        # Call the function to process the URLs and retrieve podcast guest information
        podcast_info = process_podcast_info(url)

        # Right section - Newsletter content
        st.header("Newsletter Content")

        # Display the podcast title
        st.subheader("Episode Title")
        st.write(podcast_info['podcast_details']['episode_title'], unsafe_allow_html=True)

        # Display the podcast summary and the cover image in a side-by-side layout
        col1
