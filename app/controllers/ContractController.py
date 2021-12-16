
from flask import render_template, url_for, request, redirect, flash
import app
from app.models.Contract import Contract
from app import db, app
import pdfkit

app.config['PDF_FOLDER'] = 'app/static/pdf/'
app.config['TEMPLATE_FOLDER'] = 'app/views/contracts/'
URL_INDEX_TO_PRINT = 'http://127.0.0.1:5001/contracts'
WKHTMLTOPDF_PATH = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'

#definimos clase controlador
class ContractController():
    def __init__(self):
        pass
 
    #se retorna el metodo index igual con self
    def index1(self):
        contracts = Contract.query.all()
        return render_template('contracts/index.html', contracts = contracts)

    def create(self):
        #users = User.query.all()
        return render_template('contracts/create.html')

    def store(self):
        if request.method == 'POST':
            client = request.form['client']
            tipe = request.form['tipe']
            date = request.form['date']
            color = request.form['color']
            total = request.form['total']
            #from app.models.Alumno import Alumno
            contractadd = Contract(client = client, tipe = tipe, date = date, color = color, total=total)
            db.session.add(contractadd)
            db.session.commit()
            flash('El nuevo contrato se ha registrado correctamente!!!')
            return redirect(url_for('contract_router.index'))

    def delete(self, _id):
        contract = Contract.query.get(_id)
        db.session.delete(contract)
        db.session.commit()
        flash('El contrato se ha eliminado con exito')
        return redirect(url_for('contract_router.index'))

    def edit(self, _id):
        contract = Contract.query.get(_id)
        return render_template('contracts/edit.html', contract = contract)

    def update(self, _id):
        if request.method == 'POST':
            clientv = request.form['client']
            tipev = request.form['tipe']
            datev = request.form['date']
            colorv = request.form['color']
            totalv = request.form['total']
            #from app.models.Alumno import Alumno
            contractDB = Contract.query.get(_id)
            contractDB.client = clientv
            contractDB.tipe = tipev
            contractDB.date = datev
            contractDB.color = colorv
            contractDB.total = totalv
            db.session.commit()
            flash('El contrato se ha editado correctamente!!!')
            return redirect(url_for('contract_router.index'))

    def convertpdf(self):
        config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)
        #htmlfile = app.config['TEMPLATE_FOLDER'] + 'index.html'
        htmlfile = 'http://127.0.0.1:5001/contracts'
        #img = ''
        contracts = Contract.query.all()
        header = '''
        
        
        '''
        body = render_template('contracts/index.html', contracts=contracts)
        footer= '''<p>Fin de todo</p>'''
        #htmlfile = header+body+footer
        #htmlfile = "<img src='https://conceptodefinicion.de/wp-content/uploads/2014/05/Imagen-2.jpg'>"
        
        pdffile = app.config['PDF_FOLDER'] + 'demo.pdf'
        options={
                'page-size': 'Letter',
                'margin-top': '0.75in',
                'margin-right': '0.75in',
                'margin-bottom': '0.75in',
                'margin-left': '0.75in',
                'encoding': "UTF-8",
                'custom-header': [
                    ('Accept-Encoding', 'gzip')
                ],
            }
        css = 'app/static/css/style.css'
        try:
            pdfkit.from_url(htmlfile, pdffile, configuration=config, options=options)
            #pdfkit.from_file(htmlfile, pdffile,configuration=config, options=options)
            
            #pdfkit.from_string(htmlfile, pdffile,configuration=config, options=options)
            return '''Click para abrir el reporte en pdf: <a href="http://127.0.0.1:5001/static/pdf/demo.pdf">pdf</a>.'''
        except OSError as e:
            if 'Done' not in str(e):
                raise e
        
contractcontroller = ContractController()