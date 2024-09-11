from flask import Flask, request, redirect
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'data'
app.config['MAX_CONTENT_LENGTH'] = None

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def index():
    return '''
<!doctype html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/dropzone@5/dist/min/dropzone.min.js"></script>
    <link rel="stylesheet" href="https://unpkg.com/dropzone@5/dist/min/dropzone.min.css" type="text/css" />
    <style>
        body {
            background: radial-gradient(circle at top right, #1e293b, #0f172a);
        }

        .upload-container {
            background: rgba(31, 41, 55, 0.85);
            backdrop-filter: blur(10px);
            border-radius: 10px;
            padding: 20px;
            max-width: 500px;
            width: 100%;
        }

        .upload-btn {
            background: linear-gradient(to right, #2563eb, #1d4ed8);
            transition: transform 0.3s ease, background 0.3s ease;
        }

        .upload-btn:hover {
            background: linear-gradient(to right, #1d4ed8, #2563eb);
            transform: translateY(-3px);
        }

        .dz-message {
            color: #cbd5e1;
            font-size: 16px;
            text-align: center;
            margin: 20px 0;
        }

        .dropzone {
            border: 2px dashed #2563eb;
            background-color: rgba(31, 41, 55, 0.6);
            border-radius: 8px;
            padding: 40px;
            transition: background-color 0.3s ease;
        }

        .dropzone:hover {
            background-color: rgba(31, 41, 55, 0.8);
        }

        .dropzone .dz-preview .dz-image {
            border-radius: 8px;
        }
    </style>
</head>

<body class="text-gray-100 flex items-center justify-center min-h-screen">
    <div class="upload-container shadow-2xl">
        <h2 class="text-3xl font-extrabold mb-4 text-center">Upload Your Files</h2>
        <form action="/upload" class="dropzone" id="my-dropzone">
            <div class="dz-message">Drag and drop files here or click to upload</div>
        </form>
    </div>

    <script>
        Dropzone.options.myDropzone = {
            autoProcessQueue: true, 
            acceptedFiles: 'image/*,application/pdf,video/*,audio/*,text/*,application/msword,application/vnd.openxmlformats-officedocument.wordprocessingml.document,application/vnd.ms-excel,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/zip', // Allow common file types
            dictInvalidFileType: 'File type not allowed',
            dictDefaultMessage: 'Drop files here to upload',
            accept: function(file, done) {
                if (file.name.endsWith('.exe') || file.name.endsWith('.sh') || file.name.endsWith('.bat') || file.name.endsWith('.php') || file.name.endsWith('.js') || file.name.endsWith('.dll') || file.name.endsWith('.py')) {
                    done("This file type is not allowed for security reasons.");
                } else {
                    done();
                }
            },
            success: function(file, response) {
                console.log('File uploaded successfully:', response);
            },
            error: function(file, response) {
                console.error('Error uploading file:', response);
            }
        };
    </script>
</body>

</html>
'''

@app.route('/upload', methods=['POST'])
def upload_files():
    files = request.files.getlist('file')  # Ensure 'file' matches Dropzone's field name
    if files:
        for file in files:
            if file and file.filename:
                try:
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
                except Exception as e:
                    app.logger.error(f'Upload failed: {e}')
                    return f'Error: {e}', 500
        return 'Files uploaded successfully', 200
    return redirect('/')

if __name__ == '__main__':
    app.run(port=6446)
