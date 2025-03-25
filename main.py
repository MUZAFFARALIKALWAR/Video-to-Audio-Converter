import streamlit as st
from moviepy import VideoFileClip

def convert_video_to_audio(video_path):
    # Load the video file
    video = VideoFileClip(video_path)
    
    # Extract the audio
    audio = video.audio
    
    # Save the audio file
    audio_file = "audio.mp3"
    audio.write_audiofile(audio_file)
    
    return audio_file

# Streamlit UI
st.title("Video to Audio Converter")
st.write("Upload a video file to extract audio")

video_file = st.file_uploader("Upload Video", type=["mp4", "avi", "mov"])

if video_file is not None:
    # Save uploaded file
    with open("temp_video.mp4", "wb") as f:
        f.write(video_file.getbuffer())

    if st.button("Convert"):
        audio_path = convert_video_to_audio("temp_video.mp4")
        
        st.success("Audio extracted successfully!")
        st.audio(audio_path)

        # ✅ **Add a Download Button**
        with open(audio_path, "rb") as f:
            st.download_button(label="Download Audio",
                               data=f,
                               file_name="extracted_audio.mp3",
                               mime="audio/mp3")
