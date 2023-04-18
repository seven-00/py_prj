import streamlit as st
import pytube as yt
with open( "\style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)


st.title="YouTube video downloader"
st.subheader("Enter the link of the video you want to download") 
url=st.text_input(label="URL")

if url != '':
    yt = YouTube(url)
    st.image(yt.thumbnail_url, width=300)
    st.subheader('''
    {}
    ## Length: {} seconds
    ## Rating: {} 
    '''.format(yt.title , yt.length , yt.rating))
    video = yt.streams
    if len(video) > 0:
        downloaded , download_audio = False , False
        download_video = st.button("Download Video")
        if yt.streams.filter(only_audio=True):
            download_audio = st.button("Download Audio Only")
        if download_video:
            video.get_lowest_resolution().download()
            downloaded = True
        if download_audio:
            video.filter(only_audio=True).first().download()
            downloaded = True
        if downloaded:
            st.subheader("Download Complete")
else:
    st.subheader("Sorry, this video can not be downloaded")
