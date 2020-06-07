import pytesseract as tess
import docx
from flask import Flask
from flask_restful import Resource, Api, reqparse
from PIL import Image

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class GetText(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('fileUrl', required=True)
        parser.add_argument('fileType', required=True)
        parser.add_argument('slang', required=True)
        parser.add_argument('dlang', required=True)

        args = parser.parse_args()
        fileUrl = args['fileUrl']

        tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        img = Image.open(fileUrl)
        text = tess.image_to_string(img, lang='eng')

        return {'message': 'success', 'data': text}


api.add_resource(HelloWorld, '/')
api.add_resource(GetText, '/gettext')

if __name__ == '__main__':
    app.run(debug=True)
