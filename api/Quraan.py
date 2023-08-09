from pywebio import *
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask
import pywebio
from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio import config
from pywebio.session import run_js
import argparse
import locale
app=Flask(__name__)

css="""

@import url('https://fonts.googleapis.com/css2?family=Ruwudu:wght@500&display=swap');

#y{
font-family: 'Ruwudu', serif;
}

#p{
font-family: 'Ruwudu', serif;
}


#img {  
max-width: 1000%;  
height: auto;  
}  


#y{
width:100%;
background:   #1B2631 ;

}



#audio-container{
    width: 100%;
}
"""


@config(css_style=css,theme="dark")
@app.route("/")

def run_app():
    put_image("https://mvslim.com/wp-content/uploads/2021/03/quran-1.jpeg",width="1000px",height="250px",title="img")
    
    put_html("""
             
             <h3 id='h3'>مرحبا بكم في منصتنا للإستماع وتحميل القرآن الكريم</h3>
             <hr>
             <p id='p'>(الله لا إله إلا هو الحي القيوم لا تأخذه سنة ولا نوم له ما في السماوات وما في الأرض من ذا الذي يشفع عنده إلا بإذنه يعلم ما بين أيديهم وما خلفهم ولا يحيطون بشيء من علمه إلا بما شاء وسع كرسيه السماوات والأرض ولا يئوده حفظهما وهو العلي العظيم)</p>
             <hr>
             
             <ul id='list'>
             
             <li> حفظ القرآن الكريم</li>
             <li> الإستماع الي القرآن الكريم</li>
             <li> تنزيل القرآن الكريم </li>
             </ul>
             <hr>
             
             
             <details id='y'>  
             
             <summary>القرآن الكريم/مصحف مرتل / حفص عن عاصم / أبو بكر الشاطري </summary>
                <p>          سورة الفاتحه          </p>
               <audio controls id='audio-container'>
                <source src="https://dl2.sura.pw/dl/reciter/11/128/001.mp3?h=Cob-JPKVwhLnqkDXKDAPOQ&expires=1691642557&dl=true" type="audio/ogg">
               </audio>
                
                
                <p>            سورة البقره          </p>
               <audio controls id='audio-container'>
                <source src="https://dl2.sura.pw/dl/reciter/11/128/002.mp3?h=Nr6ieH0eZBSe5t7ksmwYhQ&expires=1691645553&dl=true" type="audio/ogg">
               </audio>
               
               
               
               
               <p>          سورة آل عمران        </p>
               <audio controls id='audio-container'>
                <source src="https://dl2.sura.pw/dl/reciter/11/128/003.mp3?h=WnZXsrE2Dts7AZmKCrmMjg&expires=1691666529&dl=true" type="audio/ogg">
               </audio>
               
               
             
             </details>
             
             
             
             
             
             
             
             
             
             <details id='y'>  
             
             <summary> القرآن الكريم/مصحف مرتل / حفص عن عاصم / 	
                                                                  الشيخ أبو عبد الله المظفر  </summary>
                <p>          سورة الفاتحه          </p>
               <audio controls id='audio-container'>
                <source src="https://dl2.sura.pw/dl/reciter/68/160/001.mp3?h=JJ6fHY4Zqc1GVHlbB15d0g&expires=1691650588&dl=true" type="audio/ogg">
               </audio>
                
               <p>            سورة البقره          </p>
               <audio controls id='audio-container'>
                <source src="https://dl2.sura.pw/dl/reciter/68/160/002.mp3?h=iINhWai6uFCxAxbVAkKjfw&expires=1691656948&dl=true" type="audio/ogg">
               </audio>
               
             
             </details>
             
             
             
             <details id='y'>  
             
             <summary> القرآن الكريم/مصحف مرتل / حفص عن عاصم / 	
                                                                الشيخ أحمد العجمي  </summary>
                <p>          سورة الفاتحه          </p>
               <audio controls id='audio-container'>
                <source src="https://dl2.sura.pw/dl/reciter/1/128/001.mp3?h=yF8ZhySrRj9kBRxGjdxshw&expires=1691663703&dl=true" type="audio/ogg">
               </audio>
                
               <p>            سورة البقره          </p>
               <audio controls id='audio-container'>
                <source src="https://dl2.sura.pw/dl/reciter/1/128/002.mp3?h=K1gDymaz32fz0r626uVNjg&expires=1691661755&dl=true" type="audio/ogg ">
               </audio>
               
             
             </details>
             
             
             
             
             
             <details id='y'>  
             
             <summary> القرآن الكريم/مصحف مرتل / حفص عن عاصم / 	
                                                                الشيخ أحمد العجمي  </summary>
                <p>          سورة الفاتحه          </p>
               <audio controls id='audio-container'>
                <source src="https://dl2.sura.pw/dl/reciter/1/128/001.mp3?h=yF8ZhySrRj9kBRxGjdxshw&expires=1691663703&dl=true" type="audio/ogg">
               </audio>
                
               <p>            سورة البقره          </p>
               <audio controls id='audio-container'>
                <source src="https://dl2.sura.pw/dl/reciter/1/128/002.mp3?h=K1gDymaz32fz0r626uVNjg&expires=1691661755&dl=true" type="audio/ogg ">
               </audio>
               
             
             </details>
             
             
             
             
             
             """).style("direction:rtl; text-align:right;")


app.add_url_rule('/', 'webio_view', webio_view(run_app),methods=["GET","POST"])
if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("-p","--port",type=int,default=8080)
    args=parser.parse_args()
    
    pywebio.start_server(run_app, port=34345, debug=False, use_reloader=False)
# <summary>القرآن الكريم/مصحف مرتل / حفص عن عاصم / 	
# الشيخ أبو عبد الله المظفر </summary>
#              <summary>القرآن الكريم/مصحف مرتل / حفص عن عاصم / أبو بكر الشاطري </summary>
#              
