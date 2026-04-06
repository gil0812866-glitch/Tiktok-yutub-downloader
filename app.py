import streamlit as st
import yt_dlp
import os, time, glob

st.set_page_config(page_title="OMNI-WEB", page_icon="🚀")
st.title("🚀 OMNI-WEB v1.0")
st.subheader("TikTok & Spotify Downloader")

def clean():
    for f in glob.glob("web_dl_*"):
        try: os.remove(f)
        except: pass

url = st.text_input("Tempel Link TikTok atau Spotify:")

if url:
    c1, c2 = st.columns(2)
    with c1:
        if st.button("🎬 Video (No WM)"):
            with st.spinner("Proses..."):
                clean()
                fid = f"web_dl_{int(time.time())}.mp4"
                with yt_dlp.YoutubeDL({'format':'best','outtmpl':fid,'quiet':True}) as ydl:
                    info = ydl.extract_info(url, download=True)
                    st.download_button("📥 Simpan Video", open(fid,"rb"), file_name=f"{info.get('title', 'video')}.mp4")
    with c2:
        if st.button("🎵 Audio MP3"):
            with st.spinner("Proses..."):
                clean()
                fid = f"web_dl_{int(time.time())}"
                opts = {'format':'bestaudio','outtmpl':fid,'postprocessors':[{'key':'FFmpegExtractAudio','preferredcodec':'mp3'}]}
                with yt_dlp.YoutubeDL(opts) as ydl:
                    info = ydl.extract_info(url, download=True)
                    st.download_button("📥 Simpan MP3", open(f"{fid}.mp3","rb"), file_name=f"{info.get('title', 'audio')}.mp3")
                  
