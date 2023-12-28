
import PyPDF2
import glob
from PyPDF2 import PdfMerger
import streamlit as st
import time



st.markdown(" ### :darkred[Pdf Birleştirici]")


kullanıcı adı= "user_name" #optinal
if kullanıcı_adı:
    uploaded_files = st.file_uploader("Birleştirmek istediğiniz pdf dosyalarını seçiniz", accept_multiple_files=True)


    merger = PdfMerger()

    buton = st.button("Birleştir")
    if buton:
        for file in uploaded_files:
            merger.append(file)

        #merger.write('C:\\Users\\'+kullanıcı_adı+'\\Desktop\\birleştirilmiş_pdf.pdf') 
        merger.write('birleştirilmiş_dosya.pdf')
        merger.close()
        
        # importing required modules
        
 
        # creating a pdf file object
        dosya = open('birleştirilmiş_dosya.pdf', 'rb')
 

        
        

    
    



        progress_text = "Birleştiriliyor, lütfen Bekleyiniz."
        my_bar = st.progress(0, text=progress_text)

        for percent_complete in range(100):
            time.sleep(0.001)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        my_bar.empty()
        
        st.download_button(
        label="İndirmek için tıklayınız",
        data=dosya,
        file_name='birleştirilmiş.pdf',
        mime='pdf')
       
    














