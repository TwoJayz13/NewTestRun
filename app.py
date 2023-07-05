from flask import Flask, request, render_template_string
import youtube_dl

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        options = {'outtmpl': 'my_video.mp4'}
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([url])
        return 'Video downloaded!'
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <body>

    <h2>Download Video</h2>

    <form method="POST">
    <label for="url">URL:</label><br>
    <input type="text" id="url" name="url" value=""><br>
    <input type="submit" value="Submit">
    </form> 

    </body>
    </html>
    ''')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
